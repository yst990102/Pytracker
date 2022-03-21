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
        


steps = []
visited_line = {}
    
if trace_switch == 1:

    # define the filename and output file of trace
    filename = "sample1.py"
    exec_result_file = "execution.txt"

    # call linux cmd to trace customer's execution
    os.system("python3 -m trace --trace ./{} | grep {} > ./{}".format(filename, filename, exec_result_file))

    # open the result file of trace
    exec_result = open(exec_result_file)
    exec_content = exec_result.readlines()

    # parsing
    for line in exec_content:
        # use regular expression to match
        line_number = int(re.search("(\()(\d)(\):)(.*)", line.strip().replace(filename, "")).group(2))
        line_content = re.search("(\()(\d)(\):)(.*)", line.strip().replace(filename, "")).group(4)
        # print("line {} == {}".format(line_number, line_content))

        if debug_mode : print(type(line_number), type(line_content))

        space = False
        tab = False
        space_sep = re.match(r"^[ ]{4}", line_content)
        if not space_sep:
            tab_sep = re.match(r"^[\t]{1}", line_content)
        else:
            res = re.sub(r"^[ ]{4}", "", line_content)
            space = True
            print(res)

        if tab_sep: 
            res = re.sub(r"^[\t]{1}", "", line_content)
            tab = True

        is_while = re.search("^(while).*[:]$", res)
        whitespace_match = None
        if tab:
            whitespace_match = re.search(r"^[\t]{1}", res)
        elif space:
            whitespace_match = re.search(r"^[ ]{4}", res)

        if is_while and line_number not in visited_line:
            if debug_mode: print("Warning: while loop detected.")
            dict_cont = line_content.strip()
        
        visited_line[line_number] = line_content


    exec_result.close()

# print(visited_line)
# print(steps)