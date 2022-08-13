import os
import pathlib
from Pytracker import backend_main

current_absolute_path = str(pathlib.Path(__file__).parent.resolve())


class Test_Assignment():

	def test_simple_assignment(self):
		usercode = """a = 10
b = 20
tmp = a
a = b
b = tmp"""

		with open(current_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 3, 4, 5])
		assert (step_json == {
		    "d": 5,
		    "list": [{
		        "type": "step",
		        "start": 1,
		        "end": 2
		    }, {
		        "type": "step",
		        "start": 2,
		        "end": 3
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 4
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5
		    }]
		})

	def test_self_assignment(self):
		usercode = """a = 10
print(a)
a = a + 1
print(a)
a = a - 1
print(a)
a = a*1
print(a)
a =a / 1
print(a)
a += 1
print(a)
a -= 1
print(a)
a *= 1
print(a)
a /= 1
print(a)"""

		with open(current_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
		assert (step_json == {
		    "d":
		        5,
		    "list": [{
		        "type": "step",
		        "start": 1,
		        "end": 2
		    }, {
		        "type": "step",
		        "start": 2,
		        "end": 3
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 4
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 6
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 7
		    }, {
		        "type": "step",
		        "start": 7,
		        "end": 8
		    }, {
		        "type": "step",
		        "start": 8,
		        "end": 9
		    }, {
		        "type": "step",
		        "start": 9,
		        "end": 10
		    }, {
		        "type": "step",
		        "start": 10,
		        "end": 11
		    }, {
		        "type": "step",
		        "start": 11,
		        "end": 12
		    }, {
		        "type": "step",
		        "start": 12,
		        "end": 13
		    }, {
		        "type": "step",
		        "start": 13,
		        "end": 14
		    }, {
		        "type": "step",
		        "start": 14,
		        "end": 15
		    }, {
		        "type": "step",
		        "start": 15,
		        "end": 16
		    }, {
		        "type": "step",
		        "start": 16,
		        "end": 17
		    }, {
		        "type": "step",
		        "start": 17,
		        "end": 18
		    }]
		})


class Test_IF_Statement():

	def test_if(self):
		usercode = """a = 10
b = 20
if a < b:
	print("HELLO")
"""
		with open(current_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 4])
		assert (step_json == {"d": 5, "list": [{"type": "step", "start": 1, "end": 2}, {"type": "step", "start": 2, "end": 4}]})

	def test_ifelse(self):
		usercode = """a = 10
b = 20
if b < a:
	print("Hello")
else:
	print("BYE")
"""
		with open(current_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 6])
		assert (step_json == {'d': 5, 'list': [{'type': 'step', 'start': 1, 'end': 2}, {'type': 'step', 'start': 2, 'end': 6}]})


class Test_While_Statement():

	def test_simplest(self):
		usercode = """i = 0
while i < 5:
	print("Here")
	i += 1
"""
		with open(current_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, [2, 3, 4], [2, 3, 4], [2, 3, 4], [2, 3, 4], [2, 3, 4]])
		assert (step_json == {
		    "d":
		        5,
		    "list": [{
		        "type": "step",
		        "start": 1,
		        "end": 2
		    }, {
		        "type": "circle",
		        "start": 2,
		        "iteration": 1
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 2,
		        "end": 3
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 4
		    }, {
		        "type": "circle",
		        "start": 2
		    }, {
		        "type": "step",
		        "start": 2,
		        "end": 3
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 4
		    }, {
		        "type": "circle",
		        "start": 2
		    }, {
		        "type": "step",
		        "start": 2,
		        "end": 3
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 4
		    }, {
		        "type": "circle",
		        "start": 2
		    }, {
		        "type": "step",
		        "start": 2,
		        "end": 3
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 4
		    }, {
		        "type": "circle",
		        "start": 2
		    }, {
		        "type": "step",
		        "start": 2,
		        "end": 3
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 4
		    }]
		})

	def test_simplest_nested(self):
		usercode = """i = 0
j = 0
while i < 6:
	while j < 6:
		j +=1
	i += 1
"""
		with open(current_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, [3, [4, 5], [4, 5], [4, 5], [4, 5], [4, 5], [4, 5], 6], [3, 6], [3, 6], [3, 6], [3, 6], [3, 6]])
		assert (step_json == {
		    "d":
		        5,
		    "list": [{
		        "type": "step",
		        "start": 1,
		        "end": 2
		    }, {
		        "type": "step",
		        "start": 2,
		        "end": 3
		    }, {
		        "type": "circle",
		        "start": 3,
		        "iteration": 1
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 4
		    }, {
		        "type": "circle",
		        "start": 4,
		        "iteration": 1
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5
		    }, {
		        "type": "circle",
		        "start": 4
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5
		    }, {
		        "type": "circle",
		        "start": 4
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5
		    }, {
		        "type": "circle",
		        "start": 4
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5
		    }, {
		        "type": "circle",
		        "start": 4
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5
		    }, {
		        "type": "circle",
		        "start": 4
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5
		    }, {
		        "type": "while_end",
		        "start": 4,
		        "end": 5
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 6
		    }, {
		        "type": "circle",
		        "start": 3
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 6
		    }, {
		        "type": "circle",
		        "start": 3
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 6
		    }, {
		        "type": "circle",
		        "start": 3
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 6
		    }, {
		        "type": "circle",
		        "start": 3
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 6
		    }, {
		        "type": "circle",
		        "start": 3
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 6
		    }]
		})

	def test_1layer_with_ifelse(self):
		usercode = """a = 4
while a > 0:
	if a % 2 == 0:
		print("EVEN")
	else:
		print("ODD")
	a -= 1
"""
		with open(current_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, [2, 4, 7], [2, 6, 7], [2, 4, 7], [2, 6, 7]])
		assert (step_json == {
		    "d":
		        5,
		    "list": [{
		        "type": "step",
		        "start": 1,
		        "end": 2
		    }, {
		        "type": "circle",
		        "start": 2,
		        "iteration": 1
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 2,
		        "end": 4
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 7
		    }, {
		        "type": "circle",
		        "start": 2
		    }, {
		        "type": "step",
		        "start": 2,
		        "end": 6
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 7
		    }, {
		        "type": "circle",
		        "start": 2
		    }, {
		        "type": "step",
		        "start": 2,
		        "end": 4
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 7
		    }, {
		        "type": "circle",
		        "start": 2
		    }, {
		        "type": "step",
		        "start": 2,
		        "end": 6
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 7
		    }]
		})

	def test_2layer_with_ifelse(self):
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
		with open(current_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 3, [4, 5, [6, 8, 11], [6, 10, 11], 12], [4, 5, [6, 10, 11], [6, 8, 11], 12], [4, 5, [6, 8, 11], [6, 10, 11], 12], [4, 5, [6, 10, 11], [6, 8, 11], 12], 14, 15])
		assert (step_json == {
		    "d":
		        5,
		    "list": [{
		        "type": "step",
		        "start": 1,
		        "end": 2
		    }, {
		        "type": "step",
		        "start": 2,
		        "end": 3
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 4
		    }, {
		        "type": "circle",
		        "start": 4,
		        "iteration": 1
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 6
		    }, {
		        "type": "circle",
		        "start": 6,
		        "iteration": 1
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 8
		    }, {
		        "type": "step",
		        "start": 8,
		        "end": 11
		    }, {
		        "type": "circle",
		        "start": 6
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 10
		    }, {
		        "type": "step",
		        "start": 10,
		        "end": 11
		    }, {
		        "type": "while_end",
		        "start": 6,
		        "end": 11
		    }, {
		        "type": "step",
		        "start": 11,
		        "end": 12
		    }, {
		        "type": "circle",
		        "start": 4
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 6
		    }, {
		        "type": "circle",
		        "start": 6,
		        "iteration": 1
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 10
		    }, {
		        "type": "step",
		        "start": 10,
		        "end": 11
		    }, {
		        "type": "circle",
		        "start": 6
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 8
		    }, {
		        "type": "step",
		        "start": 8,
		        "end": 11
		    }, {
		        "type": "while_end",
		        "start": 6,
		        "end": 11
		    }, {
		        "type": "step",
		        "start": 11,
		        "end": 12
		    }, {
		        "type": "circle",
		        "start": 4
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 6
		    }, {
		        "type": "circle",
		        "start": 6,
		        "iteration": 1
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 8
		    }, {
		        "type": "step",
		        "start": 8,
		        "end": 11
		    }, {
		        "type": "circle",
		        "start": 6
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 10
		    }, {
		        "type": "step",
		        "start": 10,
		        "end": 11
		    }, {
		        "type": "while_end",
		        "start": 6,
		        "end": 11
		    }, {
		        "type": "step",
		        "start": 11,
		        "end": 12
		    }, {
		        "type": "circle",
		        "start": 4
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 6
		    }, {
		        "type": "circle",
		        "start": 6,
		        "iteration": 1
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 10
		    }, {
		        "type": "step",
		        "start": 10,
		        "end": 11
		    }, {
		        "type": "circle",
		        "start": 6
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 8
		    }, {
		        "type": "step",
		        "start": 8,
		        "end": 11
		    }, {
		        "type": "while_end",
		        "start": 6,
		        "end": 11
		    }, {
		        "type": "step",
		        "start": 11,
		        "end": 12
		    }, {
		        "type": "while_end",
		        "start": 4,
		        "end": 12
		    }, {
		        "type": "step",
		        "start": 12,
		        "end": 14
		    }, {
		        "type": "step",
		        "start": 14,
		        "end": 15
		    }]
		})

	def test_3layer(self):
		usercode = """i = 0
j = 0
k = 0
while i < 1:
	while j < 1:
		while k < 1:
			print(k)
			k += 1
		print(j)
		j += 1
	print(i)
	i += 1
"""
		with open(current_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 3, [4, [5, [6, 7, 8], 9, 10], 11, 12]])
		assert (step_json == {
		    "d":
		        5,
		    "list": [{
		        "type": "step",
		        "start": 1,
		        "end": 2
		    }, {
		        "type": "step",
		        "start": 2,
		        "end": 3
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 4
		    }, {
		        "type": "circle",
		        "start": 4,
		        "iteration": 1
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5
		    }, {
		        "type": "circle",
		        "start": 5,
		        "iteration": 1
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 6
		    }, {
		        "type": "circle",
		        "start": 6,
		        "iteration": 1
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 7
		    }, {
		        "type": "step",
		        "start": 7,
		        "end": 8
		    }, {
		        "type": "while_end",
		        "start": 6,
		        "end": 8
		    }, {
		        "type": "step",
		        "start": 8,
		        "end": 9
		    }, {
		        "type": "step",
		        "start": 9,
		        "end": 10
		    }, {
		        "type": "while_end",
		        "start": 5,
		        "end": 10
		    }, {
		        "type": "step",
		        "start": 10,
		        "end": 11
		    }, {
		        "type": "step",
		        "start": 11,
		        "end": 12
		    }]
		})

	def test_unused_inner_while_loop(self):
		usercode = """even_sum = 0
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
"""
		with open(current_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 3, [4, 5, [6, 8, 11], [6, 10, 11], [6, 8, 11], [6, 10, 11], [6, 18], 5, [6, 10, 11], [6, 8, 11], [6, 10, 11], [6, 8, 11], [6, 18], 20], 21])
		assert (step_json == {
		    "d":
		        5,
		    "list": [{
		        "type": "step",
		        "start": 1,
		        "end": 2
		    }, {
		        "type": "step",
		        "start": 2,
		        "end": 3
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 4
		    }, {
		        "type": "circle",
		        "start": 4,
		        "iteration": 1
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 6
		    }, {
		        "type": "circle",
		        "start": 6,
		        "iteration": 1
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 8
		    }, {
		        "type": "step",
		        "start": 8,
		        "end": 11
		    }, {
		        "type": "circle",
		        "start": 6
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 10
		    }, {
		        "type": "step",
		        "start": 10,
		        "end": 11
		    }, {
		        "type": "circle",
		        "start": 6
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 8
		    }, {
		        "type": "step",
		        "start": 8,
		        "end": 11
		    }, {
		        "type": "circle",
		        "start": 6
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 10
		    }, {
		        "type": "step",
		        "start": 10,
		        "end": 11
		    }, {
		        "type": "circle",
		        "start": 6
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 18
		    }, {
		        "type": "while_end",
		        "start": 6,
		        "end": 18
		    }, {
		        "type": "step",
		        "start": 18,
		        "end": 5
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 6
		    }, {
		        "type": "circle",
		        "start": 6,
		        "iteration": 6
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 10
		    }, {
		        "type": "step",
		        "start": 10,
		        "end": 11
		    }, {
		        "type": "circle",
		        "start": 6
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 8
		    }, {
		        "type": "step",
		        "start": 8,
		        "end": 11
		    }, {
		        "type": "circle",
		        "start": 6
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 10
		    }, {
		        "type": "step",
		        "start": 10,
		        "end": 11
		    }, {
		        "type": "circle",
		        "start": 6
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 8
		    }, {
		        "type": "step",
		        "start": 8,
		        "end": 11
		    }, {
		        "type": "circle",
		        "start": 6
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 18
		    }, {
		        "type": "while_end",
		        "start": 6,
		        "end": 18
		    }, {
		        "type": "step",
		        "start": 18,
		        "end": 20
		    }, {
		        "type": "while_end",
		        "start": 4,
		        "end": 20
		    }, {
		        "type": "step",
		        "start": 20,
		        "end": 21
		    }]
		})

	def test_while_in_ifelse(self):
		usercode = """a = 0
if a == 0:
	while a < 2:
		print(1)
		a += 1
else:
	while a < 2:
		print(2)
		a += 1
"""
		with open(current_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, [3, 4, 5], [3, 4, 5]])
		assert (step_json == {
		    "d":
		        5,
		    "list": [{
		        "type": "step",
		        "start": 1,
		        "end": 3
		    }, {
		        "type": "circle",
		        "start": 3,
		        "iteration": 1
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 4
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5
		    }, {
		        "type": "circle",
		        "start": 3
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 4
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5
		    }]
		})


class Test_Different_Main():

	def test_call_by_main_method(self):
		usercode = """def main():
	a = 123
	print(a)
	b = 321
	print(f"b == {b}")

main()"""

		with open(current_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 7, 2, 3, 4, 5])
		assert (step_json == {
		    "d":
		        5,
		    "list": [{
		        "type": "step",
		        "start": 1,
		        "end": 7
		    }, {
		        "type": "step",
		        "start": 7,
		        "end": 2
		    }, {
		        "type": "step",
		        "start": 2,
		        "end": 3
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 4
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5
		    }]
		})

	def test_call_by_ifname(self):
		usercode = """def main():
	a = 123
	print(a)
	b = 321
	print(f"b == {b}")

if __name__ == "__main__":
	main()"""

		with open(current_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 8, 2, 3, 4, 5])
		assert (step_json == {
		    "d":
		        5,
		    "list": [{
		        "type": "step",
		        "start": 1,
		        "end": 8
		    }, {
		        "type": "step",
		        "start": 8,
		        "end": 2
		    }, {
		        "type": "step",
		        "start": 2,
		        "end": 3
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 4
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5
		    }]
		})

	def test_no_main_or_ifname(self):
		usercode = """a = 123
print(a)
b = 321
print(f"b == {b}")"""

		with open(current_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 3, 4])
		assert (step_json == {"d": 5, "list": [{"type": "step", "start": 1, "end": 2}, {"type": "step", "start": 2, "end": 3}, {"type": "step", "start": 3, "end": 4}]})


class Test_For_Statement():
	# TODO: TypeError: unhashable type: 'list'
	def test_simple_forloop(self):
		usercode = """for i in range(5):
	print("Here")
"""
		with open(current_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]])
		assert (step_json == {})

	# TODO: TypeError: unhashable type: 'list'
	def test_complex_forloop(self):
		usercode = """for a in range(4):
	if a % 2 == 0:
		print("EVEN")
	else:
		print("ODD")
"""
		with open(current_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [[1, 3], [1, 5], [1, 3], [1, 5]])
		assert (step_json == {
		    'd':
		        5,
		    'list': [{
		        'end': 1,
		        'start': 0,
		        'type': 'step'
		    }, {
		        'iteration': 1,
		        'start': 1,
		        'type': 'circle'
		    }, {
		        'depth': -1,
		        'type': 'while_start'
		    }, {
		        'end': 3,
		        'start': 1,
		        'type': 'step'
		    }, {
		        'end': 6,
		        'start': 3,
		        'type': 'step'
		    }, {
		        'start': 1,
		        'type': 'circle'
		    }, {
		        'end': 5,
		        'start': 1,
		        'type': 'step'
		    }, {
		        'end': 6,
		        'start': 5,
		        'type': 'step'
		    }, {
		        'start': 1,
		        'type': 'circle'
		    }, {
		        'end': 3,
		        'start': 1,
		        'type': 'step'
		    }, {
		        'end': 6,
		        'start': 3,
		        'type': 'step'
		    }, {
		        'start': 1,
		        'type': 'circle'
		    }, {
		        'end': 5,
		        'start': 1,
		        'type': 'step'
		    }, {
		        'end': 6,
		        'start': 5,
		        'type': 'step'
		    }]
		})

	def test_nested_forloop(self):
		usercode = """even_sum = 0
odd_sum = 0
i = 0
for i in range(4):
	for j in range(4, 6):
		if (i + j) % 2 == 0:
			even_sum += (i + j)
		else:
			odd_sum += (i + j)

print(even_sum)
print(odd_sum)
"""
		with open(current_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 3, [4, [5, 7], [5, 9], [5, 9], [5, 7], [5, 7], [5, 9], [5, 9], [5, 7], 11], 12])
		assert (step_json == {
		    "d":
		        5,
		    "list": [{
		        "type": "step",
		        "start": 1,
		        "end": 2
		    }, {
		        "type": "step",
		        "start": 2,
		        "end": 3
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 4
		    }, {
		        "type": "circle",
		        "start": 4,
		        "iteration": 1
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5
		    }, {
		        "type": "circle",
		        "start": 5,
		        "iteration": 1
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 7
		    }, {
		        "type": "circle",
		        "start": 5
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 9
		    }, {
		        "type": "circle",
		        "start": 5
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 9
		    }, {
		        "type": "circle",
		        "start": 5
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 7
		    }, {
		        "type": "circle",
		        "start": 5
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 7
		    }, {
		        "type": "circle",
		        "start": 5
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 9
		    }, {
		        "type": "circle",
		        "start": 5
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 9
		    }, {
		        "type": "circle",
		        "start": 5
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 7
		    }, {
		        "type": "while_end",
		        "start": 5,
		        "end": 7
		    }, {
		        "type": "step",
		        "start": 7,
		        "end": 11
		    }, {
		        "type": "while_end",
		        "start": 4,
		        "end": 11
		    }, {
		        "type": "step",
		        "start": 11,
		        "end": 12
		    }]
		})


class Test_Function_Calling():
	# TODO: function loading error??
	def test_one_function_calling(self):
		usercode = """def myprint(something):
    print(something)

def main():
    a=123
    myprint(a)
    b=321
    myprint(b)

main()
	"""
		with open(current_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 4, 10, 5, 6, 2, 7, 8, 2])
		assert (step_json == {
		    "d":
		        5,
		    "list": [{
		        "type": "step",
		        "start": 1,
		        "end": 4
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 10
		    }, {
		        "type": "step",
		        "start": 10,
		        "end": 5
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 6
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 2
		    }, {
		        "type": "step",
		        "start": 2,
		        "end": 7
		    }, {
		        "type": "step",
		        "start": 7,
		        "end": 8
		    }, {
		        "type": "step",
		        "start": 8,
		        "end": 2
		    }]
		})

	# TODO: need to be done
	def test_multi_function_calling(self):
		pass


class Test_Input():

	def test_simple_input(self):
		usercode = """a = input("enter your a:")
print(a)
"""
		with open(current_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2])
		assert (step_json == {"d": 5, "list": [{"type": "step", "start": 1, "end": 2}]})
