from Pytracker_exceptions import Direction_ERROR

Print_Forward  = 0
Print_Backward = 1

class Program():
    statements = []
    def __init__(self):
        return
    
    def get_first_process(self):
        pointer = self.statements[0]
        if isinstance(pointer, Assignment):
            return pointer
        elif isinstance(pointer, While_Loop):
            return pointer.get_first_inner_step()
            
    def get_last_process(self):
        pointer = self.statements[-1]
        if isinstance(pointer, Assignment):
            return pointer
        elif isinstance(pointer, While_Loop):
            return pointer.get_last_inner_step()
    
    def add_statement(self, statement):
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
    
    def print_statements(self):
        for statement in self.statements:
            statement.print_info()
            
    def print_linklist(self, direction, end=""):
        try:
            if (direction != Print_Forward and direction != Print_Backward):
                raise Direction_ERROR(direction)
        except Direction_ERROR as de:
            print(de)
    
        if direction == Print_Forward:
            pointer_statement = self.statements[0]
            while pointer_statement:
                pointer_statement.print_val()
                print(" -> ", end=end)
                pointer_statement = pointer_statement.get_next()
        elif direction == Print_Backward:
            pointer_statement = self.statements[-1]
            while pointer_statement:
                pointer_statement.print_val()
                print(" -> ", end=end)
                pointer_statement = pointer_statement.get_previous()
        print()

class Statement():
    def __init__(self):
        self.steps = []
        self.previous = None
        self.next     = None
    
    # set the previous statement
    def set_previous(self, previous):
        if isinstance(self, Assignment):
            self.previous = previous
        elif isinstance(self, While_Loop):
            pointer = self.get_first_inner_step()
            pointer.previous = previous
    
    # set the next statement
    def set_next(self, next):
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
    general_steps = []
    def __init__(self, steps):
        super().__init__()
        print(f"---- create While_Loop {steps}")
        
        # add statements for self.steps
        self.general_steps = steps
        for step in steps:
            if isinstance(step, int):
                new_statement = Assignment(step)
            elif isinstance(step, list):
                new_statement = While_Loop(step)
            self.steps.append(new_statement)

        # set the inner bi-linklist in self.steps
        for i in range(len(self.steps)):
            if i != 0:
                self.steps[i].set_previous(self.steps[i-1])
            if i != len(self.steps) - 1:
                self.steps[i].set_next(self.steps[i+1])
        return

    def get_first_inner_step(self):
        pointer = self.steps[0]
        if isinstance(pointer, Assignment):
            return pointer
        elif isinstance(pointer, While_Loop):
            return pointer.get_first_inner_step()
            
    def get_last_inner_step(self):
        pointer = self.steps[-1]
        if isinstance(pointer, Assignment):
            return pointer
        elif isinstance(pointer, While_Loop):
            return pointer.get_last_inner_step()

    def print_info(self):
        print(f"==== While_Loop {hex(id(self))} =====")
        for  step in self.steps:
            step.print_info()
        print(f"previous = {self.previous}, next = {self.next}")
    
    def print_val(self):
        print(self.general_steps, end=" ")
        
class Assignment(Statement):
    def __init__(self, line_no):
        super().__init__()
        print(f"---- create Assignment {line_no}")
        self.line_no = line_no

    def print_info(self):
        print(f"==== Assignment {hex(id(self))} =====")
        print(f"line_no == {self.line_no}")
        print(f"previous = {self.previous}, next = {self.next}")
        
    def print_val(self):
        print(self.line_no, end=" ")