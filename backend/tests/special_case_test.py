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
		    'd':
		        1,
		    'list': [{
		        'end': 1,
		        'local_variables': {
		            'a': 123
		        },
		        'start': 0,
		        'stdout': '',
		        'type': 'step'
		    }, {
		        'end': 2,
		        'local_variables': {
		            'a': 123
		        },
		        'start': 1,
		        'stdout': '123\n',
		        'type': 'step'
		    }, {
		        'end': 3,
		        'local_variables': {
		            'a': 123,
		            'b': 321
		        },
		        'start': 2,
		        'stdout': '123\n',
		        'type': 'step'
		    }, {
		        'end': 4,
		        'local_variables': {
		            'a': 123,
		            'b': 321
		        },
		        'start': 3,
		        'stdout': '123\nb == 321\n',
		        'type': 'step'
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
		assert (step_json == {'d': 1, 'list': [{'end': 1, 'local_variables': {'a': 123}, 'start': 0, 'stdout': '', 'type': 'step'}]})
