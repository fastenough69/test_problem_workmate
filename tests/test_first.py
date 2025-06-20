import pytest
import subprocess

PATH_TO_PY = "../venv/Scripts/python.exe"
PATH_TO_SCRIPT = "../main.py"
CSV_FILE = "../test.csv"
DIR_TEST_FILES = "out_files"

class TestClass:
    def test1(self):
        out = subprocess.run([PATH_TO_PY, PATH_TO_SCRIPT, "--file", CSV_FILE], capture_output=True, text=True, check=True).stdout
        test_out: str = ""
        with open("out_files/test1.txt", "r") as fl:
            test_out = fl.read()
        assert out == test_out

    def test2(self):
        out = subprocess.run([PATH_TO_PY, PATH_TO_SCRIPT, "--file", CSV_FILE, "--where", "rating=4.4"], capture_output=True, text=True, check=True).stdout
        test_out: str = ""
        with open(f"{DIR_TEST_FILES}/test2.txt") as fl:
            test_out = fl.read()
        assert out == test_out

    def test3(self):
        out = subprocess.run([PATH_TO_PY, PATH_TO_SCRIPT, "--file", CSV_FILE, "--where", "rating>4.4"], capture_output=True, text=True, check=True).stdout
        tets_out: str = ""
        with open(f"{DIR_TEST_FILES}/test3.txt", "r") as fl:
            tets_out = fl.read()
        assert out == tets_out