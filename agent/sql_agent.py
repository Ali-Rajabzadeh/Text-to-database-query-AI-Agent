
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.utilities import SQLDatabase
from database.db import engine

from llm import llm

# Connect LangChain to our SQLite database
db = SQLDatabase(engine)

# Retrieve database schema
schema = db.get_table_info()


# Create prompt template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an expert SQL developer.

        Your task is to convert natural language questions
        into valid SQLite SQL queries.

        Database schema:
        {schema}

        Rules:
        - Generate only SELECT queries.
        - Use only existing tables and columns.
        - Do not generate INSERT, UPDATE, DELETE or DROP.
        - Return only SQL code.
        - Do not include markdown code blocks.
        """
    ),
    ("human", "{question}")
])


# Create a chain
sql_chain = prompt | llm


def generate_sql(question: str):
    response = sql_chain.invoke({
        "schema": schema,
        "question": question
    })

    return response.content
