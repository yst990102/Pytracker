import os


single_while_loop = """
def main():
	i = 5
	while (i > 0):
		print("i == " ,i)
		i -= 1
		
if __name__ == "__main__":
	main()
"""

# helper functions
def export_test_case_to_file(output_file:str, test_case:str) -> None:
    with open(output_file + ".txt", "w") as f_write:
        f_write.write(test_case)
    f_write.close()
    return

def delete_file(file_name:str) -> None:
    os.remove(file_name + ".txt")
    return

def display_file(file_name:str) -> None:
    with open(file_name + ".txt", 'r') as f_read:
        content = f_read.read()
    print(content)
    f_read.close()

if __name__ == "__main__":
    export_test_case_to_file("testing_case", single_while_loop)
    display_file("testing_case")
    delete_file("testing_case")