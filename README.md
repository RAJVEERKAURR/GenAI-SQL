# Natural Language to SQL Generator

An AI-powered tool that translates natural language questions into SQL queries, allowing non-technical users to easily query a database using conversational language.

## Overview

This project uses OpenAI's GPT-4 to convert natural language questions about Bollywood movies into SQL queries. The system then executes these queries against a SQLite database and returns the results.

## Features

- Converts natural language questions to SQL queries
- Executes generated SQL against a database
- Returns structured query results
- Handles complex queries about movie data
- Includes data import utilities

## Example Queries

- "Show me all movies directed by Kabir Khan"
- "What are the top 5 highest-grossing movies after 2018?"
- "Which web series have more than 10 episodes and an IMDb rating above 8?"
- "List all movies available on Netflix with a critics score above 85"

## Technical Details

### Technologies Used:
- **LangChain**: For creating LLM chains and prompts
- **OpenAI GPT-4**: For natural language understanding
- **SQLite**: Database for storing and querying movie data
- **Pandas**: For data manipulation and display

### Project Structure:
- `nlsql.py`: Core NL-to-SQL conversion system
- `sql_data.py`: Database setup and data import utilities
- `test.py`: Simple test file for LangChain functionality
- `bollywood_movie.csv`: Dataset containing movie information

## Setup Instructions

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your OpenAI API key
4. Run `python sql_data.py` to set up the database
5. Run `python nlsql.py` to start converting natural language to SQL

## Future Improvements

- Web interface for easier interaction
- Support for more complex queries
- Enhanced error handling
- Query validation to prevent SQL injection# GenAI-SQL
AI tool that translates natural language questions into SQL queries
