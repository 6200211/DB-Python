# Імпортуємо необхідні модулі з Flask і Flask-RESTful для створення веб-додатка
from flask import Flask
from flask_restful import Api, Resource, reqparse

# Створюємо екземпляр Flask додатка
app = Flask(__name__)
# Створюємо екземпляр API
api = Api()

# Словник users містить дані користувачів з їх іменами і віком
users = {
    1: {"name": "Alice", "age": 30},
    2: {"name": "Kuzya", "age": 18},
    3: {"name": "Maya", "age": 25},
    4: {"name": "Ivan", "age": 42},
    5: {"name": "Denis", "age": 13},
    6: {"name": "Grisha", "age": 22}
}

# Створюємо парсер для обробки аргументів запиту
parser = reqparse.RequestParser()
parser.add_argument("name", type=str)
parser.add_argument("age", type=int)

# Створюємо клас Main, що буде обробляти різні типи HTTP-запитів
class Main(Resource):
    def get(self, userID):
        # Повертаємо всі дані користувачів, якщо userID дорівнює 0
        if userID == 0:
            return users
        # Повертаємо дані конкретного користувача за його ID
        else:
            return users[userID]

    def delete(self, userID):
        # Видаляємо користувача за його ID
        del users[userID]
        # Повертаємо оновлений словник користувачів
        return users

    def post(self, userID):
        # Додаємо або оновлюємо дані користувача за його ID з параметрами, отриманими з запиту
        users[userID] = parser.parse_args()
        # Повертаємо оновлений словник користувачів
        return users

    def put(self, userID):
        # Оновлюємо дані користувача за його ID з параметрами, отриманими з запиту
        users[userID] = parser.parse_args()
        # Повертаємо оновлений словник користувачів
        return users

# Додаємо ресурс Main до API за шляхом "/api/users/<int:userID>"
api.add_resource(Main, "/api/users/<int:userID>")
# Ініціалізуємо API з Flask додатком
api.init_app(app)

# Запускаємо додаток, якщо цей файл виконується напряму
if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")
