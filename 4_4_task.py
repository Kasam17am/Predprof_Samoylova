import csv

# Чтение данных из файла astronaut_time.csv
data = []
with open('astronaut_time.csv', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip('\n').split(',')
        data.append(line)

# Группировка данных по номеру станции и подсчет общего времени простоя в часах
station_time = {}
for i in range (1,len(data)):
    station = data[i][1]
    count_time = int(data[i][4])
    if station in station_time:
        station_time[station] += count_time
    else:
        station_time[station] = count_time

# Отбор станций с временем простоя 9 и занесение их номеров в список stations_with_max_downtime
stations_with_max_downtime = [station for station, count_time in station_time.items() if count_time == 9]

# Вывод станций с временем простоя равным 9
print("Станции с временем простоя равным 9:")
for station in stations_with_max_downtime:
    print(f"Станция {station}")

# Запись списка станций с временем простоя равным 9 в новый файл station_max_downtime.csv
with open('station_max_downtime.csv', 'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Station'])
    for station in stations_with_max_downtime:
        csv_writer.writerow([station])
