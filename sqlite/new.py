import sqlite3

# Подключение к базе данных
con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# Шаг 1: Получить названия всех таблиц
cur.execute("SELECT tbl_name FROM sqlite_master WHERE type='table';")
table = cur.fetchall()[0][0]  # Предположим, что нас интересует первая таблица

# Шаг 2: Вывести значения столбцов title и description
results = cur.execute(f"SELECT title, description FROM {table};")

# Вывод полученных записей
for result in results:
    print(result)

# Закрытие соединения
con.close()
