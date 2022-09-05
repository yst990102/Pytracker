#!/usr/bin/env python3

# portions copyright 2001, Autonomous Zones Industries, Inc., all rights...
# err...  reserved and offered to the public under the terms of the
# Python 2.2 license.
# Author: Zooko O'Whielacronx
# http://zooko.com/
# mailto:zooko@zooko.com
#
# Copyright 2000, Mojam Media, Inc., all rights reserved.
# Author: Skip Montanaro
#
# Copyright 1999, Bioreason, Inc., all rights reserved.
# Author: Andrew Dalke
#
# Copyright 1995-1997, Automatrix, Inc., all rights reserved.
# Author: Skip Montanaro
#
# Copyright 1991-1995, Stichting Mathematisch Centrum, all rights reserved.
#
#
# Permission to use, copy, modify, and distribute this Python software and
# its associated documentation for any purpose without fee is hereby
# granted, provided that the above copyright notice appears in all copies,
# and that both that copyright notice and this permission notice appear in
# supporting documentation, and that the name of neither Automatrix,
# Bioreason or Mojam Media be used in advertising or publicity pertaining to
# distribution of the software without specific, written prior permission.
#
"""program/module to trace Python program or function execution

Sample use, command line:
  trace.py -c -f counts --ignore-dir '$prefix' spam.py eggs
  trace.py -t --ignore-dir '$prefix' spam.py eggs
  trace.py --trackcalls spam.py eggs

Sample use, programmatically
  import sys

  # create a Trace object, telling it what to ignore, and whether to
  # do tracing or line-counting or both.
  tracer = trace.Trace(ignoredirs=[sys.base_prefix, sys.base_exec_prefix,],
					   trace=0, count=1)
  # run the new command using the given tracer
  tracer.run('main()')
  # make a report, placing output in /tmp
  r = tracer.results()
  r.write_results(show_missing=True, coverdir="/tmp")
"""
__all__ = ['Trace', 'CoverageResults']

from io import StringIO
import linecache
import os
import sys
import sysconfig
import token
import tokenize
import inspect
import gc
import dis
import pickle
from time import monotonic as _time

import threading

# personal import
from trace import CoverageResults, _Ignore, _modname


class Trace:

	def __init__(self, count=1, trace=1, countfuncs=0, countcallers=0, ignoremods=(), ignoredirs=(), infile=None, outfile=None, usercode_file="UserCode.py", timing=False):
		"""
		@param count true iff it should count number of times each
					 line is executed
		@param trace true iff it should print out each line that is
					 being counted
		@param countfuncs true iff it should just output a list of
					 (self.filename, modulename, funcname,) for functions
					 that were called at least once;  This overrides
					 `count' and `trace'
		@param ignoremods a list of the names of modules to ignore
		@param ignoredirs a list of the names of directories to ignore
					 all of the (recursive) contents of
		@param infile file from which to read stored counts to be
					 added into the results
		@param outfile file in which to write the results
		@param timing true iff timing information be displayed
		"""
		self.infile = infile
		self.outfile = outfile
		self.ignore = _Ignore(ignoremods, ignoredirs)
		self.counts = {}  # keys are (filename, linenumber)
		self.pathtobasename = {}  # for memoizing os.path.basename
		self.donothing = 0
		self.trace = trace
		self._calledfuncs = {}
		self._callers = {}
		self._caller_cache = {}
		self.start_time = None

		# 个人定义的self属性
		self.usercode_file = usercode_file

		if timing:
			self.start_time = _time()
		if countcallers:
			self.globaltrace = self.globaltrace_trackcallers
		elif countfuncs:
			self.globaltrace = self.globaltrace_countfuncs
		elif trace and count:
			self.globaltrace = self.globaltrace_lt
			self.localtrace = self.localtrace_trace_and_count
		elif trace:
			self.globaltrace = self.globaltrace_lt
			self.localtrace = self.localtrace_trace
		elif count:
			self.globaltrace = self.globaltrace_lt
			self.localtrace = self.localtrace_count
		else:
			# Ahem -- do nothing?  Okay.
			self.donothing = 1

	def run(self, cmd):
		import __main__
		dict = __main__.__dict__
		
		# TODO: idk why replace this part with that will fix the local_variables missing issue for multi-run in web.py
		# self.initial_locals_keys = set(dict.keys())
		# self.initial_globals_keys = set(dict.keys())
		
		self.initial_locals_keys = {'__builtins__', '__cached__', '__spec__', '__name__', '__annotations__', 'usercode', '__package__', 'Pytracker', '__file__', '__doc__', '__loader__'}
		self.initial_globals_keys = {'__builtins__', '__cached__', '__spec__', '__name__', '__annotations__', 'usercode', '__package__', 'Pytracker', '__file__', '__doc__', '__loader__'}
		
		global line_no_list, line_content_list, local_variable_list
		line_no_list = []
		line_content_list = []
		local_variable_list = []
		global execution_processes
		execution_processes = []
		
		self.runctx(cmd, dict.copy(), dict.copy())

	def runctx(self, cmd, globals=None, locals=None):
		self.usercode = cmd

		if globals is None:
			globals = {}
		if locals is None:
			locals = {}
		if not self.donothing:
			threading.settrace(self.globaltrace)
			sys.settrace(self.globaltrace)
		
		global Pytracker_outIO
		Pytracker_outIO = StringIO()
		# redirect the stdout
		old_stdout = sys.stdout
		sys.stdout = Pytracker_outIO
		
		try:
			exec(cmd, globals, locals)
		except:
			raise
		finally:
			sys.stdout = old_stdout
			
			local_variables = {}
			local_variables_set_diff = list(locals.keys() - self.initial_locals_keys)
			for key in local_variables_set_diff:
				local_variables[key] = locals[key]
			local_variable_list.append(local_variables)
			del local_variable_list[0]
			
			assert(len(line_no_list) == len(line_content_list) == len(local_variable_list))
			for i in range(len(line_no_list)):
				line_info = {'line_no': line_no_list[i], "line_content": line_content_list[i], "local_variables": local_variable_list[i]}
				execution_processes.append(line_info)
			
			if not self.donothing:
				sys.settrace(None)
				threading.settrace(None)

	def file_module_function_of(self, frame):
		code = frame.f_code
		filename = code.co_filename
		if filename:
			modulename = _modname(filename)
		else:
			modulename = None

		funcname = code.co_name
		clsname = None
		if code in self._caller_cache:
			if self._caller_cache[code] is not None:
				clsname = self._caller_cache[code]
		else:
			self._caller_cache[code] = None
			## use of gc.get_referrers() was suggested by Michael Hudson
			# all functions which refer to this code object
			funcs = [f for f in gc.get_referrers(code) if inspect.isfunction(f)]
			# require len(func) == 1 to avoid ambiguity caused by calls to
			# new.function(): "In the face of ambiguity, refuse the
			# temptation to guess."
			if len(funcs) == 1:
				dicts = [d for d in gc.get_referrers(funcs[0]) if isinstance(d, dict)]
				if len(dicts) == 1:
					classes = [c for c in gc.get_referrers(dicts[0]) if hasattr(c, "__bases__")]
					if len(classes) == 1:
						# ditto for new.classobj()
						clsname = classes[0].__name__
						# cache the result - assumption is that new.* is
						# not called later to disturb this relationship
						# _caller_cache could be flushed if functions in
						# the new module get called.
						self._caller_cache[code] = clsname
		if clsname is not None:
			funcname = "%s.%s" % (clsname, funcname)

		return self.usercode_file, modulename, funcname

	def globaltrace_trackcallers(self, frame, why, arg):
		"""Handler for call events.

		Adds information about who called who to the self._callers dict.
		"""
		if why == 'call':
			# XXX Should do a better job of identifying methods
			this_func = self.file_module_function_of(frame)
			parent_func = self.file_module_function_of(frame.f_back)
			self._callers[(parent_func, this_func)] = 1

	def globaltrace_countfuncs(self, frame, why, arg):
		"""Handler for call events.

		Adds (filename, modulename, funcname) to the self._calledfuncs dict.
		"""
		if why == 'call':
			this_func = self.file_module_function_of(frame)
			self._calledfuncs[this_func] = 1

	def globaltrace_lt(self, frame, why, arg):
		"""Handler for call events.

		If the code block being entered is to be ignored, returns `None',
		else returns self.localtrace.
		"""
		if why == 'call':
			code = frame.f_code
			filename = frame.f_globals.get('__file__', None)
			if filename:
				# XXX _modname() doesn't work right for packages, so
				# the ignore support won't work right for packages
				modulename = _modname(filename)
				if modulename is not None:
					ignore_it = self.ignore.names(filename, modulename)
					if not ignore_it:
						if self.trace:
							# print((" --- modulename: %s, funcname: %s" % (modulename, code.co_name)))
							pass
						return self.localtrace
			else:
				return self.localtrace

	def localtrace_trace_and_count(self, frame, why, arg):
		if frame.f_code.co_name == "input":
			return self.localtrace
		if why == "line":
			# record the file name and line number of every trace
			lineno = frame.f_lineno
			key = self.usercode_file, lineno
			self.counts[key] = self.counts.get(key, 0) + 1

			frame_locals = frame.f_locals
			frame_globals = frame.f_globals

			local_variables = {}
			local_variables_set_diff = list(frame_locals.keys() - self.initial_locals_keys)
			for key in local_variables_set_diff:
				local_variables[key] = frame_locals[key]
			# global_variables = {}
			# global_variables_set_diff = list(frame_globals.keys() - self.initial_globals_keys)
			# for key in global_variables_set_diff:
			# 	global_variables[key] = frame_globals[key]

			if self.start_time:
				print('%.2f' % (_time() - self.start_time), end=' ')

			try:
				line_no_list.append(lineno)
				line_content_list.append(self.usercode.splitlines()[lineno - 1])
				local_variable_list.append(local_variables)
			except OSError as err:
				print("Can't save localtrace_trace_and_count output because %s" % err, file=sys.stderr)

		return self.localtrace

	def localtrace_trace(self, frame, why, arg):
		if why == "line":
			# record the file name and line number of every trace
			lineno = frame.f_lineno

			if self.start_time:
				print('%.2f' % (_time() - self.start_time), end=' ')

			# print("(%d): %s" % (lineno, linecache.getline(self.usercode_file, lineno)), end='')
			print("(%d): %s" % (lineno, self.usercode.splitlines()[lineno - 1]), end='\n')

		return self.localtrace

	def localtrace_count(self, frame, why, arg):
		if why == "line":
			lineno = frame.f_lineno
			key = self.usercode_file, lineno
			self.counts[key] = self.counts.get(key, 0) + 1
		return self.localtrace

	def results(self):
		return CoverageResults(self.counts, infile=self.infile, outfile=self.outfile, calledfuncs=self._calledfuncs, callers=self._callers)


def main():
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument('--version', action='version', version='trace 2.0')

	grp = parser.add_argument_group('Main options', 'One of these (or --report) must be given')

	grp.add_argument('-c',
	                 '--count',
	                 action='store_true',
	                 help='Count the number of times each line is executed and write '
	                 'the counts to <module>.cover for each module executed, in '
	                 'the module\'s directory. See also --coverdir, --file, '
	                 '--no-report below.')
	grp.add_argument('-t', '--trace', action='store_true', help='Print each line to sys.stdout before it is executed')
	grp.add_argument('-l',
	                 '--listfuncs',
	                 action='store_true',
	                 help='Keep track of which functions are executed at least once '
	                 'and write the results to sys.stdout after the program exits. '
	                 'Cannot be specified alongside --trace or --count.')
	grp.add_argument('-T', '--trackcalls', action='store_true', help='Keep track of caller/called pairs and write the results to '
	                 'sys.stdout after the program exits.')

	grp = parser.add_argument_group('Modifiers')

	_grp = grp.add_mutually_exclusive_group()
	_grp.add_argument('-r',
	                  '--report',
	                  action='store_true',
	                  help='Generate a report from a counts file; does not execute any '
	                  'code. --file must specify the results file to read, which '
	                  'must have been created in a previous run with --count '
	                  '--file=FILE')
	_grp.add_argument('-R', '--no-report', action='store_true', help='Do not generate the coverage report files. '
	                  'Useful if you want to accumulate over several runs.')

	grp.add_argument('-f', '--file', help='File to accumulate counts over several runs')
	grp.add_argument('-C', '--coverdir', help='Directory where the report files go. The coverage report '
	                 'for <package>.<module> will be written to file '
	                 '<dir>/<package>/<module>.cover')
	grp.add_argument('-m', '--missing', action='store_true', help='Annotate executable lines that were not executed with '
	                 '">>>>>> "')
	grp.add_argument('-s', '--summary', action='store_true', help='Write a brief summary for each file to sys.stdout. '
	                 'Can only be used with --count or --report')
	grp.add_argument('-g', '--timing', action='store_true', help='Prefix each line with the time since the program started. '
	                 'Only used while tracing')

	grp = parser.add_argument_group('Filters', 'Can be specified multiple times')
	grp.add_argument('--ignore-module', action='append', default=[], help='Ignore the given module(s) and its submodules '
	                 '(if it is a package). Accepts comma separated list of '
	                 'module names.')
	grp.add_argument('--ignore-dir', action='append', default=[], help='Ignore files in the given directory '
	                 '(multiple directories can be joined by os.pathsep).')

	parser.add_argument('--module', action='store_true', default=False, help='Trace a module. ')
	parser.add_argument('progname', nargs='?', help='file to run as main program')
	parser.add_argument('arguments', nargs=argparse.REMAINDER, help='arguments to the program')

	opts = parser.parse_args()

	if opts.ignore_dir:
		_prefix = sysconfig.get_path("stdlib")
		_exec_prefix = sysconfig.get_path("platstdlib")

	def parse_ignore_dir(s):
		s = os.path.expanduser(os.path.expandvars(s))
		s = s.replace('$prefix', _prefix).replace('$exec_prefix', _exec_prefix)
		return os.path.normpath(s)

	opts.ignore_module = [mod.strip() for i in opts.ignore_module for mod in i.split(',')]
	opts.ignore_dir = [parse_ignore_dir(s) for i in opts.ignore_dir for s in i.split(os.pathsep)]

	if opts.report:
		if not opts.file:
			parser.error('-r/--report requires -f/--file')
		results = CoverageResults(infile=opts.file, outfile=opts.file)
		return results.write_results(opts.missing, opts.summary, opts.coverdir)

	if not any([opts.trace, opts.count, opts.listfuncs, opts.trackcalls]):
		parser.error('must specify one of --trace, --count, --report, '
		             '--listfuncs, or --trackcalls')

	if opts.listfuncs and (opts.count or opts.trace):
		parser.error('cannot specify both --listfuncs and (--trace or --count)')

	if opts.summary and not opts.count:
		parser.error('--summary can only be used with --count or --report')

	if opts.progname is None:
		parser.error('progname is missing: required with the main options')

	t = Trace(opts.count,
	          opts.trace,
	          countfuncs=opts.listfuncs,
	          countcallers=opts.trackcalls,
	          ignoremods=opts.ignore_module,
	          ignoredirs=opts.ignore_dir,
	          infile=opts.file,
	          outfile=opts.file,
	          timing=opts.timing)
	try:
		if opts.module:
			import runpy
			module_name = opts.progname
			mod_name, mod_spec, code = runpy._get_module_details(module_name)
			sys.argv = [code.co_self.filename, *opts.arguments]
			globs = {
			    '__name__': '__main__',
			    '__file__': code.co_self.filename,
			    '__package__': mod_spec.parent,
			    '__loader__': mod_spec.loader,
			    '__spec__': mod_spec,
			    '__cached__': None,
			}
		else:
			sys.argv = [opts.progname, *opts.arguments]
			sys.path[0] = os.path.dirname(opts.progname)

			# 2022-08-14这边不用compile的，不然runctx里面self.usercode不是用户输入代码的字符串
			# with open(opts.progname, 'rb') as fp:
			# 	code = compile(fp.read(), opts.progname, 'exec')
			code = open(opts.progname, 'r').read()

			# try to emulate __main__ namespace as much as possible
			globs = {
			    '__file__': opts.progname,
			    '__name__': '__main__',
			    '__package__': None,
			    '__cached__': None,
			}
		t.runctx(code, globs, globs)
	except OSError as err:
		sys.exit("Cannot run file %r because: %s" % (sys.argv[0], err))
	except SystemExit:
		pass

	results = t.results()

	if not opts.no_report:
		results.write_results(opts.missing, opts.summary, opts.coverdir)


if __name__ == '__main__':
	main()
