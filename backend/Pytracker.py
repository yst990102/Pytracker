import pathlib
import sys
import re
import time
import json
from yapf.yapflib.yapf_api import FormatFile, FormatCode

import my_trace as my_trace
import helper_functions as hf

backend_absolute_path  = str(pathlib.Path(__file__).parent.resolve())
frontend_absolute_path = str(pathlib.Path(__file__).parent.parent.resolve()) + "/frontend"
sys.path.insert(0, frontend_absolute_path)

# SIGNAL
SIG_TIME_COST = 0
SIG_FILE_IO_OFF = 1

def trace_execution_tracking(execution_processes):
	while_lines = []
	if_else_lines = []
	tab_dict = {}

	all_line_nos = []
	all_local_variables = []
	all_stdouts = []

	for process in execution_processes:
		line_no = process['line_no']
		line_content = process["line_content"]
		local_variables = process["local_variables"]
		stdout = process["stdout"]

		all_line_nos.append(line_no)
		all_local_variables.append(local_variables)
		all_stdouts.append(stdout)

		# CASE 1: IF_STATEMENT
		if_search = re.search(r"if\s*(.*)\s*:", line_content)
		if if_search:
			if_else_lines.append(line_no)

		# CASE 2: WHILE_LOOP
		# use regular expression to match
		while_loop_search = re.search(r"while\s*(.*)\s*:", line_content)
		if (while_loop_search):
			while_lines.append(line_no)

		# CASE 3: FOR_LOOP
		for_loop_search = re.search(r"for\s*(.*)\s*:", line_content)
		if (for_loop_search):
			while_lines.append(line_no)

		tab_dict[line_no] = line_content.count('\t')

	# parse str_ListOfList into ListOfList
	listoflist = hf.parse_strListOfList_into_ListOfList(all_line_nos, while_lines, tab_dict)
	# integrate listoflist and all_local_variables and all_stdouts
	listoflist_integrated = hf.integrate_listoflist_with_local_variables(listoflist, all_local_variables, all_stdouts)
	
	return listoflist, listoflist_integrated, tab_dict, while_lines, if_else_lines


def backend_main(*test_signals, usercode=None):
	# region [Stage 1.1](reformat user's code)
	if SIG_TIME_COST in test_signals:
		reformat_start_time = time.time()
	global reformatted_code
	if usercode == None:
		usercode = open(backend_absolute_path + "/" + "UserCode.py", 'r').read()
		# format with yapf3 before create test_script
		reformatted_code, encoding, changed = FormatFile(filename=f"{backend_absolute_path}/UserCode.py", style_config=f"{backend_absolute_path}/.style.yapf")
	else:
		reformatted_code, changed = FormatCode(unformatted_source=usercode, style_config=f"{backend_absolute_path}/.style.yapf")
	if SIG_TIME_COST in test_signals:
		reformat_end_time = time.time()
	if SIG_TIME_COST in test_signals:
		print(f"[Stage 1.1](reformat user's code) \t\t\t: {reformat_end_time - reformat_start_time} seconds")
	# endregion

	# region [Stage 1.2](pre_clean the wrote_output file)
	if SIG_TIME_COST in test_signals:
		file_clean_start_time = time.time()

	if SIG_FILE_IO_OFF not in test_signals:
		hf.clean_content_in_file(backend_absolute_path + "/" + "listoflist")
		hf.clean_content_in_file(backend_absolute_path + "/" + "listoflist_integrated")
		hf.clean_content_in_file(backend_absolute_path + "/" + "TupleOfIntAndTuple")
		hf.clean_content_in_file(backend_absolute_path + "/" + "step_json.json")

	if SIG_TIME_COST in test_signals:
		file_clean_end_time = time.time()
	if SIG_TIME_COST in test_signals:
		print(f"[Stage 1.2](pre_clean the wrote_output file) \t\t: {file_clean_end_time - file_clean_start_time} seconds")
	# endregion

	# region [Stage 1.3](create tracer and run)
	if SIG_TIME_COST in test_signals:
		tracer_start_time = time.time()

	tracer = my_trace.Trace(ignoredirs=[sys.prefix, sys.exec_prefix], trace=1, count=1)
	tracer.run(reformatted_code)

	if SIG_TIME_COST in test_signals:
		tracer_end_time = time.time()
	if SIG_TIME_COST in test_signals:
		print(f"[Stage 1.3](create tracer and run) \t\t\t: {tracer_end_time - tracer_start_time} seconds")
	# endregion

	# region [Stage 2.1](generate list of list via trace_output)
	if SIG_TIME_COST in test_signals:
		listoflist_start_time = time.time()

	# trace the whole execution, return a ListOfList
	global listoflist
	listoflist, listoflist_integrated, tab_dict, while_lines, if_else_lines = trace_execution_tracking(my_trace.execution_processes)

	# remove single_list -> "[0-9]" from the listoflist
	listoflist = hf.remove_singlelist_from_listoflist(listoflist)
	listoflist_integrated = hf.remove_singlelist_from_listoflist_integrated(listoflist_integrated)
	listoflist = hf.remove_if_else_lines_from_listoflist(if_else_lines, listoflist)
	listoflist_integrated = hf.remove_if_else_lines_from_listoflist_integrated(if_else_lines, listoflist_integrated)

	if SIG_FILE_IO_OFF not in test_signals:
		# write listoflist into "listoflist"
		with open(backend_absolute_path + "/" + "listoflist", 'w') as listoflist_out:
			listoflist_out.write(str(listoflist))
		listoflist_out.close()
		with open(backend_absolute_path + "/" + "listoflist_integrated", 'w') as listoflist_integrated_out:
			listoflist_integrated_out.write(str(listoflist_integrated))
		listoflist_integrated_out.close()

	if SIG_TIME_COST in test_signals:
		listoflist_end_time = time.time()
	if SIG_TIME_COST in test_signals:
		print(f"[Stage 2.1](generate list of list via trace_output) \t: {listoflist_end_time - listoflist_start_time} seconds")
	# endregion

	# region [Stage 2.2](convert list of list to program)
	if SIG_TIME_COST in test_signals:
		program_generate_start_time = time.time()

	# convert ListOfList into TupleOfIntAndTuple
	TupleOfIntAndTuple = hf.ListOfList_to_ListOfIntAndTuple(listoflist)
	TupleOfIntAndTuple_integrated = hf.ListOfList_to_ListOfIntAndTuple_integrated(listoflist_integrated)

	if SIG_FILE_IO_OFF not in test_signals:
		# write listoflist into "listoflist"
		with open(backend_absolute_path + "/" + "TupleOfIntAndTuple", 'w') as TupleOfIntAndTuple_out:
			TupleOfIntAndTuple_out.write(str(TupleOfIntAndTuple))
		TupleOfIntAndTuple_out.close()

	grid_indent = hf.tabdict_to_gridindent(tab_dict, while_lines)
	# then convert into Program
	program_integrated = hf.parse_convert_TupleOfIntAndTuple_integrated_into_Program(TupleOfIntAndTuple_integrated, tab_dict, grid_indent)

	# TEST: all available print ways testing for program
	# program.print_statements()
	# program.print_linklist(parse_classes.Print_Forward)
	# program.print_linklist(parse_classes.Print_Backward)
	# program.print_while_loops_inlayer()

	if SIG_TIME_COST in test_signals:
		program_generate_end_time = time.time()
	if SIG_TIME_COST in test_signals:
		print(f"[Stage 2.2](convert list of list to program) \t\t: {program_generate_end_time - program_generate_start_time} seconds")
	# endregion

	# region [Stage 3.1](get step_json via program)
	if SIG_TIME_COST in test_signals:
		json_generate_start_time = time.time()

	global step_json
	step_json = hf.get_step_json(program_integrated)

	if SIG_FILE_IO_OFF not in test_signals:
		# write step_json into "step_json"
		with open(backend_absolute_path + "/" + "step_json.json", "w") as step_json_file_write:
			json.dump(step_json, step_json_file_write)
		step_json_file_write.close()

	if SIG_TIME_COST in test_signals:
		json_generate_end_time = time.time()
	if SIG_TIME_COST in test_signals:
		print(f"[Stage 3.1](get step_json via program) \t\t\t: {json_generate_end_time - json_generate_start_time} seconds")
	# endregion

	if SIG_TIME_COST in test_signals:
		print(f"--------------- All Stages --------------- \t\t: {json_generate_end_time - reformat_start_time} seconds")
	return listoflist, TupleOfIntAndTuple, program_integrated, step_json


if __name__ == "__main__":
	backend_main()
