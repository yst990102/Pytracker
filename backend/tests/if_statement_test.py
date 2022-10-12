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
		assert (step_json == {
		    'd':
		        1,
		    'list': [{
		        'end': 1,
		        'local_variables': {
		            'a': 10
		        },
		        'start': 0,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 2,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 1,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 4,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 2,
		        'stdout': 'HELLO\n',
		        'type': 'step'
		    }]
		})

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
		    'd':
		        1,
		    'list': [{
		        'end': 1,
		        'local_variables': {
		            'a': 10
		        },
		        'start': 0,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 2,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 1,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 7,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 2,
		        'stdout': '10\n',
		        'type': 'step'
		    }, {
		        'end': 8,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 7,
		        'stdout': '10\n20\n',
		        'type': 'step'
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
		    'd':
		        4,
		    'list': [{
		        'end': 1,
		        'local_variables': {
		            'a': 10
		        },
		        'start': 0,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 2,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 1,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 4,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 2,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 1,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 4,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'depth': -1,
		        'type': 'while_start'
		    }, {
		        'end': 6,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 4,
		        'stdout': 'HELLO\n',
		        'type': 'step'
		    }, {
		        'end': 7,
		        'local_variables': {
		            'a': 11,
		            'b': 20
		        },
		        'start': 6,
		        'stdout': 'HELLO\n',
		        'type': 'step'
		    }, {
		        'iteration': 2,
		        'local_variables': {
		            'a': 11,
		            'b': 20
		        },
		        'start': 4,
		        'stdout': 'HELLO\n',
		        'type': 'circle'
		    }, {
		        'end': 6,
		        'local_variables': {
		            'a': 11,
		            'b': 20
		        },
		        'start': 4,
		        'stdout': 'HELLO\n'
		                  'HELLO\n',
		        'type': 'step'
		    }, {
		        'end': 7,
		        'local_variables': {
		            'a': 12,
		            'b': 20
		        },
		        'start': 6,
		        'stdout': 'HELLO\n'
		                  'HELLO\n',
		        'type': 'step'
		    }, {
		        'end': 7,
		        'start': 4,
		        'type': 'while_end'
		    }, {
		        'end': 8,
		        'local_variables': {
		            'a': 12,
		            'b': 20
		        },
		        'start': 7,
		        'stdout': 'HELLO\n'
		                  'HELLO\n',
		        'type': 'step'
		    }, {
		        'iteration': 1,
		        'local_variables': {
		            'a': 12,
		            'b': 20
		        },
		        'start': 8,
		        'stdout': 'HELLO\n'
		                  'HELLO\n',
		        'type': 'circle'
		    }, {
		        'depth': -1,
		        'type': 'while_start'
		    }, {
		        'end': 9,
		        'local_variables': {
		            'a': 12,
		            'b': 20
		        },
		        'start': 8,
		        'stdout': 'HELLO\n'
		                  'HELLO\n'
		                  'WORLD\n',
		        'type': 'step'
		    }, {
		        'end': 10,
		        'local_variables': {
		            'a': 12,
		            'b': 21
		        },
		        'start': 9,
		        'stdout': 'HELLO\n'
		                  'HELLO\n'
		                  'WORLD\n',
		        'type': 'step'
		    }, {
		        'end': 15,
		        'local_variables': {
		            'a': 12,
		            'b': 21
		        },
		        'start': 10,
		        'stdout': 'HELLO\n'
		                  'HELLO\n'
		                  'WORLD\n',
		        'type': 'step'
		    }, {
		        'iteration': 1,
		        'local_variables': {
		            'a': 12,
		            'b': 21
		        },
		        'start': 15,
		        'stdout': 'HELLO\n'
		                  'HELLO\n'
		                  'WORLD\n',
		        'type': 'circle'
		    }, {
		        'depth': -1,
		        'type': 'while_start'
		    }, {
		        'end': 17,
		        'local_variables': {
		            'a': 12,
		            'b': 21
		        },
		        'start': 15,
		        'stdout': 'HELLO\n'
		                  'HELLO\n'
		                  'WORLD\n'
		                  'this is not b\n',
		        'type': 'step'
		    }, {
		        'end': 18,
		        'local_variables': {
		            'a': 12,
		            'b': 22
		        },
		        'start': 17,
		        'stdout': 'HELLO\n'
		                  'HELLO\n'
		                  'WORLD\n'
		                  'this is not b\n',
		        'type': 'step'
		    }, {
		        'iteration': 4,
		        'local_variables': {
		            'a': 12,
		            'b': 24
		        },
		        'start': 15,
		        'stdout': 'HELLO\n'
		                  'HELLO\n'
		                  'WORLD\n'
		                  'this is not b\n'
		                  'this is not b\n'
		                  'this is not b\n',
		        'type': 'circle'
		    }, {
		        'end': 17,
		        'local_variables': {
		            'a': 12,
		            'b': 24
		        },
		        'start': 15,
		        'stdout': 'HELLO\n'
		                  'HELLO\n'
		                  'WORLD\n'
		                  'this is not b\n'
		                  'this is not b\n'
		                  'this is not b\n'
		                  'this is not b\n',
		        'type': 'step'
		    }, {
		        'end': 18,
		        'local_variables': {
		            'a': 12,
		            'b': 25
		        },
		        'start': 17,
		        'stdout': 'HELLO\n'
		                  'HELLO\n'
		                  'WORLD\n'
		                  'this is not b\n'
		                  'this is not b\n'
		                  'this is not b\n'
		                  'this is not b\n',
		        'type': 'step'
		    }],
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
		    'd':
		        1,
		    'list': [{
		        'end': 1,
		        'local_variables': {
		            'a': 10
		        },
		        'start': 0,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 2,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 1,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 4,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 2,
		        'stdout': 'HELLO\n',
		        'type': 'step'
		    }, {
		        'end': 9,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 4,
		        'stdout': 'HELLO\n'
		                  'HELLO WORLD\n',
		        'type': 'step'
		    }],
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
		assert (step_json == {
		    'd':
		        1,
		    'list': [{
		        'end': 1,
		        'local_variables': {
		            'a': 10
		        },
		        'start': 0,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 2,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 1,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 6,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 2,
		        'stdout': 'BYE\n',
		        'type': 'step'
		    }],
		})

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
		assert (step_json == {
		    'd':
		        1,
		    'list': [{
		        'end': 1,
		        'local_variables': {
		            'a': 10
		        },
		        'start': 0,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 2,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 1,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 13,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 2,
		        'stdout': '20\n',
		        'type': 'step'
		    }],
		})

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
		    'd':
		        4,
		    'list': [{
		        'end': 1,
		        'local_variables': {
		            'a': 10
		        },
		        'start': 0,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 2,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 1,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 11,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 2,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 1,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 11,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'depth': -1,
		        'type': 'while_start'
		    }, {
		        'end': 12,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 11,
		        'stdout': 'WORLD\n',
		        'type': 'step'
		    }, {
		        'end': 21,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 12,
		        'stdout': 'WORLD\n',
		        'type': 'step'
		    }, {
		        'iteration': 1,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 21,
		        'stdout': 'WORLD\n',
		        'type': 'circle'
		    }, {
		        'depth': -1,
		        'type': 'while_start'
		    }, {
		        'end': 23,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 21,
		        'stdout': 'WORLD\n'
		                  'this is not b\n',
		        'type': 'step'
		    }, {
		        'end': 26,
		        'local_variables': {
		            'a': 10,
		            'b': 21
		        },
		        'start': 23,
		        'stdout': 'WORLD\n'
		                  'this is not b\n',
		        'type': 'step'
		    }, {
		        'iteration': 5,
		        'local_variables': {
		            'a': 10,
		            'b': 24
		        },
		        'start': 21,
		        'stdout': 'WORLD\n'
		                  'this is not b\n'
		                  'this is not b\n'
		                  'this is not b\n'
		                  'this is not b\n',
		        'type': 'circle'
		    }, {
		        'end': 23,
		        'local_variables': {
		            'a': 10,
		            'b': 24
		        },
		        'start': 21,
		        'stdout': 'WORLD\n'
		                  'this is not b\n'
		                  'this is not b\n'
		                  'this is not b\n'
		                  'this is not b\n'
		                  'this is not b\n',
		        'type': 'step'
		    }, {
		        'end': 26,
		        'local_variables': {
		            'a': 10,
		            'b': 25
		        },
		        'start': 23,
		        'stdout': 'WORLD\n'
		                  'this is not b\n'
		                  'this is not b\n'
		                  'this is not b\n'
		                  'this is not b\n'
		                  'this is not b\n',
		        'type': 'step'
		    }, {
		        'end': 26,
		        'start': 21,
		        'type': 'while_end'
		    }, {
		        'end': 27,
		        'local_variables': {
		            'a': 10,
		            'b': 26
		        },
		        'start': 26,
		        'stdout': 'WORLD\n'
		                  'this is not b\n'
		                  'this is not b\n'
		                  'this is not b\n'
		                  'this is not b\n'
		                  'this is not b\n',
		        'type': 'step'
		    }],
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
		    'd':
		        1,
		    'list': [{
		        'end': 1,
		        'local_variables': {
		            'a': 10
		        },
		        'start': 0,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 2,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 1,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 4,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 2,
		        'stdout': 'HELLO\n',
		        'type': 'step'
		    }, {
		        'end': 14,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 4,
		        'stdout': 'HELLO\n'
		                  'HELLO WORLD finall\n',
		        'type': 'step'
		    }],
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
		assert (step_json == {
		    'd':
		        1,
		    'list': [{
		        'end': 1,
		        'local_variables': {
		            'a': 10
		        },
		        'start': 0,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 2,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 1,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 6,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 2,
		        'stdout': 'BYE\n',
		        'type': 'step'
		    }],
		})

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
		    'd':
		        1,
		    'list': [{
		        'end': 1,
		        'local_variables': {
		            'a': 10
		        },
		        'start': 0,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 2,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 1,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 6,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 2,
		        'stdout': '20\n',
		        'type': 'step'
		    }, {
		        'end': 10,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 6,
		        'stdout': '20\n'
		                  '20\n',
		        'type': 'step'
		    }, {
		        'end': 14,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 10,
		        'stdout': '20\n'
		                  '20\n'
		                  '20\n',
		        'type': 'step'
		    }],
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
		    'd':
		        1,
		    'list': [{
		        'end': 1,
		        'local_variables': {
		            'a': 10
		        },
		        'start': 0,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 2,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 1,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 4,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 2,
		        'stdout': 'HELLO\n',
		        'type': 'step'
		    }, {
		        'end': 6,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 4,
		        'stdout': 'HELLO\n'
		                  'HELLO 02\n',
		        'type': 'step'
		    }, {
		        'end': 17,
		        'local_variables': {
		            'a': 10,
		            'b': 20
		        },
		        'start': 6,
		        'stdout': 'HELLO\n'
		                  'HELLO 02\n'
		                  'HELLO WORLD finall\n',
		        'type': 'step'
		    }],
		})
