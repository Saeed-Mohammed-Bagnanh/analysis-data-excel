from dotenv import load_dotenv
import os
import streamlit as st
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import pandas as pd
import matplotlib

matplotlib.use('TkAgg')

load_dotenv()
# API_KEY = os.environ['OPENAI_API_KEY']

# create an LLM by instantiating OpenAI object, and passing API token
llm = OpenAI(api_token="sk-bhkn-oIEBZE1IkPHuZkAi2acBT3BlbkFJsGaF5VJgtaQQcQPkq15G")

# create PandasAI object, passing the LLM
pandas_ai = PandasAI(llm)

st.title("Analysis Data Excel")
uploaded_file = st.file_uploader("Upload a CSV file for analysis", type=['csv'])


if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(3))

    prompt = st.sidebar.text_area("Enter your prompt:")

    if st.sidebar.button("Generate"):
        if prompt:
            # call pandas_ai.run(), passing dataframe and prompt
            with st.spinner("Generating response..."):
                st.write(pandas_ai.run(df, prompt))
        else:
            st.warning("please enter your prompt. ")