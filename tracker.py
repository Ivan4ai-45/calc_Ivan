import pandas as pd


class Tracker():

    def __init__(self):
        self.columns = ['Категория', 'Сумма', 'Описание']
        self.data = pd.DataFrame(columns=self.columns)

    def add_expense(self, amount: str, category: str, description: str):
        try:
            amount = float(amount)
            self.data.loc[len(self.data)] = [category, amount, description]
            return "\nРасход добавлен!"
        except ValueError:
            return "Некорректный ввод!"

    def get_expense(self):
        if self.data.empty:
            return "У вас нет расходов!"
        return self.data.to_dict('records')

    def get_total(self):
        if self.data.empty:
            return "У вас нет расходов!"
        return sum(self.data['Сумма'].tolist())

    def get_by_category(self, category_for_print):
        if self.data.empty:
            return "У вас нет расходов!"
        try:
            output = self.data[self.data['Категория'].str.contains(category_for_print, case=False, na=False)].to_dict('records')
            if output == []:
                return "Данной категории нет в списке!"
            return output
        except ValueError as e:
            return f"Ошибка ввода: {e}"
