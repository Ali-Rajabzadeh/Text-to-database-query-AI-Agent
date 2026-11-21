
from agent.sql_agent import generate_sql

question = "How many customers are there?"

sql_query = generate_sql(question)

print("Generated SQL:")
print(sql_query)

