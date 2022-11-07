# ADDED: Assignment => Test_Assignment.test_simple_assignment
a = 10
b = 20
c = 30
c = b
a = c

# ADDED: If statement => Test_IF_Statement.test_simplest
a = 10
b = 20
if a == 10:
	print(a)

# ADDED: Else statement => Test_IF_Else_Statement.test_simplest
a = 10
b = 20
if a == b:
	print(a)
else:
	print(b)

# ADDED: elif statement => Test_IF_Elif_Statement.test_simplest
a = 10
b = 20
if a == 20:
	print(a)
elif a + b == 30:
	print(a + b)
else:
	print(b)


# ADDED: Simple while loop => Test_While_Statement.test_simplest
i = 0
while i < 100:
	print(i)
	i += 1

# ADDED: A more complex while loop => Test_While_Statement.test_1layer_with_ifelse
i = 100
j = 1
odd_sum = 0
even_sum = 0
while j <= i:
	if j % 2 == 0:
		even_sum += j
	else:
		odd_sum += j
	j += 1

if odd_sum > even_sum:
	print(odd_sum)
else:
	print(even_sum)



# ADDED: Nested while loop (simple) => Test_While_Statement.test_simplest_nested
i = 0
j = 0
while i < 6:
	while j < 6:
		j += 1
	i += 1

# ADDED: Nested while loop with conditional => Test_While_Statement.test_2layer_with_ifelse
even_sum = 0
odd_sum = 0
i = 0
while i < 4:
	j = 4
	while j < 6:
		if (i + j) % 2 == 0:
			even_sum += (i + j)
		else:
			odd_sum += (i + j)
		j += 1
	i += 1

print(even_sum)
print(odd_sum)

# ADDED: While edge case => Test_While_Statement.test_not_increament_at_edge
even_sum = 0
odd_sum = 0
i = 0
while i < 4:
	i += 1
	j = 4
	while j < 6:
		j += 1
		if (i + j) % 2 == 0:
			even_sum += (i + j)
		else:
			odd_sum += (i + j)

print(even_sum)
print(odd_sum)



# ADDED: Quadruple nested while loop => Test_While_Statement.test_quadruple_nested_while
i = 0
j = 0
k = 0
l = 0
while i < 3:
	while j < 3:
		while k < 3:
			while l < 3:
				print(l)
				l += 1
			print(k)
			k += 1
		print(j)
		j += 1
	print(i)
	i += 1

# ADDED: 3 unique execution paths => Test_While_Statement.test_3_unique_execpaths
sum = 0
i = 0
while i < 2:
	j = 0
	while j < 4:
		if (i + j) % 2 == 0:
			sum += (i + j)
		elif (i + j) % 3 == 0:
			sum += (i + j)
		else:
			sum -= (i + j)
		j += 1
	i += 1

print(sum)

# ADDED: Arbitrary number of nested => Test_While_Statement.test_arbitrary_nested_level
a = 0
if a == 0:
	sum = 0
	i = 0
	while i < 2:
		j = 0
		while j < 4:
			if (i + j) % 2 == 0:
				sum += (i + j)
			elif (i + j) % 3 == 0:
				sum += (i + j)
			else:
				sum -= (i + j)
			j += 1
		i += 1
else:
	while a < 2:
		print(2)
		a += 1

print(sum)


# for-loop
# 1. simple for-loop
for i in range(3):
    print("Hello World")

# 2. multi-path, simple for-loop
for i in range(5):
    print("case -1")
    if i == 0:
        print("case 0")
    elif i == 1:
        print("case 1")
    else:
        print("case 2")
    print("case 3")

# nested for-loop, single path
for i in range(2):
    for j in range(2):
        for k in range(2):
            print("Hello World")

for i in range(2):
    print("layer 1")
    for j in range(2):
        print("layer 2")
        for k in range(2):
            print("layer 3")
            if k == 1:
                print(k)
        if j == 1:
            print(j)
    if i == 1:
        print(i)

