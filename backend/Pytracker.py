import sys
import my_trace
import re
import traceback
import parse


# import user file
import sample1


# global variables
SUCCESS = 1
FAILURE = 0

# global switch
trace_switch = 1
traceback_switch = 1

def isBracket_match(s:str) -> bool:
	finding = []
	for ch in s:
		if ch == '(':
			finding.append(')')
		elif ch == '[':
			finding.append(']')
		elif ch == '{':
			finding.append('}')
		elif ch.isdigit() or ch == ",":
			continue
		elif not finding or not ch == finding.pop(-1) :
			return False
	return len(finding) == 0

def del_line_in_file(filename, content):
	with open(filename, "r") as f:
		lines = f.readlines()
	with open(filename, "w") as f_w:
		for line in lines:
			if content in line:
				continue
			f_w.write(line)
	f.close()
	f_w.close()


def clean_txt_file(filename):
	try:
		with open(filename, "r+") as f:
			f.seek(0)
			f.truncate()  # 清空文件
			f.close()
			return
	except FileNotFoundError:
		# file does not exist, create a blank file
		open(filename, 'w').close()
		return


def traceback_bug_catch():
	print(
		"************************************************************\n" +
		"*************            traceback             *************\n" +
		"************************************************************"
	)

	if traceback_switch == 1:
		try:
			sample1.main()
		except Exception as e:
			exc_type, exc_value, exc_traceback = sys.exc_info()

			# trackback summary
			traceback_summary = traceback.extract_tb(exc_traceback)
			traceback.print_tb(exc_traceback)
			return FAILURE
	return SUCCESS


def trace_execution_tracking(filename, result_file):
	print(
		"************************************************************\n" +
		"*************              trace               *************\n" +
		"************************************************************"
	)

	# steps -- all the execution steps
	# formate -- [(line_no, local_variables), (..), ...]
	steps_info = []
	while_lines = []
	tab_dict = {}
	if trace_switch == 1:

		# call trace customer's execution
		tracer = my_trace.Trace(ignoredirs=[sys.prefix, sys.exec_prefix], trace=1, count=1, outfile=result_file)
		tracer.run(UserFile.strip(".py") + ".main()")

		# delete the initial <string>(1) line in the execution output
		del_line_in_file(exec_result_file, "<string>")

		from itertools import islice
		with open(result_file, 'r') as exec_result:
			while True:
				exec_lines_gen = islice(exec_result, 2)
				exec_content = list(exec_lines_gen)
	
				cur_while_info = []
				if not exec_content:
					break
				else:
					# grab information for the code line
					# 0 for userfile_name, 1 for line_no, 2 for line_content
					code_parse = list(parse.parse("{0}({1}): {2}", exec_content[0]))
					if filename == code_parse[0]:

						line_no = int(code_parse[1])
						line_content = code_parse[2]

						# if it is a while loop
						# use regular expression to match
						while_loop_search = re.search(r"while\s*\((.*)\)\s*:", line_content)
						if (while_loop_search):
							while_statement = while_loop_search.group(0)
							while_judgement = while_loop_search.group(1)
							# DONE: 2022-05-11 while_statement and while_judgement parsing correctly
							# if (while_statement is not None):
							# 	print(f"while_statement == {while_statement}")
							# 	print(f"while_judgement == {while_judgement}")
							while_lines.append(line_no)

						# DONE: 2022-05-11 tabs parsing correctly
						# print("Tabs Count ==", line_content.count('\t'))
						tab_dict[line_no] = line_content.count('\t')

					# grab information for the local_variable line
					vari_parse = list(parse.parse("local_variables == {0}", exec_content[1]))
					local_variables = eval(vari_parse[0])
					steps_info.append((line_no, local_variables))
					# DONE: 2022-05-11 variable parsing correctly
					# print(f"variable == {local_variables}")
					# print(f"while_lines == {while_lines}, steps == {steps_info}, tab_dict == {tab_dict}")
		exec_result.close()

	all_line_nos = [line_no for (line_no, _) in steps_info]

	# Create a stack, put it in from left to right, and pop one out every time the indentation is greater than or equal to.
	stack = []
	result = ""
	for count, line_no in enumerate(all_line_nos):
		if while_lines == []:
			if tab_dict[line_no] > tab_dict[stack[-1]]:
				# print(f"{line_no}\t in loop {stack} {while_lines}")
				result = result + str(line_no)
			else:
				# print(f"{line_no}\t outer break, {stack} {while_lines}")
				result = result + "]" + str(line_no)
				stack.pop()
		elif line_no == while_lines[0]:
			if line_no in stack:
				# print(f"{line_no}\t next round loop, loop statement, {stack} {while_lines}")
				result = result + "]" + "[" + str(line_no)
			else:
				# print(f"{line_no}\t new loop statement, {stack} {while_lines}")
				stack.append(while_lines[0])
				result = result + "[" + str(line_no)
			del while_lines[0]
		else:
			if stack == []:
				# print(f"{line_no}\t out of loop, {stack} {while_lines}")
				result = result + str(line_no)
			elif tab_dict[line_no] > tab_dict[stack[-1]]:
				# print(f"{line_no}\t in loop, {stack} {while_lines}")
				result = result + str(line_no)
			else:
				# print(f"{line_no}\t inner break, {stack} {while_lines}")
				result = result + str(line_no) + "]"
				stack.pop()
		if count < len(all_line_nos) - 1:
			result = result + ","
	
	result = "[" + result + "]"
	result = result.replace(",]", "],")

	assert(isBracket_match(result) == True)
	parse_result = eval(result)
	print(parse_result)
 
 
 
if __name__ == "__main__":

	# 【non-necessary】pre-step: call traceback to check if any bug
	if not traceback_bug_catch():
		sys.exit("======== error occured ========")

	# define the UserFile and output file of execution process
	UserFile = sample1.__name__ + ".py"
	exec_result_file = "execution.txt"

	# clean the execution txt before start a new tracer
	clean_txt_file(exec_result_file)

	# trace the whole execution process via my_tracer
	trace_execution_tracking(UserFile, exec_result_file)
