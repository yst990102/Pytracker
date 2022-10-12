import os
import pathlib

backend_absolute_path = str(pathlib.Path(__file__).parent.parent.resolve())


class Test_Assignment():

	def test_simple_assignment(self):
		usercode = """a = 10
b = 20
tmp = a
a = b
b = tmp"""

		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 3, 4, 5])
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
		        'end': 3,
		        'local_variables': {
		            'a': 10,
		            'b': 20,
		            'tmp': 10
		        },
		        'start': 2,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 4,
		        'local_variables': {
		            'a': 20,
		            'b': 20,
		            'tmp': 10
		        },
		        'start': 3,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 5,
		        'local_variables': {
		            'a': 20,
		            'b': 10,
		            'tmp': 10
		        },
		        'start': 4,
		        'stdout': '',
		        'type': 'step'
		    }],
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

		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
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
		            'a': 10
		        },
		        'start': 1,
		        'stdout': '10\n',
		        'type': 'step'
		    }, {
		        'end': 3,
		        'local_variables': {
		            'a': 11
		        },
		        'start': 2,
		        'stdout': '10\n',
		        'type': 'step'
		    }, {
		        'end': 4,
		        'local_variables': {
		            'a': 11
		        },
		        'start': 3,
		        'stdout': '10\n'
		                  '11\n',
		        'type': 'step'
		    }, {
		        'end': 5,
		        'local_variables': {
		            'a': 10
		        },
		        'start': 4,
		        'stdout': '10\n'
		                  '11\n',
		        'type': 'step'
		    }, {
		        'end': 6,
		        'local_variables': {
		            'a': 10
		        },
		        'start': 5,
		        'stdout': '10\n'
		                  '11\n'
		                  '10\n',
		        'type': 'step'
		    }, {
		        'end': 7,
		        'local_variables': {
		            'a': 10
		        },
		        'start': 6,
		        'stdout': '10\n'
		                  '11\n'
		                  '10\n',
		        'type': 'step'
		    }, {
		        'end': 8,
		        'local_variables': {
		            'a': 10
		        },
		        'start': 7,
		        'stdout': '10\n'
		                  '11\n'
		                  '10\n'
		                  '10\n',
		        'type': 'step'
		    }, {
		        'end': 9,
		        'local_variables': {
		            'a': 10.0
		        },
		        'start': 8,
		        'stdout': '10\n'
		                  '11\n'
		                  '10\n'
		                  '10\n',
		        'type': 'step'
		    }, {
		        'end': 10,
		        'local_variables': {
		            'a': 10.0
		        },
		        'start': 9,
		        'stdout': '10\n'
		                  '11\n'
		                  '10\n'
		                  '10\n'
		                  '10.0\n',
		        'type': 'step'
		    }, {
		        'end': 11,
		        'local_variables': {
		            'a': 11.0
		        },
		        'start': 10,
		        'stdout': '10\n'
		                  '11\n'
		                  '10\n'
		                  '10\n'
		                  '10.0\n',
		        'type': 'step'
		    }, {
		        'end': 12,
		        'local_variables': {
		            'a': 11.0
		        },
		        'start': 11,
		        'stdout': '10\n'
		                  '11\n'
		                  '10\n'
		                  '10\n'
		                  '10.0\n'
		                  '11.0\n',
		        'type': 'step'
		    }, {
		        'end': 13,
		        'local_variables': {
		            'a': 10.0
		        },
		        'start': 12,
		        'stdout': '10\n'
		                  '11\n'
		                  '10\n'
		                  '10\n'
		                  '10.0\n'
		                  '11.0\n',
		        'type': 'step'
		    }, {
		        'end': 14,
		        'local_variables': {
		            'a': 10.0
		        },
		        'start': 13,
		        'stdout': '10\n'
		                  '11\n'
		                  '10\n'
		                  '10\n'
		                  '10.0\n'
		                  '11.0\n'
		                  '10.0\n',
		        'type': 'step'
		    }, {
		        'end': 15,
		        'local_variables': {
		            'a': 10.0
		        },
		        'start': 14,
		        'stdout': '10\n'
		                  '11\n'
		                  '10\n'
		                  '10\n'
		                  '10.0\n'
		                  '11.0\n'
		                  '10.0\n',
		        'type': 'step'
		    }, {
		        'end': 16,
		        'local_variables': {
		            'a': 10.0
		        },
		        'start': 15,
		        'stdout': '10\n'
		                  '11\n'
		                  '10\n'
		                  '10\n'
		                  '10.0\n'
		                  '11.0\n'
		                  '10.0\n'
		                  '10.0\n',
		        'type': 'step'
		    }, {
		        'end': 17,
		        'local_variables': {
		            'a': 10.0
		        },
		        'start': 16,
		        'stdout': '10\n'
		                  '11\n'
		                  '10\n'
		                  '10\n'
		                  '10.0\n'
		                  '11.0\n'
		                  '10.0\n'
		                  '10.0\n',
		        'type': 'step'
		    }, {
		        'end': 18,
		        'local_variables': {
		            'a': 10.0
		        },
		        'start': 17,
		        'stdout': '10\n'
		                  '11\n'
		                  '10\n'
		                  '10\n'
		                  '10.0\n'
		                  '11.0\n'
		                  '10.0\n'
		                  '10.0\n'
		                  '10.0\n',
		        'type': 'step'
		    }],
		})
