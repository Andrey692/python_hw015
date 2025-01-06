# Задача 4. Опции и флаги.
# Напишите скрипт, который принимает два аргумента командной строки: число и
# строку. Добавьте следующие опции:
# ● --verbose, если этот флаг установлен, скрипт должен выводить
# дополнительную информацию о процессе.
# ● --repeat, если этот параметр установлен, он должен указывать,
# сколько раз повторить строку в выводе.


import argparse

def main():
    parser = argparse.ArgumentParser(description="Процессинг числа и строки с дополнительными опциями.")

    # Основные аргументы
    parser.add_argument("number", type=int, help="Число для вывода.")
    parser.add_argument("string", type=str, help="Строка для вывода.")

    # Опции
    parser.add_argument("--verbose", action="store_true", help="Вывод дополнительной информации.")
    parser.add_argument("--repeat", type=int, default=1, help="Количество повторений строки.")

    # Парсинг аргументов
    args = parser.parse_args()

    if args.verbose:
        print(f"записанное число: {args.number}")
        print(f"записанная строка: '{args.string}'")
        print(f"сколько раз повторить строку: {args.repeat}")

    # Повтор строки указанное количество раз
    for i in range(args.repeat):
        if args.verbose:
            print(f"вывод повторения {i + 1}/{args.repeat}: {args.string}")
        else:
            print(args.string)

if __name__ == "__main__":
    main()

# Сохраним код в файл, hw000004.py.
# Запустим скрипт из терминала Windows PowerShell, передав нужные аргументы:
# python "C:\Users\besed\OneDrive\Рабочий стол\MY_PYTHON\15\HW\hw000004.py" 42 Hello
# python "C:\Users\besed\OneDrive\Рабочий стол\MY_PYTHON\15\HW\hw000004.py" 42 Hello --repeat 5
# python "C:\Users\besed\OneDrive\Рабочий стол\MY_PYTHON\15\HW\hw000004.py" 42 Hello --verbose