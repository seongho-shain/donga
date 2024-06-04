import streamlit as st 
"page 3"
value = st.text_input("값을 입력하세요")
if st.button("저장"):
    st.session_state["a"] = value #선언