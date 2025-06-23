import os
import psycopg
from psycopg.rows import class_row
from ..models.recipe import Recipe


class RecipeRepository:
    def __init__(self):
        pass

    def _get_connection(self):
        host = os.environ["POSTGRES_SERVER"]
        port = os.environ["POSTGRES_PORT"]
        dbname = os.environ["POSTGRES_DB"]
        user = os.environ["POSTGRES_USER"]
        password = os.environ["POSTGRES_PASSWORD"]

        return psycopg.connect(
            f"host={host} port={port} dbname={dbname} user={user} password={password}"
        )

    def get_all_recipes(self) -> list[Recipe]:
        results = []

        with (
            self._get_connection() as conn,
            conn.cursor(row_factory=class_row(Recipe)) as cur,
        ):
            cur.execute("SELECT * FROM recipes")
            for record in cur:
                results.append(record)

        return results
