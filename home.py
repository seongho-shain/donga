import streamlit as st 
st.title("Hi")
st.text("Hello World!")
if st.button("눌러보세요"):
    st.text("Well done")
val = st.text_input("이름을 입력하세요")
st.text(f"{val}님 환영합니다.")
"Magic!!!"
import streamlit as st

with st.form(key='my_form'):
    text_input = st.text_input(label='Enter some text')
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        st.write('Form submitted! You entered:', text_input)
        
import pandas as pd

@st.cache_data
def load_data(url):
    return pd.read_csv(url)

url = 'https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv'
data = load_data(url)
st.write(data)

