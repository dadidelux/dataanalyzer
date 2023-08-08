import os
import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import matplotlib

matplotlib.use('tkAgg')

os.environ["OPENAI_API_KEY"] = "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"

llm = OpenAI()
pandas_ai = PandasAI(llm)

st.title("Data Analysis with AI using Prompts")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload a CSV File for analysis:", type=['csv'])


if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

prompt = st.text_area("Enter your prompt:")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating response"):
            st.write(pandas_ai.run(df, prompt=prompt))
    else:
        st.warning("Please enter a prompt.")
