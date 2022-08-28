import os
import pathlib

backend_absolute_path = str(pathlib.Path(__file__).parent.parent.resolve())


class Test_IF_Statement():

	def test_simplest(self):
		usercode = """a = 10
b = 20
if a < b:
	print("HELLO")"""
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 4])
		assert (step_json == {"d": 1, "list": [{"type": "step", "start": 0, "end": 1}, {"type": "step", "start": 1, "end": 2}, {"type": "step", "start": 2, "end": 4}]})

	def test_nested(self):
		usercode = """a = 10
b = 20
if a < b:
	if b > a:
		if a == 10:
			if b == 20:
				print(a)
				print(b)"""
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 7, 8])
		assert (step_json == {
		    "d": 1,
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
		        "end": 7
		    }, {
		        "type": "step",
		        "start": 7,
		        "end": 8
		    }]
		})

	def test_with_while(self):
		usercode = """a = 10
b = 20
if a < b:
	while a < 12:
		if a == a:
			print("HELLO")
		a += 1
	while b == 20:
		print("WORLD")
		b += 1
		while b < 12:
			if b > 16:
				print("this is b")
			break
		while b < 25:
			if b > a:
				print("this is not b")
			b += 1"""
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, [4, 6, 7], [4, 6, 7], [8, 9, 10, [15, 17, 18], [15, 17, 18], [15, 17, 18], [15, 17, 18]]])
		assert (step_json == {
		    "d":
		        4,
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
		        "end": 6
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 7
		    }, {
		        "type": "circle",
		        "start": 4,
		        "iteration": 2
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 6
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 7
		    }, {
		        "type": "while_end",
		        "start": 4,
		        "end": 7
		    }, {
		        "type": "step",
		        "start": 7,
		        "end": 8
		    }, {
		        "type": "circle",
		        "start": 8,
		        "iteration": 1
		    }, {
		        "type": "while_start",
		        "depth": -1
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
		        "end": 15
		    }, {
		        "type": "circle",
		        "start": 15,
		        "iteration": 1
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 15,
		        "end": 17
		    }, {
		        "type": "step",
		        "start": 17,
		        "end": 18
		    }, {
		        "type": "circle",
		        "start": 15,
		        "iteration": 4
		    }, {
		        "type": "step",
		        "start": 15,
		        "end": 17
		    }, {
		        "type": "step",
		        "start": 17,
		        "end": 18
		    }]
		})

	def test_true_or_false(self):
		usercode = """a = 10
b = 20
if True:
	print("HELLO")

if False:
	print("WORLD")

print("HELLO WORLD")"""
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 4, 9])
		assert (step_json == {
		    "d": 1,
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
		        "end": 4
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 9
		    }]
		})


class Test_IF_Else_Statement():

	def test_simplest(self):
		usercode = """a = 10
b = 20
if b < a:
	print("Hello")
else:
	print("BYE")"""
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 6])
		assert (step_json == {"d": 1, "list": [{"type": "step", "start": 0, "end": 1}, {'type': 'step', 'start': 1, 'end': 2}, {'type': 'step', 'start': 2, 'end': 6}]})

	def test_nested(self):
		usercode = """a = 10
b = 20
if a > b:
	print(a)
else:
	if b < a:
		print(b)
	else:
		if a != 10:
			print(a)
		else:
			if b == 20:
				print(b)
			else:
				print(a)"""
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 13])
		assert (step_json == {"d": 1, "list": [{"type": "step", "start": 0, "end": 1}, {"type": "step", "start": 1, "end": 2}, {"type": "step", "start": 2, "end": 13}]})

	def test_with_while(self):
		usercode = """a = 10
b = 20
if a >= b:
	while a < 12:
		if a == a:
			print("HELLO")
		else:
			print(b != b)
		a += 1
else:
	while b == 20:
		print("WORLD")
		if 1 == 2:
			while b < 12:
				if b > 16:
					print("this is b")
				else:
					print("this is not b")
				break
		else:
			while b < 25:
				if b > a:
					print("this is not b")
				else:
					print("this is b")
				b += 1
		b += 1"""
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, [11, 12, [21, 23, 26], [21, 23, 26], [21, 23, 26], [21, 23, 26], [21, 23, 26], 27]])
		assert (step_json == {
		    "d":
		        4,
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
		        "end": 11
		    }, {
		        "type": "circle",
		        "start": 11,
		        "iteration": 1
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 11,
		        "end": 12
		    }, {
		        "type": "step",
		        "start": 12,
		        "end": 21
		    }, {
		        "type": "circle",
		        "start": 21,
		        "iteration": 1
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 21,
		        "end": 23
		    }, {
		        "type": "step",
		        "start": 23,
		        "end": 26
		    }, {
		        "type": "circle",
		        "start": 21,
		        "iteration": 5
		    }, {
		        "type": "step",
		        "start": 21,
		        "end": 23
		    }, {
		        "type": "step",
		        "start": 23,
		        "end": 26
		    }, {
		        "type": "while_end",
		        "start": 21,
		        "end": 26
		    }, {
		        "type": "step",
		        "start": 26,
		        "end": 27
		    }]
		})

	def test_true_or_false(self):
		usercode = """a = 10
b = 20
if True:
	print("HELLO")
else:
	if False:
		print("WORLD")
	if True:
		print("HELLO 02")
	else:
		if False:
			print("WORLD 02")

print("HELLO WORLD finall")"""
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 4, 14])
		assert (step_json == {
		    "d": 1,
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
		        "end": 4
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 14
		    }]
		})


class Test_IF_Elif_Statement():

	def test_simplest(self):
		usercode = """a = 10
b = 20
if b < a:
	print("Hello")
elif b == 20:
	print("BYE")"""
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 6])
		assert (step_json == {"d": 1, "list": [{"type": "step", "start": 0, "end": 1}, {'type': 'step', 'start': 1, 'end': 2}, {'type': 'step', 'start': 2, 'end': 6}]})

	def test_nested(self):
		usercode = """a = 10
b = 20
if a > b:
	print(a)
elif a <= b:
	print(b)
	if a != 10:
		print(a)
	elif a == 10:
		print(b)
		if b != 20:
			print(a)
		elif b == 20:
			print(b)"""
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 6, 10, 14])
		assert (step_json == {
		    "d":
		        1,
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
		        "end": 6
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 10
		    }, {
		        "type": "step",
		        "start": 10,
		        "end": 14
		    }]
		})

	def test_with_while(self):
		pass

	def test_true_or_false(self):
		usercode = """a = 10
b = 20
if True:
	print("HELLO")
	if True:
		print("HELLO 02")
	elif a == 10:
		if a != 10:
			print("a")
		elif b == 20 and False:
			print("b")
		elif a == 10 and True:
			print(a+b)
elif False:
	print("WORLD")

print("HELLO WORLD finall")"""
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 4, 6, 17])
		assert (step_json == {
		    "d":
		        1,
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
		        "end": 4
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 6
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 17
		    }]
		})
