import unittest

import sys
sys.path.append("../..")
from backend.helper_functions import export_test_case_to_file, display_file, delete_file

class Test_Single_While_Loop(unittest.TestCase):
    test_content = """
def main():
    i = 5
    while (i > 0):
        print("i == " ,i)
        i -= 1
        
if __name__ == "__main__":
    main()
"""
    def test_run(self):
        export_test_case_to_file(self.__class__.__name__, self.test_content)
        display_file(self.__class__.__name__)
        delete_file(self.__class__.__name__)

if __name__ == "__main__":
    Test01 = Test_Single_While_Loop()
    Test01.test_run()