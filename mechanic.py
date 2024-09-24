import streamlit as st
from langchain import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI()

# Define a prompt template that focuses on car repairs
prompt_template = PromptTemplate(
    input_variables=["question"],
    template="""
    You are a mechanic bot that provides information and advice only about car repairs. If the question is beyond car repairs kindly say "sorry I can only help you with car repairs".
    Answer the following question accurately, concisely and provide step by step in complete details:
    {question}
    """
)

# Create a chain with the LLM and prompt
mechanic_chain = LLMChain(llm=llm, prompt=prompt_template)

# Streamlit app setup
st.title("Mechanic Bot")
st.write("Ask your car repair questions here:")

# User input
user_question = st.text_input("Enter your question about car repairs:")

# Add a button to submit the question
if st.button("Click"):
    if user_question:
        response = mechanic_chain.run(question=user_question)
        st.write("**Mechanic Bot's Response:**")
        st.write(response)
    else:
        st.warning("Please enter a question before clicking the button.")
