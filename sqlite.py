# Імпортуємо бібліотеки sqlite3 для роботи з базою даних SQLite і os для роботи з файловою системою
import sqlite3
import os

# Функція для створення нового користувача
def createUser(name, age):
    # Підключаємося до бази даних my_database.db (створюється автоматично, якщо не існує)
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()

    # Створюємо таблицю users, якщо вона не існує
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                          id INTEGER PRIMARY KEY,
                          name TEXT,
                          age INTEGER
                      )''')

    # Додаємо нового користувача в таблицю
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))

    # Зберігаємо зміни і закриваємо підключення
    connection.commit()
    connection.close()

# Функція для отримання користувача за його ID
def getUserByID(user_id):
    # Підключаємося до бази даних
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()

    # Виконуємо запит для отримання користувача за його ID
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user = cursor.fetchone()
    
    connection.close()
    return user

# Функція для оновлення віку користувача за його ID
def updateUserAge(user_id, new_age):
    # Підключаємося до бази даних
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()

    # Виконуємо запит для оновлення віку користувача
    cursor.execute("UPDATE users SET age=? WHERE id=?", (new_age, user_id))

    # Зберігаємо зміни і закриваємо підключення
    connection.commit()
    connection.close()

# Функція для видалення користувача за його ID
def deleteUser(user_id):
    # Підключаємося до бази даних
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()

    # Виконуємо запит для видалення користувача
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))

    connection.commit()
    connection.close()

# Функція для отримання всіх користувачів
def getAllUsers():
    # Підключаємося до бази даних
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()

    # Виконуємо запит для отримання всіх користувачів
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    connection.close()
    return users

# Функція для видалення бази даних
def delete_database():
    database_file = "my_database.db"
    if os.path.exists(database_file):
        # Видаляємо файл бази даних, якщо він існує
        os.remove(database_file)
        print("База даних успішно видалена")
    else:
        print("База даних не існує")

# Створюємо декілька користувачів
createUser("Alice", 30)
createUser("Kuzya", 18)
createUser("Maya", 25)
createUser("Ivan", 42)
createUser("Denis", 13)
createUser("Grisha", 22)

# Отримуємо всіх користувачів і виводимо їх на екран
allUsers = getAllUsers()
for user in allUsers:
    print(user)

# Отримуємо користувача за його ID
user = getUserByID(1)
print(user)  # Виведе інформацію про користувача з id=1, якщо він існує

# Оновлюємо вік користувача з id=1
updateUserAge(1, 35)  # Оновить вік користувача з id=1 на 35 років
print(getUserByID(1))

# Видаляємо користувача з id=1
deleteUser(1)  # Удалить користувача з id=1

# Закоментований виклик функції для видалення бази даних
# delete_database()
