case_1        = [3, 4, 5, [6, 7, 8, 9]]
case_1_ini    = [3, 4, 5, 6, 7, 8, 9]
case_1_exp    = [3, 4, 5, (1,[6, 7, 8, 9])]
tab_dict_1    = {3:1, 4:1, 5:1, 6:1, 7:2, 8:2, 9:2}

case_2        = [2, [3, 4, 5, [6, 7, 8, 9], [6, 7, 9]]]
case_2_ini    = [2, 3, 4, 5, 6, 7, 8, 9, 6, 7, 9]
case_2_exp    = [2, (1,[3, 4, 5, (1,[6, 7, 8, 9]), (2,[6, 7, 9])])]
tab_dict_2    = {2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3}

case_3        = [2, [3, 4, 5, [6, 7, 8, 9], [6, 7, 9]], [3, 4, 5, [6, 7, 8, 9]]]
case_3_ini    = [2, 3, 4, 5, 6, 7, 8, 9, 6, 7, 9, 3, 4, 5, 6, 7, 8, 9]
case_3_exp    = [2, (1,[3, 4, 5, (1,[6, 7, 8, 9]), (2,[6, 7, 9])]), (2,[3, 4, 5, (1,[6, 7, 8, 9])])]
tab_dict_3    = {2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3}

case_4        = [2, [3, 4, 5, [6, 7, 8, 9], [6, 7, 9]], [3, 4, 5, [6, 7, 8, 9]], [3, 4, 5, [6, 9]], [3, 4, 5, [6], 9, 10, 11], 12]
case_4_ini    = [2, 3, 4, 5, 6, 7, 8, 9, 6, 7, 9, 3, 4, 5, 6, 7, 8, 9, 3, 4, 5, 6, 9, 3, 4, 5, 6, 9, 10, 11, 12]
case_4_exp    = [2, (1,[3, 4, 5, (1,[6, 7, 8, 9]), (2,[6, 7, 9])]), (2,[3, 4, 5, (1,[6, 7, 8, 9])]), (3,[3, 4, 5, (1,[6, 9])]), (4,[3, 4, 5, (1,[6]), 9, 10, 11]), 12]
tab_dict_4    = {2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3, 10:3, 11:3, 12:3}

case_5        = [2, [3, 4, 5, [6, [7, 8], 9], [6, [7], 9]], [3, 4, 5, [6, [7], 8, 9]]]
case_5_ini    = [2, 3, 4, 5, 6, 7, 8, 9, 6, 7, 9, 3, 4, 5, 6, 7, 8, 9]
case_5_exp    = [2, (1,[3, 4, 5, (1,[6, (1,[7, 8]), 9]), (2,[6, (1,[7]), 9])]), (2,[3, 4, 5, (1,[6, (1,[7]), 8, 9])])]
tab_dict_5    = {2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3}


# This works!!
def nestedlist_to_simplelist(nestedlist):
    if type(nestedlist) == int:
        yield nestedlist
    elif type(nestedlist) == list:
        for i in nestedlist:
            yield from nestedlist_to_simplelist(i)

# 2022-06-25 使用递归式修改列表
# change nestedlist_to_listofint&tuple
def listoflist_to_listofinttuple(item, count_dict:dict):
    if type(item) == int:
        return item
    elif type(item) == list:
        while_line = item[0]
        try:
            count_dict[while_line] += 1
            clear_keys = [i for i in count_dict.keys() if i > while_line]
            for i in clear_keys:
                count_dict.pop(i)
        except:
            count_dict[while_line] = 1
        list_in_tuple = []
        for i in item:
            list_in_tuple.append(listoflist_to_listofinttuple(i, count_dict))
        return (count_dict[while_line], list_in_tuple)

input = listoflist_to_listofinttuple(case_1, {})
print(input)

input = listoflist_to_listofinttuple(case_2, {})
print(input)

input = listoflist_to_listofinttuple(case_3, {})
print(input)

input = listoflist_to_listofinttuple(case_4, {})
print(input)

input = listoflist_to_listofinttuple(case_5, {})
print(input)

# test for nestedlist_to_simplelist
# assert(list(nestedlist_to_simplelist(case_1)) == case_1_ini)
# assert(list(nestedlist_to_simplelist(case_2)) == case_2_ini)
# assert(list(nestedlist_to_simplelist(case_3)) == case_3_ini)
# assert(list(nestedlist_to_simplelist(case_4)) == case_4_ini)



import sys
from io import StringIO

code = """
i = [0,1,2]
for j in i :
    print(j)
"""

old_stdout = sys.stdout
redirected_output = sys.stdout = StringIO()
try:
    exec(code)
except:
    raise
finally:  # !
    sys.stdout = old_stdout  # !

print(redirected_output.getvalue())
print('Hello, World!')  # now we see it in case of the exception above
