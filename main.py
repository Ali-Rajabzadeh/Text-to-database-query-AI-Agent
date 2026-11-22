
from agent.sql_agent import generate_sql
from database.query_executor import execute_sql
import fa_console

from langchain.messages import HumanMessage, AIMessage, SystemMessage, RemoveMessage
from llm import llm

question = "کدام مشتری بیشترین مبلغ را هزینه کرده است؟ و چه مقدار؟"

# 1. Generate SQL
sql_query = generate_sql(question)

print("Generated SQL:")
print(sql_query)

# 2. Execute SQL
try:
    result = execute_sql(sql_query)

    print("\nQuery result:")
    print(result)

except Exception as error:
    print(f"SQL execution failed: {error}")
    raise

# 3. Prepare messages for the LLM

system_message = SystemMessage(
    content="""
    You are a helpful database assistant.
    Answer the user's question using the database results.
    Do not invent information that is not present in the results.
    """
)
human_message = HumanMessage(
    content=f"""
    User question:
    {question}

    Database result:
    {result}

    Briefly explain the result.
    """
)

# 4. Generate natural-language answer

response = llm.invoke([
    system_message,
    human_message
])
print("\nFinal Answer:")
print(response.content)
print(f"Usage: {response.usage_metadata}")