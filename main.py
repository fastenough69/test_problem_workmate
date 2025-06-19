import csv
from tabulate import tabulate
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
    
class CsvProcessing:
    def __init__(self, filename: str, where: str=None, agregate: str=None, order_by: str=None):
        self.__filename: str = filename
        self.__where = where
        self.__agregate = agregate
        self.__order_by = order_by
        self.__namesfields: dict = {}
        self.__data: list[list] = None
        self.set_namefields()
        self.set_data()
        self.condition_where()

    def set_namefields(self):
        with open(self.__filename, "r", encoding="UTF-8") as csvfile:
            fields = list(csv.reader(csvfile, quotechar='|'))[0]
            for i, field in enumerate(fields):
                self.__namesfields[field] = self.__namesfields.get(field, i)

    def condition_where(self):
        if(not self.__where):
           return
        
        symbols = ['>', '<', '=']
        symbol: str = ''

        for sm in symbols:
            if(sm in self.__where):
                symbol = sm
                break

        field, value = self.__where.split(symbol)
        
        index = self.__namesfields[field]
        temp: list[list] = []

        for row in self.__data:
            if(symbol == '='):
                if(row[index] == value):
                    temp.append(row)
            elif(symbol == '>'):
                if(row[index] > value):
                    temp.append(row)
            elif(symbol == '<'):
                if(row[index] < value):
                    temp.append(row)

        self.__data = temp

    def condition_agregate(self):
        if(not self.__agregate):
            return

        operators: list[str] = ["avg", "max", "min"]
        operator: str = ""

        for op in operators:
            if(op in self.__agregate):
                operator = op
                break

        field, value = self.__agregate.split('=')
        res: float = 0
        index: int = self.__namesfields[field]

        # for row in self.__data:
        #     if(operator == value == operators[1]):
        #         res += row[index]




    def set_data(self):
        with open(self.__filename, "r", encoding="UTF-8") as csvfile:
            data = list(csv.reader(csvfile, quotechar='|'))[1:]
            self.__data = data

    def print_all_rows(self):
        print(tabulate(self.__data, headers=self.__namesfields, tablefmt="pretty"))

def main():
    parser = ParseArgs(argparse.ArgumentParser(description="Processing .csv"))
    filename, where, agregate, order_by = parser.get_all()
    read_csv = CsvProcessing(filename, where=where, agregate=agregate)
    read_csv.print_all_rows()


if(__name__ == "__main__"):
    main()