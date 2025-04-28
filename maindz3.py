#Создаёт словарь с данными для отправки: {'title': 'foo', 'body': 'bar', 'userId': 1}.
#Отправляет POST-запрос с этим словарём как данные в формате JSON на API jsonplaceholder.typicode.com.
#Печатает:
#Статус-код ответа (например, 201, если данные успешно добавлены).
#Ответ в формате JSON (что вернул API после добавления данных).

# Импортируем библиотеку для работы с HTTP-запросами
import requests

# Указываем URL API для создания новых постов
url = "https://jsonplaceholder.typicode.com/posts"

# Создаем словарь с данными для отправки (данные нового поста)
data = {'title': 'foo', 'body': 'bar', 'userId': 1}

# Отправляем POST-запрос с данными в формате JSON
response = requests.post(url, json=data)

# Печатаем статус-код ответа
print(f"Status code: {response.status_code}")  # Печатаем статус-код (например, 201 для успешного добавления)

# Печатаем содержимое ответа в формате JSON
print(f"Ответ: {response.json()}")  # response.json() нужно вызывать как функцию
