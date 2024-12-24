## integrate code with openai api
import os
from constants import openai_key

from langchain.llms import OpenAI

import streamlit as st

os.environ['OPENAI_API_KEY']=openai_key

# initialzie stramlit framework

st.title('Langchain demo with openai API')
input_text = st.text_input("Search the topic you want.")

# initilaze openAI llm models
llm = OpenAI(temperature=0.8)


if input_text:
    st.write(llm(input_text))  # input text is given to llm to predict and st.write to print prediction that got from llm