from parse_classes import Print_Backward, Print_Forward
from parse_classes import Basic_While_Loop, Nested_While_Loop, Program, Assignment

case_1     = [3, 4, 5, [6, 7, 8, 9]]
tab_dict_1 = {3:1, 4:1, 5:1, 6:1, 7:2, 8:2, 9:2}

case_2     = [2, [3, 4, 5, [6, 7, 8, 9], [6, 7, 9]]]
tab_dict_2 = {2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3}

case_3     = [2, [3, 4, 5, [6, 7, 8, 9], [6, 7, 9]], [3, 4, 5, [6, 7, 8, 9]]]
tab_dict_3 = {2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3}

case_4     = [2, [3, 4, 5, [6, 7, 8, 9], [6, 7, 9]], [3, 4, 5, [6, 7, 8, 9]], [3, 4, 5, [6, 9]], [3, 4, 5, [6], 9, 10, 11], 12]
tab_dict_4 = {2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3, 10:3, 11:3, 12:3}

case_5     = [2, [3, 4, 5, [6, [7, 8], 9], [6, [7], 9]], [3, 4, 5, [6, [7], 8, 9]]]
tab_dict_5 = {2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3}


case = case_5

program = Program()

for step_no_index in range(len(case)):
    if isinstance(case[step_no_index], int):
        new_statement = Assignment(case[step_no_index], program)
    elif isinstance(case[step_no_index], list):
        if all(isinstance(i, int) for i in case[step_no_index]):
            new_statement = Basic_While_Loop(case[step_no_index], program)
        else:
            new_statement = Nested_While_Loop(case[step_no_index], program)
    program.add_statement(new_statement)

print("""
=================================================
============== Statements Printing ==============
=================================================
""")

program.print_statements()

print("""
=================================================
=============== Forward Printing ================
=================================================
""")
program.print_linklist(Print_Forward)


print("""
=================================================
=============== Backward Printing ===============
=================================================
""")
program.print_linklist(Print_Backward)

print("""
=================================================
============= while_loops Printing ==============
=================================================
""")
program.print_while_loops_inlayer()

