import sys
import my_trace
import re
import traceback

def insert_line_into_steps(line, step):
    return


if __name__ == "__main__":
    # import user file
    import sample1
    import sample2

    # global switch
    trace_switch = 1
    traceback_switch = 1

    print(
        "************************************************************\n" +
        "*************            traceback             *************\n" +
        "************************************************************"
    )

    if traceback_switch == 1:
        try:
            sample2.main()
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            
            # trackback summary
            traceback_summary = traceback.extract_tb(exc_traceback)
            for trackback_line in traceback_summary:
                print("filename = {}, line = {}, method = {}".format(trackback_line.filename, trackback_line.lineno, trackback_line.name))
            

    print(
        "************************************************************\n" +
        "*************              trace               *************\n" +
        "************************************************************"
    )

    steps = []

    if trace_switch == 1:

        # define the filename and output file of trace
        filename = "sample1.py"
        exec_result_file = "execution.txt"

        # call trace customer's execution
        tracer = my_trace.Trace(ignoredirs=[sys.prefix, sys.exec_prefix],trace=1,count=1,outfile=exec_result_file)
        tracer.run("sample1.main()")

        # open the result file of trace
        exec_result = open(exec_result_file)
        exec_content = exec_result.readlines()

        # parsing
        for line in exec_content:
            
            #  if the line_content is (a line of code)
            if filename in line:
                # use regular expression to match
                line_number = int(re.search(r"(\()(\d)(\):)(.*)", line.strip().replace(filename, "")).group(2))
                line_content = re.search(r"(\()(\d)(\):)(.*)", line.strip().replace(filename, "")).group(4)
                assert(type(line_number) == int)
                assert(type(line_content) == str)
                print(f"line {line_number}=={line_content}")
                
                # if it is a while loop
                if (re.search(r"while\s*\((.*)\)\s*:", line_content)):
                    while_statement = re.search(r"while\s*\((.*)\)\s*:", line_content).group(0)
                    while_judgement = re.search(r"while\s*\((.*)\)\s*:", line_content).group(1)
                    if (while_statement is not None):
                        print(f"while_statement == {while_statement}")
                        print(f"while_judgement == {while_judgement}")
                
            # if the line_content is (a line of local_variables)
            elif "local_variables" in line:
                local_variables = eval(re.match("{.*}", line.strip().replace("local_variables == ","")).group(0))
                assert(type(local_variables) == dict)
                print(f"variable == {local_variables}")
            
        exec_result.close()