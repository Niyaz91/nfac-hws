from contextlib import nullcontext

import asyncpg
import asyncio


async def create_table():
    conn = await asyncpg.connect(user='nfactor', password='555555', database='postgres', host='localhost')
    create_table_query = """
    CREATE TABLE IF NOT EXISTS people2 (
        id SERIAL PRIMARY KEY,
        category VARCHAR(50),   
        name VARCHAR(100),      
        gpa DECIMAL(3, 2),      
        study_year INTEGER      
    );
    """
    await conn.execute(create_table_query)
    await conn.close()

async def insert_data():
    conn = await asyncpg.connect(user='nfactor', password='555555', database='postgres', host='localhost')

    insert_query = """
    INSERT INTO people2 (category, name, gpa, study_year)
    VALUES ($1, $2, $3, $4)
    """
    await conn.execute(insert_query, 'Teacher', 'Dalida', None , None)
    await conn.close()

async def delete_data():
    conn = await asyncpg.connect(user='nfactor', password='555555', database='postgres', host='localhost')

    delete_query = """
    DELETE FROM people2 WHERE name = $1
    """
    await conn.execute(delete_query, 'Gleb')
    await conn.close()


asyncio.run(insert_data())
