import unittest, os, shutil
from main import ProgramSearch


class TestProgramSearchWriter(unittest.TestCase):
    """Тесты для функции"""
    myData_test = [['2013-02-08', '67.7142', '68.4014', '66.8928', '67.8542', '158168416', 'TEST'],
                   ['2013-02-11', '68.0714', '69.2771', '67.6071', '68.5614', '129029425', 'TEST'],
                   ['2013-02-12', '68.5014', '68.9114', '66.8205', '66.8428', '151829363', 'TEST']]

    names_test = ['date', 'open', 'high', 'low', 'close', 'volume', 'Name']

    def test_create_dir_and_csv_and_count(self):
        ps = ProgramSearch("test")
        ps.myData = self.myData_test
        ps.names = self.names_test
        self.assertEqual(ps.names, self.names_test)
        self.assertEqual(ps.myData, self.myData_test)
        self.assertTrue(ps.generate_dict())
        self.assertIsNotNone(ps.create_dir_and_csv(create=True))

        path_del = os.getcwd() + "/test/"

        try:
            self.assertIn("open", ps.reade_csv("TEST"))
            self.assertFalse(shutil.rmtree(path_del))
        except OSError as e:
            return f"Удалить директорию {path_del} не удалось причина {e}"
        else:
            return f"Успешно удалена директория {path_del}"


if __name__ == '__main__':
    unittest.main()
