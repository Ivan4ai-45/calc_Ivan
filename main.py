from tracker import *

def main():
    calc = tracker()

    while True:
        print("\nМеню:")
        print("1. Добавить расход")
        print("2. Показать все расходы")
        print("3. Показать общую сумму")
        print("4. Показать расходы по категории")
        print("5. Выйти")

        user_input = input()

        if user_input == '1':
            calc.add_expense(float(input("Введите сумму: ")), input("Ввидите категорию: "), input("Ввидите категорию: "))
        elif user_input == '2':
            print(calc.get_expense())
        elif user_input == '3':
            print(calc.get_total())
        elif user_input == '4':
            print(calc.get_by_category(input('Введите категорию: ')))
        elif user_input == '5':
            print('Программа завершила работу успешно!')
            break
        else:
            print("Некорректный ввод")

if __name__ == "__main__":
    main()