import os
import pathlib

current_absolute_path = str(pathlib.Path(__file__).parent.resolve())

class Test_Input():

	def test_simple_input(self):
		usercode = """a = input("enter your a:")
print(a)
"""
		with open(current_absolute_path + "/../" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/../" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/../" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/../" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2])
		assert (step_json == {"d": 5, "list": [{"type": "step", "start": 0, "end": 1}, {"type": "step", "start": 1, "end": 2}]})
