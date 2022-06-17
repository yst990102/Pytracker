import os, sys
from helper_functions import clean_content_in_file, create_test_file, delete_file
from Pytracker import trace_execution_tracking
import my_trace

if __name__ == "__main__":
	test_cases = os.listdir("./test_cases")
	parsing_input_file   = [i for i in test_cases if "." not in i]
	parsing_output_file  = [i+".out" for i in parsing_input_file]
	parsing_trace_file   = [i+".trace" for i in parsing_input_file]
	expected_output_file = [i for i in test_cases if ".expected" in i]
	
	parsing_input_file.sort()
	parsing_output_file.sort()
	parsing_trace_file.sort()
	expected_output_file.sort()
	
	print(parsing_input_file)
	print(parsing_output_file)
	print(parsing_trace_file)
	print(expected_output_file)

	assert(len(parsing_input_file) == len(expected_output_file))
	file_number = len(parsing_input_file)
	
	for i in range(file_number):
		print(f"------ Generate Tests for {parsing_input_file[i]} ------")
		input_file, output_file, trace_file = parsing_input_file[i], parsing_output_file[i], parsing_trace_file[i]
		
		with open("test_cases/"+input_file, 'r') as f_in:
			input_file_content = f_in.read()
		f_in.close()
		
		# create tracer	
		tracer = my_trace.Trace(ignoredirs=[sys.prefix, sys.exec_prefix], trace=1, count=1, outfile="test_cases/"+trace_file)
		tracer.run(input_file_content)
		# trace the whole execution, return a ListOfList
		parse_result = trace_execution_tracking(tracer, "test_cases/"+trace_file)
		print("parse_result == ", parse_result)
		
		with open("test_cases/"+output_file, 'w') as f:
			f.write(str(parse_result))
		f.close()