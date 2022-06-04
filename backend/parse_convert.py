from parse_classes import Print_Backward, Print_Forward, Program, While_Loop, Assignment

case_1 = [3, 4, 5, [6, 7, 8, 9]]
case_2 = [2, [3, 4, 5, [6, 7, 8, 9]]]
case_3 = [2, [3, 4, 5, [6, 7, 8, 9]], [3, 4, 5, [6, 7, 8, 9]]]
case_4  = [2, [3, 4, 5, [6, 7, 8, 9]], [3, 4, 5, [6, 7, 8, 9]], [3, 4, 5, [6, 9]], [3, 4, 5, [6], 9, 10, 11], 12]

case = case_4

classes_steps = Program()

for step_no_index in range(len(case)):
    if isinstance(case[step_no_index], int):
        new_statement = Assignment(case[step_no_index])
    elif isinstance(case[step_no_index], list):
        new_statement = While_Loop(case[step_no_index])
        
    classes_steps.add_statement(new_statement)

print("""
=================================================
============== Statements Printing ==============
=================================================
""")

classes_steps.print_statements()

print("""
=================================================
=============== Forward Printing ================
=================================================
""")
classes_steps.print_linklist(Print_Forward)


print("""
=================================================
=============== Backward Printing ===============
=================================================
""")
classes_steps.print_linklist(Print_Backward)

