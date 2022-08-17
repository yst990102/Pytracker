# Assignment
a = 10
b = 20
c = 30
c = b
a = c

# If statement
a = 10
b = 20
if a == 10:
    print(a)
else:
    print(b)

# Else statement
a = 10
b = 20
if a == b:
    print(a)
else:
    print(b)

# elif statement
a = 10
b = 20
if a == 20:
    print(a)
elif a + b == 30:
    print(a + b)
else:
    print(b)

# Nested if statement
a = 10
b = 20
if a < b:
	if b > a:
		if a == 10:
			if b == 20:
				print(a)
				print(b)

# Simple while loop
i = 0
while i < 100:
    print(i)
    i += 1

# A more complex while loop
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

#Unused while loop
even_sum = 0
odd_sum = 0
i = 2
j = 0
while j < 4:
	if (i + j) % 2 == 0:
		even_sum += (i + j)
	else:
		odd_sum += (i + j)
	j += 1
	
while j < 4:
	if (i + j) % 2 == 0:
		even_sum += (i + j)
	else:
		odd_sum += (i + j)
	j += 1
i += 1

print(even_sum)
print(odd_sum)

# Nested while loop (simple)
i = 0
j = 0
while i < 6:
	while j < 6:
		j +=1
	i += 1

# Nested while loop with conditional
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

# Nested while loop that is unused
even_sum = 0
odd_sum = 0
i = 0
while i < 2:
	j = 0
	while j < 4:
		if (i + j) % 2 == 0:
			even_sum += (i + j)
		else:
			odd_sum += (i + j)
		j += 1

	while j < 4:
		if (i + j) % 2 == 0:
			even_sum += (i + j)
		else:
			odd_sum += (i + j)
		j += 1
	i += 1

print(even_sum)
print(odd_sum)

# Nested while loop that is same depth
even_sum = 0
odd_sum = 0
i = 0
while i < 2:
	j = 0
	while j < 4:
		if (i + j) % 2 == 0:
			even_sum += (i + j)
		else:
			odd_sum += (i + j)
		j += 1

	j = 0
	while j < 4:
		if (i + j) % 2 == 0:
			even_sum += (i + j)
		else:
			odd_sum += (i + j)
		j += 1
	i += 1

print(even_sum)
print(odd_sum)

# Quadruple nested while loop
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

# 3 unique execution paths
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

# Arbitrary number of nested
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