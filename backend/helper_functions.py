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

def clean_txt_file(filename):
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

def NameEqMain_check(file_name):
	with open(file_name, 'r') as f:
		f_content = f.read()
		if re.search(f_content, "if[ ]*__name__[ ]*==[ ]*\"__main__\"[ ]*:"):
			# user input contains __name__ == __main__ structure
			return True
		else:
			return False
			
def add_main_to_file(file_name):
	return