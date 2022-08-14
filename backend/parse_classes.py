Print_Forward = 0
Print_Backward = 1

creation_print = False


class Statement():

	def __init__(self, program, path) -> None:
		self.__previous = None
		self.__next = None
		self.path = path

		self.program = program

	# set the previous statement
	def set_previous(self, previous) -> None:
		if isinstance(self, Assignment):
			self.__previous = previous
		elif isinstance(self, Iteration):
			pointer = self.get_first_inner_step()
			pointer.__previous = previous

	# set the next statement
	def set_next(self, next) -> None:
		if isinstance(self, Assignment):
			self.__next = next
		elif isinstance(self, Iteration):
			pointer = self.get_last_inner_step()
			pointer.__next = next

	# get the previous statement
	def get_previous(self):
		pointer = self.__previous
		if isinstance(pointer, Assignment):
			return pointer
		elif isinstance(pointer, Iteration):
			return pointer.get_last_inner_step()

	# get the next statement
	def get_next(self):
		pointer = self.__next
		if isinstance(pointer, Assignment):
			return pointer
		elif isinstance(pointer, Iteration):
			return pointer.get_first_inner_step()


class Iteration(Statement):

	def __init__(self, steps: tuple, program, path) -> None:
		super().__init__(program, path)

		if creation_print:
			print(f"---- create {self.__class__.__name__} {steps}")
		self.general_steps = steps[1] # general step list, formed by integer
		self.while_line_no = self.general_steps[0]
		self.steps = [] # list of all Assignment/Iteration Nodes
		self.iteration_num = steps[0] # integer for iteration number

	def inner_bi_linklist_set(self) -> None:
		# set the inner bi-linklist in self.steps
		for i in range(len(self.steps)):
			if i != 0:
				self.steps[i].set_previous(self.steps[i - 1])
			if i != len(self.steps) - 1:
				self.steps[i].set_next(self.steps[i + 1])

	def get_first_inner_step(self) -> Statement:
		pointer = self.steps[0]
		if isinstance(pointer, Assignment):
			return pointer
		elif isinstance(pointer, Iteration):
			return pointer.get_first_inner_step()

	def get_last_inner_step(self) -> Statement:
		pointer = self.steps[-1]
		if isinstance(pointer, Assignment):
			return pointer
		elif isinstance(pointer, Iteration):
			return pointer.get_last_inner_step()

	# def set_enter_into_point(self):
	# 	assert (isinstance(self.get_first_inner_step(), Assignment))
	# 	self.get_first_inner_step().enter_into_iteration = self

	# def set_break_out_point(self):
	# 	assert (isinstance(self.get_last_inner_step(), Assignment))
	# 	self.get_last_inner_step().break_out_iterations += [self]

	def print_info(self) -> None:
		print(f"\n==== {self.__class__.__name__} {hex(id(self))} =====")
		print(f"iteration_num == {self.iteration_num}, while_line_no = {self.while_line_no}")
		for step in self.steps:
			step.print_info()

class Basic_While_Iteration(Iteration):

	def __init__(self, steps: tuple, program, path) -> None:
		super().__init__(steps, program, path)

		# classify iteration to program.while_loops attribute
		assert (isinstance(self.program, Program))
		self.program.add_while_loop(self)

		self.add_sub_statements(steps)
		self.inner_bi_linklist_set()

		# self.set_enter_into_point()
		# self.set_break_out_point()

	def add_sub_statements(self, steps: tuple) -> None:
		# add statements for self.steps
		for step in steps[1]:
			new_statement = Assignment(step, self.program, self.path + [self])
			self.steps.append(new_statement)


class Nested_While_Iteration(Iteration):

	def __init__(self, steps: tuple, program, path) -> None:
		super().__init__(steps, program, path)

		# classify iteration to program.while_loops attribute
		assert (isinstance(self.program, Program))
		self.program.add_while_loop(self)

		self.add_sub_statements(steps)
		self.inner_bi_linklist_set()

		# self.set_enter_into_point()
		# self.set_break_out_point()

	def add_sub_statements(self, steps: tuple) -> None:
		# add statements for self.steps
		for step in steps[1]:
			if isinstance(step, int):
				new_statement = Assignment(step, self.program, self.path + [self])
			elif isinstance(step, tuple):
				if all(isinstance(i, int) for i in step):
					new_statement = Basic_While_Iteration(step, self.program, self.path + [self])
				else:
					new_statement = Nested_While_Iteration(step, self.program, self.path + [self])
			self.steps.append(new_statement)


class Assignment(Statement):

	def __init__(self, line_no: int, program, path) -> None:
		super().__init__(program, path)
		if creation_print:
			print(f"---- create {self.__class__.__name__} {line_no}")
		self.line_no = line_no

		# self.enter_into_iteration = None
		# self.break_out_iterations = []

	def print_info(self) -> None:
		print(f"==== {self.__class__.__name__} {hex(id(self))} =====")
		print(f"line_no == {self.line_no}")
		print(f"previous = {self.get_previous()}, next = {self.get_next()}")
		print(f"path = {self.path}")
		# print(f"enter_into_iteration = {self.enter_into_iteration}, break_out_iterations = {self.break_out_iterations}")

	def print_val(self) -> None:
		if isinstance(self.path[-1], Iteration):
			print(f"{self.line_no}, itr_num = {self.path[-1].iteration_num}", end=" ")
		else:
			print(f"{self.line_no}", end=" ")


class Program():

	def __init__(self, TupleOfIntAndTuple: tuple, tab_dict: dict, grid_indent: dict) -> None:
		self.TupleOfIntAndTuple = TupleOfIntAndTuple
		self.tab_dict = tab_dict
		self.grid_indent = grid_indent  # stored but not in use

		self.statements = []
		self.while_loops = []  # classify iterations by while_line, not in use

		for step_no_index in range(len(self.TupleOfIntAndTuple[1])):
			if isinstance(self.TupleOfIntAndTuple[1][step_no_index], int):
				new_statement = Assignment(self.TupleOfIntAndTuple[1][step_no_index], self, [self])
			elif isinstance(self.TupleOfIntAndTuple[1][step_no_index], tuple):
				if all(isinstance(i, int) for i in self.TupleOfIntAndTuple[1][step_no_index]):
					new_statement = Basic_While_Iteration(self.TupleOfIntAndTuple[1][step_no_index], self, [self])
				else:
					new_statement = Nested_While_Iteration(self.TupleOfIntAndTuple[1][step_no_index], self, [self])
			self.add_statement(new_statement)
		
		# IMPORTANT: this is implementation for the filter of Pytracker
		self.filt_algo_implement()

	def add_while_loop(self, new_iteration: Iteration):
		new_while_path = new_iteration.path

		refered_found = False
		for while_loop_info in self.while_loops:
			cur_while_path, cur_while_iterations = while_loop_info["path"], while_loop_info["iterations"]
			if new_while_path == cur_while_path:
				cur_while_iterations.append(new_iteration)
				refered_found = True
				break
		if not refered_found:
			self.while_loops.append({"path": new_while_path, "iterations": [new_iteration]})
	
	def filt_algo_implement(self):
		for while_loop_info in self.while_loops:
			while_path, while_iterations = while_loop_info["path"], while_loop_info["iterations"]

			while_iteration_set = []
			for while_iteration in while_iterations[:-1]:
				if while_iteration.general_steps not in while_iteration_set:
					while_iteration_set.append(while_iteration.general_steps)
				else:
					self.move_out_from_linklist(while_iteration)

				
	def get_first_statement(self) -> Statement:
		pointer = self.statements[0]
		if isinstance(pointer, Assignment):
			return pointer
		elif isinstance(pointer, Iteration):
			return pointer.get_first_inner_step()

	def get_last_statement(self) -> Statement:
		pointer = self.statements[-1]
		if isinstance(pointer, Assignment):
			return pointer
		elif isinstance(pointer, Iteration):
			return pointer.get_last_inner_step()

	def add_statement(self, statement: Statement) -> None:
		# first statement in program, no need to set_previous or set_next
		if len(self.statements) < 1:
			self.statements.append(statement)
			return
		# everytime append a new statement
		# set_previous & set_next for new statemenet
		# set_next for the previous statement in self.statements
		else:
			# new_statement set_previous and set_next
			statement.set_previous(self.statements[-1])
			statement.set_next(None)

			# previous statement in self.statements set_next
			self.statements[-1].set_next(statement)

			self.statements.append(statement)

	def move_out_from_linklist(self, statement: Statement) -> None:
		if isinstance(statement, Iteration):
			self.move_out_iteration(statement)
		elif isinstance(Statement, Assignment):
			self.move_out_assignment(statement)
		
	def move_out_assignment(self, assignment: Assignment) -> None:
		prev_node = assignment.get_previous()
		afte_node = assignment.get_next()
		
		if prev_node != None:
			prev_node.set_next(afte_node)
		if afte_node != None:
			afte_node.set_previous(prev_node)
		
	def move_out_iteration(self, iteration: Iteration) -> None:
		prev_node = iteration.get_first_inner_step().get_previous()
		afte_node = iteration.get_last_inner_step().get_next()
		
		if prev_node != None:
			prev_node.set_next(afte_node)
		if afte_node != None:
			afte_node.set_previous(prev_node)

	# ============= printing ways of program =============
	def print_statements(self) -> None:
		for statement in self.statements:
			statement.print_info()

	def print_linklist(self, direction: int, end="") -> None:
		try:
			assert (direction == Print_Forward or direction == Print_Backward)
		except:
			raise Exception(f"Direction for {self.print_linklist.__name__} is not acceptable.")

		if direction == Print_Forward:
			if isinstance(self.statements[0], Assignment):
				pointer_statement = self.statements[0]
			elif isinstance(self.statements[0], Iteration):
				pointer_statement = self.statements[0].get_first_inner_step()

			while pointer_statement:
				pointer_statement.print_val()
				if pointer_statement.get_next():
					print(" -> ", end=end)
				pointer_statement = pointer_statement.get_next()
		elif direction == Print_Backward:
			if isinstance(self.statements[-1], Assignment):
				pointer_statement = self.statements[-1]
			elif isinstance(self.statements[-1], Iteration):
				pointer_statement = self.statements[-1].get_last_inner_step()

			while pointer_statement:
				pointer_statement.print_val()
				if pointer_statement.get_previous():
					print(" -> ", end=end)
				pointer_statement = pointer_statement.get_previous()
		print()

	def print_while_loops_inlayer(self):
		for while_loop_info in self.while_loops:
			while_line_no, iterations = while_loop_info["while_line_no"], while_loop_info["iterations"]
			print(f"while_loop_info == {while_loop_info}")
			for iteration in iterations:
				print(iteration.general_steps)
