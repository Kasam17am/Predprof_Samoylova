def calculate_actual_time(stop_time, count):
    stop_hour, stop_minute, stop_second = map(int, stop_time.split(':'))

    total_seconds = stop_hour * 3600 + stop_minute * 60 + stop_second + count
    actual_hour = total_seconds // 3600
    actual_minute = (total_seconds % 3600) // 60
    actual_second = total_seconds % 60

    return f"{actual_hour:02d}:{actual_minute:02d}:{actual_second:02d}"

# Открываем файл astronaut_time.csv для чтения
with open('astronaut_time.csv', encoding='utf-8') as file:
    lines = file.readlines()

# Сортировка файлa по номерам кают методом сортировки вставками
for i in range(1, len(lines)):
    current_line = lines[i]
    current_cabin = current_line.strip().split(',')[2]
    j = i - 1
    while j >= 0 and lines[j].strip().split(',')[2] > current_cabin:
        lines[j + 1] = lines[j]
        j -= 1
    lines[j + 1] = current_line

# Вывод первых трех станций после сортировки
for line in lines[1:4]:
    parts = line.strip().split(',')
    station = parts[1]
    cabin = parts[2]
    stop_time = parts[3]
    count = int(parts[4])

    actual_time = calculate_actual_time(stop_time, count)
    print(f'На станции {station} в каюте {cabin} восстановлено время. Актуальное время: {actual_time}')