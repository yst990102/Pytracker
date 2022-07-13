import os
import sys
from my_trace import Trace
import re
import parse

# import helper_functions
# file_op helpers
from helper_functions import ListOfList_to_ListOfIntAndTuple, create_test_file, del_line_in_file, delete_file, clean_content_in_file
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
DEBUG_listoflist_to_json = False

step_list_in_json = []


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

				local_variables = vari_parse[0]
				local_variables = re.sub("<function", "'<function", local_variables)
				local_variables = re.sub(">", ">'", local_variables)
				local_variables = eval(local_variables)

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

	if DEBUG_parse_strListOfList_into_ListOfList:
		print("before listoflist evaluated", result)
	parse_result = eval(result)
	if DEBUG_parse_strListOfList_into_ListOfList:
		print("after listoflist evaluated", parse_result)

	return parse_result


def parse_convert_TupleOfIntTuple_into_Program(TupleOfIntAndTuple, tab_dict: dict, grid_indent: dict):
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


def minus1_for_listoflist(item):
	if type(item) == int:
		return item - 1
	elif type(item) == list:
		minus1_list = []
		for i in item:
			minus1_list.append(minus1_for_listoflist(i))
		return minus1_list


# remove single_list == remove the last loop statement check
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


# remove if_else_lines from listoflist
def remove_if_else_lines_from_listoflist(if_else_lines, listoflist):
	if all(isinstance(item, int) for item in listoflist):
		return [x for x in listoflist if x not in if_else_lines]
	else:
		return_list = []
		for i in listoflist:
			if isinstance(i, list):
				return_list.append(remove_if_else_lines_from_listoflist(if_else_lines, i))
			elif isinstance(i, int):
				if i not in if_else_lines:
					return_list.append(i)
		return return_list


def get_step_json(program: Program, while_lines: list):
	start_statement = program.get_first_statement()
	end_statement = start_statement.get_next()

	step_list = []
	while end_statement:
		start_location = start_statement.line_no - 1
		end_location = end_statement.line_no - 1

		entered_iteration = end_statement.enter_into_iteration
		breaked_iterations = start_statement.break_out_iterations
		exiting_iterations = end_statement.break_out_iterations
		enter_iteration_under_same_while_loop = False
		try:
			for breaked_iteration in breaked_iterations:
				if breaked_iteration.while_line_no == entered_iteration.while_line_no:
					enter_iteration_under_same_while_loop = True
		except:
			pass
		finally:
			# case 1: simply enter into a loop
			# need: step, circle, while_start
			if entered_iteration and not breaked_iterations:
				print("========== case 01 ==========")
				start_of_entered_iteration = entered_iteration.while_line_no - 1
				step_list.append({"type": "step", "start": start_location, "end": end_location})
				step_list.append({"type": "circle", "start": start_of_entered_iteration})
				step_list.append({"type": "while_start", "depth": -1})
			# case 2: from iteration_1 to iteration_2, which belongs to same while-loop
			# need: step, circle
			elif entered_iteration and breaked_iterations and enter_iteration_under_same_while_loop:
				print("========== case 02 ==========")
				start_of_entered_iteration = entered_iteration.while_line_no - 1
				step_list.append({"type": "circle", "start": start_of_entered_iteration})
			# case 3: break from a while-loop, get into a normal step
			# need: step, while_end
			elif not entered_iteration and breaked_iterations:
				print("========== case 03 ==========")
				step_list.append({"type": "step", "start": start_location, "end": end_location})
				for breaked_iteration in breaked_iterations:
					start_of_breaked_iteration = breaked_iteration.while_line_no - 1
					end_of_breaked_iteration = breaked_iteration.get_last_inner_step().line_no - 1
					step_list.append({"type": "while_end", "start": start_of_breaked_iteration, "end": end_of_breaked_iteration})
			# case 4: break from a while-loop, get into another while-loop
			# need: step, while_end, circle, while_start
			elif entered_iteration and breaked_iterations and not enter_iteration_under_same_while_loop:
				print("========== case 04 ==========")
				step_list.append({"type": "step", "start": start_location, "end": end_location})
				for breaked_iteration in breaked_iterations:
					start_of_breaked_iteration = breaked_iteration.while_line_no - 1
					end_of_breaked_iteration = breaked_iteration.get_last_inner_step().line_no - 1
					step_list.append({"type": "while_end", "start": start_of_breaked_iteration, "end": end_of_breaked_iteration})
				start_of_entered_iteration = entered_iteration.while_line_no - 1
				step_list.append({"type": "circle", "start": start_of_entered_iteration})
				step_list.append({"type": "while_start", "depth": -1})
			elif not entered_iteration and not breaked_iterations:
				print("========== case 05 ==========")
				step_list.append({"type": "step", "start": start_location, "end": end_location})

			start_statement = start_statement.get_next()
			end_statement = end_statement.get_next()

	# TODO: need to find a way to calculate the maximum depth
	max_depth = 5
	return {"depth": max_depth, "list": step_list}


def listoflist_to_json(cur_depth, listoflist, while_stack) -> None:
	index = 0
	while index < len(listoflist) - 1:
		p1, _ = get_first(listoflist[index])
		p2, enter_loop = get_first(listoflist[index + 1])

		if not enter_loop:
			if isinstance(listoflist[index], int):
				if DEBUG_listoflist_to_json:
					print(f"step, {p1} => {p2}")
				step_list_in_json.append({"type": "step", "start": p1, "end": p2})
			elif isinstance(listoflist[index], list):
				if DEBUG_listoflist_to_json:
					print(f"step, {listoflist[index][-1]} => {p2}")
				step_list_in_json.append({"type": "step", "start": listoflist[index][-1], "end": p2})
		else:
			entered_loop = listoflist[index + 1]

			if p1 != p2:
				if DEBUG_listoflist_to_json:
					print(f"step, {p1} => {p2}")
				step_list_in_json.append({"type": "step", "start": p1, "end": p2})

			if DEBUG_listoflist_to_json:
				print(f"circle, {p2}")
			step_list_in_json.append({"type": "circle", "start": p2})

			if p2 not in while_stack:
				while_stack.append(p2)
				if DEBUG_listoflist_to_json:
					print(f"while_start, {cur_depth}")
				step_list_in_json.append({"type": "while_start", "depth": cur_depth})

			listoflist_to_json(cur_depth + 1, entered_loop, while_stack)

			try:
				follow_items = listoflist[index + 2]
				if isinstance(follow_items, int):
					while_stack.pop()
					if DEBUG_listoflist_to_json:
						print(f"while_end, {entered_loop[0]} => {entered_loop[-1]}")
					step_list_in_json.append({"type": "while_end", "start": entered_loop[0], "end": entered_loop[-1]})

				elif isinstance(follow_items, list) and p2 != follow_items[0]:
					if DEBUG_listoflist_to_json:
						print("wtf???")
			except:
				continue
		index += 1


def get_first(item):
	if isinstance(item, int):
		return (item, False)
	elif isinstance(item, list):
		return (item[0], True)


def tabdict_to_gridindent(tab_dict: dict, while_lines: list) -> dict:
	if DEBUG_tabdict_to_gridindent:
		print(f"tab_dict == {tab_dict}\nwhile_lines == {while_lines}")
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


def backend_main():
	# =====================================================
	# ===========   Stage 01 : previous_check   ===========
	# =====================================================
	input_file, output_file, listoflist_file = pre_execute_check()

	# format with yapf3 before create test_script
	os.system(f"yapf -i {input_file}")

	# clean the execution txt before start a new tracer
	clean_content_in_file(output_file)

	# create tracer
	tracer = Trace(ignoredirs=[sys.prefix, sys.exec_prefix], trace=1, count=1, outfile=output_file)
	tracer.run(open(input_file).read())

	# =====================================================
	# ============   Stage 02 : main_tracing   ============
	# =====================================================
	# trace the whole execution, return a ListOfList
	listoflist_result, tab_dict, while_lines, if_else_lines = trace_execution_tracking(tracer, output_file)

	# ADD: 2022-06-26 remove single_list -> "[0-9]" from the listoflist_result
	listoflist_result = remove_singlelist_from_item(listoflist_result)
	listoflist_result = remove_if_else_lines_from_listoflist(if_else_lines, listoflist_result)

	# write listoflist_result into listoflist_file
	with open(listoflist_file, 'w') as listoflist_out:
		listoflist_out.write(str(listoflist_result))
	listoflist_out.close()

	# =====================================================
	# =========   Stage 03 : convert_to_program   =========
	# =====================================================
	# convert ListOfList into TupleOfIntAndTuple
	TupleOfIntAndTuple = ListOfList_to_ListOfIntAndTuple(listoflist_result, {})
	grid_indent = tabdict_to_gridindent(tab_dict, while_lines)
	# then convert into Program
	program = parse_convert_TupleOfIntTuple_into_Program(TupleOfIntAndTuple, tab_dict, grid_indent)

	# TEST: all available print ways testing for program
	program.print_statements()
	# program.print_linklist(Print_Forward)
	# program.print_linklist(Print_Backward)
	# program.print_while_loops_inlayer()

	# =====================================================
	# ===========   Stage 03 : get_step_json   ============
	# =====================================================
	print(f"listoflist_result == {listoflist_result}")
	# method 01 : get json from program
	step_json = get_step_json(program, while_lines)
	# method 02 : get json from listoflist
	# listoflist_to_json(0, listoflist_result, [])
	# step_json = {"d": 5, "list": step_list_in_json}

	print(f"step_json == {step_json}")

	return step_json


if __name__ == "__main__":
	backend_main()
