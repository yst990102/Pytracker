import os
import pathlib

backend_absolute_path = str(pathlib.Path(__file__).parent.parent.resolve())

class Test_IF_Statement():
	def test_simplest(self):
		usercode = """a = 10\nb = 20\nif a < b:\n\tprint("HELLO")"""
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()
		
		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 4])
		assert (step_json == {"d": 5, "list": [{"type": "step", "start": 0, "end": 1}, {"type": "step", "start": 1, "end": 2}, {"type": "step", "start": 2, "end": 4}]})
	
	def test_nested(self):
		usercode = """a = 10\nb = 20\nif a < b:\n\tif b > a:\n\t\tif a == 10:\n\t\t\tif b == 20:\n\t\t\t\tprint(a)\n\t\t\t\tprint(b)"""
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 7, 8])
		assert (step_json == {"d": 5, "list": [{"type": "step", "start": 0, "end": 1}, {"type": "step", "start": 1, "end": 2}, {"type": "step", "start": 2, "end": 7}, {"type": "step", "start": 7, "end": 8}]})
	
	def test_with_while(self):
		pass

	def test_true_or_false(self):
		pass


class Test_IF_Else_Statement():
	def test_simplest(self):
		usercode = """a = 10\nb = 20\nif b < a:\n\tprint("Hello")\nelse:\n\tprint("BYE")"""
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 2, 6])
		assert (step_json == {"d": 5, "list": [{"type": "step", "start": 0, "end": 1}, {'type': 'step', 'start': 1, 'end': 2}, {'type': 'step', 'start': 2, 'end': 6}]})
	
	def test_nested(self):
		pass

	def test_with_while(self):
		pass

	def test_true_or_false(self):
		pass


class Test_IF_Elif_Statement():
	def test_simplest(self):
		pass
	
	def test_nested(self):
		pass

	def test_with_while(self):
		pass

	def test_true_or_false(self):
		pass


if __name__ == "__main__":
	print(backend_absolute_path)