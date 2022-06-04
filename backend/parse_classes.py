class Program():
    statements = []
    def __init__(self):
        return
    
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
    
    def print(self):
        for statement in self.statements:
            statement.print()

class Statement():
    def __init__(self):
        self.steps = []
        self.previous = None
        self.next     = None
    
    # set the previous statement
    def set_previous(self, previous):
        self.previous = previous
    
    # set the next statement
    def set_next(self, next):
        self.next = next
    
    # get the previous statement
    def get_previous(self):
        return self.previous
    
    # get the next statement
    def get_next(self):
        return self.next

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

    def print(self):
        print(f"==== While_Loop {hex(id(self))} =====")
        for  step in self.steps:
            step.print()
        print(f"previous = {self.previous}, next = {self.next}")
        
class Assignment(Statement):
    def __init__(self, line_no):
        super().__init__()
        print(f"---- create Assignment {line_no}")
        self.line_no = line_no

    def print(self):
        print(f"==== Assignment {hex(id(self))} =====")
        print(f"line_no == {self.line_no}")
        print(f"previous = {self.previous}, next = {self.next}")