import streamlit as st
import pandas as pd
from langchain.llms import GooglePalm

st.set_page_config(page_title="🤖 UniQbot App 💬")
st.title('🤖 UniQbot App 💬')

# Initializing  empty dataframe to store queries and responses
data = {'Query': [], 'Response': []}
df = pd.DataFrame(data)

def generate_response(input_text):
    llm = GooglePalm(google_api_key='A------------M', temperature=0.1)
    response = llm(input_text)
    st.info(response)

    # Append the query and response to the dataframe
    df.loc[len(df)] = [input_text, response]

# User input form
with st.form('my_form'):
    text = st.text_area('Enter text:', 'what is your name')
    submitted = st.form_submit_button('Submit')

# Generate response when the button is clicked
if submitted:
    generate_response(text)

# Display queries and responses
st.subheader('Query History:')
st.table(df)
