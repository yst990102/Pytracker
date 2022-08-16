import pathlib
import sys
import re
import parse
import json
from yapf.yapflib.yapf_api import FormatFile, FormatCode

try:
	import backend.my_trace as my_trace
except:
	import my_trace as my_trace
try:
	import backend.helper_functions as hf
except:
	import helper_functions as hf
try:
	import backend.parse_classes as parse_classes
except:
	import parse_classes as parse_classes

current_absolute_path = str(pathlib.Path(__file__).parent.resolve())

# DEBUG switches
DEBUG_parse_strListOfList_into_ListOfList = False


def trace_execution_tracking(result_file):
	# steps -- all the execution steps
	# formate -- [(line_no, local_variables), (..), ...]
	steps_info = []
	while_lines = []
	if_else_lines = []
	tab_dict = {}

	# delete the initial <string>(1) line in the execution output
	hf.del_line_in_file(result_file, "<string>")

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

				steps_info.append((line_no, local_variables))

	exec_result.close()

	all_line_nos = [line_no for (line_no, _) in steps_info]
	all_local_variables = [local_variables for (_, local_variables) in steps_info]
	tab_dict = dict(sorted(tab_dict.items()))

	# parse str_ListOfList into ListOfList
	listoflist = parse_strListOfList_into_ListOfList(all_line_nos, while_lines[:], tab_dict)

	print(f"trace_execution_tracking : listoflist == {listoflist}")
	print(f"trace_execution_tracking : tab_dict == {tab_dict}")
	print(f"trace_execution_tracking : while_lines == {while_lines}")
	print(f"trace_execution_tracking : if_else_lines == {if_else_lines}\n")
	return listoflist, tab_dict, while_lines, if_else_lines


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
				if stack == []:
					stack.append(while_lines[0])
					result = result + "[" + str(line_no)
					result = result.replace(",]", "],")
					if DEBUG_parse_strListOfList_into_ListOfList:
						print(f"{line_no}\t new loop statement_1\t {stack}\t {result}")
				elif tab_dict[stack[-1]] < tab_dict[line_no]:
					stack.append(while_lines[0])
					result = result + "[" + str(line_no)
					result = result.replace(",]", "],")
					if DEBUG_parse_strListOfList_into_ListOfList:
						print(f"{line_no}\t new loop statement_2\t {stack}\t {result}")
				elif tab_dict[stack[-1]] == tab_dict[line_no]:
					del stack[-1]
					stack.append(while_lines[0])
					result = result + "][" + str(line_no)
					result = result.replace(",]", "],")
					if DEBUG_parse_strListOfList_into_ListOfList:
						print(f"{line_no}\t new loop statement_3\t {stack}\t {result}")
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
		assert (hf.isBracket_match(result) == True)
	except:
		print(f"ERROR: isBracket_match Failed! result == {result}, stack == {stack}")
		exit(1)

	return eval(result)


def parse_convert_TupleOfIntTuple_into_Program(TupleOfIntAndTuple, tab_dict: dict, grid_indent: dict):
	return parse_classes.Program(TupleOfIntAndTuple, tab_dict, grid_indent)


def backend_main(usercode=None):
	# =====================================================
	# ===========   Stage 01 : previous_check   ===========
	# =====================================================
	global reformatted_code
	if usercode == None:
		usercode = open(current_absolute_path + "/" + "UserCode.py", 'r').read()
		# format with yapf3 before create test_script
		reformatted_code, encoding, changed = FormatFile(filename=f"{current_absolute_path}/UserCode.py", style_config=f"{current_absolute_path}/.style.yapf")
	else:
		reformatted_code, changed = FormatCode(unformatted_source=usercode, style_config=f"{current_absolute_path}/.style.yapf")

	# clean the execution txt before start a new tracer
	hf.clean_content_in_file(current_absolute_path + "/" + "Pytracker_output")

	# create tracer
	tracer = my_trace.Trace(ignoredirs=[sys.prefix, sys.exec_prefix], trace=1, count=1, outfile=current_absolute_path + "/" + "Pytracker_output")
	tracer.run(reformatted_code)

	# =====================================================
	# ============   Stage 02 : main_tracing   ============
	# =====================================================
	# trace the whole execution, return a ListOfList
	global listoflist
	listoflist, tab_dict, while_lines, if_else_lines = trace_execution_tracking(current_absolute_path + "/" + "Pytracker_output")

	# remove single_list -> "[0-9]" from the listoflist
	listoflist = hf.remove_singlelist_from_listoflist(listoflist)
	listoflist = hf.remove_if_else_lines_from_listoflist(if_else_lines, listoflist)

	# write listoflist into "listoflist"
	with open(current_absolute_path + "/" + "listoflist", 'w') as listoflist_out:
		listoflist_out.write(str(listoflist))
	listoflist_out.close()

	# =====================================================
	# =========   Stage 03 : convert_to_program   =========
	# =====================================================
	# convert ListOfList into TupleOfIntAndTuple
	TupleOfIntAndTuple = hf.ListOfList_to_ListOfIntAndTuple(listoflist)
	# write listoflist into "listoflist"
	with open(current_absolute_path + "/" + "TupleOfIntAndTuple", 'w') as TupleOfIntAndTuple_out:
		TupleOfIntAndTuple_out.write(str(TupleOfIntAndTuple))
	TupleOfIntAndTuple_out.close()

	grid_indent = hf.tabdict_to_gridindent(tab_dict, while_lines)
	# then convert into Program
	program = parse_convert_TupleOfIntTuple_into_Program(TupleOfIntAndTuple, tab_dict, grid_indent)

	# TEST: all available print ways testing for program
	# program.print_statements()
	# program.print_linklist(parse_classes.Print_Forward)
	# program.print_linklist(parse_classes.Print_Backward)
	# program.print_while_loops_inlayer()

	# =====================================================
	# ===========   Stage 03 : get_step_json   ============
	# =====================================================
	# method 01 : get json from program
	global step_json
	step_json = hf.get_step_json(program)
	# method 02 : get json from listoflist
	# hf.listoflist_to_json(0, listoflist, [])
	# step_json = {"d": 5, "list": step_list_in_json}

	# write step_json into "step_json"
	with open(current_absolute_path + "/" + "step_json.json", "w") as step_json_file_write:
		json.dump(step_json, step_json_file_write)
	step_json_file_write.close()


if __name__ == "__main__":
	backend_main()
