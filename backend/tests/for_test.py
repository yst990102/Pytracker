import os
import pathlib

backend_absolute_path = str(pathlib.Path(__file__).parent.parent.resolve())


class Test_For_Statement():

	def test_simple_forloop(self):
		usercode = """for i in range(5):
	print("Here")
"""
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]])
		assert (step_json == {
		    'd':
		        2,
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
		        'stdout': 'Here\n',
		        'type': 'step'
		    }, {
		        'iteration': 5,
		        'local_variables': {
		            'i': 4
		        },
		        'start': 1,
		        'stdout': 'Here\n'
		                  'Here\n'
		                  'Here\n'
		                  'Here\n',
		        'type': 'circle'
		    }, {
		        'end': 2,
		        'local_variables': {
		            'i': 4
		        },
		        'start': 1,
		        'stdout': 'Here\n'
		                  'Here\n'
		                  'Here\n'
		                  'Here\n'
		                  'Here\n',
		        'type': 'step'
		    }],
		})

	def test_complex_forloop(self):
		usercode = """for a in range(4):
	if a % 2 == 0:
		print("EVEN")
	else:
		print("ODD")
"""
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [[1, 3], [1, 5], [1, 3], [1, 5]])
		assert (step_json == {
		    'd':
		        2,
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
		        'stdout': 'EVEN\n',
		        'type': 'step'
		    }, {
		        'iteration': 4,
		        'local_variables': {
		            'a': 3
		        },
		        'start': 1,
		        'stdout': 'EVEN\n'
		                  'ODD\n'
		                  'EVEN\n',
		        'type': 'circle'
		    }, {
		        'end': 5,
		        'local_variables': {
		            'a': 3
		        },
		        'start': 1,
		        'stdout': 'EVEN\n'
		                  'ODD\n'
		                  'EVEN\n'
		                  'ODD\n',
		        'type': 'step'
		    }],
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
		# 应该获取与如下代码类似结果
		# even_sum = 0
		# odd_sum = 0
		# i = 0
		# j = 4
		# while i < 4:
		# 	while j < 6:
		# 		if (i + j) % 2 == 0:
		# 			even_sum += (i + j)
		# 		else:
		# 			odd_sum += (i + j)
		# 		j += 1
		# 	i += 1

		# print(even_sum)
		# print(odd_sum)

		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 3, [4, [5, 7], [5, 9]], [4, [5, 9], [5, 7]], [4, [5, 7], [5, 9]], [4, [5, 9], [5, 7]], 11, 12])
		assert (step_json == {
		    "d":
		        4,
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
		            "even_sum": 0,
		            "i": 0,
		            "odd_sum": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 4,
		        "local_variables": {
		            "even_sum": 0,
		            "i": 0,
		            "odd_sum": 0
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 4,
		        "iteration": 1,
		        "local_variables": {
		            "even_sum": 0,
		            "i": 0,
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
		            "even_sum": 0,
		            "i": 0,
		            "odd_sum": 0,
		            "j": 4
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 5,
		        "iteration": 1,
		        "local_variables": {
		            "even_sum": 0,
		            "i": 0,
		            "odd_sum": 0,
		            "j": 4
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
		            "even_sum": 4,
		            "i": 0,
		            "odd_sum": 0,
		            "j": 4
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 5,
		        "iteration": 2,
		        "local_variables": {
		            "even_sum": 4,
		            "i": 0,
		            "odd_sum": 0,
		            "j": 5
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 9,
		        "local_variables": {
		            "even_sum": 4,
		            "i": 0,
		            "odd_sum": 5,
		            "j": 5
		        },
		        "stdout": ""
		    }, {
		        "type": "while_end",
		        "start": 5,
		        "end": 9
		    }, {
		        "type": "circle",
		        "start": 4,
		        "iteration": 4,
		        "local_variables": {
		            "even_sum": 16,
		            "i": 3,
		            "odd_sum": 17,
		            "j": 5
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 5,
		        "local_variables": {
		            "even_sum": 16,
		            "i": 3,
		            "odd_sum": 17,
		            "j": 4
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 5,
		        "iteration": 1,
		        "local_variables": {
		            "even_sum": 16,
		            "i": 3,
		            "odd_sum": 17,
		            "j": 4
		        },
		        "stdout": ""
		    }, {
		        "type": "while_start",
		        "depth": -1
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 9,
		        "local_variables": {
		            "even_sum": 16,
		            "i": 3,
		            "odd_sum": 24,
		            "j": 4
		        },
		        "stdout": ""
		    }, {
		        "type": "circle",
		        "start": 5,
		        "iteration": 2,
		        "local_variables": {
		            "even_sum": 16,
		            "i": 3,
		            "odd_sum": 24,
		            "j": 5
		        },
		        "stdout": ""
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 7,
		        "local_variables": {
		            "even_sum": 24,
		            "i": 3,
		            "odd_sum": 24,
		            "j": 5
		        },
		        "stdout": ""
		    }, {
		        "type": "while_end",
		        "start": 4,
		        "end": 7
		    }, {
		        "type": "while_end",
		        "start": 5,
		        "end": 7
		    }, {
		        "type": "step",
		        "start": 7,
		        "end": 11,
		        "local_variables": {
		            "even_sum": 24,
		            "i": 3,
		            "odd_sum": 24,
		            "j": 5
		        },
		        "stdout": "24\n"
		    }, {
		        "type": "step",
		        "start": 11,
		        "end": 12,
		        "local_variables": {
		            "even_sum": 24,
		            "i": 3,
		            "odd_sum": 24,
		            "j": 5
		        },
		        "stdout": "24\n24\n"
		    }]
		})
