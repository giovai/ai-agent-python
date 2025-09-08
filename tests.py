import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

class TestGetFilesInfo(unittest.TestCase):
    def test_current_dir(self):
        result = get_files_info("calculator")
        print(result)
        self.assertEqual(result, 
        """- tests.py: file_size=1343, is_dir=False
- main.py: file_size=576, is_dir=False
- pkg: file_size=128, is_dir=True""")
    
    def test_calculator_dir(self):
        result = get_files_info("calculator", "pkg")
        print(result)
        self.assertEqual(result, 
        """- render.py: file_size=767, is_dir=False
- calculator.py: file_size=1738, is_dir=False""")
    
    def test_outside_work_dir(self):
        result = get_files_info("calculator", "/bin")
        print(result)
        self.assertEqual('Error: failed to get files info: Error: Cannot access "/bin" as it is outside the permitted working directory', result)
    
    def test_outside_work_dir_relative(self):
        result = get_files_info("calculator", "../")
        print(result)
        self.assertEqual('Error: failed to get files info: Error: Cannot access "../" as it is outside the permitted working directory', result)

class TestGetFileContent(unittest.TestCase):
    def test_shorter_than_limit(self):
        result = get_file_content("calculator", "main.py")
        print(result)
    def test_nested(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)
    def test_outside_permitted_dir(self):
        result = get_file_content("calculator", "/bin/cat")
        print(result)
    def test_non_existent(self):
        result = get_file_content("calculator", "pkg/asdfsdf.py")
        print(result)

class TestWriteFileContent(unittest.TestCase):
    def test_existing_file(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)
    def test_new_file(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result)
    def test_nested_dir(self):
        result = write_file("calculator", "pkg/more/lorem.txt", "lorem ipsum dolor sit amet")
        print(result)
    def test_outside_permitted_dir(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(result)

class TestRunPythonFile(unittest.TestCase):
    def test_missing_args(self):
        result = run_python_file("calculator", "main.py")
        print(result)
    def test_with_args(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        print(result)
    def test_execute_tests(self):
        result = run_python_file("calculator", "tests.py")
        print(result)
    def test_outside_permitted_dir(self):
        result = run_python_file("calculator", "../main.py")
        print(result)
    def test_non_existent(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(result)
    def test_not_python(self):
        result = run_python_file("calculator", "nonexistent.bla")
        print(result)

if __name__ == "__main__":
    unittest.main()
