# Импортируем библиотеку для работы с HTTP-запросами
import requests

# Указываем URL API для поиска репозиториев на GitHub
url = "https://api.github.com/search/repositories"

# Задаем параметры запроса: ищем репозитории с кодом на языке HTML
params = {"q": "language:html"}

# Отправляем GET-запрос на указанный URL с параметрами
response = requests.get(url, params=params)

# Выводим статус-код ответа (должно быть 200, если запрос успешный)
print(f"Status code: {response.status_code}")

# Выводим содержимое ответа в формате JSON (словарь с результатами поиска)
print(response.json())
