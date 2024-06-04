import streamlit as st 

st.page_link("home.py", label="Home", icon="🏠")
st.page_link("pages/3_page1.py", label="Page 1", icon="1️⃣")
st.page_link("pages/2_page2.py", label="Page 2", icon="2️⃣", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")
st.snow()