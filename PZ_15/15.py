#Приложение РАСПРЕДЕЛЕНИЕ ДОПОЛНИТЕЛЬНЫХ ОБЯЗАННОСТЕЙ для 
#некоторой организации. БД должна содержать таблицу Обязанности со следующей 
#структурой записи: ФИО работника, вид дополнительной работы, сумма оплаты, срок. 
import sqlite3

conn = sqlite3.connect('obyazannosti.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Obyazannosti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fio TEXT NOT NULL,
    rabota TEXT NOT NULL,
    oplata REAL NOT NULL,
    srok TEXT NOT NULL
)
''')


try:
    cursor.executemany('''
    INSERT INTO Obyazannosti (fio, rabota, oplata, srok)
    VALUES (?, ?, ?, ?)
    ''', [
        ('Иванов И.И.', 'Куратор практики', 3000, '2025-12'),
        ('Петров П.П.', 'Ответственный за охрану труда', 5000, '2025-08'),
        ('Сидорова А.А.', 'Пожарная безопасность', 4500, '2025-09'),
        ('Кузнецов Д.Д.', 'Организация мероприятий', 2500, '2025-11'),
        ('Орлова Н.Н.', 'Ведение документации', 2000, '2025-10'),
        ('Белоусова Л.Л.', 'Заместитель ответственного', 3200, '2025-07'),
        ('Тарасов С.С.', 'Медиа сопровождение', 1500, '2025-08'),
        ('Фролова Е.Е.', 'Помощник куратора', 1800, '2025-12'),
        ('Смирнов М.М.', 'Проверка отчётов', 2700, '2025-09'),
        ('Дмитриев В.В.', 'Контроль расписания', 1600, '2025-07')
    ])
    conn.commit()
except:
    pass


def menu():
    while True:
        print("\nМеню:")
        print("1 - Показать все записи")
        print("2 - Поиск по ФИО")
        print("3 - Поиск по работе")
        print("4 - Поиск по сроку")
        print("5 - Удалить по ФИО")
        print("6 - Удалить по сроку")
        print("7 - Удалить по ID")
        print("8 - Изменить оплату по ФИО")
        print("9 - Изменить работу по ID")
        print("10 - Изменить срок по ФИО")
        print("0 - Выйти")

        choice = input("Выбор: ")

        if choice == "1":
            cursor.execute("SELECT * FROM Obyazannosti")
            for row in cursor.fetchall():
                print(row)

        elif choice == "2":
            fio = input("Введите часть ФИО: ")
            cursor.execute("SELECT * FROM Obyazannosti WHERE fio LIKE ?", ('%' + fio + '%',))
            for row in cursor.fetchall():
                print(row)

        elif choice == "3":
            rabota = input("Введите часть названия работы: ")
            cursor.execute("SELECT * FROM Obyazannosti WHERE rabota LIKE ?", ('%' + rabota + '%',))
            for row in cursor.fetchall():
                print(row)

        elif choice == "4":
            srok = input("Введите срок (например, 2025-09): ")
            cursor.execute("SELECT * FROM Obyazannosti WHERE srok = ?", (srok,))
            for row in cursor.fetchall():
                print(row)

        elif choice == "5":
            fio = input("Введите ФИО для удаления: ")
            cursor.execute("DELETE FROM Obyazannosti WHERE fio = ?", (fio,))
            conn.commit()
            print("Удалено.")

        elif choice == "6":
            srok = input("Введите срок для удаления: ")
            cursor.execute("DELETE FROM Obyazannosti WHERE srok = ?", (srok,))
            conn.commit()
            print("Удалено.")

        elif choice == "7":
            record_id = int(input("Введите ID для удаления: "))
            cursor.execute("DELETE FROM Obyazannosti WHERE id = ?", (record_id,))
            conn.commit()
            print("Удалено.")

        elif choice == "8":
            fio = input("Введите ФИО: ")
            oplata = float(input("Новая сумма оплаты: "))
            cursor.execute("UPDATE Obyazannosti SET oplata = ? WHERE fio = ?", (oplata, fio))
            conn.commit()
            print("Обновлено.")

        elif choice == "9":
            record_id = int(input("Введите ID: "))
            rabota = input("Новая работа: ")
            cursor.execute("UPDATE Obyazannosti SET rabota = ? WHERE id = ?", (rabota, record_id))
            conn.commit()
            print("Обновлено.")

        elif choice == "10":
            fio = input("Введите ФИО: ")
            srok = input("Новый срок (например, 2026-01): ")
            cursor.execute("UPDATE Obyazannosti SET srok = ? WHERE fio = ?", (srok, fio))
            conn.commit()
            print("Обновлено.")

        elif choice == "0":
            print("Выход.")
            break

        else:
            print("Неверный выбор.")

menu()
conn.close()
