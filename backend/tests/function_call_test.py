import os
import pathlib

backend_absolute_path = str(pathlib.Path(__file__).parent.parent.resolve())


class Test_Function_Calling():
	# TODO: NameError: name 'myprint' is not defined
	# 2022-10-14 已查明原因，global variables为能更新，thesisB-demo是能正常工作的。
	# Correct output should be like below: 
# (1): def myprint(something):
# local_variables == {}
# (5): def main():
# local_variables == {'myprint': <function myprint at 0x7ff8397e0670>}
# (12): main()
# local_variables == {'myprint': <function myprint at 0x7ff8397e0670>, 'main': <function main at 0x7ff8397e0790>}
# (6): 	a = 123
# local_variables == {}
# (7): 	myprint(a)
# local_variables == {'a': 123}
# (2): 	print(something)
# local_variables == {'something': 123}
# (8): 	b = 321
# local_variables == {'a': 123}
# (9): 	myprint(b)
# local_variables == {'a': 123, 'b': 321}
# (2): 	print(something)
# local_variables == {'something': 321}

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
				"end": 5
			}, {
				"type": "step",
				"start": 5,
				"end": 12
			}, {
				"type": "step",
				"start": 12,
				"end": 6
			}, {
				"type": "step",
				"start": 6,
				"end": 7
			}, {
				"type": "step",
				"start": 7,
				"end": 2
			}, {
				"type": "step",
				"start": 2,
				"end": 8
			}, {
				"type": "step",
				"start": 8,
				"end": 9
			}, {
				"type": "step",
				"start": 9,
				"end": 2
			}]
		})

	# TODO: need to be done
	def test_multi_function_calling(self):
		pass
