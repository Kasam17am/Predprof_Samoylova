# Predprof_Samoylova
Конкурс "Интеллектуальный мегаполис. Потенциал"
Astronaut_time
Решение варианта №27  к конкурсу "Интеллектуальный мегаполис. Потенциал" ИТ-класс

Обработка базы данных с временем на космических станциях
Данные решения направлены на помощь космонавтам: восстановить работу часов га станциях, чтобы те могли понимать время. В них содержатся функционал по восстановлению работы часов, обработке базы данных и есть удобный поиск в файле.

Оглавление
1) Технологии
2) Как установить и запустить проект
3) Как использовать проект


Технологии
Python 3.10

Как установить и запустить проект
Данное приложение не предусматривает установки, для запуска необходим интерпретатор Python и среда разработки/текстовый редактор.


Как использовать проект

1_1_tsk.py
Реализована функция по определению правильного времени и создан новый файл, в котором прописано, какое время на каждой станции

2_2.py
Реализована сортровка вставками в алфавитном порядке по трехзначным буквенным шифрам номерам кают(столбец cabinNumber). 

3_3.py
Реализован удобный поиск по базе данных, используемые для нахождения, когда была остановка и какое сейчас время на каждой станции. В случае, если был введен номер станции, которой нет в базе данных, выводится "На этой станции все хорошо"

4_4_task.py
Реализована группировка данных по номеру станции и посчитано общее время простоя часов на каждой из них. Выведен список из станций с временем простоя, равным 9. Использована библиотека csv для создания station_max_downtime.csv файла с станциями.
