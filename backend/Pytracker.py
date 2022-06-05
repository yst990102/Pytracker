import os
import sys
import my_trace
import re
import traceback
import parse


# import user file
import sample1

# import helper_functions
# file_op helpers
from helper_functions import del_line_in_file, delete_file, clean_txt_file
# checkers
from helper_functions import isBracket_match
# classes and objects definition
from parse_classes import Assignment, Print_Backward, Print_Forward, Program, While_Loop



# global variables
SUCCESS = 1
FAILURE = 0

# global switch
trace_switch = 1
traceback_switch = 1

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
	
				if not exec_content:
					break
				else:				
        			# ===================================================================================
					# STEP 1: grab information for the code line
					# 0 for userfile_name, 1 for line_no, 2 for line_content
					code_parse = list(parse.parse("{0}({1}): {2}", exec_content[0]))
					a,b,c = list(parse.parse("{0}({1}): {2}", exec_content[0]))
					# print(code_parse)
					if filename == code_parse[0]:

						line_no = int(code_parse[1])
						line_content = code_parse[2]
						# CASE 1: IF_STATEMENT
						if_search = re.search(r"if\s*\((.*)\)\s*:", line_content)
						if if_search:
							continue

						# CASE 2: WHILE_LOOP
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

					# ===================================================================================
					# STEP 2: grab information for the local_variable line
					vari_parse = list(parse.parse("local_variables == {0}", exec_content[1]))
					local_variables = eval(vari_parse[0])
					steps_info.append((line_no, local_variables))
					# DONE: 2022-05-11 variable parsing correctly
					# print(f"variable == {local_variables}")
					# print(f"while_lines == {while_lines}, steps == {steps_info}, tab_dict == {tab_dict}")
		exec_result.close()
		# delete result_file after tracer_using
		delete_file(result_file)
		all_line_nos = [line_no for (line_no, _) in steps_info]

		# parse str_ListOfList into ListOfList
		parse_result = parse_strListOfList_into_ListOfList(all_line_nos, while_lines, tab_dict)
		print("list of list == ", parse_result)
		
		program = parse_convert_ListOfList_into_Program(parse_result)
		program.print_linklist(Print_Forward)
		program.print_linklist(Print_Backward)
		
	else:
		return	

def parse_strListOfList_into_ListOfList(all_line_nos, while_lines, tab_dict):  
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
	return parse_result
 
def parse_convert_ListOfList_into_Program(listoflist):
	program = Program()
	for statement_index in range(len(listoflist)):
		if isinstance(listoflist[statement_index], int):
			new_statement = Assignment(listoflist[statement_index])
		elif isinstance(listoflist[statement_index], list):
			new_statement = While_Loop(listoflist[statement_index])
			
		program.add_statement(new_statement)
	return program
	
 
if __name__ == "__main__":

	# 【non-necessary】pre-step: call traceback to check if any bug
	if not traceback_bug_catch():
		sys.exit("======== error occured ========")

	# define the UserFile and output file of execution process
	UserFile = sample1.__name__ + ".py"
	exec_result_file = "execution"

	# clean the execution txt before start a new tracer
	clean_txt_file(exec_result_file)

	# trace the whole execution process via my_tracer
	trace_execution_tracking(UserFile, exec_result_file)
