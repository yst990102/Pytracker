import json
import os
import pathlib
import sys
from backend.my_trace import Trace
import re
import parse

# Pytracker import
# file_op helpers
from backend.helper_functions import create_test_file, del_line_in_file, delete_file, clean_content_in_file
# list of list processors
from backend.helper_functions import ListOfList_to_ListOfIntAndTuple, remove_if_else_lines_from_listoflist, remove_singlelist_from_listoflist
# json processors
from backend.helper_functions import get_step_json, listoflist_to_json
# other processors
from backend.helper_functions import tabdict_to_gridindent
# checkers
from backend.helper_functions import isBracket_match
# classes and objects definition
from backend.parse_classes import Program

# Pytracker globals
global Pytracker_locals
global Pytracker_globals
Pytracker_locals = locals()
Pytracker_globals = globals()

# Pytracker defines
current_absolute_path = str(pathlib.Path(__file__).parent.resolve())

# DEBUG switches
DEBUG_parse_strListOfList_into_ListOfList = False


def trace_execution_tracking(tracer, result_file):
	# steps -- all the execution steps
	# formate -- [(line_no, local_variables), (..), ...]
	steps_info = []
	while_lines = []
	if_else_lines = []
	tab_dict = {}

	# delete the initial <string>(1) line in the execution output
	del_line_in_file(result_file, "<string>")

	from itertools import islice
	with open(result_file, 'r') as exec_result:
		while True:
			exec_lines_gen = islice(exec_result, 2)
			exec_content = list(exec_lines_gen)

			if not exec_content:
				break
			else:
				# ===================================================================================
				# STEP 1: grab information for the code line
				# 0 for line_no, 1 for line_content
				code_parse = list(parse.parse("({0}): {1}", exec_content[0]))

				line_no = int(code_parse[0])
				line_content = code_parse[1]
				# CASE 1: IF_STATEMENT
				if_search = re.search(r"if\s*(.*)\s*:", line_content)
				if if_search:
					if_else_lines.append(line_no)

				# CASE 2: WHILE_LOOP
				# use regular expression to match
				while_loop_search = re.search(r"while\s*(.*)\s*:", line_content)
				if (while_loop_search):
					# while_statement = while_loop_search.group(0)
					# while_judgement = while_loop_search.group(1)
					while_lines.append(line_no)

				# CASE 3: FOR_LOOP
				for_loop_search = re.search(r"for(.*)in(.*):", line_content)
				if (for_loop_search):
					while_lines.append(line_no)

				tab_dict[line_no] = line_content.count('\t')

				# ===================================================================================
				# STEP 2: grab information for the local_variable line
				vari_parse = list(parse.parse("local_variables == {0}", exec_content[1]))

				# TODO: 这边的local_variable需要将Pytracker_locals里面对应的东西去除
				local_variables = vari_parse[0]

				steps_info.append((line_no, local_variables))

	exec_result.close()
	all_line_nos = [line_no for (line_no, _) in steps_info]
	tab_dict = dict(sorted(tab_dict.items()))

	# parse str_ListOfList into ListOfList
	listoflist_result = parse_strListOfList_into_ListOfList(all_line_nos, while_lines[:], tab_dict)
	return listoflist_result, tab_dict, while_lines, if_else_lines


def parse_strListOfList_into_ListOfList(all_line_nos, while_lines, tab_dict):
	if DEBUG_parse_strListOfList_into_ListOfList:
		print("========================== parse_strListOfList_into_ListOfList ==========================")
		print(f"all_line_nos == {all_line_nos}\nwhile_lines == {while_lines}\ntab_dict == {tab_dict}")

	# Create a stack, put it in from left to right, and pop one out every time the indentation is greater than or equal to.
	stack = []
	result = ""
	for count, line_no in enumerate(all_line_nos):
		if while_lines == []:
			if stack == []:
				result = result + str(line_no)
				result = result.replace(",]", "],")
				if DEBUG_parse_strListOfList_into_ListOfList:
					print(f"{line_no}\t out of loop\t {stack}\t {result}")
			elif tab_dict[line_no] > tab_dict[stack[-1]]:
				result = result + str(line_no)
				result = result.replace(",]", "],")
				if DEBUG_parse_strListOfList_into_ListOfList:
					print(f"{line_no}\t in loop\t {stack}\t {result}")
			else:
				result = result + "]" + str(line_no)
				stack.pop()
				result = result.replace(",]", "],")
				if DEBUG_parse_strListOfList_into_ListOfList:
					print(f"{line_no}\t outer break\t {stack}\t {result}")
		elif line_no == while_lines[0]:
			if line_no in stack:
				result = result + "]" + "[" + str(line_no)
				result = result.replace(",]", "],")
				if DEBUG_parse_strListOfList_into_ListOfList:
					print(f"{line_no}\t next round loop, loop statement\t {stack}\t {result}")
			else:
				stack.append(while_lines[0])
				result = result + "[" + str(line_no)
				result = result.replace(",]", "],")
				if DEBUG_parse_strListOfList_into_ListOfList:
					print(f"{line_no}\t new loop statement\t {stack}\t {result}")
			del while_lines[0]
		else:
			if stack == []:
				result = result + str(line_no)
				result = result.replace(",]", "],")
				if DEBUG_parse_strListOfList_into_ListOfList:
					print(f"{line_no}\t out of loop\t {stack}\t {result}")
			elif tab_dict[line_no] > tab_dict[stack[-1]]:
				result = result + str(line_no)
				result = result.replace(",]", "],")
				if DEBUG_parse_strListOfList_into_ListOfList:
					print(f"{line_no}\t in loop\t {stack}\t {result}")
			else:
				result = result + "]" + str(line_no)
				stack.pop()
				result = result.replace(",]", "],")
				if DEBUG_parse_strListOfList_into_ListOfList:
					print(f"{line_no}\t inner break\t {stack}\t {result}")

		if count < len(all_line_nos) - 1:
			result = result + ","

	# add remaining right bracket from stack.pop()
	result = result + len(stack) * "]"
	stack.clear()  # clear stack

	result = "[" + result + "]"

	try:
		assert (isBracket_match(result) == True)
	except:
		print(f"ERROR: isBracket_match Failed! result == {result}, stack == {stack}")
		exit(1)

	return eval(result)


def parse_convert_TupleOfIntTuple_into_Program(TupleOfIntAndTuple, tab_dict: dict, grid_indent: dict):
	return Program(TupleOfIntAndTuple, tab_dict, grid_indent)


def backend_main(usercode=open(current_absolute_path + "/" + "UserCode.py").read()):
	# =====================================================
	# ===========   Stage 01 : previous_check   ===========
	# =====================================================
	# format with yapf3 before create test_script
	os.system(f"yapf -i {current_absolute_path}/UserCode.py")

	# clean the execution txt before start a new tracer
	clean_content_in_file(current_absolute_path + "/" + "Pytracker_output")

	# create tracer
	tracer = Trace(ignoredirs=[sys.prefix, sys.exec_prefix], trace=1, count=1, outfile=current_absolute_path + "/" + "Pytracker_output")
	tracer.run(usercode)

	# =====================================================
	# ============   Stage 02 : main_tracing   ============
	# =====================================================
	# trace the whole execution, return a ListOfList
	global listoflist
	listoflist, tab_dict, while_lines, if_else_lines = trace_execution_tracking(tracer, current_absolute_path + "/" + "Pytracker_output")

	# remove single_list -> "[0-9]" from the listoflist_result
	listoflist = remove_singlelist_from_listoflist(listoflist)
	listoflist = remove_if_else_lines_from_listoflist(if_else_lines, listoflist)

	# =====================================================
	# =========   Stage 03 : convert_to_program   =========
	# =====================================================
	# convert ListOfList into TupleOfIntAndTuple
	TupleOfIntAndTuple = ListOfList_to_ListOfIntAndTuple(listoflist)
	grid_indent = tabdict_to_gridindent(tab_dict, while_lines)
	# then convert into Program
	program = parse_convert_TupleOfIntTuple_into_Program(TupleOfIntAndTuple, tab_dict, grid_indent)

	# TEST: all available print ways testing for program
	# program.print_statements()
	# program.print_linklist(Print_Forward)
	# program.print_linklist(Print_Backward)
	# program.print_while_loops_inlayer()

	# =====================================================
	# ===========   Stage 03 : get_step_json   ============
	# =====================================================
	# method 01 : get json from program
	global step_json
	step_json = get_step_json(program)
	# method 02 : get json from listoflist
	# listoflist_to_json(0, listoflist_result, [])
	# step_json = {"d": 5, "list": step_list_in_json}


if __name__ == "__main__":
	backend_main()
