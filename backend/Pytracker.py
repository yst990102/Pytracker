import os
import sys
import my_trace
import re
import parse

# import helper_functions
# file_op helpers
from helper_functions import create_test_file, del_line_in_file, delete_file, clean_content_in_file
# checkers
from helper_functions import isBracket_match
# classes and objects definition
from parse_classes import Assignment, Basic_Iteration, Nested_Iteration, Print_Backward, Print_Forward, Program, Iteration

# global variables
SUCCESS = 1
FAILURE = 0

# DEBUG_printing
DEBUG_parse_strListOfList_into_ListOfList = False
DEBUG_tabdict_to_gridindent = False


def trace_execution_tracking(tracer, result_file):
	# print(
	# 	"************************************************************\n" +
	# 	"*************              trace               *************\n" +
	# 	"************************************************************"
	# )

	# steps -- all the execution steps
	# formate -- [(line_no, local_variables), (..), ...]
	steps_info = []
	while_lines = []
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
				# 0 for userfile_name, 1 for line_no, 2 for line_content
				code_parse = list(parse.parse("{0}({1}): {2}", exec_content[0]))
				a, b, c = list(parse.parse("{0}({1}): {2}", exec_content[0]))
				# print(code_parse)

				line_no = int(code_parse[1])
				line_content = code_parse[2]
				# CASE 1: IF_STATEMENT
				if_search = re.search(r"if\s*(.*)\s*:", line_content)
				if if_search:
					continue

				# CASE 2: WHILE_LOOP
				# use regular expression to match
				while_loop_search = re.search(r"while\s*(.*)\s*:", line_content)
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

				# ===================================================================================
				# STEP 2: grab information for the local_variable line
				vari_parse = list(parse.parse("local_variables == {0}", exec_content[1]))
				local_variables = eval(vari_parse[0])
				steps_info.append((line_no, local_variables))
				# DONE: 2022-05-11 variable parsing correctly
				# print(f"variable == {local_variables}")
				# print(f"while_lines == {while_lines}, steps == {steps_info}, tab_dict == {tab_dict}")
	exec_result.close()
	all_line_nos = [line_no for (line_no, _) in steps_info]
	tab_dict = dict(sorted(tab_dict.items()))

	# parse str_ListOfList into ListOfList
	listoflist_result = parse_strListOfList_into_ListOfList(all_line_nos, while_lines[:], tab_dict)
	return listoflist_result, tab_dict, while_lines


def parse_strListOfList_into_ListOfList(all_line_nos, while_lines, tab_dict):
	if DEBUG_parse_strListOfList_into_ListOfList:
		print("========================== parse_strListOfList_into_ListOfList ==========================")

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
				result = result + str(line_no) + "]"
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

	if DEBUG_parse_strListOfList_into_ListOfList:
		print("before listoflist evaluated", result)
	parse_result = eval(result)
	if DEBUG_parse_strListOfList_into_ListOfList:
		print("after listoflist evaluated", parse_result)

	return parse_result


def parse_convert_TupleOfIntTuple_into_Program(TupleOfIntAndTuple, tab_dict:dict, grid_indent:dict):
	program = Program(TupleOfIntAndTuple, tab_dict, grid_indent)
	return program


def pre_execute_check():
	if len(sys.argv) != 1 and len(sys.argv) != 2 and len(sys.argv) != 3 and len(sys.argv) != 4:
		raise Exception(f"Arguments Error: execute format: python {__file__.split('/')[-1]} [User_Code] [Output_File] [ListOfList_File]")

	if len(sys.argv) >= 2:
		try:
			open(sys.argv[1], 'r')
		except FileNotFoundError:
			raise FileNotFoundError(f"Can't open your input file: {sys.argv[1]}")

	# define the IO files
	if len(sys.argv) == 1:
		input_file = "UserCode.py"
		output_file = "Pytracker_output"
		listoflist_file = "listoflist"
	elif len(sys.argv) == 2:
		input_file = sys.argv[1]
		output_file = "Pytracker_output"
		listoflist_file = "listoflist"
	elif len(sys.argv) == 3:
		input_file = sys.argv[1]
		output_file = sys.argv[2]
		listoflist_file = "listoflist"
	elif len(sys.argv) == 4:
		input_file = sys.argv[1]
		output_file = sys.argv[2]
		listoflist_file = sys.argv[3]

	return input_file, output_file, listoflist_file


# 2022-06-25 使用递归式修改列表
# change nestedlist_to_listofint&tuple
def listoflist_to_listofinttuple(item, count_dict: dict):
	if type(item) == int:
		return item
	elif type(item) == list:
		while_line = item[0]
		try:
			count_dict[while_line] += 1
			clear_keys = [i for i in count_dict.keys() if i > while_line]
			for i in clear_keys:
				count_dict.pop(i)
		except:
			count_dict[while_line] = 1
		list_in_tuple = []
		for i in item:
			list_in_tuple.append(listoflist_to_listofinttuple(i, count_dict))
		return (count_dict[while_line], list_in_tuple)


def minus1_for_listoflist(item):
	if type(item) == int:
		return item - 1
	elif type(item) == list:
		minus1_list = []
		for i in item:
			minus1_list.append(minus1_for_listoflist(i))
		return minus1_list

def remove_singlelist_from_item(item):
	if type(item) == int:
		return item
	elif type(item) == list:
		return_list = []
		for i in item:
			if type(i) == list and len(i) == 1:
				continue
			return_list.append(remove_singlelist_from_item(i))
		return return_list

def get_step_json(program: Program, while_lines:list):
	start_statement = program.get_first_statement()
	end_statement = start_statement.get_next()
	while_line_set = list(set(while_lines))

	step_list = []
	while end_statement:
		start_location = (program.grid_indent[start_statement.line_no], start_statement.line_no)
		end_location = (program.grid_indent[end_statement.line_no], end_statement.line_no)

		# if start at a while_line, need an extra step: "circle"
		if start_statement.line_no in while_line_set:
			extra_step = {"type": "circle"}
			step_list.append(extra_step)
			cur_step = {"type": "step", "start": start_location, "end": end_location}
			step_list.append(cur_step)
		# if end at a while_line, need an extra step: "dash_line"
		elif end_statement.line_no in while_line_set:
			cur_step = {"type": "dash_line", "start": start_location, "end": end_location}
			step_list.append(cur_step)
		else:
			cur_step = {"type": "step", "start": start_location, "end": end_location}
			step_list.append(cur_step)

		start_statement = start_statement.get_next()
		end_statement = end_statement.get_next()

	max_depth = max(program.grid_indent.values())
	return {"depth": max_depth, "list": step_list}


def tabdict_to_gridindent(tab_dict: dict, while_lines: list) -> dict:
	if DEBUG_tabdict_to_gridindent: print(f"tab_dict == {tab_dict}\nwhile_lines == {while_lines}")
	if while_lines == []:
		return tab_dict
	while_list = list(set(while_lines))
	while_line_iter = 0
	cur_while = while_list[while_line_iter]

	grid_indent = tab_dict.copy()
	for i in [k for k, v in tab_dict.items() if k > cur_while and v > tab_dict[cur_while]]:
		if i not in while_list:
			if tab_dict[i] > tab_dict[cur_while]:
				grid_indent[i] = tab_dict[cur_while]
			else:
				while_line_iter -= 1
				cur_while = while_list[while_line_iter]
				grid_indent[i] = tab_dict[cur_while]
		else:
			while_line_iter += 1
			cur_while = while_list[while_line_iter]
		if DEBUG_tabdict_to_gridindent:
			print(f"i == {i}\ngrid_indent == {grid_indent}\ncur_while == {cur_while}")

	if DEBUG_tabdict_to_gridindent:
		print(f"tab_dict == \t{tab_dict}\ngrid_indent == \t{grid_indent}")
	return grid_indent


if __name__ == "__main__":
	# =====================================================
	# ===========   Stage 01 : previous_check   ===========
	# =====================================================
	input_file, output_file, listoflist_file = pre_execute_check()

	# format with yapf3 before create test_script
	os.system(f"yapf -i {input_file}")
	# base on input file, create a test script with main() method
	do_usercode_have_main = create_test_file(input_file, "test_script_with_main.py")
	test_script_with_main = __import__("test_script_with_main")

	# clean the execution txt before start a new tracer
	clean_content_in_file(output_file)
	clean_content_in_file(output_file+".stdout")

	# create tracer
	tracer = my_trace.Trace(ignoredirs=[sys.prefix, sys.exec_prefix], trace=1, count=1, outfile=output_file)
	# tracer method 01: from main method
	tracer.run(test_script_with_main.__name__ + ".main()")
	# tracer method 02: from read()
	# tracer.run(open(input_file).read())

	# =====================================================
	# ============   Stage 02 : main_tracing   ============
	# =====================================================
	# trace the whole execution, return a ListOfList
	listoflist_result, tab_dict, while_lines = trace_execution_tracking(tracer, output_file)

	# ADD: 2022-06-25 minus1_for_item add, used for minusing 1 for every item in the listoflist
	if do_usercode_have_main == False:
		listoflist_result = minus1_for_listoflist(listoflist_result)
		tab_dict = dict(zip([i - 1 for i in tab_dict.keys()], [i - 1 for i in tab_dict.values()]))
		while_lines = [i - 1 for i in while_lines]

	# ADD: 2022-06-26 remove single_list -> "[0-9]" from the listoflist_result
	listoflist_result = remove_singlelist_from_item(listoflist_result)

	# write listoflist_result into listoflist_file
	with open(listoflist_file, 'w') as listoflist_out:
		listoflist_out.write(str(listoflist_result))
	listoflist_out.close()

	# clean after execution
	delete_file(test_script_with_main.__name__ + ".py")  # delete test_script_with_main for UserCode_test_file

	# =====================================================
	# =========   Stage 03 : convert_to_program   =========
	# =====================================================
	# convert ListOfList into TupleOfIntAndTuple
	count_tab = {}
	TupleOfIntAndTuple = listoflist_to_listofinttuple(listoflist_result, count_tab)
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
	step_json = get_step_json(program, while_lines)
