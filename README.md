# Text-to-Database Query AI Agent

An experimental project exploring how AI agents can interact with relational databases through natural language.

This repository is a **proof of concept (PoC)** developed as a technical experiment for a practical project. It focuses on exploring the architecture, tools, and workflows required to build an AI-powered database assistant. It is not intended to be a standalone, ready-to-use application.

## Overview

The idea behind this project is to bridge the gap between natural language and SQL databases.

Instead of writing SQL queries manually, users can ask questions in plain language. An AI agent interprets the request, generates an appropriate SQL query based on the database schema, validates the query, executes it, and converts the results into a human-readable response.

The project explores how LLMs, database utilities, and agent workflows can work together to achieve this.

## Key Features

- **Natural Language to SQL:** Convert natural language questions into SQL queries using an LLM.
- **Database Schema Awareness:** Retrieve database schema information and provide it as context during SQL generation.
- **SQL Validation:** Validate generated SQL queries using SQLGlot before execution.
- **Controlled Query Execution:** Restrict query execution to supported read-only SQL statements.
- **Natural Language Responses:** Interpret database results and generate human-readable answers.
- **Tool Calling:** Enable the LLM to identify and invoke Python tools for database operations.
- **Modular Architecture:** Separate SQL generation, validation, database operations, and LLM configuration.

## Architecture

The main Text-to-SQL workflow consists of the following steps:

```text
          User Question
                |
                v
       SQL Generation Agent
                |
                v
        SQL Query Validator
                |
                v
        Database Execution
                |
                v
         Query Results
                |
                v
        LLM Result Analysis
                |
                v
        Natural Language Answer
```

### Workflow

1. **User Input:** Receive a question in natural language.
2. **SQL Generation:** Retrieve the database schema and provide it to the LLM along with the user's question.
3. **SQL Validation:** Parse and validate the generated SQL query using SQLGlot.
4. **Query Execution:** Execute validated queries against the database.
5. **Result Interpretation:** Pass the query results to the LLM to generate a human-readable answer.

## Technologies

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | LLM integration, prompts, and tool calling |
| OpenRouter | LLM API access |
| SQLAlchemy | Database connection and ORM |
| SQLite | Relational database |
| SQLGlot | SQL parsing and validation |
| python-dotenv | Environment variable management |

## LLM Flexibility

Although the current implementation uses OpenRouter for accessing language models, the architecture is not limited to a specific LLM provider.

Depending on the model integration and LangChain compatibility, different language models can be used, including:

- **OpenRouter:** Access multiple models through a unified API.
- **OpenAI:** Use OpenAI models through their API.
- **NVIDIA:** Access supported models through NVIDIA APIs.
- **Other Cloud Providers:** Integrate models from other providers.
- **Local LLMs:** Run models locally using tools such as Ollama or other compatible inference frameworks.

The LLM configuration can be adapted to use a different provider without changing the overall Text-to-SQL workflow.

## Project Structure

```text
Text-to-database-query-AI-Agent/
│
├── agent/
│   ├── sql_agent.py
│   ├── sql_validator.py
│   └── tools.py
│
├── database/
│   ├── db.py
│   ├── langchain_db.py
│   └── query_executor.py
│
├── data/
│   └── sample.db
│
├── llm.py
├── main.py
├── README.md
└── LICENSE
```

## Current Scope

This repository is an experimental implementation intended to explore the technical foundations of an AI-powered database assistant.

The current scope includes:

- SQLite database integration.
- Schema-aware SQL generation.
- SQL query validation and execution.
- LLM-based query result interpretation.
- LangChain tool calling.
- Experimentation with different LLM providers.

**Important:** This project is not a complete or independently deployable application. The code serves as a technical prototype and reference for developing a practical solution.

## Future Improvements

Potential areas for further development include:

- Support for additional database systems such as PostgreSQL and MySQL.
- Conversational memory for multi-turn database interactions.
- Improved SQL error handling and automatic query correction.
- More advanced agent workflows using LangGraph.
- Integration with external interfaces such as Telegram bots or web applications.

## Author

**Ali Rajabzadeh**

[GitHub](https://github.com/Ali-Rajabzadeh)