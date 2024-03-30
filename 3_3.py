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

with open('astronaut_time.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Поиск времени остановки для номера станции, введенного пользователем
while True:
    station_input = input("Введите номер станции (или 'stop' для выхода): ")
    if station_input.lower() == 'stop':
        break

    found = False
    for line in lines[1:]:
        parts = line.strip().split(',')
        station = parts[1]
        if station == station_input:
            cabin = parts[2]
            stop_time = parts[3]
            count = int(parts[4])

            actual_time = calculate_actual_time(stop_time, count)
            print(f'На станции {station} восстановлено время (время остановки: {stop_time}). Актуальное время: {actual_time}')
            found = True
            break

    if not found:
        print("На этой станции все хорошо")