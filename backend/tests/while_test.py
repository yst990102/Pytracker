import os
import pathlib

current_absolute_path = str(pathlib.Path(__file__).parent.resolve())


class Test_While_Statement():

	def test_simplest(self):
		usercode = """i = 0
while i < 5:
	print("Here")
	i += 1
"""
		with open(current_absolute_path + "/../" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/../" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/../" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/../" + "step_json.json", 'r').read())

		assert (listoflist == [1, [2, 3, 4], [2, 3, 4], [2, 3, 4], [2, 3, 4], [2, 3, 4]])
		assert (step_json == {
		    "d":
		        5,
		    "list": [{
		        "type": "step",
		        "start": 0,
		        "end": 1
		    }, {
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
		        "start": 2,
		        "iteration": 5
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
		with open(current_absolute_path + "/../" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/../" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/../" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/../" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, [3, [4, 5], [4, 5], [4, 5], [4, 5], [4, 5], [4, 5], 6], [3, 6], [3, 6], [3, 6], [3, 6], [3, 6]])
		assert (step_json == {
		    "d":
		        5,
		    "list": [{
		        "type": "step",
		        "start": 0,
		        "end": 1
		    }, {
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
		        "start": 4,
		        "iteration": 6
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
		        "start": 3,
		        "iteration": 2
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 6
		    }, {
		        "type": "circle",
		        "start": 3,
		        "iteration": 6
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
		with open(current_absolute_path + "/../" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/../" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/../" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/../" + "step_json.json", 'r').read())

		assert (listoflist == [1, [2, 4, 7], [2, 6, 7], [2, 4, 7], [2, 6, 7]])
		assert (step_json == {
		    "d":
		        5,
		    "list": [{
		        "type": "step",
		        "start": 0,
		        "end": 1
		    }, {
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
		        "start": 2,
		        "iteration": 2
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
		        "start": 2,
		        "iteration": 4
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
		with open(current_absolute_path + "/../" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/../" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/../" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/../" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 3, [4, 5, [6, 8, 11], [6, 10, 11], 12], [4, 5, [6, 10, 11], [6, 8, 11], 12], [4, 5, [6, 8, 11], [6, 10, 11], 12], [4, 5, [6, 10, 11], [6, 8, 11], 12], 14, 15])
		assert (step_json == {"d": 5, "list": [{"type": "step", "start": 0, "end": 1}, {"type": "step", "start": 1, "end": 2}, {"type": "step", "start": 2, "end": 3}, {"type": "step", "start": 3, "end": 4}, {"type": "circle", "start": 4, "iteration": 1}, {"type": "while_start", "depth": -1}, {"type": "step", "start": 4, "end": 5}, {"type": "step", "start": 5, "end": 6}, {"type": "circle", "start": 6, "iteration": 1}, {"type": "while_start", "depth": -1}, {"type": "step", "start": 6, "end": 8}, {"type": "step", "start": 8, "end": 11}, {"type": "circle", "start": 6, "iteration": 2}, {"type": "step", "start": 6, "end": 10}, {"type": "step", "start": 10, "end": 11}, {"type": "while_end", "start": 6, "end": 11}, {"type": "step", "start": 11, "end": 12}, {"type": "circle", "start": 4, "iteration": 2}, {"type": "step", "start": 4, "end": 5}, {"type": "step", "start": 5, "end": 6}, {"type": "circle", "start": 6, "iteration": 1}, {"type": "while_start", "depth": -1}, {"type": "step", "start": 6, "end": 10}, {"type": "step", "start": 10, "end": 11}, {"type": "circle", "start": 6, "iteration": 2}, {"type": "step", "start": 6, "end": 8}, {"type": "step", "start": 8, "end": 11}, {"type": "while_end", "start": 6, "end": 11}, {"type": "step", "start": 11, "end": 12}, {"type": "circle", "start": 4, "iteration": 4}, {"type": "step", "start": 4, "end": 5}, {"type": "step", "start": 5, "end": 6}, {"type": "circle", "start": 6, "iteration": 1}, {"type": "while_start", "depth": -1}, {"type": "step", "start": 6, "end": 10}, {"type": "step", "start": 10, "end": 11}, {"type": "circle", "start": 6, "iteration": 2}, {"type": "step", "start": 6, "end": 8}, {"type": "step", "start": 8, "end": 11}, {"type": "while_end", "start": 6, "end": 11}, {"type": "step", "start": 11, "end": 12}, {"type": "while_end", "start": 4, "end": 12}, {"type": "step", "start": 12, "end": 14}, {"type": "step", "start": 14, "end": 15}]})

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
		with open(current_absolute_path + "/../" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/../" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/../" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/../" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 3, [4, [5, [6, 7, 8], 9, 10], 11, 12]])
		assert (step_json == {
		    "d":
		        5,
		    "list": [{
		        "type": "step",
		        "start": 0,
		        "end": 1
		    }, {
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

	# TODO: need to check the straight line-back issue
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
		with open(current_absolute_path + "/../" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/../" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/../" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/../" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 3, [4, 5, [6, 8, 11], [6, 10, 11], [6, 8, 11], [6, 10, 11], 18], [4, 5, [6, 10, 11], [6, 8, 11], [6, 10, 11], [6, 8, 11], 18], 20, 21])
		assert (step_json == {
		    "d":
		        5,
		    "list": [{
		        "type": "step",
		        "start": 0,
		        "end": 1
		    }, {
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
		        "start": 6,
		        "iteration": 2
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
		        "start": 6,
		        "iteration": 4
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
		        "end": 18
		    }, {
		        "type": "circle",
		        "start": 4,
		        "iteration": 2
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
		        "start": 6,
		        "iteration": 2
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
		        "start": 6,
		        "iteration": 4
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
		        "end": 18
		    }, {
		        "type": "while_end",
		        "start": 4,
		        "end": 18
		    }, {
		        "type": "step",
		        "start": 18,
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
		with open(current_absolute_path + "/../" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/../" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/../" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/../" + "step_json.json", 'r').read())

		assert (listoflist == [1, [3, 4, 5], [3, 4, 5]])
		assert (step_json == {
		    "d":
		        5,
		    "list": [{
		        "type": "step",
		        "start": 0,
		        "end": 1
		    }, {
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
		        "start": 3,
		        "iteration": 2
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
