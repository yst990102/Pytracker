import sys
from trace import Trace
import pytest
from Pytracker import RETURN_LISTOFLIST, backend_main


def test_assignment():
	usercode = """a = 10
b = 20
tmp = a
a = b
b = tmp"""
	listoflist = backend_main(usercode=usercode, return_data=RETURN_LISTOFLIST)
	assert (listoflist == [1, 2, 3, 4, 5])


def test_complexwhile():
	usercode = """a = 4
while a > 0:
	if a % 2 == 0:
		print("EVEN")
	else:
		print("ODD")
	a -= 1
"""
	listoflist = backend_main(usercode=usercode, return_data=RETURN_LISTOFLIST)
	assert (listoflist == [1, [2, 4, 7], [2, 6, 7], [2, 4, 7], [2, 6, 7]])


def test_if():
	usercode = """a = 10
b = 20
if a < b:
	print("HELLO")
"""
	listoflist = backend_main(usercode=usercode, return_data=RETURN_LISTOFLIST)
	assert (listoflist == [1, 2, 4])


def test_ifelse():
	usercode = """a = 10
b = 20
if b < a:
	print("Hello")
else:
	print("BYE")
"""
	listoflist = backend_main(usercode=usercode, return_data=RETURN_LISTOFLIST)
	assert (listoflist == [1, 2, 6])


def test_nestedwhile():
	usercode = """even_sum = 0
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
"""
	listoflist = backend_main(usercode=usercode, return_data=RETURN_LISTOFLIST)
	assert (listoflist == [
	    1, 2, 3, [4, 5, [6, 8, 11], [6, 10, 11], 12], [4, 5, [6, 10, 11], [6, 8, 11], 12], [4, 5, [6, 8, 11], [6, 10, 11], 12], [4, 5, [6, 10, 11], [6, 8, 11], 12], 14, 15
	])


def test_simplewhile():
	usercode = """i = 0
while i < 5:
	print("Here")
	i += 1
"""
	listoflist = backend_main(usercode=usercode, return_data=RETURN_LISTOFLIST)
	assert (listoflist == [1, [2, 3, 4], [2, 3, 4], [2, 3, 4], [2, 3, 4], [2, 3, 4]])