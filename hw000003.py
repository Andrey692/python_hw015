# Задача 3. Планирование задач.
# Напишите функцию, принимающую количество дней от текущей даты и
# возвращает дату, которая наступит через указанное количество дней. Дополнительно,
# выведите эту дату в формате YYYY-MM-DD.



from datetime import datetime, timedelta


def future_date(days_from_now):

    # Получение текущей даты и времени
    today = datetime.now()
    # Вычисление даты через указанное количество дней
    future_date = today + timedelta(days=days_from_now)
    # Форматирование будущей даты в строку в формате YYYY-MM-DD
    formatted_future_date = future_date.strftime('%Y-%m-%d')
    return formatted_future_date


if __name__ == '__main__':
    days = 3 # Количество дней для вычисления
    print(f'Дата, которая наступит через {days} дней(дня): {future_date(days)}')