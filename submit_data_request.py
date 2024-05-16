import requests

# URL вашего API
url = 'http://django1991.pythonanywhere.com/api/submitData/'

# JSON данные для отправки
data = {
    "beauty_title": "пер.",
    "title": "Пхия",
    "other_titles": "Триев",
    "connect": "123",
    "add_time": "2024-09-22 19:13:59",
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
        "winter": "1A",
        "summer": "1А",
        "autumn": "1А",
        "spring": "1A"
    },
    "images": []
}

# Отправляем POST запрос
response = requests.post(url, json=data)

if response.status_code == 200 and response.text:
    # Выводим результат
    print(response.json())
else:
    print("Ошибка при получении данных:", response.status_code)

# Выводим результат
print(response.json())
