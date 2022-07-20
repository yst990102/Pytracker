import os
import re

from parse_classes import Iteration, Program

DEBUG_listoflist_to_json = False
DEBUG_get_step_json = True


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
def ListOfList_to_ListOfIntAndTuple(item, count_dict={}):
	if type(item) == int:
		return item
	elif type(item) == list:
		while_line = item[0]
		try:
			count_dict[while_line] += 1
			clear_keys = [i for i in count_dict.keys() if i > while_line]
			for i in clear_keys:
				count_dict.pop(i)
		except:
			count_dict[while_line] = 1
		list_in_tuple = []
		for i in item:
			list_in_tuple.append(ListOfList_to_ListOfIntAndTuple(i, count_dict))
		return (count_dict[while_line], list_in_tuple)


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


def get_step_json(program: Program):
	start_statement = program.get_first_statement()
	end_statement = start_statement.get_next()

	step_list = []
	while_stack = []
	while end_statement:
		start_location = start_statement.line_no - 1
		end_location = end_statement.line_no - 1
		'''
		method 01: not fully worked
		entered_iteration = end_statement.enter_into_iteration
		breaked_iterations = start_statement.break_out_iterations
		exiting_iterations = end_statement.break_out_iterations
		enter_iteration_under_same_while_loop = False
		try:
			for breaked_iteration in breaked_iterations:
				if breaked_iteration.while_line_no == entered_iteration.while_line_no:
					enter_iteration_under_same_while_loop = True
		except:
			pass
		finally:
			# case 1: simply enter into a loop
			# need: step, circle, while_start
			if entered_iteration and not breaked_iterations:
				if DEBUG_get_step_json:
					print("========== case 01 ==========")
				start_of_entered_iteration = entered_iteration.while_line_no - 1
				step_list.append({"type": "step", "start": start_location, "end": end_location})
				step_list.append({"type": "circle", "start": start_of_entered_iteration})
				step_list.append({"type": "while_start", "depth": -1})
			# case 2: from iteration_1 to iteration_2, which belongs to same while-loop
			# need: step, circle
			elif entered_iteration and breaked_iterations and enter_iteration_under_same_while_loop:
				if DEBUG_get_step_json:
					print("========== case 02 ==========")
				start_of_entered_iteration = entered_iteration.while_line_no - 1
				step_list.append({"type": "circle", "start": start_of_entered_iteration})
			# case 3: break from a while-loop, get into a normal step
			# need: step, while_end
			elif not entered_iteration and breaked_iterations:
				if DEBUG_get_step_json:
					print("========== case 03 ==========")
				step_list.append({"type": "step", "start": start_location, "end": end_location})
				for breaked_iteration in breaked_iterations:
					start_of_breaked_iteration = breaked_iteration.while_line_no - 1
					end_of_breaked_iteration = breaked_iteration.get_last_inner_step().line_no - 1
					step_list.append({"type": "while_end", "start": start_of_breaked_iteration, "end": end_of_breaked_iteration})
			# case 4: break from a while-loop, get into another while-loop
			# need: step, while_end, circle, while_start
			elif entered_iteration and breaked_iterations and not enter_iteration_under_same_while_loop:
				if DEBUG_get_step_json:
					print("========== case 04 ==========")
				step_list.append({"type": "step", "start": start_location, "end": end_location})
				for breaked_iteration in breaked_iterations:
					start_of_breaked_iteration = breaked_iteration.while_line_no - 1
					end_of_breaked_iteration = breaked_iteration.get_last_inner_step().line_no - 1
					step_list.append({"type": "while_end", "start": start_of_breaked_iteration, "end": end_of_breaked_iteration})
				start_of_entered_iteration = entered_iteration.while_line_no - 1
				step_list.append({"type": "circle", "start": start_of_entered_iteration})
				step_list.append({"type": "while_start", "depth": -1})
			elif not entered_iteration and not breaked_iterations:
				if DEBUG_get_step_json:
					print("========== case 05 ==========")
				step_list.append({"type": "step", "start": start_location, "end": end_location})
			'''

		# method 02: use path to judge
		# CASE 01: start a new while-loop
		if len(end_statement.path) > len(start_statement.path):
			entered_iteration = end_statement.path[-1]

			step_list.append({"type": "step", "start": start_location, "end": end_location})
			step_list.append({"type": "circle", "start": end_location, "iteration": entered_iteration.iteration_num})
			step_list.append({"type": "while_start", "depth": -1})
		# CASE 02: end a while-loop
		elif len(end_statement.path) < len(start_statement.path):
			ended_iteration = start_statement.path[-1]

			step_list.append({"type": "while_end", "start": ended_iteration.get_first_inner_step().line_no - 1, "end": ended_iteration.get_last_inner_step().line_no - 1})
			step_list.append({"type": "step", "start": start_location, "end": end_location})
		else:
			# CASE 03: length equalled, entering a new iteration under same while-loop
			if start_statement.path != end_statement.path:
				step_list.append({"type": "circle", "start": end_location})
			# CASE 04: normal step
			else:
				step_list.append({"type": "step", "start": start_location, "end": end_location})

		start_statement = start_statement.get_next()
		end_statement = end_statement.get_next()

	# TODO: need to find a way to calculate the maximum depth
	max_depth = 5
	return {"depth": max_depth, "list": step_list}


step_list_in_json = []


def listoflist_to_json(cur_depth, listoflist, while_stack) -> None:
	index = 0
	while index < len(listoflist) - 1:
		p1, _ = get_first(listoflist[index])
		p2, enter_loop = get_first(listoflist[index + 1])

		if not enter_loop:
			if isinstance(listoflist[index], int):
				if DEBUG_listoflist_to_json:
					print(f"step, {p1} => {p2}")
				step_list_in_json.append({"type": "step", "start": p1, "end": p2})
			elif isinstance(listoflist[index], list):
				if DEBUG_listoflist_to_json:
					print(f"step, {listoflist[index][-1]} => {p2}")
				step_list_in_json.append({"type": "step", "start": listoflist[index][-1], "end": p2})
		else:
			entered_loop = listoflist[index + 1]

			if p1 != p2:
				if DEBUG_listoflist_to_json:
					print(f"step, {p1} => {p2}")
				step_list_in_json.append({"type": "step", "start": p1, "end": p2})

			if DEBUG_listoflist_to_json:
				print(f"circle, {p2}")
			step_list_in_json.append({"type": "circle", "start": p2})

			if p2 not in while_stack:
				while_stack.append(p2)
				if DEBUG_listoflist_to_json:
					print(f"while_start, {cur_depth}")
				step_list_in_json.append({"type": "while_start", "depth": cur_depth})

			listoflist_to_json(cur_depth + 1, entered_loop, while_stack)

			try:
				follow_items = listoflist[index + 2]
				if isinstance(follow_items, int):
					while_stack.pop()
					if DEBUG_listoflist_to_json:
						print(f"while_end, {entered_loop[0]} => {entered_loop[-1]}")
					step_list_in_json.append({"type": "while_end", "start": entered_loop[0], "end": entered_loop[-1]})

				elif isinstance(follow_items, list) and p2 != follow_items[0]:
					if DEBUG_listoflist_to_json:
						print("wtf???")
			except:
				continue
		index += 1


def get_first(item):
	if isinstance(item, int):
		return (item, False)
	elif isinstance(item, list):
		return (item[0], True)


# minus 1 for every item in the nested list
def minus1_for_listoflist(listoflist):
	if type(listoflist) == int:
		return listoflist - 1
	elif type(listoflist) == list:
		minus1_list = []
		for i in listoflist:
			minus1_list.append(minus1_for_listoflist(i))
		return minus1_list


# remove single_list == remove the last loop statement check
def remove_singlelist_from_listoflist(listoflist):
	if type(listoflist) == int:
		return listoflist
	elif type(listoflist) == list:
		return_list = []
		for i in listoflist:
			if type(i) == list and len(i) == 1:
				continue
			return_list.append(remove_singlelist_from_listoflist(i))
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
