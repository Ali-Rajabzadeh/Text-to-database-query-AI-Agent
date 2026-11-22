
from database.langchain_db import db
from agent.sql_validator import validate_sql


def execute_sql(query: str):

    if not validate_sql(query):
        raise ValueError("Unsafe or invalid SQL query!")

    result = db.run(query)

    return result
