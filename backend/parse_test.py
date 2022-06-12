import os
from helper_functions import clean_content_in_file, create_test_file, delete_file
from Pytracker import trace_execution_tracking

if __name__ == "__main__":
    test_cases = os.listdir("./test_cases")
    user_code_input_file = [i for i in test_cases if ".expected" not in i]
    parsing_output_file  = [i+".out" for i in user_code_input_file]
    parsing_trace_file   = [i+".trace" for i in user_code_input_file]
    expected_output_file = [i for i in test_cases if ".expected" in i]
    
    user_code_input_file.sort()
    parsing_output_file.sort()
    parsing_trace_file.sort()
    expected_output_file.sort()
    
    assert(len(user_code_input_file) == len(expected_output_file))
    file_number = len(user_code_input_file)
    
    for i in range(file_number):
        print(f"------ Generate Tests for {user_code_input_file[i]} ------")
        user_code_file, trace_output_file = user_code_input_file[i], parsing_trace_file[i]
        create_test_file("./test_cases/"+user_code_file, "UserCode.py")
        UserCode = __import__("UserCode")
        trace_execution_tracking("UserCode", "parse_test_output")
        clean_content_in_file("UserCode.py")
