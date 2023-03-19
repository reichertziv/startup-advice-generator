import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

template = """
    You are an AI bot that is here to serve startup founders seeking advice on company building.
    You will take the following information given to you by a tech founder and reply to them with the best advice you can come up with.
    Please tailor your advice to the stage of the company, their business model/type, as well as to their specific query.
    Please give consice advice.
    Company stage: {company_stage}
    Type of company: {company_type}
    Area looking for advice in: {advice_area}
    Specific problem looking to solve: {specific_advice} 
"""

# load OpenAI LLM
llm = OpenAI(temperature=0.5, model="text-davinci-003")

# page title
st.markdown('# Startup Advice Generator')
st.write("---")

st.markdown('### Input:')

col1, col2 = st.columns(2)

with col1:
    company_stage = st.selectbox('Company stage:', ['Seed', 'Series A', 'Series B', 'Series C+'])
    advice_area = st.selectbox('Looking for advice about:', ['Fundraising', 'Hiring', 'Compensation', 'Sales', 'Growth', 'Product Development', 'Legal'])

with col2:
    company_type = st.selectbox('Company Type:', ['SaaS', 'Enterprise Software', 'Deep Tech', 'Consumer Software'])
    specific_advice = st.text_input("Can you elaborate on what you want advice on?")

col1, col2 = st.columns(2)

with col1:
    st.write("")
    button_status = st.button("Generate...")

with col2:
    st.write("")

st.write("---")

prompt = PromptTemplate(
    input_variables=["company_stage","company_type","advice_area","specific_advice"],
    template=template,
)

st.markdown('### Output:')

if button_status:
    if company_stage is not "" and company_type is not "" and advice_area is not "" and specific_advice is not "":
      email_output = llm(prompt.format(company_stage=company_stage,company_type=company_type,advice_area=advice_area,specific_advice=specific_advice))
      st.write(email_output)
    else:
        st.write("Fill in the input fields above...")
else:
    st.write("Fill in the input fields above...")

st.write("---")