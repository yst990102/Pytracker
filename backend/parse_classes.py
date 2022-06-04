class Program():
    statements = []
    def __init__(self):
        return
    
    def add_statement(self, statement):
        self.statements.append(statement)
    
    def print(self):
        for statement in self.statements:
            statement.print()

class Statement(object):
    def __init__(self):
        self.steps = []
        self.previous = None
        self.next     = None

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
        print(f"==== While_Loop {self.general_steps} printing =====")
        for  step in self.steps:
            step.print()
        
class Assignment(Statement):
    def __init__(self, line_no):
        super().__init__()
        print(f"---- create Assignment {line_no}")
        self.line_no = line_no

    def print(self):
        print(f"==== Assignment {self.line_no} printing =====")
        print(f"line_no == {self.line_no}")