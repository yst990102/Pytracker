import sys
import my_trace
import re
import traceback
import parse


# import user file
import sample1
import sample2

# global switch
trace_switch = 1
traceback_switch = 1


def insert_line_into_steps(line, step):
	return

def clean_txt_file(filename):
	with open(filename, "r+") as f:
		f.seek(0)
		f.truncate()   #清空文件
		return

def traceback_bug_catch():
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
	return


def trace_execution_tracking(filename, result_file):
	print(
		"************************************************************\n" +
		"*************              trace               *************\n" +
		"************************************************************"
	)

	steps = []

	if trace_switch == 1:

		# call trace customer's execution
		tracer = my_trace.Trace(ignoredirs=[sys.prefix, sys.exec_prefix],trace=1,count=1,outfile=result_file)
		tracer.run("sample1.main()")

		# open the result file of trace
		exec_result = open(result_file)
		exec_content = exec_result.readlines()

		# parsing
		for line in exec_content:
			code_parse = parse.parse("{0}({1}): {2}", line)
			vari_parse = parse.parse("local_variables == {0}", line)
			
			#  if the line_content is (a line of code)
			if code_parse is not None:
				code_parse = list(code_parse)
				if filename == code_parse[0]:
					# use regular expression to match
					line_number = int(code_parse[1])
					line_content = code_parse[2]
					
					assert(type(line_number) == int)
					assert(type(line_content) == str)
					print(f"line {line_number}=={line_content}")
					
					# if it is a while loop
					while_loop_search = re.search(r"while\s*\((.*)\)\s*:", line_content)
					if (while_loop_search):
						while_statement = while_loop_search.group(0)
						while_judgement = while_loop_search.group(1)
						if (while_statement is not None):
							print(f"while_statement == {while_statement}")
							print(f"while_judgement == {while_judgement}")
       
					print("Tabs Count ==", line_content.count('\t'))
				
			# if the line_content is (a line of local_variables)
			elif vari_parse is not None:
				vari_parse = list(vari_parse)
				local_variables = eval(vari_parse[0])
				
				assert(type(local_variables) == dict)
				print(f"variable == {local_variables}")
			
		exec_result.close()



if __name__ == "__main__":
	
	traceback_bug_catch()
	
	# define the filename and output file of trace
	filename = "sample1.py"
	exec_result_file = "execution.txt"
	
	# clean the execution txt
	clean_txt_file(exec_result_file)
	
	trace_execution_tracking(filename, exec_result_file)

	