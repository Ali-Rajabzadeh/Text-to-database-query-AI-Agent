
from langchain_community.utilities import SQLDatabase
from database.db import engine

# Connect LangChain to our SQLite database
db = SQLDatabase(engine)

# ================================================
# Create a database connection for LangChain
# ================================================

# # Print database information
# print("Usable tables:", db.get_usable_table_names())

# # Print database schema
# print(db.get_table_info())

# ================================================
## Execute SQL through LangChain
# ================================================

# query = """
# SELECT COUNT(*) FROM customers
# """

# result = db.run(query)

# print("\nQuery result:")
# print(result)