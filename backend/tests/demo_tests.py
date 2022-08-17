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