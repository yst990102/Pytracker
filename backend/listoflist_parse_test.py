from Pytracker import RETURN_JSON, RETURN_LISTOFLIST, backend_main


class Test_Assignment():

	def test_one(self):
		usercode = """a = 10
b = 20
tmp = a
a = b
b = tmp"""
		listoflist = backend_main(usercode=usercode, return_data=RETURN_LISTOFLIST)
		step_json = backend_main(usercode=usercode, return_data=RETURN_JSON)

		assert (listoflist == [1, 2, 3, 4, 5])
		assert (step_json == {
		    'd': 5,
		    'list': [{
		        'type': 'step',
		        'start': 0,
		        'end': 1
		    }, {
		        'type': 'step',
		        'start': 1,
		        'end': 2
		    }, {
		        'type': 'step',
		        'start': 2,
		        'end': 3
		    }, {
		        'type': 'step',
		        'start': 3,
		        'end': 4
		    }]
		})


class Test_IF_Statement():

	def test_if(self):
		usercode = """a = 10
b = 20
if a < b:
	print("HELLO")
"""
		listoflist = backend_main(usercode=usercode, return_data=RETURN_LISTOFLIST)
		step_json = backend_main(usercode=usercode, return_data=RETURN_JSON)

		assert (listoflist == [1, 2, 4])
		assert (step_json == {'d': 5, 'list': [{'type': 'step', 'start': 0, 'end': 1}, {'type': 'step', 'start': 1, 'end': 3}]})

	def test_ifelse(self):
		usercode = """a = 10
b = 20
if b < a:
	print("Hello")
else:
	print("BYE")
"""
		listoflist = backend_main(usercode=usercode, return_data=RETURN_LISTOFLIST)
		step_json = backend_main(usercode=usercode, return_data=RETURN_JSON)

		assert (listoflist == [1, 2, 6])
		assert (step_json == {'d': 5, 'list': [{'type': 'step', 'start': 0, 'end': 1}, {'type': 'step', 'start': 1, 'end': 5}]})


class Test_While_Statement():

	def test_complexwhile(self):
		usercode = """a = 4
while a > 0:
	if a % 2 == 0:
		print("EVEN")
	else:
		print("ODD")
	a -= 1
"""
		listoflist = backend_main(usercode=usercode, return_data=RETURN_LISTOFLIST)
		step_json = backend_main(usercode=usercode, return_data=RETURN_JSON)

		assert (listoflist == [1, [2, 4, 7], [2, 6, 7], [2, 4, 7], [2, 6, 7]])
		assert (step_json == {
		    'd':
		        5,
		    'list': [{
		        'type': 'step',
		        'start': 0,
		        'end': 1
		    }, {
		        'type': 'circle',
		        'start': 1,
		        'iteration': 1
		    }, {
		        'type': 'while_start',
		        'depth': -1
		    }, {
		        'type': 'step',
		        'start': 1,
		        'end': 3
		    }, {
		        'type': 'step',
		        'start': 3,
		        'end': 6
		    }, {
		        'type': 'circle',
		        'start': 1
		    }, {
		        'type': 'step',
		        'start': 1,
		        'end': 5
		    }, {
		        'type': 'step',
		        'start': 5,
		        'end': 6
		    }, {
		        'type': 'circle',
		        'start': 1
		    }, {
		        'type': 'step',
		        'start': 1,
		        'end': 3
		    }, {
		        'type': 'step',
		        'start': 3,
		        'end': 6
		    }, {
		        'type': 'circle',
		        'start': 1
		    }, {
		        'type': 'step',
		        'start': 1,
		        'end': 5
		    }, {
		        'type': 'step',
		        'start': 5,
		        'end': 6
		    }]
		})

	def test_nestedwhile(self):
		usercode = """even_sum = 0
odd_sum = 0
i = 0
while i < 4:
	j = 4
	while j < 6:
		if (i + j) % 2 == 0:
			even_sum += (i + j)
		else:
			odd_sum += (i + j)
		j += 1
	i += 1

print(even_sum)
print(odd_sum)
"""
		listoflist = backend_main(usercode=usercode, return_data=RETURN_LISTOFLIST)
		step_json = backend_main(usercode=usercode, return_data=RETURN_JSON)

		assert (listoflist == [1, 2, 3, [4, 5, [6, 8, 11], [6, 10, 11], 12], [4, 5, [6, 10, 11], [6, 8, 11], 12], [4, 5, [6, 8, 11], [6, 10, 11], 12], [4, 5, [6, 10, 11], [6, 8, 11], 12], 14, 15])
		assert (step_json == {
		    'd':
		        5,
		    'list': [{
		        'type': 'step',
		        'start': 0,
		        'end': 1
		    }, {
		        'type': 'step',
		        'start': 1,
		        'end': 2
		    }, {
		        'type': 'step',
		        'start': 2,
		        'end': 3
		    }, {
		        'type': 'circle',
		        'start': 3,
		        'iteration': 1
		    }, {
		        'type': 'while_start',
		        'depth': -1
		    }, {
		        'type': 'step',
		        'start': 3,
		        'end': 4
		    }, {
		        'type': 'step',
		        'start': 4,
		        'end': 5
		    }, {
		        'type': 'circle',
		        'start': 5,
		        'iteration': 1
		    }, {
		        'type': 'while_start',
		        'depth': -1
		    }, {
		        'type': 'step',
		        'start': 5,
		        'end': 7
		    }, {
		        'type': 'step',
		        'start': 7,
		        'end': 10
		    }, {
		        'type': 'circle',
		        'start': 5
		    }, {
		        'type': 'step',
		        'start': 5,
		        'end': 9
		    }, {
		        'type': 'step',
		        'start': 9,
		        'end': 10
		    }, {
		        'type': 'while_end',
		        'start': 5,
		        'end': 10
		    }, {
		        'type': 'step',
		        'start': 10,
		        'end': 11
		    }, {
		        'type': 'circle',
		        'start': 3
		    }, {
		        'type': 'step',
		        'start': 3,
		        'end': 4
		    }, {
		        'type': 'step',
		        'start': 4,
		        'end': 5
		    }, {
		        'type': 'circle',
		        'start': 5,
		        'iteration': 1
		    }, {
		        'type': 'while_start',
		        'depth': -1
		    }, {
		        'type': 'step',
		        'start': 5,
		        'end': 9
		    }, {
		        'type': 'step',
		        'start': 9,
		        'end': 10
		    }, {
		        'type': 'circle',
		        'start': 5
		    }, {
		        'type': 'step',
		        'start': 5,
		        'end': 7
		    }, {
		        'type': 'step',
		        'start': 7,
		        'end': 10
		    }, {
		        'type': 'while_end',
		        'start': 5,
		        'end': 10
		    }, {
		        'type': 'step',
		        'start': 10,
		        'end': 11
		    }, {
		        'type': 'circle',
		        'start': 3
		    }, {
		        'type': 'step',
		        'start': 3,
		        'end': 4
		    }, {
		        'type': 'step',
		        'start': 4,
		        'end': 5
		    }, {
		        'type': 'circle',
		        'start': 5,
		        'iteration': 1
		    }, {
		        'type': 'while_start',
		        'depth': -1
		    }, {
		        'type': 'step',
		        'start': 5,
		        'end': 7
		    }, {
		        'type': 'step',
		        'start': 7,
		        'end': 10
		    }, {
		        'type': 'circle',
		        'start': 5
		    }, {
		        'type': 'step',
		        'start': 5,
		        'end': 9
		    }, {
		        'type': 'step',
		        'start': 9,
		        'end': 10
		    }, {
		        'type': 'while_end',
		        'start': 5,
		        'end': 10
		    }, {
		        'type': 'step',
		        'start': 10,
		        'end': 11
		    }, {
		        'type': 'circle',
		        'start': 3
		    }, {
		        'type': 'step',
		        'start': 3,
		        'end': 4
		    }, {
		        'type': 'step',
		        'start': 4,
		        'end': 5
		    }, {
		        'type': 'circle',
		        'start': 5,
		        'iteration': 1
		    }, {
		        'type': 'while_start',
		        'depth': -1
		    }, {
		        'type': 'step',
		        'start': 5,
		        'end': 9
		    }, {
		        'type': 'step',
		        'start': 9,
		        'end': 10
		    }, {
		        'type': 'circle',
		        'start': 5
		    }, {
		        'type': 'step',
		        'start': 5,
		        'end': 7
		    }, {
		        'type': 'step',
		        'start': 7,
		        'end': 10
		    }, {
		        'type': 'while_end',
		        'start': 5,
		        'end': 10
		    }, {
		        'type': 'step',
		        'start': 10,
		        'end': 11
		    }, {
		        'type': 'while_end',
		        'start': 3,
		        'end': 11
		    }, {
		        'type': 'step',
		        'start': 11,
		        'end': 13
		    }, {
		        'type': 'step',
		        'start': 13,
		        'end': 14
		    }]
		})

	def test_simplewhile(self):
		usercode = """i = 0
while i < 5:
	print("Here")
	i += 1
"""
		listoflist = backend_main(usercode=usercode, return_data=RETURN_LISTOFLIST)
		step_json = backend_main(usercode=usercode, return_data=RETURN_JSON)

		assert (listoflist == [1, [2, 3, 4], [2, 3, 4], [2, 3, 4], [2, 3, 4], [2, 3, 4]])
		assert (step_json == {
		    'd':
		        5,
		    'list': [{
		        'type': 'step',
		        'start': 0,
		        'end': 1
		    }, {
		        'type': 'circle',
		        'start': 1,
		        'iteration': 1
		    }, {
		        'type': 'while_start',
		        'depth': -1
		    }, {
		        'type': 'step',
		        'start': 1,
		        'end': 2
		    }, {
		        'type': 'step',
		        'start': 2,
		        'end': 3
		    }, {
		        'type': 'circle',
		        'start': 1
		    }, {
		        'type': 'step',
		        'start': 1,
		        'end': 2
		    }, {
		        'type': 'step',
		        'start': 2,
		        'end': 3
		    }, {
		        'type': 'circle',
		        'start': 1
		    }, {
		        'type': 'step',
		        'start': 1,
		        'end': 2
		    }, {
		        'type': 'step',
		        'start': 2,
		        'end': 3
		    }, {
		        'type': 'circle',
		        'start': 1
		    }, {
		        'type': 'step',
		        'start': 1,
		        'end': 2
		    }, {
		        'type': 'step',
		        'start': 2,
		        'end': 3
		    }, {
		        'type': 'circle',
		        'start': 1
		    }, {
		        'type': 'step',
		        'start': 1,
		        'end': 2
		    }, {
		        'type': 'step',
		        'start': 2,
		        'end': 3
		    }]
		})


class Test_Different_Main():

	def test_call_by_main_method(self):
		usercode = """def main():
	a = int(input("enter a num:"))
	print(a)
	b = int(input("enter a num:"))
	print(f"b == {b}")

main()"""

		listoflist = backend_main(usercode=usercode, return_data=RETURN_LISTOFLIST)
		step_json = backend_main(usercode=usercode, return_data=RETURN_JSON)

		assert (listoflist == [1, 7, 2, 3, 4, 5])
		assert (step_json == {
		    'd':
		        5,
		    'list': [{
		        'end': 6,
		        'start': 0,
		        'type': 'step'
		    }, {
		        'end': 1,
		        'start': 6,
		        'type': 'step'
		    }, {
		        'end': 2,
		        'start': 1,
		        'type': 'step'
		    }, {
		        'end': 3,
		        'start': 2,
		        'type': 'step'
		    }, {
		        'end': 4,
		        'start': 3,
		        'type': 'step'
		    }]
		})

	def test_call_by_ifname(self):
		usercode = """def main():
	a = int(input("enter a num:"))
	print(a)
	b = int(input("enter a num:"))
	print(f"b == {b}")

if __name__ == "__main__":
	main()"""

		listoflist = backend_main(usercode=usercode, return_data=RETURN_LISTOFLIST)
		step_json = backend_main(usercode=usercode, return_data=RETURN_JSON)

		assert (listoflist == [1, 8, 2, 3, 4, 5])
		assert (step_json == {
		    'd':
		        5,
		    'list': [{
		        'end': 7,
		        'start': 0,
		        'type': 'step'
		    }, {
		        'end': 1,
		        'start': 7,
		        'type': 'step'
		    }, {
		        'end': 2,
		        'start': 1,
		        'type': 'step'
		    }, {
		        'end': 3,
		        'start': 2,
		        'type': 'step'
		    }, {
		        'end': 4,
		        'start': 3,
		        'type': 'step'
		    }]
		})

	def test_no_main_or_ifname(self):
		usercode = """a = int(input("enter a num:"))
print(a)
b = int(input("enter a num:"))
print(f"b == {b}")"""

		listoflist = backend_main(usercode=usercode, return_data=RETURN_LISTOFLIST)
		step_json = backend_main(usercode=usercode, return_data=RETURN_JSON)

		assert (listoflist == [1, 2, 3, 4])
		assert (step_json == {'d': 5, 'list': [{'end': 1, 'start': 0, 'type': 'step'}, {'end': 2, 'start': 1, 'type': 'step'}, {'end': 3, 'start': 2, 'type': 'step'}]})
