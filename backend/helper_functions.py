from io import StringIO
import os
import parse_classes as parse_classes

# DEBUG switches
DEBUG_parse_strListOfList_into_ListOfList = False
DEBUG_listoflist_to_json = False
DEBUG_get_step_json = True


IS_WHILE = 0
IS_FOR = 1


# helper functions
def export_test_case_to_file(output_file: str, test_case: str) -> None:
	with open(output_file, "w") as f_write:
		f_write.write(test_case)
	f_write.close()
	return


def delete_file(file_name: str) -> None:
	os.remove(file_name)
	return


def display_file(file_name: str) -> None:
	with open(file_name, 'r') as f_read:
		content = f_read.read()
	print(content)
	f_read.close()

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

def isBracket_match(s: str) -> bool:
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
		elif not finding or not ch == finding.pop(-1):
			return False
	return len(finding) == 0


def TupleOfIntAndTuple_to_ListOfList(TupleOfIntAndTuple):
	if isinstance(TupleOfIntAndTuple, int):
		return TupleOfIntAndTuple
	elif isinstance(TupleOfIntAndTuple, tuple):
		iteration_no = TupleOfIntAndTuple[0]
		iteration_content = TupleOfIntAndTuple[1]
		if all(isinstance(x, int) for x in iteration_content):
			return iteration_content
		else:
			ret_list = []
			for i in iteration_content:
				ret_list.append(TupleOfIntAndTuple_to_ListOfList(i))
			return ret_list


# 2022-06-25 使用递归式修改列表
# change nestedlist_to_listofint&tuple
def ListOfList_to_ListOfIntAndTuple(item, count_dict=None):
	if count_dict == None:
		count_dict = {}
	if isinstance(item, int):
		return item
	elif isinstance(item, list):
		while_line = get_first_item(item)
		while_or_for = IS_WHILE if get_first_item(item) == item[0] else IS_FOR
		try:
			count_dict[while_line] += 1
			clear_keys = [i for i in count_dict.keys() if i > while_line]
			for i in clear_keys:
				count_dict.pop(i)
		except:
			if while_or_for == IS_FOR:
				count_dict[while_line] = 0
			elif while_or_for == IS_WHILE:
				count_dict[while_line] = 1

		list_in_tuple = []
		for i in item:
			list_in_tuple.append(ListOfList_to_ListOfIntAndTuple(i, count_dict))
		return (count_dict[while_line], list_in_tuple)
def ListOfList_to_ListOfIntAndTuple_integrated(item, count_dict=None):
	if count_dict == None:
		count_dict = {}
	
	if isinstance(item, dict):
		return item
	elif isinstance(item, list):
		while_line = get_first_item_integrated(item)['line_no']
		while_or_for = IS_WHILE if get_first_item_integrated(item) == item[0] else IS_FOR
		try:
			count_dict[while_line] += 1
			clear_keys = [i for i in count_dict.keys() if i > while_line]
			for i in clear_keys:
				count_dict.pop(i)
		except:
			if while_or_for == IS_FOR:
				count_dict[while_line] = 0
			elif while_or_for == IS_WHILE:
				count_dict[while_line] = 1

		list_in_tuple = []
		for i in item:
			list_in_tuple.append(ListOfList_to_ListOfIntAndTuple_integrated(i, count_dict))
		return (count_dict[while_line], list_in_tuple)

def get_first_item(item):
	if isinstance(item, int):
		return item
	elif isinstance(item, list):
		return get_first_item(item[0])
def get_first_item_integrated(item):
	if isinstance(item, dict):
		return item
	elif isinstance(item, list):
		return get_first_item_integrated(item[0])


def tabdict_to_gridindent(tab_dict: dict, while_lines: list) -> dict:
	if while_lines == []:
		return tab_dict
	while_list = list(set(while_lines))
	while_line_iter = 0
	cur_while = while_list[while_line_iter]

	grid_indent = tab_dict.copy()
	for i in [k for k, v in tab_dict.items() if k > cur_while and v > tab_dict[cur_while]]:
		if i not in while_list:
			if tab_dict[i] > tab_dict[cur_while]:
				grid_indent[i] = tab_dict[cur_while]
			else:
				while_line_iter -= 1
				cur_while = while_list[while_line_iter]
				grid_indent[i] = tab_dict[cur_while]
		else:
			while_line_iter += 1
			cur_while = while_list[while_line_iter]
	return grid_indent


def get_step_json(program:parse_classes.Program):
	start_statement = program.get_first_statement()
	end_statement = start_statement.get_next()
	assert(isinstance(start_statement, parse_classes.Assignment))
	assert(isinstance(end_statement, parse_classes.Assignment) or end_statement is None)

	cur_max = 1
	max_max = 1
	cur_or_max = False
	stack = []

	step_list = [{"type": "step", "start": 0, "end": start_statement.line_no, "local_variables": start_statement.local_variables, "stdout": start_statement.stdout}]
	while end_statement:
		start_location = start_statement.line_no
		end_location = end_statement.line_no
		# use path to judge
		# CASE 01: start a new while-loop
		if len(end_statement.path) > len(start_statement.path):
			if stack != []:
				cur_or_max = True
			entered_iteration = end_statement.path[-1]
			step_list.append({"type": "step", "start": start_location, "end": end_location, "local_variables": end_statement.local_variables, "stdout": end_statement.stdout})
			step_list.append({"type": "circle", "start": end_location, "iteration": entered_iteration.iteration_num, "local_variables": end_statement.local_variables, "stdout": end_statement.stdout})
			step_list.append({"type": "while_start", "depth": -1})
			stack.append(cur_max)
			cur_max += 1
		# CASE 02: end a while-loop and indent backward
		elif len(end_statement.path) < len(start_statement.path):			
			# HERE: test printing of Assignments' self.while_ends property
			# exit_str = ""
			# for while_end_iteration in start_statement.while_ends:
			# 	exit_str = exit_str + str(while_end_iteration.general_steps) + " ,"
			# if start_statement.while_ends:
			# 	print(f"{start_statement.line_no}: exit=={exit_str}")

			for while_end_iteration in start_statement.while_ends:
				step_list.append({"type": "while_end", "start": while_end_iteration.get_first_inner_step().line_no, "end": while_end_iteration.get_last_inner_step().line_no})
				# print(f"append start:{while_end_iteration.get_first_inner_step().line_no}, end:{while_end_iteration.get_last_inner_step().line_no}")
			
			if end_location in program.while_lines_set:
				entered_iteration = end_statement.path[-1]
				step_list.append({"type": "circle", "start": end_location, "iteration": entered_iteration.iteration_num, "local_variables": end_statement.local_variables, "stdout": end_statement.stdout})
			else:
				step_list.append({"type": "step", "start": start_location, "end": end_location, "local_variables": end_statement.local_variables, "stdout": end_statement.stdout})
			cur_max = stack.pop()
			cur_or_max = False
		else:
			if start_statement.path != end_statement.path:
				start_while_line_no = start_statement.path[-1].while_line_no
				end_while_line_no = end_statement.path[-1].while_line_no
				if start_while_line_no == end_while_line_no:
					# CASE 03: enter a new iteration which from same while-loop
					entered_iteration = end_statement.path[-1]
					step_list.append({"type": "circle", "start": end_location, "iteration": entered_iteration.iteration_num, "local_variables": end_statement.local_variables, "stdout": end_statement.stdout})
					cur_max = (cur_max + 1) if cur_or_max == True else (max_max + 1)
				else:
					# CASE 04: end current while-loop, then start and enter a parallel while-loop,
					ended_iteration = start_statement.path[-1]
					step_list.append({"type": "while_end", "start": ended_iteration.get_first_inner_step().line_no, "end": ended_iteration.get_last_inner_step().line_no})
					step_list.append({"type": "step", "start": start_location, "end": end_location, "local_variables": end_statement.local_variables, "stdout": end_statement.stdout})
					entered_iteration = end_statement.path[-1]
					step_list.append({"type": "circle", "start": end_location, "iteration": entered_iteration.iteration_num, "local_variables": end_statement.local_variables, "stdout": end_statement.stdout})
					step_list.append({"type": "while_start", "depth": -1})
					cur_max = stack.pop()
					cur_or_max = False
			# CASE 05: normal step
			else:
				step_list.append({"type": "step", "start": start_location, "end": end_location, "local_variables": end_statement.local_variables, "stdout": end_statement.stdout})
		max_max = max(cur_max, max_max)
		start_statement = start_statement.get_next()
		end_statement = end_statement.get_next()

	max_depth = max_max
	return {"d": max_depth, "list": step_list}


# remove single_list == remove the last loop statement check
def remove_singlelist_from_listoflist(listoflist):
	if isinstance(listoflist, int):
		return listoflist
	elif isinstance(listoflist, list):
		return_list = []
		for i in listoflist:
			if isinstance(i,list) and len(i) == 1:
				continue
			return_list.append(remove_singlelist_from_listoflist(i))
		return return_list
def remove_singlelist_from_listoflist_integrated(listoflist_integrated):
	if isinstance(listoflist_integrated, dict):
		return listoflist_integrated
	elif isinstance(listoflist_integrated, list):
		return_list = []
		for i in listoflist_integrated:
			if isinstance(i,list) and len(i) == 1:
				continue
			return_list.append(remove_singlelist_from_listoflist_integrated(i))
		return return_list

# remove if_else_lines from listoflist
def remove_if_else_lines_from_listoflist(if_else_lines, listoflist):
	if all(isinstance(item, int) for item in listoflist):
		return [x for x in listoflist if x not in if_else_lines]
	else:
		return_list = []
		for i in listoflist:
			if isinstance(i, list):
				return_list.append(remove_if_else_lines_from_listoflist(if_else_lines, i))
			elif isinstance(i, int):
				if i not in if_else_lines:
					return_list.append(i)
		return return_list
def remove_if_else_lines_from_listoflist_integrated(if_else_lines, listoflist_integrated):
	if all(isinstance(item, dict) for item in listoflist_integrated):
		return [x for x in listoflist_integrated if x['line_no'] not in if_else_lines]
	else:
		return_list = []
		for i in listoflist_integrated:
			if isinstance(i, list):
				return_list.append(remove_if_else_lines_from_listoflist_integrated(if_else_lines, i))
			elif isinstance(i, dict):
				if i['line_no'] not in if_else_lines:
					return_list.append(i)
		return return_list


# the str_parsing takes the MOST runtime of backend_main
def parse_strListOfList_into_ListOfList(all_line_nos, while_lines, tab_dict):
	if DEBUG_parse_strListOfList_into_ListOfList:
		print("========================== parse_strListOfList_into_ListOfList ==========================")
		print(f"all_line_nos == {all_line_nos}\nwhile_lines == {while_lines}\ntab_dict == {tab_dict}")

	# Create a stack, put it in from left to right, and pop one out every time the indentation is greater than or equal to.
	stack = []
	result = []
	for count, line_no in enumerate(all_line_nos):
		if while_lines == []:
			if stack == []:
				result.append(str(line_no))
				if DEBUG_parse_strListOfList_into_ListOfList:
					print(f"{line_no}\t out of loop\t {stack}\t {result}")
			elif tab_dict[line_no] > tab_dict[stack[-1]]:
				result.append(str(line_no))
				if DEBUG_parse_strListOfList_into_ListOfList:
					print(f"{line_no}\t in loop\t {stack}\t {result}")
			else:
				result.append("]")
				result.append(str(line_no))
				stack.pop()
				if DEBUG_parse_strListOfList_into_ListOfList:
					print(f"{line_no}\t outer break\t {stack}\t {result}")
		elif line_no == while_lines[0]:
			if line_no in stack:
				while stack[:].pop() != line_no:
					stack.pop()
					result.append("]")
				result.append("]")
				result.append("[")
				result.append(str(line_no))
				if DEBUG_parse_strListOfList_into_ListOfList:
					print(f"{line_no}\t next round loop, loop statement\t {stack}\t {result}")
			else:
				if stack == []:
					stack.append(while_lines[0])
					result.append("[")
					result.append(str(line_no))
					if DEBUG_parse_strListOfList_into_ListOfList:
						print(f"{line_no}\t new loop statement_1\t {stack}\t {result}")
				elif tab_dict[stack[-1]] < tab_dict[line_no]:
					stack.append(while_lines[0])
					result.append("[")
					result.append(str(line_no))
					if DEBUG_parse_strListOfList_into_ListOfList:
						print(f"{line_no}\t new loop statement_2\t {stack}\t {result}")
				elif tab_dict[stack[-1]] == tab_dict[line_no]:
					del stack[-1]
					stack.append(while_lines[0])
					result.append("][")
					result.append(str(line_no))
					if DEBUG_parse_strListOfList_into_ListOfList:
						print(f"{line_no}\t new loop statement_3\t {stack}\t {result}")
			del while_lines[0]
		else:
			if stack == []:
				result.append(str(line_no))
				if DEBUG_parse_strListOfList_into_ListOfList:
					print(f"{line_no}\t out of loop\t {stack}\t {result}")
			elif tab_dict[line_no] > tab_dict[stack[-1]]:
				result.append(str(line_no))
				if DEBUG_parse_strListOfList_into_ListOfList:
					print(f"{line_no}\t in loop\t {stack}\t {result}")
			else:
				result.append("]")
				result.append(str(line_no))
				stack.pop()
				if DEBUG_parse_strListOfList_into_ListOfList:
					print(f"{line_no}\t inner break\t {stack}\t {result}")

		if count < len(all_line_nos) - 1:
			result.append(",")

	# add remaining right bracket from stack.pop()
	result.append(len(stack) * "]")
	stack.clear()  # clear stack

	result.insert(0, "[")
	result.append("]")

	result = "".join(result)
	result = result.replace(",]", "],")
	result = result.replace("],]", "]],")

	try:
		assert (isBracket_match(result) == True)
	except:
		print(f"ERROR: isBracket_match Failed! result == {result}")
		exit(1)

	return eval(result)


def parse_convert_TupleOfIntAndTuple_integrated_into_Program(TupleOfIntAndTuple_integrated, tab_dict: dict, grid_indent: dict, while_lines):
	return parse_classes.Program(TupleOfIntAndTuple_integrated, tab_dict, grid_indent, while_lines)

def integrate_listoflist_with_local_variables(listoflist, all_local_variables, all_stdouts):
	# yielder for local_variables and listoflist
	def yield_locals():
		for i in all_local_variables:
			yield i
	def yield_stdouts():
		for i in all_stdouts:
			yield i
	def listoflist_yield(listoflist):
		if isinstance(listoflist, int):
			yield listoflist
		elif isinstance(listoflist, list):
			for i in listoflist:
				yield from listoflist_yield(i)
	
	# map method
	def map(line_no, local_variables, stdout):
		return {'line_no': line_no, "local_variables": local_variables, "stdout": stdout}
	
	# main integration method
	def integration(listoflist):
		if isinstance(listoflist, int):
			return map(listoflist, next(locals_iterator), next(stdout_iterator))
		elif isinstance(listoflist, list):
			return_list = []
			for i in listoflist:
				return_list.append(integration(i))
			return return_list
	
	# check listoflist length
	def listoflist_len(listoflist):
		if all(isinstance(i, int) for i in listoflist):
			return len(listoflist)
		else:
			length = 0
			for i in listoflist:
				if isinstance(i, int):
					length += 1
				if isinstance(i, list):
					length += listoflist_len(i)
			return length
		
	assert(listoflist_len(listoflist) == len(all_local_variables))
	locals_iterator = yield_locals()
	stdout_iterator = yield_stdouts()
	
	return integration(listoflist)

def get_general_steps(info):
	if isinstance(info, dict):
		return info['line_no']
	elif isinstance(info, tuple):
		return_list = []
		for i in info[1]:
			return_list.append(get_general_steps(i))
		return return_list