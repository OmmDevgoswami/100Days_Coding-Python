import streamlit as st

st.write("# Choose your Favorite Coding Language")

code = ["C", "C++", "Java", "Python"]
value = st.radio("Choose your favorite Codinng Language", code, index = None)
st.write(f"User Choice is {value}")
value = st.selectbox("Choose your favorite Coding Language", code, index = None)
st.write(f"User Choice is {value}")