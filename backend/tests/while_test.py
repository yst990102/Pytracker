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
