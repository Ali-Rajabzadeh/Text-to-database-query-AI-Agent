from agent.tools import get_customer_by_id
from langchain.messages import HumanMessage, ToolMessage
from llm import llm

# Bind the tool to the LLM
llm_with_tools = llm.bind_tools([get_customer_by_id])

question = "اطلاعات کاربر با آیدی شماره ۲ رو بده."

messages = [HumanMessage(content=question)]

# 1. Get tool call from LLM
response = llm_with_tools.invoke(messages)
messages.append(response)
print(f"messages: {messages}")

# 2. Execute tool calls
for tool_call in response.tool_calls:

    if tool_call["name"] == get_customer_by_id.name:
        result = get_customer_by_id.invoke(tool_call["args"])

        # 3. Send tool result back to the conversation
        messages.append(
            ToolMessage(
                content=str(result),
                tool_call_id=tool_call["id"]
            )
        )

# 4. Get final answer from LLM
final_response = llm.invoke(messages)

print(final_response.content)
