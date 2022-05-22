class node:
    next = None
    content = None


class normal_node(node):
    def __init__(self, content) -> None:
        self.content = content
    
    def __next__(self, next_node):
        self.next = next_node





class while_node(node):
    def __init__(self, lineno) -> None:
        self.lineno = lineno
        self.content = []

    def __next__(self, next_node):
        self.next = next_node
        
    def add(self, item):
        self.content.append(item)