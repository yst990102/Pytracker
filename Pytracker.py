import sys
import trace
import os
import re
import traceback

# import user file
import sample1
import sample2

# switch of debug
debug_mode = False

# global switch
trace_switch = 1
traceback_switch = 1



if traceback_switch == 1:
    try:
        sample2.main()
    except Exception as e:
        if debug_mode: print("bug detected")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        
        # trackback summary
        traceback_summary = traceback.extract_tb(exc_traceback)
        for trackback_line in traceback_summary:
            print("filename = {}, line = {}, method = {}".format(trackback_line.filename, trackback_line.lineno, trackback_line.name))
        


    
if trace_switch == 1:

    # define the filename and output file of trace
    filename = "sample1.py"
    exec_result_file = "execution.txt"

    # call linux cmd to trace customer's execution
    os.system("python3 -m trace --trace ./{} | grep {} > ./{}".format(filename, filename, exec_result_file))

    # open the result file of trace
    exec_result = open(exec_result_file)
    exec_content = exec_result.readlines()

    # set a dict for the while loop in execution
    while_loop_dict = {}

    # parsing
    for line in exec_content:
        # use regular expression to match
        line_number = int(re.search("(\()(\d)(\):)(.*)", line.strip().replace(filename, "")).group(2))
        line_content = re.search("(\()(\d)(\):)(.*)", line.strip().replace(filename, "")).group(4)
        print("line {} == {}".format(line_number, line_content))
        if debug_mode : print(type(line_number), type(line_content))

        if "while" in line_content:
            if debug_mode: print("Warning: while loop detected.")
            while_loop_dict[line_content] = [i for i,v in enumerate(exec_content) if v == line]

    print(while_loop_dict)


    exec_result.close()
