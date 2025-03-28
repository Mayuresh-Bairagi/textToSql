# AI-Powered SQL Query Generator

## Overview
This project is a Streamlit-based web application that converts natural language questions into SQL queries using Google Gemini AI and executes them on an SQLite database. It allows users to interact with databases without needing SQL knowledge.

## Features
- Convert English questions into SQL queries using AI.
- Execute the generated SQL queries on an SQLite database.
- Display the query results in a structured format.
- Error handling for invalid queries.

## Technologies Used
- Python
- Streamlit
- Google Gemini AI (via `google.generativeai`)
- SQLite
- Pandas

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Mayuresh-Bairagi/textToSql
   cd textToSql
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Create a `.env` file in the project root and add your Google Gemini AI API key:
     ```
     GENAI_API_KEY=your_api_key_here
     ```

## Usage
1. Ensure you have an SQLite database (`student.db`) with a `student` table.
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Enter a natural language question in the text input field.
4. Click the "Generate Query" button to get an AI-generated SQL query.
5. View the query results displayed in a table format.

## Example Queries
- "What is the name of the student in section A?"
- "Find the average marks of students in section B."
- "List students from section C who scored between 50 and 70."
.

