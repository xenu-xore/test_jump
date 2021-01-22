from fnmatch import filter
from functools import partial
from itertools import chain
from os import path, walk
import csv, argparse


class ProgramSearch(object):
    myData = [['2013-02-08', '67.7142', '68.4014', '66.8928', '67.8542', '158168416', 'RUS'],
              ['2013-02-11', '68.0714', '69.2771', '67.6071', '68.5614', '129029425', 'DE'],
              ['2013-02-12', '68.5014', '68.9114', '66.8205', '66.8428', '151829363', 'PL']]

    names = ['date', 'open', 'high', 'low', 'close', 'volume', 'Name']

    def __init__(self, directory):

        self.directory = directory
        self.result = (chain.from_iterable(
            (map(partial(path.join, root), filter(file_names, "*.csv")) for root, _, file_names in
             walk(self.directory))))

    def generate_dict(self):
        return [dict(zip(self.names, i)) for i in self.myData]

    def writer_csv(self):

        for file_csv in self.result:

            with open(file_csv, mode="r+", encoding='utf-8') as w_file:
                fieldnames = ['date', 'open', 'high', 'low', 'close', 'volume', 'Name']
                file_writer = csv.DictWriter(w_file, delimiter=",", lineterminator="\r", fieldnames=fieldnames)
                file_writer.writeheader()
                for i in self.generate_dict():
                    file_writer.writerow(i)

    def reade_csv(self, word):

        _opens = 0.0
        _high = 0.0
        _low = 0.0
        _close = 0.0
        _volume = 0.0

        _count_files = 0

        for file_csv in self.result:
            try:
                with open(file_csv, mode="r+", encoding='utf-8') as w_file:
                    reader = csv.reader(w_file)

                    for reader_row in reader:

                        if reader_row[6] == word:
                            _count_files += 1

                            opens = reader_row[1]
                            _opens += float(opens)

                            high = reader_row[2]
                            _high += float(high)

                            low = reader_row[3]
                            _low += float(low)

                            close = reader_row[4]
                            _close += float(close)
                        else:
                            pass
            except IndexError:
                print(f"В файле {file_csv} нет искомых полей")

        try:
            return {'open': round(_opens / _count_files, 3),
                    'high': round(_high / _count_files, 3),
                    'low': round(_low / _count_files, 3),
                    'close': round(_close / _count_files, 3)
                    }
        except Exception as e:
            return f"Не удалось получить результат {e}"




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=str, help="Enter directory name")

    parser.add_argument('word', type=str, help="Enter searching word")
    args = parser.parse_args()

    if args.directory and args.word:
        crawl = ProgramSearch(args.directory)
        print(crawl.reade_csv(args.word))
