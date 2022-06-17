import os, sys, parse, re
from helper_functions import clean_content_in_file, create_test_file, delete_file, del_line_in_file, isBracket_match
import my_trace

if __name__ == "__main__":
	tests_folder_absolute_dir = "/home/yst990102/cs4951/Pytracker/backend/test_cases"
	test_cases = os.listdir(tests_folder_absolute_dir)
	
	parsing_input_file       = [i for i in test_cases if "." not in i]
	parsing_listoflist_file  = [i+".out" for i in parsing_input_file]
	parsing_output_file      = [i+".stdout" for i in parsing_input_file]
	parsing_trace_file       = [i+".trace" for i in parsing_input_file]
	
	expected_output_file     = [i for i in test_cases if ".expected" in i]
	
	parsing_input_file.sort()
	parsing_listoflist_file.sort()
	parsing_output_file.sort()
	parsing_trace_file.sort()
	
	expected_output_file.sort()

	assert(len(parsing_input_file) == len(expected_output_file))
	file_number = len(parsing_input_file)
	
	for i in range(file_number):
		print(f"------ Generate Tests for {parsing_input_file[i]} ------")
		input_file_dir      = tests_folder_absolute_dir+"/"+parsing_input_file[i]
		listoflist_file_dir = tests_folder_absolute_dir+"/"+parsing_listoflist_file[i]
		output_file_dir     = tests_folder_absolute_dir+"/"+parsing_output_file[i]
		trace_file_dir      = tests_folder_absolute_dir+"/"+parsing_trace_file[i]
		
		print(input_file_dir)
		print(listoflist_file_dir)
		print(output_file_dir)
		print(trace_file_dir)
		
		os.system(f"python Pytracker.py {input_file_dir} {trace_file_dir} {listoflist_file_dir} > {output_file_dir}")
		
		
		