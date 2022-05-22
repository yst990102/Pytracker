while_lines = [3]
execution_lines = [2,3,4,5,3,4,5,3,4,5,3]
tab_dict = {2: 1, 3: 1, 4: 2, 5: 2}

expect_result = [2,[3,4,5],[3,4,5],[3,4,5],3]

# list to string
execution_lines_str = str(execution_lines)
print(execution_lines_str)



while_lines = [3, 6]
result = [2, [3, 4, 5, [6, 7], 8], [3, 4, 5, [6, 7], 8], [3, 4, 5, [6], 8], [3, 4, 5, [6], 8]]
steps  = [2,  3, 4, 5,  6, 7,  8,   3, 4, 5,  6, 7,  8,   3, 4, 5,  6,  8,   3, 4, 5,  6,  8]
indes  = [1,  1, 2, 2,  2, 3,  2,   1, 2, 2,  2, 3,  2,   1, 2, 2,  2,  2,   1, 2, 2,  2,  2]
tab_dict = {2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 3, 8: 2}


'''
def main():
	i = 5
	while (i > 0):
		print("i == " ,i)
		i -= 1
		while (i > 2):
			break
        if i == 1: break
'''