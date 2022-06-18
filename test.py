
import sys

case_1        = [3, 4, 5, [6, 7, 8, 9]]
case_1_ini    = [3, 4, 5, 6, 7, 8, 9]
while_lines_1 = [6]
tab_dict_1    = {3:1, 4:1, 5:1, 6:1, 7:2, 8:2, 9:2}

case_2        = [2, [3, 4, 5, [6, 7, 8, 9], [6, 7, 9]]]
case_2_ini    = [2, 3, 4, 5, 6, 7, 8, 9, 6, 7, 9]
while_lines_2 = [3, 6]
tab_dict_2    = {2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3}

case_3        = [2, [3, 4, 5, [6, 7, 8, 9], [6, 7, 9]], [3, 4, 5, [6, 7, 8, 9]]]
case_3_ini    = [2, 3, 4, 5, 6, 7, 8, 9, 6, 7, 9, 3, 4, 5, 6, 7, 8, 9]
while_lines_3 = [3, 6]
tab_dict_3    = {2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3}

case_4        = [2, [3, 4, 5, [6, 7, 8, 9], [6, 7, 9]], [3, 4, 5, [6, 7, 8, 9]], [3, 4, 5, [6, 9]], [3, 4, 5, [6], 9, 10, 11], 12]
case_4_ini    = [2, 3, 4, 5, 6, 7, 8, 9, 6, 7, 9, 3, 4, 5, 6, 7, 8, 9, 3, 4, 5, 6, 9, 3, 4, 5, 6, 9, 10, 11, 12]
while_lines_4 = [3, 6]
tab_dict_4    = {2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3, 10:3, 11:3, 12:3}

case_5        = [2, [3, 4, 5, [6, [7, 8], 9], [6, [7], 9]], [3, 4, 5, [6, [7], 8, 9]]]
case_5_ini    = [2, 3, 4, 5, 6, 7, 8, 9, 6, 7, 9, 3, 4, 5, 6, 7, 8, 9]
while_lines_5 = [3, 6, 7]
tab_dict_5    = {2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3}

def nestedlist_to_simplelist(nestedlist):
    if type(nestedlist) == int:
        yield nestedlist
    elif type(nestedlist) == list:
        for i in nestedlist:
            yield from nestedlist_to_simplelist(i)

def simplelist_to_nestedlist(simplelist, while_lines, tab_dict):
    for i in range(len(simplelist)):
        cur_line = simplelist[i]
        if cur_line not in while_lines:
            yield cur_line
        elif cur_line in while_lines:
            yield [cur_line] + list(simplelist_to_nestedlist(simplelist[i+1:], while_lines, tab_dict))
            break
        elif tab_dict[cur_line] > tab_dict[simplelist[i+1]]:
            yield cur_line
            
def print_generator(f):
    while True:
        try:
            print(next(f), end="\n")
        except StopIteration:
            print()
            return
            
     
assert(list(nestedlist_to_simplelist(case_1)) == case_1_ini)
assert(list(nestedlist_to_simplelist(case_2)) == case_2_ini)
assert(list(nestedlist_to_simplelist(case_3)) == case_3_ini)
assert(list(nestedlist_to_simplelist(case_4)) == case_4_ini)


simplelist_to_nestedlist_1 = simplelist_to_nestedlist(case_1_ini, while_lines_1, tab_dict_1)
simplelist_to_nestedlist_2 = simplelist_to_nestedlist(case_2_ini, while_lines_2, tab_dict_2)
simplelist_to_nestedlist_3 = simplelist_to_nestedlist(case_3_ini, while_lines_3, tab_dict_3)
simplelist_to_nestedlist_4 = simplelist_to_nestedlist(case_4_ini, while_lines_4, tab_dict_4)
print_generator(simplelist_to_nestedlist_1)
print_generator(simplelist_to_nestedlist_2)
print_generator(simplelist_to_nestedlist_3)
print_generator(simplelist_to_nestedlist_4)