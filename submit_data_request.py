import requests

# URL вашего API
url = 'http://127.0.0.1:8000/api/submitData/'

# JSON данные для отправки
data = {
    "beauty_title": "пер.",
    "title": "Пхия",
    "other_titles": "Триев",
    "connect": "",
    "add_time": "2021-09-22 13:18:13",
    "user": {
        "email": "qwerty@mail.ru",
        "fam": "Пупкин",
        "name": "Василий",
        "otc": "Иванович",
        "phone": "+7 555 55 55"
    },
    "coords": {
        "latitude": "45.3842",
        "longitude": "7.1525",
        "height": "1200"
    },
    "level": {
        "winter": "",
        "summer": "1А",
        "autumn": "1А",
        "spring": ""
    },
    "images": [
        {"data": "<картинка1>", "title": "Седловина"},
        {"data": "<картинка>", "title": "Подъём"}
    ]
}

# Отправляем POST запрос
response = requests.post(url, json=data)

# Выводим результат
print(response.json())