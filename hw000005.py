# Задача 5. Запуск из командной строки.
# Напишите код, который запускается из командной строки и получает на вход путь
# до директории на ПК. Соберите информацию о содержимом в виде объектов
# namedtuple. Каждый объект хранит:
# -имя файла без расширения или название каталога;
# -расширение если это файл;
# -флаг каталога;
# -название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.

import logging
from collections import namedtuple
import argparse
from pathlib import Path

# Настройка логирования
logging.basicConfig(
    filename='directory_contents.log',
    filemode='w',  # перезапись
    encoding='utf-8',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Определение namedtuple для хранения информации о файле/каталоге
FileInfo = namedtuple('FileInfo', 'name, extension, is_dir, parent')


def read_dir(path: Path) -> None:
    """
    Рекурсивно обходит директорию и записывает информацию о содержимом в лог.
    """
    try:
        for file in path.iterdir():
            file_info = FileInfo(
                name=file.stem if file.is_file() else file.name,
                extension=file.suffix if file.is_file() else '',
                is_dir=file.is_dir(),
                parent=file.parent.name
            )
            logger.info(file_info)
            print(file_info)  # Для наглядности выводим в консоль

            if file_info.is_dir:
                read_dir(file)  # Рекурсивный вызов для вложенных каталогов
    except PermissionError as e:
        logger.warning(f"Нет доступа к каталогу: {path} - {e}")
    except Exception as e:
        logger.error(f"Ошибка при обработке {path}: {e}")


def main():
    """
    Основная функция для обработки аргументов командной строки и вызова функции read_dir.
    """
    parser = argparse.ArgumentParser(
        description="Запись данных о содержимом каталога в лог-файл.",
        prog='directory_walker'
    )
    parser.add_argument('-p', '--path', type=Path, required=True, help="Введите путь до директории.")
    args = parser.parse_args()

    if not args.path.exists():
        print(f"Указанный путь не существует: {args.path}")
        return
    if not args.path.is_dir():
        print(f"Указанный путь не является директорией: {args.path}")
        return

    read_dir(args.path)


if __name__ == '__main__':
    main()

# Запустим скрипт из терминала, передав нужные аргументы:
# python hw000005.py -p 'C:\Users\besed\OneDrive\Рабочий стол\MY_PYTHON\15\SEMINAR'