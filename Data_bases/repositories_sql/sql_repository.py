import asyncpg
import asyncio

from unicodedata import category

from Data_bases.repositories_sql.base_repository import BaseRepository

class SQLRepository(BaseRepository):
    def __init__(self, table_name):
        self.table_name = table_name

    async def get_connection(self):
        return await asyncpg.connect(user='nfactor', password='555555', database='postgres', host='localhost')

    async def create(self, category: str, name: str, gpa: float, study_year: int) -> dict:
        conn = await self.get_connection()
        query = f'''
                INSERT INTO {self.table_name} (category, name, gpa, study_year)
                VALUES ($1, $2, $3, $4)
                RETURNING id, category, name, gpa, study_year;
                '''
        result = await conn.fetchrow(query, category, name, gpa, study_year)
        await conn.close()
        return dict(result)

    async def update(self, record_id: int, category: str, name: str, gpa: float, study_year: int):
        conn = await self.get_connection()
        query = f'''
          UPDATE {self.table_name}
          SET category = COALESCE($2, category),
              name = COALESCE($3, name),
              gpa = COALESCE($4, gpa),
              study_year = COALESCE($5, study_year)
          WHERE id = $1
          RETURNING id, category, name, gpa, study_year;
          '''
        result = await conn.fetchrow(query, record_id, category, name, gpa, study_year)
        await conn.close()
        return dict(result) if result else None

    async def read(self) -> list[dict]:
        conn = await self.get_connection()
        query = '''
        SELECT id, category, name, gpa, study_year
        FROM people2;
        '''
        results = await conn.fetch(query)
        await conn.close()
        print(results)

    async def delete(self, record_id: int):
        conn = await self.get_connection()
        query = '''
        DELETE FROM people2 WHERE id = $1;
        '''
        await conn.execute(query, record_id)
        await conn.close()



if __name__ == "__main__":
    repo = SQLRepository("people2")
    asyncio.run(repo.delete(8))
    ""","student","Alex",4,1))"""