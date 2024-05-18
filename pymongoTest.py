# Імпортуємо бібліотеку pymongo для роботи з MongoDB
import pymongo

# Функція для створення нового користувача
def createUser(name, age):
    # Підключаємося до MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # Вибираємо базу даних "myDatabase"
    db = client["myDatabase"]
    # Вибираємо колекцію "users"
    usersCollection = db["users"]

    # Створюємо словник з даними користувача
    userData = {"name": name, "age": age}
    # Вставляємо новий документ в колекцію
    usersCollection.insert_one(userData)

# Функція для отримання користувача за його ID
def getUserById(userId):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["myDatabase"]
    usersCollection = db["users"]

    # Знаходимо користувача за його ID
    user = usersCollection.find_one({"_id": userId})
    return user

# Функція для оновлення віку користувача за його ID
def updateUserAge(userId, newAge):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["myDatabase"]
    usersCollection = db["users"]

    # Оновлюємо вік користувача
    usersCollection.update_one({"_id": userId}, {"$set": {"age": newAge}})

# Функція для видалення користувача за його ID
def deleteUser(userId):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["myDatabase"]
    usersCollection = db["users"]

    # Видаляємо користувача за його ID
    usersCollection.delete_one({"_id": userId})

# Функція для отримання всіх користувачів
def getAllUsers():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["myDatabase"]
    usersCollection = db["users"]

    # Отримуємо всіх користувачів
    allUsers = usersCollection.find()
    return list(allUsers)

# Функція для видалення бази даних
def deleteDatabase():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # Видаляємо базу даних "myDatabase"
    client.drop_database("myDatabase")

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

# Закоментовані приклади використання функцій
# user = getUserById(1)
# print(user)  # Виведе інформацію про користувача з id=1, якщо він існує
# deleteDatabase()  # Видалить базу даних
# updateUserAge(1, 35)  # Оновить вік користувача з id=1 на 35 років
