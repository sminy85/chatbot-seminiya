import streamlit as st
import backend as be

# Streamlit 웹 인터페이스
st.title('Amazon Bedrock 기반 챗봇')
st.session_state.memory = be.buff_memory()
st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.markdown(message["text"])

# 사용자 입력 받기
input_text = st.chat_input("질문을 입력하세요:")

# 입력이 있을 때 대화 처리
if input_text:
    with st.chat_message("나"):
        st.markdown(input_text)

    st.session_state.chat_history.append({"role":"user","text":input_text})
    chat_response = be.cnvs_chain(input_text=input_text, memory=st.session_state.memory)

    with st.chat_message("챗봇"):
        st.markdown(chat_response)

    st.session_state.chat_history.append({"role":"assistant","text":chat_response})
