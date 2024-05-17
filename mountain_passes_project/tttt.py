import psycopg2

try:
    # Установка соединения с базой данных PostgreSQL
    conn = psycopg2.connect(
        dbname="default_db",
        user="gen_user",
        password="passespassespasses",
        host="82.97.254.78",
        port="5432"
    )
    cur = conn.cursor()

    # SQL-запрос для получения информации о взаимосвязях
    sql_query = """
    SELECT
        tc.table_name,
        kcu.column_name,
        ccu.table_name AS foreign_table_name,
        ccu.column_name AS foreign_column_name
    FROM
        information_schema.table_constraints AS tc
        JOIN information_schema.key_column_usage AS kcu
          ON tc.constraint_name = kcu.constraint_name
        JOIN information_schema.constraint_column_usage AS ccu
          ON ccu.constraint_name = tc.constraint_name
    WHERE constraint_type = 'FOREIGN KEY';
    """

    # Выполнение SQL-запроса
    cur.execute(sql_query)

    # Получение результатов и вывод их
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Закрытие соединения с базой данных
    cur.close()
    conn.close()

except psycopg2.Error as error:
    print("Произошла ошибка при подключении к базе данных PostgreSQL:")
    print(error)
