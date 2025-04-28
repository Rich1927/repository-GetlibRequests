#Отправляет GET-запрос на API jsonplaceholder.typicode.com с параметром userId=1.
#Если запрос успешен (статус-код 200), то:
#Получает данные в формате JSON (список постов).
#Каждый пост в списке — это словарь с данными.
#Выводит каждый пост.

# Импортируем библиотеку для работы с HTTP-запросами
import requests

# Указываем URL API для получения постов с сайта jsonplaceholder
url = "https://jsonplaceholder.typicode.com/posts"

# Задаем параметры запроса: ищем посты с userId равным 1
params = {
    'userId': 1
}

# Отправляем GET-запрос на указанный URL с параметрами
response = requests.get(url, params=params)

# Проверяем статус-код ответа
if response.status_code == 200:  # Правильное имя атрибута: status_code
    # Преобразуем полученные данные в формат JSON (список постов)
    posts = response.json()

    # Проходим по всем постам и выводим их
    for post in posts:
        print(post)  # Печатаем каждый пост (каждый пост — это словарь с данными)
else:
    # Если статус-код не 200, выводим сообщение об ошибке
    print("Error")
