
swithc_statement_print = False

class Program():
    statements = []
    def __init__(self):
        return
    
    def add_statement(self, statement):
        if len(self.statements) < 1:
            self.statements.append(statement)
            print("no need to set previous/next")
            return
        else:
            statement.set_previous(self.statements[-1])
            statement.set_next(None)
            
            self.statements[-1].set_next(statement)
            
            self.statements.append(statement)
            
            print("previous/next set")
    
    def print(self):
        for statement in self.statements:
            statement.print()

class Statement():
    def __init__(self):
        self.steps = []
        self.previous = None
        self.next     = None
        
    def set_previous(self, previous):
        self.previous = previous
        
    def set_next(self, next):
        self.next = next

class While_Loop(Statement):
    general_steps = []
    def __init__(self, steps):
        super().__init__()
        print(f"---- create While_Loop {steps}")
        
        self.general_steps = steps
        for step in steps:
            if isinstance(step, int):
                new_statement = Assignment(step)
            elif isinstance(step, list):
                new_statement = While_Loop(step)
            self.steps.append(new_statement)
            
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