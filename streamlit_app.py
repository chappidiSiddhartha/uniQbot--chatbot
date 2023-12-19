# Importing Libraries 
import streamlit as st
from langchain.llms import GooglePalm 

# Page Configuration  & Title
st.set_page_config(page_title="       🤖 UniQbot App 💬")
st.title('       🤖 UniQbot App 💬')

# Function to get response from LLM
def output_response(input_text):
  llm = GooglePalm(google_api_key='A-----------RgM', temperature=0.3) # use your google palm api key
  st.info(llm(input_text))

with st.form('my_form'):

  # Type Question
  text = st.text_area('Enter text:', "Can you provide tips for effective time management in a busy work environment?")
  submitted = st.form_submit_button('Submit')

  #if Question was submitted
  if  submitted:
    output_response(text)

  elif not submitted:
    st.warning('Please enter your Question', icon='‼️')
