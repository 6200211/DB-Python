import pymongo

def createUser(name, age):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["myDatabase"]
    usersCollection = db["users"]

    userData = {"name": name, "age": age}
    usersCollection.insert_one(userData)

def getUserById(userId):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["myDatabase"]
    usersCollection = db["users"]

    user = usersCollection.find_one({"_id": userId})
    return user

def updateUserAge(userId, newAge):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["myDatabase"]
    usersCollection = db["users"]

    usersCollection.update_one({"_id": userId}, {"$set": {"age": newAge}})

def deleteUser(userId):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["myDatabase"]
    usersCollection = db["users"]

    usersCollection.delete_one({"_id": userId})

def getAllUsers():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["myDatabase"]
    usersCollection = db["users"]

    allUsers = usersCollection.find()
    return list(allUsers)

def deleteDatabase():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    client.drop_database("myDatabase")


createUser("Alice", 30)
createUser("Kuzya", 18)
createUser("Maya", 25)
createUser("Ivan", 42)
createUser("Denis", 13)
createUser("Grisha", 22)

allUsers = getAllUsers()
for user in allUsers:
    print(user)
    pass

#user = getUserById(1)
#print(user)  # Выведет информацию о пользователе с id=1, если он существует
#deleteDatabase()  # Удалит базу данных
# updateUserAge(1, 35)  # Обновит возраст пользователя с id=1 на 35 лет