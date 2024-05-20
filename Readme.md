# Проект "Mountain Passes"

## Ссылка на сайт проекта
- **Сайт проекта:** [Mountain Passes](http://mrgerber91-mountain-passes-4324.twc1.net)

## Swagger API документация
- **Swagger UI:** [Mountain Passes API на Swagger](https://mrgerber91-mountain-passes-4324.twc1.net/swagger/)


## Задача
Проект "Mountain Passes" разработан для управления данными о перевалах, предоставляя возможность создания, хранения и редактирования информации о них. Также предоставляется REST API для взаимодействия с данными.

## Реализация
- Созданы модели для перевалов, пользователей и координат.
- Настроены REST API эндпоинты для CRUD операций с данными о перевалах.
- Добавлен функционал для работы с изображениями перевалов.
- Используется PostgreSQL база данных для хранения информации.

## Работа с REST API
1. **Создание записи о перевале:**
   - **Метод:** POST
   - **URL:** `/api/submitData/`
   - **Тело запроса:**
     ```json
     {
         "user": {
             "email": "test@example.com"
             
         },
         "beauty_title": "Красивый перевал"
         
     }
     ```
     
2. **Получение данных о перевале:**
   - **Метод:** GET
   - **URL:** `/api/submitData/{pk}/`

3. **Редактирование данных о перевале:**
   - **Метод:** PATCH
   - **URL:** `/api/submitData/{pk}/`

4. **Удаление данных о перевале:**
   - **Метод:** DELETE
   - **URL:** `/api/submitData/{pk}/`

5. **Получение данных о перевалах пользователя:**
   - **Метод:** GET
   - **URL:** `/getUserData/`

### Примеры вызова API на хостинге
```bash
# Создание новой записи о перевале
curl -X POST http://mrgerber91-mountain-passes-4324.twc1.net/api/submitData/ -H "Content-Type: application/json" -d '{"user": {"email": "test@example.com"}, "beauty_title": "Красивый перевал", ...}'

# Получение данных о перевале
curl -X GET http://mrgerber91-mountain-passes-4324.twc1.net/api/submitData/1/

# Редактирование данных о перевале
curl -X PATCH http://mrgerber91-mountain-passes-4324.twc1.net/api/submitData/1/ -H "Content-Type: application/json" -d '{"beauty_title": "Новый заголовок", ...}'

