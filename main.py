import csv
import tabulate
import argparse

class ParseArgs:
    def __init__(self, parser: argparse.ArgumentParser):
        self.__parser = parser
        self.__filename: str = None
        self.__where: str = None
        self.__agregate: str = None
        self.__order_by: str = None
        self.__create_interface()
        self.__set_args()

    def __create_interface(self):
        self.__parser.add_argument("--file", type=str, help="Input path/to/file")
        self.__parser.add_argument("--where", type=str, help="Enter your condition")
        self.__parser.add_argument("--agregate", type=str, help="Specify the aggregation condition")
        self.__parser.add_argument("--order-by", type=str, help="Please specify your field to sort by asc/desc")

    def __set_args(self):
        args = self.__parser.parse_args()
        self.__filename = args.file
        self.__where = args.where
        self.__agregate = args.agregate
        self.__order_by = args.order_by

    @property
    def filename(self):
        return self.__filename
    
    @property
    def where(self):
        return self.__where
    
    @property
    def agregate(self):
        return self.__agregate

    @property
    def order_by(self):
        return self.__order_by

    def get_all(self) -> tuple:
        result = tuple([self.__filename, self.__where, self.__agregate, self.__order_by])
        return result
    
class CsvRead:
    def __init__(self, filename: str):
        self.__filename: str = filename

    def print_all_rows(self):
        with open(self.__filename, "r", encoding="UTF-8") as csvfile:
            rows = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for ros in rows:
                print(', '.join(ros))

def main():
    parser = ParseArgs(argparse.ArgumentParser(description="Processing .csv"))
    filename, where, agregate, order_by = parser.get_all()
    read_csv = CsvRead(filename)
    read_csv.print_all_rows()



if(__name__ == "__main__"):
    main()