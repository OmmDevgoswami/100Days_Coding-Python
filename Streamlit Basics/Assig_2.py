import streamlit as st
import datetime

current_date = datetime.date.today()

st.write("# Age Calculator")

DOB = st.date_input("Enter your Date of Birth", min_value=datetime.date(1900, 1, 1), max_value=current_date)
st.write(f"Your Date of Birth is {DOB}")
age = current_date.year - DOB.year
st.write(f"Your Age is {age} years")