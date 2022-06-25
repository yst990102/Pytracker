from typing import List


Print_Forward  = 0
Print_Backward = 1

creation_print = False

class Statement():
    def __init__(self, program) -> None:
        self.__previous = None
        self.__next     = None
        
        self.program  = program
    
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
    def __init__(self, steps:List[List], program) -> None:
        super().__init__(program)
        
        if creation_print: print(f"---- create {self.__class__.__name__} {steps}")
        self.general_steps = steps
        self.steps = []
        self.while_line_no = self.general_steps[0]
        
        # classify iteration to program.while_loops attribute
        assert(isinstance(self.program, Program))
        self.program.add_while_loop(self)
            
    def inner_bi_linklist_set(self) -> None:
        # set the inner bi-linklist in self.steps
        for i in range(len(self.steps)):
            if i != 0:
                self.steps[i].set_previous(self.steps[i-1])
            if i != len(self.steps) - 1:
                self.steps[i].set_next(self.steps[i+1])
        return

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

    def print_info(self) -> None:
        print(f"==== {self.__class__.__name__} {hex(id(self))} =====")
        for  step in self.steps:
            step.print_info()
        print(f"previous = {self.__previous}, next = {self.__next}")
    
    def print_val(self) -> None:
        print(self.general_steps, end=" ")

class Basic_Iteration(Iteration):
    def __init__(self, steps:List[List], program) -> None:
        super().__init__(steps, program)
        
        self.add_sub_statements(steps)
        self.inner_bi_linklist_set()
        
    def add_sub_statements(self, steps:List[List]) -> None:
        # add statements for self.steps
        for step in steps:
            new_statement = Assignment(step, self.program)
            self.steps.append(new_statement)

class Nested_Iteration(Iteration):    
    def __init__(self, steps:tuple, program) -> None:
        super().__init__(steps, program)
        self.subloop_iterations = []
        
        self.add_sub_statements(steps)
        self.inner_bi_linklist_set()
    
    def add_sub_statements(self, steps:tuple) -> None:
        # add statements for self.steps
        for step in steps[1]:
            if isinstance(step, int):
                new_statement = Assignment(step, self.program)
            elif isinstance(step, tuple):
                if all(isinstance(i, int) for i in step):
                    new_statement = Basic_Iteration(step, self.program)
                else:
                    new_statement = Nested_Iteration(step, self.program)
                self.subloop_iterations.append(new_statement)
            self.steps.append(new_statement)
    
    def print_info(self) -> None:
        super().print_info()
        print(f"{self.__class__.__name__} {hex(id(self))} subloop_iterations = {self.subloop_iterations}")
    
class Assignment(Statement):
    def __init__(self, line_no:int, program) -> None:
        super().__init__(program)
        if creation_print: print(f"---- create {self.__class__.__name__} {line_no}")
        self.line_no = line_no

    def print_info(self) -> None:
        print(f"==== {self.__class__.__name__} {hex(id(self))} =====")
        print(f"line_no == {self.line_no}")
        print(f"previous = {self.__previous}, next = {self.__next}")
        
    def print_val(self) -> None:
        print(self.line_no, end=" ")

class Program():
    def __init__(self, tupleofinttuple: tuple, tab_dict:dict) -> None:
        self.initial_tupleofinttuple = tupleofinttuple
        self.tab_dict = tab_dict
        
        self.statements = []
        self.while_loops = []
        
        for step_no_index in range(len(self.initial_tupleofinttuple[1])):
            if isinstance(self.initial_tupleofinttuple[1][step_no_index], int):
                new_statement = Assignment(self.initial_tupleofinttuple[1][step_no_index], self)
            elif isinstance(self.initial_tupleofinttuple[1][step_no_index], tuple):
                if all(isinstance(i, int) for i in self.initial_tupleofinttuple[1][step_no_index]):
                    new_statement = Basic_Iteration(self.initial_tupleofinttuple[1][step_no_index], self)
                else:
                    new_statement = Nested_Iteration(self.initial_tupleofinttuple[1][step_no_index], self)
            self.add_statement(new_statement)
    
    def add_while_loop(self, new_iteration:Iteration):
        new_while_line_no = new_iteration.while_line_no
        
        refered_found = False
        for while_loop_info in self.while_loops:
            cur_while_line_no, cur_while_iterations = while_loop_info["while_line_no"], while_loop_info["iterations"]
            if new_while_line_no == cur_while_line_no:
                cur_while_iterations.append(new_iteration)
                refered_found = True
                break
        if not refered_found:
            self.while_loops.append({"while_line_no": new_iteration.while_line_no, "iterations": [new_iteration]})
        
        # 06-07 test for print out self.while_loops
        # self.print_while_loops_inlayer()
        
    def print_while_loops_inlayer(self):
        for while_loop_info in self.while_loops:
            while_line_no, iterations = while_loop_info["while_line_no"], while_loop_info["iterations"]
            print(f"while_loop_info == {while_loop_info}")
            for iteration in iterations:
                print(iteration.general_steps)
    
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
    
    def add_statement(self, statement:Statement) -> None:
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
        
    def remove_statement(self, statement:Statement) -> None:
        for cur_statement in self.statements:
            if cur_statement == statement:
                cur_statement.get_previous().set_next(cur_statement.get_next())
                cur_statement.get_next().set_previous(cur_statement.get_previous())
                return
        
    def print_statements(self) -> None:
        for statement in self.statements:
            statement.print_info()
            
    def print_linklist(self, direction:int, end="") -> None:
        try:
            assert(direction == Print_Forward or direction == Print_Backward)
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
