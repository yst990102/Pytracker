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
print("Over")

# 3. 1-layer-loop with multi-iteration, multi-paths
a = 1
while a < 5:
    print("Case 1")
    if a == 3:
        print("Case 2")
print("Over")

# 4. 
# six-combination of 3-layer-loop
# iteration: 000,001,010,011,100,101,110,111
# 000, 0 layer
a = 1
b = 2
c = 3
while a == 1:
    while b == 2:
        while c == 3:
            print("Hello World")
print("Hello World Again")

# 001
a = 1
b = 2
c = 3
while a == 1:
    while b == 2:
        while c < 5:
            c += 1
            print("Hello World")
print("Hello World Again")

# 010
a = 1
b = 2
c = 3
while a == 1:
    while b < 4:
        b += 1
        while c == 3:
            print("Hello World")
print("Hello World Again")

# 011
a = 1
b = 2
c = 3
while a == 1:
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
        while c == 3:
            print("Hello World")
print("Hello World Again")

# 101
a = 1
b = 2
c = 3
while a < 3:
    a += 1
    while b == 2:
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
                    c += 1
                    if c == 4:
                        print("Case 3")
                    else:
                        print("Case 4")
print("Hello World Again")