import asyncio

import asyncpg

async def create_table():
    # Установите соединение с базой данных PostgreSQL
    conn = await asyncpg.connect(user='nfactor', password='555555', database='postgres', host='localhost')

    # SQL запрос для создания таблицы
    create_table_query = """
    CREATE TABLE IF NOT EXISTS people (
        id SERIAL PRIMARY KEY,
        category VARCHAR(50),
        name VARCHAR(100),
        gpa DECIMAL(3, 2),
        study_year INTEGER
    );
    """

    # Выполнение SQL запроса
    await conn.execute(create_table_query)

    print("Table 'people' created successfully.")

    # Закрытие соединения с базой данных
    await conn.close()


# Запуск асинхронной функции
loop = asyncio.get_event_loop()
loop.run_until_complete(create_table())