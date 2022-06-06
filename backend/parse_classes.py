from typing import List


Print_Forward  = 0
Print_Backward = 1

yst_personal_debug = True

class Statement():
    def __init__(self) -> None:
        self.previous = None
        self.next     = None
    
    # set the previous statement
    def set_previous(self, previous) -> None:
        if isinstance(self, Assignment):
            self.previous = previous
        elif isinstance(self, While_Loop):
            pointer = self.get_first_inner_step()
            pointer.previous = previous
    
    # set the next statement
    def set_next(self, next) -> None:
        if isinstance(self, Assignment):
            self.next = next
        elif isinstance(self, While_Loop):
            pointer = self.get_last_inner_step()
            pointer.next = next
    
    # get the previous statement
    def get_previous(self):
        pointer = self.previous
        if isinstance(pointer, Assignment):
            return pointer
        elif isinstance(pointer, While_Loop):
            return pointer.get_last_inner_step()
    
    # get the next statement
    def get_next(self):
        pointer = self.next
        if isinstance(pointer, Assignment):
            return pointer
        elif isinstance(pointer, While_Loop):
            return pointer.get_first_inner_step()

class While_Loop(Statement):
    def __init__(self, steps:List[List]) -> None:
        super().__init__()
        
        if yst_personal_debug: print(f"---- create {self.__class__.__name__} {steps}")
        self.general_steps = steps
        self.steps = []
            
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
        elif isinstance(pointer, While_Loop):
            return pointer.get_first_inner_step()
            
    def get_last_inner_step(self) -> Statement:
        pointer = self.steps[-1]
        if isinstance(pointer, Assignment):
            return pointer
        elif isinstance(pointer, While_Loop):
            return pointer.get_last_inner_step()

    def print_info(self) -> None:
        if yst_personal_debug: print(f"==== {self.__class__.__name__} {hex(id(self))} =====")
        for  step in self.steps:
            step.print_info()
        if yst_personal_debug: print(f"previous = {self.previous}, next = {self.next}")
    
    def print_val(self) -> None:
        if yst_personal_debug: print(self.general_steps, end=" ")

class Basic_While_Loop(While_Loop):
    def __init__(self, steps:List[List]) -> None:
        super().__init__(steps)
        
        self.add_sub_statements(steps)
        self.inner_bi_linklist_set()
        
    def add_sub_statements(self, steps:List[List]) -> None:
        # add statements for self.steps
        for step in steps:
            new_statement = Assignment(step)
            self.steps.append(new_statement)

class Nested_While_Loop(While_Loop):    
    def __init__(self, steps:List[List]) -> None:
        super().__init__(steps)
        self.sub_while_loops = []
        
        self.add_sub_statements(steps)
        self.inner_bi_linklist_set()
    
    def add_sub_statements(self, steps:List[List]) -> None:
        # add statements for self.steps
        for step in steps:
            if isinstance(step, int):
                new_statement = Assignment(step)
            elif isinstance(step, list):
                if all(isinstance(i, int) for i in step):
                    new_statement = Basic_While_Loop(step)
                else:
                    new_statement = Nested_While_Loop(step)
                self.sub_while_loops.append(new_statement)
                if yst_personal_debug: print(f"before append {self.sub_while_loops}")
                if yst_personal_debug: print(f"append {new_statement.__class__.__name__} {hex(id(new_statement))} to {self.__class__.__name__} {hex(id(self))}")
                if yst_personal_debug: print(f"after append {self.sub_while_loops}")
            self.steps.append(new_statement)
    
    def print_info(self) -> None:
        super().print_info()
        if yst_personal_debug: print(f"{self.__class__.__name__} {hex(id(self))} sub_while_loop = {self.sub_while_loops}")
    
class Assignment(Statement):
    def __init__(self, line_no:int) -> None:
        super().__init__()
        if yst_personal_debug: print(f"---- create {self.__class__.__name__} {line_no}")
        self.line_no = line_no

    def print_info(self) -> None:
        if yst_personal_debug: print(f"==== {self.__class__.__name__} {hex(id(self))} =====")
        if yst_personal_debug: print(f"line_no == {self.line_no}")
        if yst_personal_debug: print(f"previous = {self.previous}, next = {self.next}")
        
    def print_val(self) -> None:
        if yst_personal_debug: print(self.line_no, end=" ")

class Program():
    def __init__(self) -> None:
        self.statements = []
    
    def get_first_process(self) -> Statement:
        pointer = self.statements[0]
        if isinstance(pointer, Assignment):
            return pointer
        elif isinstance(pointer, While_Loop):
            return pointer.get_first_inner_step()
            
    def get_last_process(self) -> Statement:
        pointer = self.statements[-1]
        if isinstance(pointer, Assignment):
            return pointer
        elif isinstance(pointer, While_Loop):
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
    
    def print_statements(self) -> None:
        for statement in self.statements:
            statement.print_info()
            
    def print_linklist(self, direction:int, end="") -> None:
        try:
            assert(direction == Print_Forward or direction == Print_Backward)
        except:
            if yst_personal_debug: raise Exception(f"Direction for {self.print_linklist.__name__} is not acceptable.")
    
        if direction == Print_Forward:
            if isinstance(self.statements[0], Assignment):
                pointer_statement = self.statements[0]
            elif isinstance(self.statements[0], While_Loop):
                pointer_statement = self.statements[0].get_first_inner_step()

            while pointer_statement:
                pointer_statement.print_val()
                if yst_personal_debug: print(" -> ", end=end)
                pointer_statement = pointer_statement.get_next()
        elif direction == Print_Backward:
            if isinstance(self.statements[-1], Assignment):
                pointer_statement = self.statements[-1]
            elif isinstance(self.statements[-1], While_Loop):
                pointer_statement = self.statements[-1].get_last_inner_step()
                
            while pointer_statement:
                pointer_statement.print_val()
                if yst_personal_debug: print(" -> ", end=end)
                pointer_statement = pointer_statement.get_previous()
        if yst_personal_debug: print()
