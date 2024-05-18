import sqlite3
import os

def createUser(name, age):
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                          id INTEGER PRIMARY KEY,
                          name TEXT,
                          age INTEGER
                      )''')

    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))

    connection.commit()
    connection.close()

def getUserByID(user_id):
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user = cursor.fetchone()

    connection.close()
    return user

def updateUserAge(user_id, new_age):
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()

    cursor.execute("UPDATE users SET age=? WHERE id=?", (new_age, user_id))

    connection.commit()
    connection.close()

def deleteUser(user_id):
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))

    connection.commit()
    connection.close()

def getAllUsers():
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    connection.close()
    return users

def delete_database():
    database_file = "my_database.db"
    if os.path.exists(database_file):
        os.remove(database_file)
        print("База даних успішно видалена")
    else:
        print("База даних не існує")


createUser("Alice", 30)
createUser("Kuzya", 18)
createUser("Maya", 25)
createUser("Ivan", 42)
createUser("Denis", 13)
createUser("Grisha", 22)

allUsers = getAllUsers()
for user in allUsers:
   print(user)

user = getUserByID(1)
print(user)  # Выведет информацию о пользователе с id=1, если он существует
updateUserAge(1, 35)  # Обновит возраст пользователя с id=1 на 35 лет
print (getUserByID(1))
deleteUser(1)  # Удалит пользователя с id=1
#delete_database()