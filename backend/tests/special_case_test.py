import os
import pathlib

backend_absolute_path = str(pathlib.Path(__file__).parent.parent.resolve())


class Test_Different_Main():

	def test_call_by_main_method(self):
		usercode = """def main():
	a = 123
	print(a)
	b = 321
	print(f"b == {b}")

main()"""

		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 8, 2, 3, 4, 5])
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

	def test_call_by_ifname(self):
		usercode = """def main():
	a = 123
	print(a)
	b = 321
	print(f"b == {b}")

if __name__ == "__main__":
	main()"""

		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 9, 2, 3, 4, 5])
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
		        "end": 9
		    }, {
		        "type": "step",
		        "start": 9,
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

		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 3, 4])
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
		        "end": 3
		    }, {
		        "type": "step",
		        "start": 3,
		        "end": 4
		    }]
		})

	def test_only_one_line_assignment(self):
		usercode = """a = 123"""

		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1])
		assert (step_json == {
		    "d": 1,
		    "list": [{
		        "type": "step",
		        "start": 0,
		        "end": 1
		    }]
		})
