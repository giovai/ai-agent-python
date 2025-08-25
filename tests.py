import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_current_dir(self):
        result = get_files_info("calculator")
        print(result)
        self.assertEqual(result, 
        """Result for current directory:
- tests.py: file_size=1343, is_dir=False
- main.py: file_size=576, is_dir=False
- pkg: file_size=128, is_dir=True""")
    
    def test_calculator_dir(self):
        result = get_files_info("calculator", "pkg")
        print(result)
        self.assertEqual(result, 
        """Result for 'pkg' directory:
- render.py: file_size=767, is_dir=False
- calculator.py: file_size=1738, is_dir=False""")
    
    def test_outside_work_dir(self):
        result = get_files_info("calculator", "/bin")
        print(result)
        self.assertEqual('Error: Cannot list "/bin" as it is outside the permitted working directory', result)
    
    def test_outside_work_dir_relative(self):
        result = get_files_info("calculator", "../")
        print(result)
        self.assertEqual('Error: Cannot list "../" as it is outside the permitted working directory', result)

if __name__ == "__main__":
    unittest.main()
