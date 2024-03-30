def calculate_actual_time(stop_time, count):
    """
    Функция подчитывает актуальное время
    :param stop_time: время, когда остановились часы
    :param count: количество часов, которое часы не работали
    :return: возращает верное время
    """
    stop_hour, stop_minute, stop_second = map(int, stop_time.split(':'))

    total_seconds = stop_hour * 3600 + stop_minute * 60 + stop_second + count*3600
    actual_hour = total_seconds // 3600
    actual_minute = (total_seconds % 3600) // 60
    actual_second = total_seconds % 60
    if actual_hour>=24:
        actual_hour = actual_hour % 24

    return f"{actual_hour:02d}:{actual_minute:02d}:{actual_second:02d}"


# Открываем файл astronaut_time.csv для чтения
with open('astronaut_time.csv', encoding='utf-8') as file:
    lines = file.readlines()


with open('new_time.txt', 'w') as new_file:
    # записываем данные в новый файл new_time.txt
    for line in lines[1:]:
        parts = line.strip().split(',')
        station = parts[1]
        cabin = parts[2]
        stop_time = parts[3]
        count = int(parts[4])

        actual_time = calculate_actual_time(stop_time, count)
        result_line = f'На станции {station} в каюте {cabin} восстановлено время. Актуальное время: {actual_time}\n'

        new_file.write(result_line)
# выводим первые 3 строчки файла
with open ('new_time.txt', 'r') as f:
    a=f.readlines()
    for i in range (3):
        print(a[i])