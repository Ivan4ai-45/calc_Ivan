import unittest
from tracker import Tracker

class MyTestCase(unittest.TestCase):

    def test_add_row(self):
        self.calc = Tracker()
        self.calc.add_expense('70', 'Карты', 'Проиграл')
        self.assertEqual(self.calc.get_expense(), [{'Категория': 'Карты', 'Сумма': 70.0, 'Описание': 'Проиграл'}])

    def test_add_rows_with_bad_settings(self):
        self.calc = Tracker()
        self.assertEqual(self.calc.add_expense('dbhbfdn', 'Карты', 'Проиграл'), "Некорректный ввод!")

    def test_show_empty_list(self):
        self.calc = Tracker()
        self.assertEqual(self.calc.get_expense(), "У вас нет расходов!")

    def test_show_two_rows(self):
        self.calc = Tracker()
        self.calc.add_expense('20', 'Еда', 'Хлеб, мясо, молоко')
        self.calc.add_expense('100', 'Авто', 'Фара')
        self.assertEqual(self.calc.get_expense(), [{'Категория': 'Еда', 'Сумма': 20.0, 'Описание': 'Хлеб, мясо, молоко'},
                                                   {'Категория': 'Авто', 'Сумма': 100.0, 'Описание': 'Фара'}])
    def test_shor_total(self):
        self.calc = Tracker()
        self.calc.add_expense('20', 'Еда', 'Хлеб, мясо, молоко')
        self.calc.add_expense('100', 'Авто', 'Фара')
        self.assertEqual(self.calc.get_total(), 120)


if __name__ == '__main__':
    unittest.main()
