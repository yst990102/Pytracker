import os
import re


# helper functions
def export_test_case_to_file(output_file:str, test_case:str) -> None:
	with open(output_file, "w") as f_write:
		f_write.write(test_case)
	f_write.close()
	return

def delete_file(file_name:str) -> None:
	os.remove(file_name)
	return

def display_file(file_name:str) -> None:
	with open(file_name, 'r') as f_read:
		content = f_read.read()
	print(content)
	f_read.close()

def isBracket_match(s:str) -> bool:
	finding = []
	for ch in s:
		if ch == '(':
			finding.append(')')
		elif ch == '[':
			finding.append(']')
		elif ch == '{':
			finding.append('}')
		elif ch.isdigit() or ch == ",":
			continue
		elif not finding or not ch == finding.pop(-1) :
			return False
	return len(finding) == 0

def del_line_in_file(filename, content):
	with open(filename, "r") as f:
		lines = f.readlines()
	with open(filename, "w") as f_w:
		for line in lines:
			if content in line:
				continue
			f_w.write(line)
	f.close()
	f_w.close()

def clean_content_in_file(filename):
	try:
		with open(filename, "r+") as f:
			f.seek(0)
			f.truncate()  # 清空文件
			f.close()
			return
	except FileNotFoundError:
		# file does not exist, create a blank file
		open(filename, 'w').close()
		return

def create_test_file(user_code_filename, test_script_filename):
		def_main_str = "def main():\n"
		if_NameEqMain_str = "\nif __name__ == \"__main__\":\n\tmain()"
		
		# ADD: 2022-06-25 return a signal variable to tell parse_test if usercode have main()
		do_main_contain = False
		
		try:
			with open(user_code_filename, 'r') as user_code:
				# nothing need to add, just create by read()
				if NameEqMain_check(user_code_filename):
					testing_user_code = user_code.read()
					do_main_contain = True
				# add main() and "if __name__ == ..."
				else:
					testing_user_code = def_main_str + "".join(["\t" + i for i in user_code.readlines()]) + if_NameEqMain_str
					do_main_contain = False
			user_code.close()
		except FileNotFoundError:
			raise FileNotFoundError("InputFile Not Found")
		
		# write to the test_script_file
		with open(test_script_filename, 'w') as user_code_output:
			user_code_output.write(testing_user_code)
		user_code_output.close()
		
		return do_main_contain

def NameEqMain_check(filename):
	with open(filename, 'r') as f:
		file_content = f.read()
		if re.search("if[ ]*__name__[ ]*==[ ]*\"__main__\"[ ]*:", file_content) and re.search("def[ ]*main[ ]*\([ ]*\)[ ]*:", file_content):
			return True
	return False
			
def add_main_to_file(file_name):
	return