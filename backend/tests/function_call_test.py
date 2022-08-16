import os
import pathlib

current_absolute_path = str(pathlib.Path(__file__).parent.resolve())

class Test_Function_Calling():
	# TODO: function loading error??
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
		with open(current_absolute_path + "/../" + "UserCode.py", 'w') as f_w:
			f_w.write(usercode)
		f_w.close()

		os.system("python " + current_absolute_path + "/../" + "Pytracker.py")

		listoflist = eval(open(current_absolute_path + "/../" + "listoflist", 'r').read())
		step_json = eval(open(current_absolute_path + "/../" + "step_json.json", 'r').read())

		assert (listoflist == [1, 4, 10, 5, 6, 2, 7, 8, 2])
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
		        "end": 4
		    }, {
		        "type": "step",
		        "start": 4,
		        "end": 10
		    }, {
		        "type": "step",
		        "start": 10,
		        "end": 5
		    }, {
		        "type": "step",
		        "start": 5,
		        "end": 6
		    }, {
		        "type": "step",
		        "start": 6,
		        "end": 2
		    }, {
		        "type": "step",
		        "start": 2,
		        "end": 7
		    }, {
		        "type": "step",
		        "start": 7,
		        "end": 8
		    }, {
		        "type": "step",
		        "start": 8,
		        "end": 2
		    }]
		})

	# TODO: need to be done
	def test_multi_function_calling(self):
		pass
