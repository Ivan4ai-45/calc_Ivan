import pandas as pd


class Tracker:
    """Класс для учёта расходов с возможностью добавления, просмотра и анализа трат.

    Атрибуты:
        columns (list): Список колонок DataFrame.
        data (pd.DataFrame): DataFrame для хранения данных о расходах.
    """

    def __init__(self):
        """Инициализирует DataFrame с заданными столбцами"""
        self.columns = ['Категория', 'Сумма', 'Описание']
        self.data = pd.DataFrame(columns=self.columns)

    def add_expense(self, amount: str, category: str, description: str) -> str:
        """Добавляет новый расход в трекер.

        Args:
            amount (str): Сумма расхода (должна быть конвертируема в float).
            category (str): Категория расхода (например, "Еда", "Транспорт").
            description (str): Описание расхода.

        Returns:
            str: Сообщение об успешном добавлении или ошибке.
        """
        try:
            amount = float(amount)
            self.data.loc[len(self.data)] = [category, amount, description]
            return "\nРасход добавлен!"
        except ValueError:
            return "Некорректный ввод!"

    def get_expense(self) -> str | list[dict]:
        """Возвращает список всех расходов в виде словарей.

        Returns:
            str | list[dict]:
                - Если расходов нет, возвращает строку "У вас нет расходов!".
                - Иначе возвращает список словарей с расходами.
        """
        if self.data.empty:
            return "У вас нет расходов!"
        return self.data.to_dict('records')

    def get_total(self) -> str | float:
        """Возвращает общую сумму всех расходов.

        Returns:
            str | float:
                - Если расходов нет, возвращает строку "У вас нет расходов!".
                - Иначе возвращает сумму всех расходов.
        """
        if self.data.empty:
            return "У вас нет расходов!"
        return sum(self.data['Сумма'].tolist())

    def get_by_category(self, category_for_print: str) -> str | list[dict]:
        """Возвращает расходы по заданной категории.

        Args:
            category_for_print (str): Категория для поиска.

        Returns:
            str | list[dict]:
                - Если расходов нет, возвращает строку "У вас нет расходов!".
                - Если категория не найдена, возвращает "Данной категории нет в списке!".
                - Иначе возвращает список словарей с расходами по категории.
        """
        if self.data.empty:
            return "У вас нет расходов!"
        try:
            output = self.data[self.data['Категория'].str.contains(category_for_print, case=False, na=False)].to_dict(
                'records')
            if output:
                return output
            return "Данной категории нет в списке!"
        except ValueError as e:
            return f"Ошибка ввода: {e}"