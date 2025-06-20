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
        args: argparse.Namespace = self.__parser.parse_args()
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

class CsvProcessing(ParseArgs):
    def __init__(self, parser):
        super().__init__(parser)
        self.__namesfields: dict = {}
        self.__data: list[list[str]] = None
        self.__set_all_data()
        self.__condition_where()
        self.__condition_agregate()
        self.__condition_orderby()

    def __condition_where(self):
        if(not self.where):
           return
        
        symbols = ['>', '<', '=']
        symbol: str = ''

        for sm in symbols:
            if(sm in self.where):
                symbol = sm
                break

        field, value = self.where.split(symbol)
        
        index = self.__namesfields[field]
        i = 0
        last = len(self.__data)

        while(i < last):
            if(symbol == '='):
                if(self.__data[i][index] != value):
                    self.__data.remove(self.__data[i])
                    last -= 1
                else:
                    i += 1
            elif(symbol == '>'):
                if(not self.__data[i][index] > value):
                    self.__data.remove(self.__data[i])
                    last -= 1
                else:
                    i += 1
            elif(symbol == '<'):
                if(not self.__data[i][index] < value):
                    self.__data.remove(self.__data[i])
                    last -= 1
                else:
                    i += 1

    def __condition_agregate(self):
        if(not self.agregate):
            return

        operators: list[str] = ["avg", "max", "min"]
        operator: str = ""

        for op in operators:
            if(op in self.agregate):
                operator = op
                break

        field, _ = self.agregate.split('=')
        temp: list = []
        index: int = self.__namesfields[field]

        for row in self.__data:
            temp.append(float(row[index]))

        self.__data.clear()
        self.__namesfields.clear()

        if(operator == operators[0]):
            self.__data.append([sum(temp) / len(temp)])
            self.__namesfields[operator] = self.__namesfields.get(operator, 1)

        elif(operator == operators[1]):
            self.__data.append([max(temp)])
            self.__namesfields[operator] = self.__namesfields.get(operator, 1)

        elif(operator == operators[2]):
            self.__data.append([min(temp)])
            self.__namesfields[operator] = self.__namesfields.get(operator, 1)

    def __condition_orderby(self):
        if(not self.order_by):
            return

        sort_by: list = ["asc", "desc"]
        operator: str = ""

        for op in sort_by:
            if(op in self.order_by):
                operator = op
                break

        field, _ = self.order_by.split('=')
        index = self.__namesfields[field]

        flag = (operator == sort_by[1])

        self.__data.sort(key=lambda row: row[index], reverse=flag)

    def __set_all_data(self):
        with open(self.filename, "r", encoding="UTF-8") as csvfile:
            data = list(csv.reader(csvfile, quotechar='|'))
            fields = data[0]
            for i, field in enumerate(fields):
                self.__namesfields[field] = self.__namesfields.get(field, i)
            self.__data = data[1:]

    def print_all_rows(self):
        print(tabulate(self.__data, headers=self.__namesfields.keys(), tablefmt="pretty"))

def main():
    processing_csv = CsvProcessing(argparse.ArgumentParser(description="Processing .csv"))
    processing_csv.print_all_rows()

if(__name__ == "__main__"):
    main()