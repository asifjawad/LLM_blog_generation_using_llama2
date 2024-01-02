import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers



def get_response(input_text,number_words,blog_style):
    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})

    template= """
            Write a blog for {blog_style} job profile for a topic {input_text}
            within this {number_words} words.

            """
    prompt = PromptTemplate(input_variables=["blog_style, input_text, number_words"], template=template)
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, number_words=number_words))
    print(response)
    return response


st.set_page_config(page_title="LLAMA Blog Generator",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("LLAMA Blog Generator")

input_text=st.text_input("Enter the keywords for the topic")

col1,col2=st.columns([5,5])

with col1:
    number_words = st.text_input("Enter the Number of words")

with col2:
    blog_style=st.text_input('Blog for', ('Artificial Intelligence Engineer', 'Data Scientist', 'Researchers'), index=0)

submit=st.button('Generate')
# Generate the final Response
if submit:
    st.write(get_response(input_text,number_words,blog_style))