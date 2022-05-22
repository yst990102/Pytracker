import sys
sys.path.append("..")
from while_parse import node, while_node, normal_node
import pytest

def nodes_print(head_node:node):
    while head_node != None:
        if head_node.__class__.__name__ == "normal_node":
            print(head_node.content, end="-")
        else:
            while_node_list = []
            for i in head_node.content:
                while_node_list.append(i.content)
            print(while_node_list, end="-")
        head_node = head_node.next
    print()

def test_this_1():
    test_input_execu_lines = [1,2,3,4,5,3,4,5,3,4,5,6,7]
    test_input_while_lines = [3]
    tab_dict = {1:1,2:1,3:1,4:2,5:2,6:1,7:1}
    
    node1 = normal_node(1)
    
    node2 = normal_node(2)
    node1.next = node2
    
    node3 = while_node(3)
    node2.next = node3
    
    node4 = normal_node(4)
    node3.add(node4)
    
    node5 = normal_node(5)
    node3.add(node5)
    
    
    nodes_print(node1)
    
    pass

if __name__ == "__main__":
    test_this_1()
