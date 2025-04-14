import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame


class tracker():
    def __init__(self):
        self.columns = ['Категория', 'Сумма', 'Описание']
        self.data = pd.DataFrame(columns=self.columns)

    def add_expense(self, amount: float, category: str, description: str):
        try:
            new_row = pd.DataFrame([[category, amount, description]], columns=self.columns)
            self.data = pd.concat([self.data, new_row], ignore_index=True)
            print("Расход добавлен!")
        except ValueError as e:
            print("Некорректный ввод!")

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
            return f"Ошибка Ввода: {e}"
