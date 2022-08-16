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
		    "d":
		        0,
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

		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
		assert (step_json == {
		    "d":
		        0,
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
