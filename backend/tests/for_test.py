import os
import pathlib

backend_absolute_path = str(pathlib.Path(__file__).parent.parent.resolve())


class Test_For_Statement():
	# DONE: TypeError: unhashable type: "list" --- fixed by 2022-08-15
	# TODO: Iteration Number Error
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
		assert (step_json == {})

	# DONE: TypeError: unhashable type: "list" --- fixed by 2022-08-15
	# TODO: Iteration Number Error
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
		    "d":
		        5,
		    "list": [{
		        "type": "step",
		        "start": 0,
		        "end": 1
		    }, {
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

	# DONE: TypeError: unhashable type: "list" --- fixed by 2022-08-15
	# TODO: Iteration Number Error
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
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 3, [4, [5, 7], [5, 9], [5, 9], [5, 7], [5, 7], [5, 9], [5, 9], [5, 7], 11], 12])
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
