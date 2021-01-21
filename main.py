from fnmatch import filter
from functools import partial
from itertools import chain
from os import path, walk
import csv, random


class ProgramSearch(object):
    myData = [['2013-02-08', '67.7142', '68.4014', '66.8928', '67.8542', '158168416', 'RUS'],
              ['2013-02-11', '68.0714', '69.2771', '67.6071', '68.5614', '129029425', 'DE'],
              ['2013-02-12', '68.5014', '68.9114', '66.8205', '66.8428', '151829363', 'PL']]

    names = ['date', 'open', 'high', 'low', 'close', 'volume', 'Name']

    def __init__(self, directory):
        self.directory = directory
        self.generate_dict = [dict(zip(self.names, i)) for i in self.myData]
        self.result = (chain.from_iterable(
            (map(partial(path.join, root), filter(filenames, "*.csv")) for root, _, filenames in
              walk(self.directory))))

    def writer_csv(self):
        for file_csv in self.result:
            with open(file_csv, mode="r+", encoding='utf-8') as w_file:
                fieldnames = ['date', 'open', 'high', 'low', 'close', 'volume', 'Name']
                file_writer = csv.DictWriter(w_file, delimiter=",", lineterminator="\r", fieldnames=fieldnames)
                file_writer.writeheader()
                for i in self.generate_dict:
                    file_writer.writerow(i)

    def reade_csv(self):
        for file_csv in self.result:
            with open(file_csv, mode="r+", encoding='utf-8') as w_file:
                reader = csv.reader(w_file)
                print(reader.line_num)

    @property
    def convert_object(self):
        return self.directory, self.result, self.generate_dict


if __name__ == "__main__":
    m = ProgramSearch("data")
    m.reade_csv()
    # for _ in range(10):
    #     m.reade_csv()
    #
    # for i in m.reade_csv():
    #     print(i)
