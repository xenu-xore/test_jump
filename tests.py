import unittest
import os
from main import ProgramSearch
import shutil

# foo = ProgramSearch('data')
# print(foo.reade_csv('RUS'))
# foo.directory = 'data'
# soo = ProgramSearch(foo.directory)
# print(soo.reade_csv('RUS'))

class TestProgramSearchMethods(unittest.TestCase):
    """ТЕвсты для функции"""
    def test_writer_csv(self):
        for i in range(5):
            with open(i+".csv" )
        search
        path = os.getcwd() + "/test/dir1/dir2/"

        try:
            os.makedirs(path)
        except OSError:
            print("Не создалась %s" % path)
        else:
            print("Создано %s" % path)

        ps = ProgramSearch("test")
        ps.writer_csv()

        # path_del = os.getcwd() + "/test/"
        #
        # try:
        #     shutil.rmtree(path_del)
        # except OSError:
        #     print("Удалить директорию %s не удалось" % path_del)
        # else:
        #     print("Успешно удалена директория %s" % path_del)


    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # Проверим, что s.split не работает, если разделитель - не строка
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
