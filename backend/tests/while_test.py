import os
import pathlib

backend_absolute_path = str(pathlib.Path(__file__).parent.parent.resolve())


class Test_While_Statement():

	def test_simplest(self):
		usercode = """i = 0
while i < 5:
	print("Here")
	i += 1
"""
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, [2, 3, 4], [2, 3, 4], [2, 3, 4], [2, 3, 4], [2, 3, 4]])
		assert (step_json == {
		    'd':
		        3,
		    'list': [{
		        'end': 1,
		        'local_variables': {
		            'i': 0
		        },
		        'start': 0,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 2,
		        'local_variables': {
		            'i': 0
		        },
		        'start': 1,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 1,
		        'local_variables': {
		            'i': 0
		        },
		        'start': 2,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'depth': -1,
		        'type': 'while_start'
		    }, {
		        'end': 3,
		        'local_variables': {
		            'i': 0
		        },
		        'start': 2,
		        'stdout': 'Here\n',
		        'type': 'step'
		    }, {
		        'end': 4,
		        'local_variables': {
		            'i': 1
		        },
		        'start': 3,
		        'stdout': 'Here\n',
		        'type': 'step'
		    }, {
		        'iteration': 5,
		        'local_variables': {
		            'i': 4
		        },
		        'start': 2,
		        'stdout': 'Here\n'
		                  'Here\n'
		                  'Here\n'
		                  'Here\n',
		        'type': 'circle'
		    }, {
		        'end': 3,
		        'local_variables': {
		            'i': 4
		        },
		        'start': 2,
		        'stdout': 'Here\n'
		                  'Here\n'
		                  'Here\n'
		                  'Here\n'
		                  'Here\n',
		        'type': 'step'
		    }, {
		        'end': 4,
		        'local_variables': {
		            'i': 5
		        },
		        'start': 3,
		        'stdout': 'Here\n'
		                  'Here\n'
		                  'Here\n'
		                  'Here\n'
		                  'Here\n',
		        'type': 'step'
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
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, [3, [4, 5], [4, 5], [4, 5], [4, 5], [4, 5], [4, 5], 6], [3, 6], [3, 6], [3, 6], [3, 6], [3, 6]])
		assert (step_json == {
		    'd':
		        5,
		    'list': [{
		        'end': 1,
		        'local_variables': {
		            'i': 0
		        },
		        'start': 0,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 2,
		        'local_variables': {
		            'i': 0,
		            'j': 0
		        },
		        'start': 1,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 3,
		        'local_variables': {
		            'i': 0,
		            'j': 0
		        },
		        'start': 2,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 1,
		        'local_variables': {
		            'i': 0,
		            'j': 0
		        },
		        'start': 3,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'depth': -1,
		        'type': 'while_start'
		    }, {
		        'end': 4,
		        'local_variables': {
		            'i': 0,
		            'j': 0
		        },
		        'start': 3,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 1,
		        'local_variables': {
		            'i': 0,
		            'j': 0
		        },
		        'start': 4,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'depth': -1,
		        'type': 'while_start'
		    }, {
		        'end': 5,
		        'local_variables': {
		            'i': 0,
		            'j': 1
		        },
		        'start': 4,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 6,
		        'local_variables': {
		            'i': 0,
		            'j': 5
		        },
		        'start': 4,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'end': 5,
		        'local_variables': {
		            'i': 0,
		            'j': 6
		        },
		        'start': 4,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 5,
		        'start': 4,
		        'type': 'while_end'
		    }, {
		        'end': 6,
		        'local_variables': {
		            'i': 1,
		            'j': 6
		        },
		        'start': 5,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 6,
		        'local_variables': {
		            'i': 5,
		            'j': 6
		        },
		        'start': 3,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'end': 6,
		        'local_variables': {
		            'i': 6,
		            'j': 6
		        },
		        'start': 3,
		        'stdout': '',
		        'type': 'step'
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
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, [2, 4, 7], [2, 6, 7], [2, 4, 7], [2, 6, 7]])
		assert (step_json == {
		    'd':
		        3,
		    'list': [{
		        'end': 1,
		        'local_variables': {
		            'a': 4
		        },
		        'start': 0,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 2,
		        'local_variables': {
		            'a': 4
		        },
		        'start': 1,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 1,
		        'local_variables': {
		            'a': 4
		        },
		        'start': 2,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'depth': -1,
		        'type': 'while_start'
		    }, {
		        'end': 4,
		        'local_variables': {
		            'a': 4
		        },
		        'start': 2,
		        'stdout': 'EVEN\n',
		        'type': 'step'
		    }, {
		        'end': 7,
		        'local_variables': {
		            'a': 3
		        },
		        'start': 4,
		        'stdout': 'EVEN\n',
		        'type': 'step'
		    }, {
		        'iteration': 4,
		        'local_variables': {
		            'a': 1
		        },
		        'start': 2,
		        'stdout': 'EVEN\n'
		                  'ODD\n'
		                  'EVEN\n',
		        'type': 'circle'
		    }, {
		        'end': 6,
		        'local_variables': {
		            'a': 1
		        },
		        'start': 2,
		        'stdout': 'EVEN\n'
		                  'ODD\n'
		                  'EVEN\n'
		                  'ODD\n',
		        'type': 'step'
		    }, {
		        'end': 7,
		        'local_variables': {
		            'a': 0
		        },
		        'start': 6,
		        'stdout': 'EVEN\n'
		                  'ODD\n'
		                  'EVEN\n'
		                  'ODD\n',
		        'type': 'step'
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
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 3, [4, 5, [6, 8, 11], [6, 10, 11], 12], [4, 5, [6, 10, 11], [6, 8, 11], 12], [4, 5, [6, 8, 11], [6, 10, 11], 12], [4, 5, [6, 10, 11], [6, 8, 11], 12], 14, 15])
		assert (step_json == {
		    'd':
		        7,
		    'list': [{
		        'end': 1,
		        'local_variables': {
		            'even_sum': 0
		        },
		        'start': 0,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 2,
		        'local_variables': {
		            'even_sum': 0,
		            'odd_sum': 0
		        },
		        'start': 1,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 3,
		        'local_variables': {
		            'even_sum': 0,
		            'i': 0,
		            'odd_sum': 0
		        },
		        'start': 2,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 4,
		        'local_variables': {
		            'even_sum': 0,
		            'i': 0,
		            'odd_sum': 0
		        },
		        'start': 3,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 1,
		        'local_variables': {
		            'even_sum': 0,
		            'i': 0,
		            'odd_sum': 0
		        },
		        'start': 4,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'depth': -1,
		        'type': 'while_start'
		    }, {
		        'end': 5,
		        'local_variables': {
		            'even_sum': 0,
		            'i': 0,
		            'j': 4,
		            'odd_sum': 0
		        },
		        'start': 4,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 6,
		        'local_variables': {
		            'even_sum': 0,
		            'i': 0,
		            'j': 4,
		            'odd_sum': 0
		        },
		        'start': 5,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 1,
		        'local_variables': {
		            'even_sum': 0,
		            'i': 0,
		            'j': 4,
		            'odd_sum': 0
		        },
		        'start': 6,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'depth': -1,
		        'type': 'while_start'
		    }, {
		        'end': 8,
		        'local_variables': {
		            'even_sum': 4,
		            'i': 0,
		            'j': 4,
		            'odd_sum': 0
		        },
		        'start': 6,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 11,
		        'local_variables': {
		            'even_sum': 4,
		            'i': 0,
		            'j': 5,
		            'odd_sum': 0
		        },
		        'start': 8,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 2,
		        'local_variables': {
		            'even_sum': 4,
		            'i': 0,
		            'j': 5,
		            'odd_sum': 0
		        },
		        'start': 6,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'end': 10,
		        'local_variables': {
		            'even_sum': 4,
		            'i': 0,
		            'j': 5,
		            'odd_sum': 5
		        },
		        'start': 6,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 11,
		        'local_variables': {
		            'even_sum': 4,
		            'i': 0,
		            'j': 6,
		            'odd_sum': 5
		        },
		        'start': 10,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 11,
		        'start': 6,
		        'type': 'while_end'
		    }, {
		        'end': 12,
		        'local_variables': {
		            'even_sum': 4,
		            'i': 1,
		            'j': 6,
		            'odd_sum': 5
		        },
		        'start': 11,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 4,
		        'local_variables': {
		            'even_sum': 16,
		            'i': 3,
		            'j': 6,
		            'odd_sum': 17
		        },
		        'start': 4,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'end': 5,
		        'local_variables': {
		            'even_sum': 16,
		            'i': 3,
		            'j': 4,
		            'odd_sum': 17
		        },
		        'start': 4,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 6,
		        'local_variables': {
		            'even_sum': 16,
		            'i': 3,
		            'j': 4,
		            'odd_sum': 17
		        },
		        'start': 5,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 1,
		        'local_variables': {
		            'even_sum': 16,
		            'i': 3,
		            'j': 4,
		            'odd_sum': 17
		        },
		        'start': 6,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'depth': -1,
		        'type': 'while_start'
		    }, {
		        'end': 10,
		        'local_variables': {
		            'even_sum': 16,
		            'i': 3,
		            'j': 4,
		            'odd_sum': 24
		        },
		        'start': 6,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 11,
		        'local_variables': {
		            'even_sum': 16,
		            'i': 3,
		            'j': 5,
		            'odd_sum': 24
		        },
		        'start': 10,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 2,
		        'local_variables': {
		            'even_sum': 16,
		            'i': 3,
		            'j': 5,
		            'odd_sum': 24
		        },
		        'start': 6,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'end': 8,
		        'local_variables': {
		            'even_sum': 24,
		            'i': 3,
		            'j': 5,
		            'odd_sum': 24
		        },
		        'start': 6,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 11,
		        'local_variables': {
		            'even_sum': 24,
		            'i': 3,
		            'j': 6,
		            'odd_sum': 24
		        },
		        'start': 8,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 11,
		        'start': 6,
		        'type': 'while_end'
		    }, {
		        'end': 12,
		        'local_variables': {
		            'even_sum': 24,
		            'i': 4,
		            'j': 6,
		            'odd_sum': 24
		        },
		        'start': 11,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 12,
		        'start': 4,
		        'type': 'while_end'
		    }, {
		        'end': 14,
		        'local_variables': {
		            'even_sum': 24,
		            'i': 4,
		            'j': 6,
		            'odd_sum': 24
		        },
		        'start': 12,
		        'stdout': '24\n',
		        'type': 'step'
		    }, {
		        'end': 15,
		        'local_variables': {
		            'even_sum': 24,
		            'i': 4,
		            'j': 6,
		            'odd_sum': 24
		        },
		        'start': 14,
		        'stdout': '24\n'
		                  '24\n',
		        'type': 'step'
		    }]
		})

	def test_3layer(self):
		usercode = """i = 0
j = 0
k = 0
while i < 3:
	while j < 3:
		while k < 3:
			print(k)
			k += 1
		print(j)
		j += 1
	print(i)
	i += 1
"""
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 3, [4, [5, [6, 7, 8], [6, 7, 8], [6, 7, 8], 9, 10], [5, 9, 10], [5, 9, 10], 11, 12], [4, 11, 12], [4, 11, 12]])
		assert (step_json == {
		    'd':
		        7,
		    'list': [{
		        'end': 1,
		        'local_variables': {
		            'i': 0
		        },
		        'start': 0,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 2,
		        'local_variables': {
		            'i': 0,
		            'j': 0
		        },
		        'start': 1,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 3,
		        'local_variables': {
		            'i': 0,
		            'j': 0,
		            'k': 0
		        },
		        'start': 2,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 4,
		        'local_variables': {
		            'i': 0,
		            'j': 0,
		            'k': 0
		        },
		        'start': 3,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 1,
		        'local_variables': {
		            'i': 0,
		            'j': 0,
		            'k': 0
		        },
		        'start': 4,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'depth': -1,
		        'type': 'while_start'
		    }, {
		        'end': 5,
		        'local_variables': {
		            'i': 0,
		            'j': 0,
		            'k': 0
		        },
		        'start': 4,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 1,
		        'local_variables': {
		            'i': 0,
		            'j': 0,
		            'k': 0
		        },
		        'start': 5,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'depth': -1,
		        'type': 'while_start'
		    }, {
		        'end': 6,
		        'local_variables': {
		            'i': 0,
		            'j': 0,
		            'k': 0
		        },
		        'start': 5,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 1,
		        'local_variables': {
		            'i': 0,
		            'j': 0,
		            'k': 0
		        },
		        'start': 6,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'depth': -1,
		        'type': 'while_start'
		    }, {
		        'end': 7,
		        'local_variables': {
		            'i': 0,
		            'j': 0,
		            'k': 0
		        },
		        'start': 6,
		        'stdout': '0\n',
		        'type': 'step'
		    }, {
		        'end': 8,
		        'local_variables': {
		            'i': 0,
		            'j': 0,
		            'k': 1
		        },
		        'start': 7,
		        'stdout': '0\n',
		        'type': 'step'
		    }, {
		        'iteration': 3,
		        'local_variables': {
		            'i': 0,
		            'j': 0,
		            'k': 2
		        },
		        'start': 6,
		        'stdout': '0\n'
		                  '1\n',
		        'type': 'circle'
		    }, {
		        'end': 7,
		        'local_variables': {
		            'i': 0,
		            'j': 0,
		            'k': 2
		        },
		        'start': 6,
		        'stdout': '0\n'
		                  '1\n'
		                  '2\n',
		        'type': 'step'
		    }, {
		        'end': 8,
		        'local_variables': {
		            'i': 0,
		            'j': 0,
		            'k': 3
		        },
		        'start': 7,
		        'stdout': '0\n'
		                  '1\n'
		                  '2\n',
		        'type': 'step'
		    }, {
		        'end': 8,
		        'start': 6,
		        'type': 'while_end'
		    }, {
		        'end': 9,
		        'local_variables': {
		            'i': 0,
		            'j': 0,
		            'k': 3
		        },
		        'start': 8,
		        'stdout': '0\n'
		                  '1\n'
		                  '2\n'
		                  '0\n',
		        'type': 'step'
		    }, {
		        'end': 10,
		        'local_variables': {
		            'i': 0,
		            'j': 1,
		            'k': 3
		        },
		        'start': 9,
		        'stdout': '0\n'
		                  '1\n'
		                  '2\n'
		                  '0\n',
		        'type': 'step'
		    }, {
		        'iteration': 3,
		        'local_variables': {
		            'i': 0,
		            'j': 2,
		            'k': 3
		        },
		        'start': 5,
		        'stdout': '0\n'
		                  '1\n'
		                  '2\n'
		                  '0\n'
		                  '1\n',
		        'type': 'circle'
		    }, {
		        'end': 9,
		        'local_variables': {
		            'i': 0,
		            'j': 2,
		            'k': 3
		        },
		        'start': 5,
		        'stdout': '0\n'
		                  '1\n'
		                  '2\n'
		                  '0\n'
		                  '1\n'
		                  '2\n',
		        'type': 'step'
		    }, {
		        'end': 10,
		        'local_variables': {
		            'i': 0,
		            'j': 3,
		            'k': 3
		        },
		        'start': 9,
		        'stdout': '0\n'
		                  '1\n'
		                  '2\n'
		                  '0\n'
		                  '1\n'
		                  '2\n',
		        'type': 'step'
		    }, {
		        'end': 10,
		        'start': 5,
		        'type': 'while_end'
		    }, {
		        'end': 11,
		        'local_variables': {
		            'i': 0,
		            'j': 3,
		            'k': 3
		        },
		        'start': 10,
		        'stdout': '0\n'
		                  '1\n'
		                  '2\n'
		                  '0\n'
		                  '1\n'
		                  '2\n'
		                  '0\n',
		        'type': 'step'
		    }, {
		        'end': 12,
		        'local_variables': {
		            'i': 1,
		            'j': 3,
		            'k': 3
		        },
		        'start': 11,
		        'stdout': '0\n'
		                  '1\n'
		                  '2\n'
		                  '0\n'
		                  '1\n'
		                  '2\n'
		                  '0\n',
		        'type': 'step'
		    }, {
		        'iteration': 3,
		        'local_variables': {
		            'i': 2,
		            'j': 3,
		            'k': 3
		        },
		        'start': 4,
		        'stdout': '0\n'
		                  '1\n'
		                  '2\n'
		                  '0\n'
		                  '1\n'
		                  '2\n'
		                  '0\n'
		                  '1\n',
		        'type': 'circle'
		    }, {
		        'end': 11,
		        'local_variables': {
		            'i': 2,
		            'j': 3,
		            'k': 3
		        },
		        'start': 4,
		        'stdout': '0\n'
		                  '1\n'
		                  '2\n'
		                  '0\n'
		                  '1\n'
		                  '2\n'
		                  '0\n'
		                  '1\n'
		                  '2\n',
		        'type': 'step'
		    }, {
		        'end': 12,
		        'local_variables': {
		            'i': 3,
		            'j': 3,
		            'k': 3
		        },
		        'start': 11,
		        'stdout': '0\n'
		                  '1\n'
		                  '2\n'
		                  '0\n'
		                  '1\n'
		                  '2\n'
		                  '0\n'
		                  '1\n'
		                  '2\n',
		        'type': 'step'
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
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 3, [4, 5, [6, 8, 11], [6, 10, 11], [6, 8, 11], [6, 10, 11], 18], [4, 5, [6, 10, 11], [6, 8, 11], [6, 10, 11], [6, 8, 11], 18], 20, 21])
		assert (step_json == {
		    'd':
		        7,
		    'list': [{
		        'end': 1,
		        'local_variables': {
		            'even_sum': 0
		        },
		        'start': 0,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 2,
		        'local_variables': {
		            'even_sum': 0,
		            'odd_sum': 0
		        },
		        'start': 1,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 3,
		        'local_variables': {
		            'even_sum': 0,
		            'i': 0,
		            'odd_sum': 0
		        },
		        'start': 2,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 4,
		        'local_variables': {
		            'even_sum': 0,
		            'i': 0,
		            'odd_sum': 0
		        },
		        'start': 3,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 1,
		        'local_variables': {
		            'even_sum': 0,
		            'i': 0,
		            'odd_sum': 0
		        },
		        'start': 4,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'depth': -1,
		        'type': 'while_start'
		    }, {
		        'end': 5,
		        'local_variables': {
		            'even_sum': 0,
		            'i': 0,
		            'j': 0,
		            'odd_sum': 0
		        },
		        'start': 4,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 6,
		        'local_variables': {
		            'even_sum': 0,
		            'i': 0,
		            'j': 0,
		            'odd_sum': 0
		        },
		        'start': 5,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 1,
		        'local_variables': {
		            'even_sum': 0,
		            'i': 0,
		            'j': 0,
		            'odd_sum': 0
		        },
		        'start': 6,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'depth': -1,
		        'type': 'while_start'
		    }, {
		        'end': 8,
		        'local_variables': {
		            'even_sum': 0,
		            'i': 0,
		            'j': 0,
		            'odd_sum': 0
		        },
		        'start': 6,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 11,
		        'local_variables': {
		            'even_sum': 0,
		            'i': 0,
		            'j': 1,
		            'odd_sum': 0
		        },
		        'start': 8,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 4,
		        'local_variables': {
		            'even_sum': 2,
		            'i': 0,
		            'j': 3,
		            'odd_sum': 1
		        },
		        'start': 6,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'end': 10,
		        'local_variables': {
		            'even_sum': 2,
		            'i': 0,
		            'j': 3,
		            'odd_sum': 4
		        },
		        'start': 6,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 11,
		        'local_variables': {
		            'even_sum': 2,
		            'i': 0,
		            'j': 4,
		            'odd_sum': 4
		        },
		        'start': 10,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 11,
		        'start': 6,
		        'type': 'while_end'
		    }, {
		        'end': 18,
		        'local_variables': {
		            'even_sum': 2,
		            'i': 1,
		            'j': 4,
		            'odd_sum': 4
		        },
		        'start': 11,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 2,
		        'local_variables': {
		            'even_sum': 2,
		            'i': 1,
		            'j': 4,
		            'odd_sum': 4
		        },
		        'start': 4,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'end': 5,
		        'local_variables': {
		            'even_sum': 2,
		            'i': 1,
		            'j': 0,
		            'odd_sum': 4
		        },
		        'start': 4,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 6,
		        'local_variables': {
		            'even_sum': 2,
		            'i': 1,
		            'j': 0,
		            'odd_sum': 4
		        },
		        'start': 5,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 1,
		        'local_variables': {
		            'even_sum': 2,
		            'i': 1,
		            'j': 0,
		            'odd_sum': 4
		        },
		        'start': 6,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'depth': -1,
		        'type': 'while_start'
		    }, {
		        'end': 10,
		        'local_variables': {
		            'even_sum': 2,
		            'i': 1,
		            'j': 0,
		            'odd_sum': 5
		        },
		        'start': 6,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 11,
		        'local_variables': {
		            'even_sum': 2,
		            'i': 1,
		            'j': 1,
		            'odd_sum': 5
		        },
		        'start': 10,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 4,
		        'local_variables': {
		            'even_sum': 4,
		            'i': 1,
		            'j': 3,
		            'odd_sum': 8
		        },
		        'start': 6,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'end': 8,
		        'local_variables': {
		            'even_sum': 8,
		            'i': 1,
		            'j': 3,
		            'odd_sum': 8
		        },
		        'start': 6,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 11,
		        'local_variables': {
		            'even_sum': 8,
		            'i': 1,
		            'j': 4,
		            'odd_sum': 8
		        },
		        'start': 8,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 11,
		        'start': 6,
		        'type': 'while_end'
		    }, {
		        'end': 18,
		        'local_variables': {
		            'even_sum': 8,
		            'i': 2,
		            'j': 4,
		            'odd_sum': 8
		        },
		        'start': 11,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 18,
		        'start': 4,
		        'type': 'while_end'
		    }, {
		        'end': 20,
		        'local_variables': {
		            'even_sum': 8,
		            'i': 2,
		            'j': 4,
		            'odd_sum': 8
		        },
		        'start': 18,
		        'stdout': '8\n',
		        'type': 'step'
		    }, {
		        'end': 21,
		        'local_variables': {
		            'even_sum': 8,
		            'i': 2,
		            'j': 4,
		            'odd_sum': 8
		        },
		        'start': 20,
		        'stdout': '8\n'
		                  '8\n',
		        'type': 'step'
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
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, [3, 4, 5], [3, 4, 5]])
		assert (step_json == {
		    'd':
		        3,
		    'list': [{
		        'end': 1,
		        'local_variables': {
		            'a': 0
		        },
		        'start': 0,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 3,
		        'local_variables': {
		            'a': 0
		        },
		        'start': 1,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 1,
		        'local_variables': {
		            'a': 0
		        },
		        'start': 3,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'depth': -1,
		        'type': 'while_start'
		    }, {
		        'end': 4,
		        'local_variables': {
		            'a': 0
		        },
		        'start': 3,
		        'stdout': '1\n',
		        'type': 'step'
		    }, {
		        'end': 5,
		        'local_variables': {
		            'a': 1
		        },
		        'start': 4,
		        'stdout': '1\n',
		        'type': 'step'
		    }, {
		        'iteration': 2,
		        'local_variables': {
		            'a': 1
		        },
		        'start': 3,
		        'stdout': '1\n',
		        'type': 'circle'
		    }, {
		        'end': 4,
		        'local_variables': {
		            'a': 1
		        },
		        'start': 3,
		        'stdout': '1\n'
		                  '1\n',
		        'type': 'step'
		    }, {
		        'end': 5,
		        'local_variables': {
		            'a': 2
		        },
		        'start': 4,
		        'stdout': '1\n'
		                  '1\n',
		        'type': 'step'
		    }]
		})

	def test_not_increament_at_edge(self):
		usercode = """even_sum = 0
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
print(odd_sum)"""

		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 3, [4, 5, 6, [7, 8, 10], [7, 8, 12]], [4, 5, 6, [7, 8, 12], [7, 8, 10]], [4, 5, 6, [7, 8, 10], [7, 8, 12]], [4, 5, 6, [7, 8, 12], [7, 8, 10]], 14, 15])
		assert (step_json == {
		    'd':
		        4,
		    'list': [{
		        'end': 1,
		        'local_variables': {
		            'even_sum': 0
		        },
		        'start': 0,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 2,
		        'local_variables': {
		            'even_sum': 0,
		            'odd_sum': 0
		        },
		        'start': 1,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 3,
		        'local_variables': {
		            'even_sum': 0,
		            'i': 0,
		            'odd_sum': 0
		        },
		        'start': 2,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 4,
		        'local_variables': {
		            'even_sum': 0,
		            'i': 0,
		            'odd_sum': 0
		        },
		        'start': 3,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 1,
		        'local_variables': {
		            'even_sum': 0,
		            'i': 0,
		            'odd_sum': 0
		        },
		        'start': 4,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'depth': -1,
		        'type': 'while_start'
		    }, {
		        'end': 5,
		        'local_variables': {
		            'even_sum': 0,
		            'i': 1,
		            'odd_sum': 0
		        },
		        'start': 4,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 6,
		        'local_variables': {
		            'even_sum': 0,
		            'i': 1,
		            'j': 4,
		            'odd_sum': 0
		        },
		        'start': 5,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 7,
		        'local_variables': {
		            'even_sum': 0,
		            'i': 1,
		            'j': 4,
		            'odd_sum': 0
		        },
		        'start': 6,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 1,
		        'local_variables': {
		            'even_sum': 0,
		            'i': 1,
		            'j': 4,
		            'odd_sum': 0
		        },
		        'start': 7,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'depth': -1,
		        'type': 'while_start'
		    }, {
		        'end': 8,
		        'local_variables': {
		            'even_sum': 0,
		            'i': 1,
		            'j': 5,
		            'odd_sum': 0
		        },
		        'start': 7,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 10,
		        'local_variables': {
		            'even_sum': 6,
		            'i': 1,
		            'j': 5,
		            'odd_sum': 0
		        },
		        'start': 8,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 2,
		        'local_variables': {
		            'even_sum': 6,
		            'i': 1,
		            'j': 5,
		            'odd_sum': 0
		        },
		        'start': 7,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'end': 8,
		        'local_variables': {
		            'even_sum': 6,
		            'i': 1,
		            'j': 6,
		            'odd_sum': 0
		        },
		        'start': 7,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 12,
		        'local_variables': {
		            'even_sum': 6,
		            'i': 1,
		            'j': 6,
		            'odd_sum': 7
		        },
		        'start': 8,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 12,
		        'start': 7,
		        'type': 'while_end'
		    }, {
		        'iteration': 4,
		        'local_variables': {
		            'even_sum': 22,
		            'i': 3,
		            'j': 6,
		            'odd_sum': 23
		        },
		        'start': 4,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'end': 5,
		        'local_variables': {
		            'even_sum': 22,
		            'i': 4,
		            'j': 6,
		            'odd_sum': 23
		        },
		        'start': 4,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 6,
		        'local_variables': {
		            'even_sum': 22,
		            'i': 4,
		            'j': 4,
		            'odd_sum': 23
		        },
		        'start': 5,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 7,
		        'local_variables': {
		            'even_sum': 22,
		            'i': 4,
		            'j': 4,
		            'odd_sum': 23
		        },
		        'start': 6,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 1,
		        'local_variables': {
		            'even_sum': 22,
		            'i': 4,
		            'j': 4,
		            'odd_sum': 23
		        },
		        'start': 7,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'depth': -1,
		        'type': 'while_start'
		    }, {
		        'end': 8,
		        'local_variables': {
		            'even_sum': 22,
		            'i': 4,
		            'j': 5,
		            'odd_sum': 23
		        },
		        'start': 7,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 12,
		        'local_variables': {
		            'even_sum': 22,
		            'i': 4,
		            'j': 5,
		            'odd_sum': 32
		        },
		        'start': 8,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'iteration': 2,
		        'local_variables': {
		            'even_sum': 22,
		            'i': 4,
		            'j': 5,
		            'odd_sum': 32
		        },
		        'start': 7,
		        'stdout': '',
		        'type': 'circle'
		    }, {
		        'end': 8,
		        'local_variables': {
		            'even_sum': 22,
		            'i': 4,
		            'j': 6,
		            'odd_sum': 32
		        },
		        'start': 7,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 10,
		        'local_variables': {
		            'even_sum': 32,
		            'i': 4,
		            'j': 6,
		            'odd_sum': 32
		        },
		        'start': 8,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 10,
		        'start': 4,
		        'type': 'while_end'
		    }, {
		        'end': 10,
		        'start': 7,
		        'type': 'while_end'
		    }, {
		        'end': 14,
		        'local_variables': {
		            'even_sum': 32,
		            'i': 4,
		            'j': 6,
		            'odd_sum': 32
		        },
		        'start': 10,
		        'stdout': '32\n',
		        'type': 'step'
		    }, {
		        'end': 15,
		        'local_variables': {
		            'even_sum': 32,
		            'i': 4,
		            'j': 6,
		            'odd_sum': 32
		        },
		        'start': 14,
		        'stdout': '32\n'
		                  '32\n',
		        'type': 'step'
		    }],
		})

	def test_nested_while_at_same_depth(self):
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

	j = 0
	while j < 4:
		if (i + j) % 2 == 0:
			even_sum += (i + j)
		else:
			odd_sum += (i + j)
		j += 1
	i += 1

print(even_sum)
print(odd_sum)"""
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [
		    1, 2, 3, [4, 5, [6, 8, 11], [6, 10, 11], [6, 8, 11], [6, 10, 11], 13, [14, 16, 19], [14, 18, 19], [14, 16, 19], [14, 18, 19], 20],
		    [4, 5, [6, 10, 11], [6, 8, 11], [6, 10, 11], [6, 8, 11], 13, [14, 18, 19], [14, 16, 19], [14, 18, 19], [14, 16, 19], 20], 22, 23
		])
		assert (step_json == {
		    "d":
		        7,
		    "list": [{
		        "type": "step",
		        "start": 0,
		        "end": 1,
		        "local_variables": {
		            "even_sum": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 1,
		        "end": 2,
		        "local_variables": {
		            "even_sum": 0,
		            "odd_sum": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 2,
		        "end": 3,
		        "local_variables": {
		            "i": 0,
		            "even_sum": 0,
		            "odd_sum": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 4,
		        "local_variables": {
		            "i": 0,
		            "even_sum": 0,
		            "odd_sum": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 4,
		        "iteration": 1,
		        "local_variables": {
		            "i": 0,
		            "even_sum": 0,
		            "odd_sum": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5,
		        "local_variables": {
		            "i": 0,
		            "j": 0,
		            "even_sum": 0,
		            "odd_sum": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 6,
		        "local_variables": {
		            "i": 0,
		            "j": 0,
		            "even_sum": 0,
		            "odd_sum": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 6,
		        "iteration": 1,
		        "local_variables": {
		            "i": 0,
		            "j": 0,
		            "even_sum": 0,
		            "odd_sum": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 8,
		        "local_variables": {
		            "i": 0,
		            "j": 0,
		            "even_sum": 0,
		            "odd_sum": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 8,
		        "end": 11,
		        "local_variables": {
		            "i": 0,
		            "j": 1,
		            "even_sum": 0,
		            "odd_sum": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 6,
		        "iteration": 4,
		        "local_variables": {
		            "i": 0,
		            "j": 3,
		            "even_sum": 2,
		            "odd_sum": 1
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 10,
		        "local_variables": {
		            "i": 0,
		            "j": 3,
		            "even_sum": 2,
		            "odd_sum": 4
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 10,
		        "end": 11,
		        "local_variables": {
		            "i": 0,
		            "j": 4,
		            "even_sum": 2,
		            "odd_sum": 4
		        },
		        "stdout": ""
		    }, {
		        "type": "while_end",
		        "start": 6,
		        "end": 11
		    }, {
		        "type": "step",
		        "start": 11,
		        "end": 13,
		        "local_variables": {
		            "i": 0,
		            "j": 0,
		            "even_sum": 2,
		            "odd_sum": 4
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 13,
		        "end": 14,
		        "local_variables": {
		            "i": 0,
		            "j": 0,
		            "even_sum": 2,
		            "odd_sum": 4
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 14,
		        "iteration": 1,
		        "local_variables": {
		            "i": 0,
		            "j": 0,
		            "even_sum": 2,
		            "odd_sum": 4
		        },
		        "stdout": ""
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 14,
		        "end": 16,
		        "local_variables": {
		            "i": 0,
		            "j": 0,
		            "even_sum": 2,
		            "odd_sum": 4
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 16,
		        "end": 19,
		        "local_variables": {
		            "i": 0,
		            "j": 1,
		            "even_sum": 2,
		            "odd_sum": 4
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 14,
		        "iteration": 4,
		        "local_variables": {
		            "i": 0,
		            "j": 3,
		            "even_sum": 4,
		            "odd_sum": 5
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 14,
		        "end": 18,
		        "local_variables": {
		            "i": 0,
		            "j": 3,
		            "even_sum": 4,
		            "odd_sum": 8
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 18,
		        "end": 19,
		        "local_variables": {
		            "i": 0,
		            "j": 4,
		            "even_sum": 4,
		            "odd_sum": 8
		        },
		        "stdout": ""
		    }, {
		        "type": "while_end",
		        "start": 14,
		        "end": 19
		    }, {
		        "type": "step",
		        "start": 19,
		        "end": 20,
		        "local_variables": {
		            "i": 1,
		            "j": 4,
		            "even_sum": 4,
		            "odd_sum": 8
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 4,
		        "iteration": 2,
		        "local_variables": {
		            "i": 1,
		            "j": 4,
		            "even_sum": 4,
		            "odd_sum": 8
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5,
		        "local_variables": {
		            "i": 1,
		            "j": 0,
		            "even_sum": 4,
		            "odd_sum": 8
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 6,
		        "local_variables": {
		            "i": 1,
		            "j": 0,
		            "even_sum": 4,
		            "odd_sum": 8
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 6,
		        "iteration": 1,
		        "local_variables": {
		            "i": 1,
		            "j": 0,
		            "even_sum": 4,
		            "odd_sum": 8
		        },
		        "stdout": ""
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 10,
		        "local_variables": {
		            "i": 1,
		            "j": 0,
		            "even_sum": 4,
		            "odd_sum": 9
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 10,
		        "end": 11,
		        "local_variables": {
		            "i": 1,
		            "j": 1,
		            "even_sum": 4,
		            "odd_sum": 9
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 6,
		        "iteration": 4,
		        "local_variables": {
		            "i": 1,
		            "j": 3,
		            "even_sum": 6,
		            "odd_sum": 12
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 8,
		        "local_variables": {
		            "i": 1,
		            "j": 3,
		            "even_sum": 10,
		            "odd_sum": 12
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 8,
		        "end": 11,
		        "local_variables": {
		            "i": 1,
		            "j": 4,
		            "even_sum": 10,
		            "odd_sum": 12
		        },
		        "stdout": ""
		    }, {
		        "type": "while_end",
		        "start": 6,
		        "end": 11
		    }, {
		        "type": "step",
		        "start": 11,
		        "end": 13,
		        "local_variables": {
		            "i": 1,
		            "j": 0,
		            "even_sum": 10,
		            "odd_sum": 12
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 13,
		        "end": 14,
		        "local_variables": {
		            "i": 1,
		            "j": 0,
		            "even_sum": 10,
		            "odd_sum": 12
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 14,
		        "iteration": 1,
		        "local_variables": {
		            "i": 1,
		            "j": 0,
		            "even_sum": 10,
		            "odd_sum": 12
		        },
		        "stdout": ""
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 14,
		        "end": 18,
		        "local_variables": {
		            "i": 1,
		            "j": 0,
		            "even_sum": 10,
		            "odd_sum": 13
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 18,
		        "end": 19,
		        "local_variables": {
		            "i": 1,
		            "j": 1,
		            "even_sum": 10,
		            "odd_sum": 13
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 14,
		        "iteration": 4,
		        "local_variables": {
		            "i": 1,
		            "j": 3,
		            "even_sum": 12,
		            "odd_sum": 16
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 14,
		        "end": 16,
		        "local_variables": {
		            "i": 1,
		            "j": 3,
		            "even_sum": 16,
		            "odd_sum": 16
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 16,
		        "end": 19,
		        "local_variables": {
		            "i": 1,
		            "j": 4,
		            "even_sum": 16,
		            "odd_sum": 16
		        },
		        "stdout": ""
		    }, {
		        "type": "while_end",
		        "start": 14,
		        "end": 19
		    }, {
		        "type": "step",
		        "start": 19,
		        "end": 20,
		        "local_variables": {
		            "i": 2,
		            "j": 4,
		            "even_sum": 16,
		            "odd_sum": 16
		        },
		        "stdout": ""
		    }, {
		        "type": "while_end",
		        "start": 4,
		        "end": 20
		    }, {
		        "type": "step",
		        "start": 20,
		        "end": 22,
		        "local_variables": {
		            "i": 2,
		            "j": 4,
		            "even_sum": 16,
		            "odd_sum": 16
		        },
		        "stdout": "16\n"
		    }, {
		        "type": "step",
		        "start": 22,
		        "end": 23,
		        "local_variables": {
		            "i": 2,
		            "j": 4,
		            "even_sum": 16,
		            "odd_sum": 16
		        },
		        "stdout": "16\n16\n"
		    }]
		})

	def test_quadruple_nested_while(self):
		usercode = """i = 0
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
	i += 1"""

		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 3, 4, [5, [6, [7, [8, 9, 10], [8, 9, 10], [8, 9, 10], 11, 12], [7, 11, 12], [7, 11, 12], 13, 14], [6, 13, 14], [6, 13, 14], 15, 16], [5, 15, 16], [5, 15, 16]])
		assert (step_json == {
		    "d":
		        9,
		    "list": [{
		        "type": "step",
		        "start": 0,
		        "end": 1,
		        "local_variables": {
		            "i": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 1,
		        "end": 2,
		        "local_variables": {
		            "j": 0,
		            "i": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 2,
		        "end": 3,
		        "local_variables": {
		            "i": 0,
		            "k": 0,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 4,
		        "local_variables": {
		            "i": 0,
		            "l": 0,
		            "k": 0,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5,
		        "local_variables": {
		            "i": 0,
		            "l": 0,
		            "k": 0,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 5,
		        "iteration": 1,
		        "local_variables": {
		            "i": 0,
		            "l": 0,
		            "k": 0,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 6,
		        "local_variables": {
		            "i": 0,
		            "l": 0,
		            "k": 0,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 6,
		        "iteration": 1,
		        "local_variables": {
		            "i": 0,
		            "l": 0,
		            "k": 0,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 7,
		        "local_variables": {
		            "i": 0,
		            "l": 0,
		            "k": 0,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 7,
		        "iteration": 1,
		        "local_variables": {
		            "i": 0,
		            "l": 0,
		            "k": 0,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 7,
		        "end": 8,
		        "local_variables": {
		            "i": 0,
		            "l": 0,
		            "k": 0,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 8,
		        "iteration": 1,
		        "local_variables": {
		            "i": 0,
		            "l": 0,
		            "k": 0,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 8,
		        "end": 9,
		        "local_variables": {
		            "i": 0,
		            "l": 0,
		            "k": 0,
		            "j": 0
		        },
		        "stdout": "0\n"
		    }, {
		        "type": "step",
		        "start": 9,
		        "end": 10,
		        "local_variables": {
		            "i": 0,
		            "l": 1,
		            "k": 0,
		            "j": 0
		        },
		        "stdout": "0\n"
		    }, {
		        "type": "circle",
		        "start": 8,
		        "iteration": 3,
		        "local_variables": {
		            "i": 0,
		            "l": 2,
		            "k": 0,
		            "j": 0
		        },
		        "stdout": "0\n1\n"
		    }, {
		        "type": "step",
		        "start": 8,
		        "end": 9,
		        "local_variables": {
		            "i": 0,
		            "l": 2,
		            "k": 0,
		            "j": 0
		        },
		        "stdout": "0\n1\n2\n"
		    }, {
		        "type": "step",
		        "start": 9,
		        "end": 10,
		        "local_variables": {
		            "i": 0,
		            "l": 3,
		            "k": 0,
		            "j": 0
		        },
		        "stdout": "0\n1\n2\n"
		    }, {
		        "type": "while_end",
		        "start": 8,
		        "end": 10
		    }, {
		        "type": "step",
		        "start": 10,
		        "end": 11,
		        "local_variables": {
		            "i": 0,
		            "l": 3,
		            "k": 0,
		            "j": 0
		        },
		        "stdout": "0\n1\n2\n0\n"
		    }, {
		        "type": "step",
		        "start": 11,
		        "end": 12,
		        "local_variables": {
		            "i": 0,
		            "l": 3,
		            "k": 1,
		            "j": 0
		        },
		        "stdout": "0\n1\n2\n0\n"
		    }, {
		        "type": "circle",
		        "start": 7,
		        "iteration": 3,
		        "local_variables": {
		            "i": 0,
		            "l": 3,
		            "k": 2,
		            "j": 0
		        },
		        "stdout": "0\n1\n2\n0\n1\n"
		    }, {
		        "type": "step",
		        "start": 7,
		        "end": 11,
		        "local_variables": {
		            "i": 0,
		            "l": 3,
		            "k": 2,
		            "j": 0
		        },
		        "stdout": "0\n1\n2\n0\n1\n2\n"
		    }, {
		        "type": "step",
		        "start": 11,
		        "end": 12,
		        "local_variables": {
		            "i": 0,
		            "l": 3,
		            "k": 3,
		            "j": 0
		        },
		        "stdout": "0\n1\n2\n0\n1\n2\n"
		    }, {
		        "type": "while_end",
		        "start": 7,
		        "end": 12
		    }, {
		        "type": "step",
		        "start": 12,
		        "end": 13,
		        "local_variables": {
		            "i": 0,
		            "l": 3,
		            "k": 3,
		            "j": 0
		        },
		        "stdout": "0\n1\n2\n0\n1\n2\n0\n"
		    }, {
		        "type": "step",
		        "start": 13,
		        "end": 14,
		        "local_variables": {
		            "i": 0,
		            "l": 3,
		            "k": 3,
		            "j": 1
		        },
		        "stdout": "0\n1\n2\n0\n1\n2\n0\n"
		    }, {
		        "type": "circle",
		        "start": 6,
		        "iteration": 3,
		        "local_variables": {
		            "i": 0,
		            "l": 3,
		            "k": 3,
		            "j": 2
		        },
		        "stdout": "0\n1\n2\n0\n1\n2\n0\n1\n"
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 13,
		        "local_variables": {
		            "i": 0,
		            "l": 3,
		            "k": 3,
		            "j": 2
		        },
		        "stdout": "0\n1\n2\n0\n1\n2\n0\n1\n2\n"
		    }, {
		        "type": "step",
		        "start": 13,
		        "end": 14,
		        "local_variables": {
		            "i": 0,
		            "l": 3,
		            "k": 3,
		            "j": 3
		        },
		        "stdout": "0\n1\n2\n0\n1\n2\n0\n1\n2\n"
		    }, {
		        "type": "while_end",
		        "start": 6,
		        "end": 14
		    }, {
		        "type": "step",
		        "start": 14,
		        "end": 15,
		        "local_variables": {
		            "i": 0,
		            "l": 3,
		            "k": 3,
		            "j": 3
		        },
		        "stdout": "0\n1\n2\n0\n1\n2\n0\n1\n2\n0\n"
		    }, {
		        "type": "step",
		        "start": 15,
		        "end": 16,
		        "local_variables": {
		            "i": 1,
		            "l": 3,
		            "k": 3,
		            "j": 3
		        },
		        "stdout": "0\n1\n2\n0\n1\n2\n0\n1\n2\n0\n"
		    }, {
		        "type": "circle",
		        "start": 5,
		        "iteration": 3,
		        "local_variables": {
		            "i": 2,
		            "l": 3,
		            "k": 3,
		            "j": 3
		        },
		        "stdout": "0\n1\n2\n0\n1\n2\n0\n1\n2\n0\n1\n"
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 15,
		        "local_variables": {
		            "i": 2,
		            "l": 3,
		            "k": 3,
		            "j": 3
		        },
		        "stdout": "0\n1\n2\n0\n1\n2\n0\n1\n2\n0\n1\n2\n"
		    }, {
		        "type": "step",
		        "start": 15,
		        "end": 16,
		        "local_variables": {
		            "i": 3,
		            "l": 3,
		            "k": 3,
		            "j": 3
		        },
		        "stdout": "0\n1\n2\n0\n1\n2\n0\n1\n2\n0\n1\n2\n"
		    }]
		})

	def test_3_unique_execpaths(self):
		usercode = """sum = 0
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

print(sum)"""

		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, [3, 4, [5, 7, 12], [5, 11, 12], [5, 7, 12], [5, 9, 12], 13], [3, 4, [5, 11, 12], [5, 7, 12], [5, 9, 12], [5, 7, 12], 13], 15])
		assert (step_json == {
		    "d":
		        9,
		    "list": [{
		        "type": "step",
		        "start": 0,
		        "end": 1,
		        "local_variables": {
		            "sum": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 1,
		        "end": 2,
		        "local_variables": {
		            "sum": 0,
		            "i": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 2,
		        "end": 3,
		        "local_variables": {
		            "sum": 0,
		            "i": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 3,
		        "iteration": 1,
		        "local_variables": {
		            "sum": 0,
		            "i": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 4,
		        "local_variables": {
		            "i": 0,
		            "sum": 0,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5,
		        "local_variables": {
		            "i": 0,
		            "sum": 0,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 5,
		        "iteration": 1,
		        "local_variables": {
		            "i": 0,
		            "sum": 0,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 7,
		        "local_variables": {
		            "i": 0,
		            "sum": 0,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 7,
		        "end": 12,
		        "local_variables": {
		            "i": 0,
		            "sum": 0,
		            "j": 1
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 5,
		        "iteration": 2,
		        "local_variables": {
		            "i": 0,
		            "sum": 0,
		            "j": 1
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 11,
		        "local_variables": {
		            "i": 0,
		            "sum": -1,
		            "j": 1
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 11,
		        "end": 12,
		        "local_variables": {
		            "i": 0,
		            "sum": -1,
		            "j": 2
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 5,
		        "iteration": 4,
		        "local_variables": {
		            "i": 0,
		            "sum": 1,
		            "j": 3
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 9,
		        "local_variables": {
		            "i": 0,
		            "sum": 4,
		            "j": 3
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 9,
		        "end": 12,
		        "local_variables": {
		            "i": 0,
		            "sum": 4,
		            "j": 4
		        },
		        "stdout": ""
		    }, {
		        "type": "while_end",
		        "start": 5,
		        "end": 12
		    }, {
		        "type": "step",
		        "start": 12,
		        "end": 13,
		        "local_variables": {
		            "i": 1,
		            "sum": 4,
		            "j": 4
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 3,
		        "iteration": 2,
		        "local_variables": {
		            "i": 1,
		            "sum": 4,
		            "j": 4
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 4,
		        "local_variables": {
		            "i": 1,
		            "sum": 4,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5,
		        "local_variables": {
		            "i": 1,
		            "sum": 4,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 5,
		        "iteration": 1,
		        "local_variables": {
		            "i": 1,
		            "sum": 4,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 11,
		        "local_variables": {
		            "i": 1,
		            "sum": 3,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 11,
		        "end": 12,
		        "local_variables": {
		            "i": 1,
		            "sum": 3,
		            "j": 1
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 5,
		        "iteration": 3,
		        "local_variables": {
		            "i": 1,
		            "sum": 5,
		            "j": 2
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 9,
		        "local_variables": {
		            "i": 1,
		            "sum": 8,
		            "j": 2
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 9,
		        "end": 12,
		        "local_variables": {
		            "i": 1,
		            "sum": 8,
		            "j": 3
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 5,
		        "iteration": 4,
		        "local_variables": {
		            "i": 1,
		            "sum": 8,
		            "j": 3
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 7,
		        "local_variables": {
		            "i": 1,
		            "sum": 12,
		            "j": 3
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 7,
		        "end": 12,
		        "local_variables": {
		            "i": 1,
		            "sum": 12,
		            "j": 4
		        },
		        "stdout": ""
		    }, {
		        "type": "while_end",
		        "start": 5,
		        "end": 12
		    }, {
		        "type": "step",
		        "start": 12,
		        "end": 13,
		        "local_variables": {
		            "i": 2,
		            "sum": 12,
		            "j": 4
		        },
		        "stdout": ""
		    }, {
		        "type": "while_end",
		        "start": 3,
		        "end": 13
		    }, {
		        "type": "step",
		        "start": 13,
		        "end": 15,
		        "local_variables": {
		            "i": 2,
		            "sum": 12,
		            "j": 4
		        },
		        "stdout": "12\n"
		    }]
		})

	def test_arbitrary_nested_level(self):
		usercode = """a = 0
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

print(sum)"""

		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 3, 4, [5, 6, [7, 9, 14], [7, 13, 14], [7, 9, 14], [7, 11, 14], 15], [5, 6, [7, 13, 14], [7, 9, 14], [7, 11, 14], [7, 9, 14], 15], 21])
		assert (step_json == {
		    "d":
		        9,
		    "list": [{
		        "type": "step",
		        "start": 0,
		        "end": 1,
		        "local_variables": {
		            "a": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 1,
		        "end": 3,
		        "local_variables": {
		            "sum": 0,
		            "a": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 4,
		        "local_variables": {
		            "i": 0,
		            "a": 0,
		            "sum": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5,
		        "local_variables": {
		            "i": 0,
		            "a": 0,
		            "sum": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 5,
		        "iteration": 1,
		        "local_variables": {
		            "i": 0,
		            "a": 0,
		            "sum": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 6,
		        "local_variables": {
		            "i": 0,
		            "a": 0,
		            "sum": 0,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 7,
		        "local_variables": {
		            "i": 0,
		            "a": 0,
		            "sum": 0,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 7,
		        "iteration": 1,
		        "local_variables": {
		            "i": 0,
		            "a": 0,
		            "sum": 0,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 7,
		        "end": 9,
		        "local_variables": {
		            "i": 0,
		            "a": 0,
		            "sum": 0,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 9,
		        "end": 14,
		        "local_variables": {
		            "i": 0,
		            "a": 0,
		            "sum": 0,
		            "j": 1
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 7,
		        "iteration": 2,
		        "local_variables": {
		            "i": 0,
		            "a": 0,
		            "sum": 0,
		            "j": 1
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 7,
		        "end": 13,
		        "local_variables": {
		            "i": 0,
		            "a": 0,
		            "sum": -1,
		            "j": 1
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 13,
		        "end": 14,
		        "local_variables": {
		            "i": 0,
		            "a": 0,
		            "sum": -1,
		            "j": 2
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 7,
		        "iteration": 4,
		        "local_variables": {
		            "i": 0,
		            "a": 0,
		            "sum": 1,
		            "j": 3
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 7,
		        "end": 11,
		        "local_variables": {
		            "i": 0,
		            "a": 0,
		            "sum": 4,
		            "j": 3
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 11,
		        "end": 14,
		        "local_variables": {
		            "i": 0,
		            "a": 0,
		            "sum": 4,
		            "j": 4
		        },
		        "stdout": ""
		    }, {
		        "type": "while_end",
		        "start": 7,
		        "end": 14
		    }, {
		        "type": "step",
		        "start": 14,
		        "end": 15,
		        "local_variables": {
		            "i": 1,
		            "a": 0,
		            "sum": 4,
		            "j": 4
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 5,
		        "iteration": 2,
		        "local_variables": {
		            "i": 1,
		            "a": 0,
		            "sum": 4,
		            "j": 4
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 6,
		        "local_variables": {
		            "i": 1,
		            "a": 0,
		            "sum": 4,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 7,
		        "local_variables": {
		            "i": 1,
		            "a": 0,
		            "sum": 4,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 7,
		        "iteration": 1,
		        "local_variables": {
		            "i": 1,
		            "a": 0,
		            "sum": 4,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 7,
		        "end": 13,
		        "local_variables": {
		            "i": 1,
		            "a": 0,
		            "sum": 3,
		            "j": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 13,
		        "end": 14,
		        "local_variables": {
		            "i": 1,
		            "a": 0,
		            "sum": 3,
		            "j": 1
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 7,
		        "iteration": 3,
		        "local_variables": {
		            "i": 1,
		            "a": 0,
		            "sum": 5,
		            "j": 2
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 7,
		        "end": 11,
		        "local_variables": {
		            "i": 1,
		            "a": 0,
		            "sum": 8,
		            "j": 2
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 11,
		        "end": 14,
		        "local_variables": {
		            "i": 1,
		            "a": 0,
		            "sum": 8,
		            "j": 3
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 7,
		        "iteration": 4,
		        "local_variables": {
		            "i": 1,
		            "a": 0,
		            "sum": 8,
		            "j": 3
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 7,
		        "end": 9,
		        "local_variables": {
		            "i": 1,
		            "a": 0,
		            "sum": 12,
		            "j": 3
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 9,
		        "end": 14,
		        "local_variables": {
		            "i": 1,
		            "a": 0,
		            "sum": 12,
		            "j": 4
		        },
		        "stdout": ""
		    }, {
		        "type": "while_end",
		        "start": 7,
		        "end": 14
		    }, {
		        "type": "step",
		        "start": 14,
		        "end": 15,
		        "local_variables": {
		            "i": 2,
		            "a": 0,
		            "sum": 12,
		            "j": 4
		        },
		        "stdout": ""
		    }, {
		        "type": "while_end",
		        "start": 5,
		        "end": 15
		    }, {
		        "type": "step",
		        "start": 15,
		        "end": 21,
		        "local_variables": {
		            "i": 2,
		            "a": 0,
		            "sum": 12,
		            "j": 4
		        },
		        "stdout": "12\n"
		    }]
		})
