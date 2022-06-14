import os
from helper_functions import clean_content_in_file, create_test_file, delete_file
from Pytracker import trace_execution_tracking

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
        input_file, output_file = parsing_input_file[i], parsing_trace_file[i]
        os.system(f"python Pytracker.py test_cases/{input_file} test_cases/{output_file}")
