import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
import sqlite3
import pandas as pd

# Load environment variables
load_dotenv()

# Configure Gemini AI
genai.configure(api_key=os.getenv("GENAI_API_KEY"))

def generate_sql(question, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt, question])
    return response.text.strip()

def execute_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        df = pd.read_sql_query(sql, conn)
        conn.close()
        return df
    except Exception as e:
        return f"Error executing query: {str(e)}"

# Prompt for AI
prompt = """
You are an expert in converting English questions into SQL queries.

Database Name: student  
Tables:  
- student (NAME, SECTION, MARK)

Guidelines:  
- Generate only the SQL query.  
- Do not include explanations or triple backticks in the output.
"""

# Streamlit UI
st.title("AI-Powered SQL Query Generator")
st.markdown("### Convert natural language questions into SQL queries and execute them.")

# User input
question = st.text_input("Enter your question:")
if st.button("Generate Query"):
    if question:
        sql_query = generate_sql(question, prompt)
        st.subheader("Generated SQL Query:")
        st.code(sql_query, language='sql')
        
        # Execute the query
        db = "student.db"
        result = execute_sql_query(sql_query, db)
        
        if isinstance(result, pd.DataFrame):
            st.subheader("Query Results:")
            st.dataframe(result)
        else:
            st.error(result)
    else:
        st.warning("Please enter a question to generate an SQL query.")