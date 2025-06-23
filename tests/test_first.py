import pytest
import subprocess

PATH_TO_PY = "python3"
PATH_TO_SCRIPT = "../main.py"
CSV_FILE = "../test.csv"
DIR_TEST_FILES = "out_files"

class TestClass:
    def test1(self):
        out = subprocess.run([PATH_TO_PY, PATH_TO_SCRIPT, "--file", CSV_FILE], capture_output=True, text=True, check=True).stdout
        test_out: str = ""
        with open(f"{DIR_TEST_FILES}/test1.txt", "r") as fl:
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

    def test4(self):
        out = subprocess.run([PATH_TO_PY, PATH_TO_SCRIPT, "--file", CSV_FILE, "--where", "rating<4.6"], capture_output=True, text=True, check=True).stdout
        test_out: str = ""
        with open(f"{DIR_TEST_FILES}/test4.txt", "r") as fl:
            test_out = fl.read()
        assert out == test_out

    def test5(self):
        out = subprocess.run([PATH_TO_PY, PATH_TO_SCRIPT, "--file", CSV_FILE, "--agregate", "price=avg"], capture_output=True, text=True, check=True).stdout
        test_out: str = ""
        with open(f"{DIR_TEST_FILES}/test5.txt", "r") as fl:
            test_out = fl.read()
        assert out == test_out

    def test6(self):
        out = subprocess.run([PATH_TO_PY, PATH_TO_SCRIPT, "--file", CSV_FILE, "--agregate", "price=min"], capture_output=True, text=True, check=True).stdout
        test_out: str = ""
        with open(f"{DIR_TEST_FILES}/test6.txt", "r") as fl:
            test_out = fl.read()
        assert out == test_out

    def test7(self):
        out = subprocess.run([PATH_TO_PY, PATH_TO_SCRIPT, "--file", CSV_FILE, "--agregate", "price=max"], capture_output=True, text=True, check=True).stdout
        test_out: str = ""
        with open(f"{DIR_TEST_FILES}/test7.txt", "r") as fl:
            test_out = fl.read()
        assert out == test_out

    def test8(self):
        out = subprocess.run([PATH_TO_PY, PATH_TO_SCRIPT, "--file", CSV_FILE, "--where", "brand=xiaomi", "--agregate", "price=max"], capture_output=True, text=True, check=True).stdout
        test_out: str = ""
        with open(f"{DIR_TEST_FILES}/test8.txt", "r") as fl:
            test_out = fl.read()
        assert out == test_out

    def test9(self):
        out = subprocess.run([PATH_TO_PY, PATH_TO_SCRIPT, "--file", CSV_FILE, "--order-by", "rating=asc"], capture_output=True, text=True, check=True).stdout
        test_out: str = ""
        with open(f"{DIR_TEST_FILES}/test9.txt", "r") as fl:
            test_out = fl.read()
        assert out == test_out

    def test10(self):
        out = subprocess.run([PATH_TO_PY, PATH_TO_SCRIPT, "--file", CSV_FILE, "--order-by", "rating=desc"], capture_output=True, text=True, check=True).stdout
        test_out: str = ""
        with open(f"{DIR_TEST_FILES}/test10.txt", "r") as fl:
            test_out = fl.read()
        assert out == test_out

    def test11(self):
        out = subprocess.run([PATH_TO_PY, PATH_TO_SCRIPT, "--file", CSV_FILE, "--where", "brand=xiaomi", "--order-by", "rating=desc"], capture_output=True, text=True, check=True).stdout
        test_out: str = ""
        with open(f"{DIR_TEST_FILES}/test11.txt", "r") as fl:
            test_out = fl.read()
        assert out == test_out
