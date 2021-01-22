import unittest, os, shutil, csv
from main import ProgramSearch


class TestProgramSearchMethodsR(unittest.TestCase):
    """Тесты для функции"""
    myData_test = [['2013-02-08', '67.7142', '68.4014', '66.8928', '67.8542', '158168416', 'RUS'],
                   ['2013-02-11', '1.50', '2.50', '3.50', '4.50', '5', 'TEST'],
                   ['2013-02-12', '68.5014', '68.9114', '66.8205', '66.8428', '151829363', 'TEST']]

    names_test = ['date', 'open', 'high', 'low', 'close', 'volume', 'Name']

    def test_writer_csv(self):
        path = os.getcwd() + "/test/dir1/dir2/dir3/"

        try:
            os.makedirs(path)

            dir_name = []
            for dirpath, dirnames, filenames in os.walk("test"):
                for dirname in dirnames:
                    dir_name.append(os.path.join(dirpath, dirname))

            for i in range(1):
                for dirs in dir_name:
                    with open(dirs + "-" + str(i) + ".csv", "w+") as f:
                        csv.writer(f)
                        ps = ProgramSearch("test")
                        ps.myData = self.myData_test
                        ps.names = self.names_test
                        ps.generate_dict()
                        ps.writer_csv()

        except OSError as e:
            return f"Создать директорию {path} не удалось причина {e}"
        else:
            return f"Успешно создана директория {path}"


class TestProgramSearchMethodsW(unittest.TestCase):
    def test_reade_csv(self):

        path_del = os.getcwd() + "/test/"

        try:
            ps = ProgramSearch("test")
            self.assertTrue(ps.reade_csv("TEST")["open"] == 35.001)
            shutil.rmtree(path_del)

        except OSError as e:
            return f"Создать директорию {path_del} не удалось причина {e}"
        else:
            return f"Успешно удалена директория {path_del}"



if __name__ == '__main__':
    unittest.main()
