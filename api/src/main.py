from fastapi import FastAPI
import psycopg
from pydantic import BaseModel
from psycopg.rows import class_row
import os

app = FastAPI()


class Recipe(BaseModel):
    id: int
    name: str


def get_connection():
    host = os.environ["POSTGRES_SERVER"]
    port = os.environ["POSTGRES_PORT"]
    dbname = os.environ["POSTGRES_DB"]
    user = os.environ["POSTGRES_USER"]
    password = os.environ["POSTGRES_PASSWORD"]

    return psycopg.connect(
        f"host={host} port={port} dbname={dbname} user={user} password={password}"
    )


@app.get("/recipes")
def read_recipes():
    result = []
    with get_connection() as conn, conn.cursor(row_factory=class_row(Recipe)) as cur:
        cur.execute("SELECT * FROM recipes")
        for record in cur:
            result.append(record)

    return result
