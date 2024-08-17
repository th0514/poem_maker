import os
import streamlit as st
from openai import OpenAI

open_api= os.getenv("OPENAI_API")
client = OpenAI(api_key=open_api)

def poem_maker(prompt):
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": prompt}
    ]
    )
    return completion.choices[0].message.content


st.title('Poem Maker')
st.subheader('시의 주제나 영감을 입력하세요')
st.sidebar.header('Option')
length = st.sidebar.selectbox('시 길이', ['길게','중간', '짧게'])
type = st.sidebar.selectbox('시 종류-형식상', ['산문시','자유시', '정형시'])
content = st.sidebar.selectbox('시 종류-내용상', ['서사시','서정시', '극시'])
topic = st.text_input('주제를 입력하세요')
button=st.button('시 생성')

prompt=f'한글로 시를 지어주는데 조건이 있어,조건들을 7가지로 나뉘어 길이는 {length}, 형식은 {type}, 내용은{content}, 주제는 {topic}인데 시를만들때 시적 허용은 포함하되, 특수문자와 .와 같은 기호(,를 제외한) 더불어 다른 틀린 맞춤법은 없어야해, 그리고 제목은 글씨를 굵어. 이 조건들로 시를 만들어줘.'

if button:

    text = poem_maker(prompt)
    st.subheader("생성된 시")
    st.write(text)

  
st.markdown(
    '''
    <style>
    #poem-maker {
    color:crimson;
    font-size: 50px;
    font-weight: 700;
    }

    h3#31d4dc6d {
    color:blue;
    }
    </style>
    ''',

    unsafe_allow_html=True 
)

