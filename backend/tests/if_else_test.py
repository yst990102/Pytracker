import os
import pathlib

current_absolute_path = str(pathlib.Path(__file__).parent.resolve())

class Test_IF_Statement():

	def test_if(self):
		usercode = """a = 10
b = 20
if a < b:
	print("HELLO")
"""
		with open(current_absolute_path + "/../" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/../" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/../" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/../" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 4])
		assert (step_json == {"d": 5, "list": [{"type": "step", "start": 0, "end": 1}, {"type": "step", "start": 1, "end": 2}, {"type": "step", "start": 2, "end": 4}]})

	def test_ifelse(self):
		usercode = """a = 10
b = 20
if b < a:
	print("Hello")
else:
	print("BYE")
"""
		with open(current_absolute_path + "/../" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/../" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/../" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/../" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 6])
		assert (step_json == {"d": 5, "list": [{"type": "step", "start": 0, "end": 1}, {'type': 'step', 'start': 1, 'end': 2}, {'type': 'step', 'start': 2, 'end': 6}]})

