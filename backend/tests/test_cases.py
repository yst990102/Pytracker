# simple assignment
a = 1

# multi assignments
a = 1
b = 2
c = 3

# simple if
if True:
    a = 1

# if statement
a = 1
if a == 1:
    print("Case 1")
else:
    print("Case 2")

# if elif 
a = 1
if a == 1:
    print("Case 1")
elif a == 0:
    print("Case 2")

# if elif else
a = 1
if a == 1:
    print("Case 1")
elif a == 0:
    print("Case 2")
else:
    print("Case 3")

# while statement
# 1. 1-layer-loop with 1-iteration
a = 1
while a == 1:
    a = 2
print("Over")

# 2. 1-layer-loop with multi-iteration
a = 1
while a < 5:
    print("Case 1")
    a += 1
print("Over")

# 3. 1-layer-loop with multi-iteration, multi-paths
a = 1
while a < 5:
    print("Case 1")
    if a == 3:
        print("Case 2")
    a += 1
print("Over")

# 4. 
# six-combination of 3-layer-loop
# iteration: 000,001,010,011,100,101,110,111
# 000, 0 layer
a = 1
b = 2
c = 3
while a == 1:
    a += 1
    while b == 2:
        b += 1
        while c == 3:
            c += 1
            print("Hello World")
print("Hello World Again")

# 001
a = 1
b = 2
c = 3
while a == 1:
    a += 1
    while b == 2:
        b += 1
        while c < 5:
            c += 1
            print("Hello World")
print("Hello World Again")

# 010
a = 1
b = 2
c = 3
while a == 1:
    a += 1
    while b < 4:
        b += 1
        while c == 3:
            c += 1
            print("Hello World")
print("Hello World Again")

# 011
a = 1
b = 2
c = 3
while a == 1:
    a += 1
    while b < 4:
        b += 1
        while c < 5:
            c += 1
            print("Hello World")
print("Hello World Again")

# 100
a = 1
b = 2
c = 3
while a < 3:
    a += 1
    while b == 2:
        b += 1
        while c == 3:
            c += 1
            print("Hello World")
print("Hello World Again")

# 101
a = 1
b = 2
c = 3
while a < 3:
    a += 1
    while b == 2:
        b += 1
        while c < 5:
            c += 1
            print("Hello World")
print("Hello World Again")

# 110
a = 1
b = 2
c = 3
while a < 3:
    a += 1
    while b < 4:
        b += 1
        while c == 3:
            c += 1
            print("Hello World")
print("Hello World Again")

# 111
a = 1
b = 2
c = 3
while a < 3:
    a += 1
    while b < 4:
        b += 1
        while c < 5:
            c += 1
            print("Hello World")
print("Hello World Again")

# 5. when multi-path meet multi-layer-loop
a = 1
b = 2
c = 3
while a < 3:
    a += 1
    while b < 4:
        b += 1
        while c < 5:
            c += 1
            if c < 5:
                print("Case 1")
            else:
                print("Case 2")
print("Hello World Again")

a = 1
b = 2
c = 3
while a < 3:
    a += 1
    while b < 4:
        b += 1
        if b == 2:
            print("Case 1")
        else:
            print("Case 2")
            while c < 5:
                c += 1
print("Hello World Again")

a = 1
b = 2
c = 3
while a < 3:
    a += 1
    while b < 4:
        b += 1
        if b == 2:
            print("Case 1")
        else:
            while c < 5:
                c += 1
                if c < 5:
                    print("Case 2")
                else:
                    print("Case 3")
print("Hello World Again")

a = 1
b = 2
c = 3
while a < 3:
    a += 1
    if a == 2:
        print("Case 1")
    else:
        while b < 4:
            b += 1
            while c < 5:
                print("Case 2")
                c += 1
print("Hello World Again")

a = 1
b = 2
c = 3
while a < 3:
    a += 1
    if a == 2:
        print("Case 1")
    else:
        while b < 4:
            b += 1
            while c < 5:
                c += 1
                if c < 5:
                    print("Case 2")
                else:
                    print("Case 3")
print("Hello World Again")

a = 1
b = 2
c = 3
while a < 3:
    a += 1
    if a == 1:
        print("Case 1")
    else:
        print("Case 2")
        while b < 4:
            if b == 2:
                b += 1
            else:
                print("Case 3")
                b += 1
                while c < 5:
                    c += 1
print("Hello World Again")

a = 1
b = 2
c = 3
while a < 3:
    a += 1
    if a == 1:
        print("Case 1")
    else:
        print("Case 2")
        while b < 4:
            if b == 2:
                b += 1
            else:
                while c < 5:
                    b += 1
                    c += 1
                    if c == 4:
                        print("Case 3")
                    else:
                        print("Case 4")
print("Hello World Again")


# function call
# see function pytest file

# yapf formating 
# see pytest file

# input
# see input pytest file

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

# nested for-loop, multi-path-in-1-layer
for i in range(2):
    for j in range(2):
        for k in range(2):
            print("case -1")
            if i == 0:
                print("case 0")
            elif i == 1:
                print("case 1")
            else:
                print("case 2")
            print("case 3")

# nested for-loop, multi-path-in-multi-layer
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

# parallel outer-for-loop
for i in range(2):
    print("loop 1")
for j in range(2):
    print("loop 2")

# parallel inner-for-loop, no other ass
for k in range(2):
    for i in range(2):
        print("loop 1")
    for j in range(2):
        print("loop 2")

# parallel inner-for-loop, with other ass
for k in range(2):
    a = 1
    for i in range(2):
        print("loop 1")
    print("interval")
    for j in range(2):
        print("loop 2")
    b = 1

# multi-path switch between for-loop and asses
for i in range(3):
    if i // 2 == 0:
        print("i == 0")
    else:
        for j in range(3):
            print(f"i == {i}")




# mix for-loop and while-loop and see if it confuses
for i in range(5):
    print("i <= 1")
    if i == 1:
        print("we have i == 1")
    else:
        j = 5
        while j >= 1:
            j -= 1
            print("j >= 1")
            for k in range(3):
                if k // 2 == 0:
                    print("i == 0")
                else:
                    for l in range(3):
                        print(f"l == {l}")
            j -= 0  # useless assignment
            for m in range(1):
                print("1-iteration paralleled for-loop")
            a = 0
            j -= 0  # useless assignment
            while a > 1:
                print("this loop should be skipped")
    

# filter test, see if the fileter select the iteration info that we want
# 1. two-paths with 10 iterations， same first and last, 1 in between
for i in range(10):
    print(f"i == {i}")
    if i == 0 or i == 9:
        print("mod 2 == 0")
    else:
        print("mode 2 == 1")

# 1. two-paths with 10 iterations, different first and last, no in between
for i in range(10):
    print(f"i == {i}")
    if i == 0:
        print("mod 2 == 0")
    else:
        print("mode 2 == 1")

# 2. 5 individual paths
for i in range(5):
    if i == 0:
        print(f"i == {i}")
    elif i == 1:
        print(f"i == {i}")
    elif i == 2:
        print(f"i == {i}")
    elif i == 3:
        print(f"i == {i}")
    else:
        print(f"i == {i}")



# path
# nested(parallel)
# assignment mixed
# 