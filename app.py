from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

#configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Load gemini model

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text

def read_sql_query(query,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

#Prompt definition
prompt = [
"""
You are an expert in converting English questions to SQL code!
The SQL database has the name STUDENT and the following columns - NAME , CLASS , SECTION\n\n
For example,\n Example 1 - How many entries of records are present?,
the SQL command will be something like this SELECT COUNT(* FROM STUDENT;
\n Example 2 - Tell me all the students studying in AI class?,
the SQL command will be something like this SELECT * FROM STUDENT WHERE CLASS = "AI";
also the sql code should not have ``` in the beginning or end and sql word in output

"""
]

#Streamlit app

st.set_page_config(page_title="I can retreive any SQL query")
st.header("Gemini App to retrieve any SQL Data")

question = st.text_input("Input:" , key="input" )
submit = st.button("Ask the question")

#If submit is clicked

if submit:
    response = get_gemini_response(question,prompt)
    print(response)
    response = read_sql_query(response,"student.db")
    st.subheader("The response is")
    for row in response:
        print(row)
        st.header(row)