import os
import pathlib

backend_absolute_path = str(pathlib.Path(__file__).parent.parent.resolve())


class Test_Function_Calling():
	def test_one_function_calling(self):
		usercode = """def myprint(something):
	print(something)

def main():
	a=123
	myprint(a)
	b=321
	myprint(b)

main()
	"""
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 5, 12, 6, 7, 2, 8, 9, 2])

	def test_multi_function_calling(self):
		usercode = """def my_print(something):
	print('this is my_print')
	print(something)

def myprint(something):
	print(something)

def main():
	a=123
	myprint(a)
	b=321
	my_print(b)

main()
	"""
		with open(backend_absolute_path + "/" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + backend_absolute_path + "/" + "Pytracker.py")

		listoflist = eval(open(backend_absolute_path + "/" + "listoflist", 'r').read())
		step_json = eval(open(backend_absolute_path + "/" + "step_json.json", 'r').read())

		assert (listoflist == [1, 6, 10, 17, 11, 12, 7, 13, 14, 2, 3])
