from fastapi import FastAPI, HTTPException

import asyncio

from repositories_sql.sql_repository import SQLRepository

app  = FastAPI

