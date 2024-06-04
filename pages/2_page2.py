import streamlit as st 
"page 2"
if st.button("불러오기"):
    if "a" in st.session_state :
        value = st.session_state["a"] #호출
        f"{value} 값을 입력하셨네요"
    else:
        f"page3에서 값을 먼저 입력해주세요."