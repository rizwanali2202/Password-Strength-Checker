import streamlit as st
import re

st.title ("Password Strength Checker")
st.markdown ("""
## Wellcome to password strength checker
       We will give you helpfull tips to create a **Strong Password**
        """)
password = st.text_input("Enter your password", type= "password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else :
        feedback.append("Password should be at least 8 character long")    
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
          feedback.append("Password should be uppercase and lowercase character")
    if re.search(r'\d', password):
        score += 1
    else:
          feedback.append("Password should contain atleast 1 digit")
    if re.search(r'[!@#$%^&()*]', password):
        score += 1
    else:
          feedback.append("Password should contain atleast 1 character [!@#$%^&()*]")
    if score == 4:
          feedback.append("Your password is strong")
    elif score == 3:         
          feedback.append("Your password is medium strength")
    else:
          feedback.append("Your password is weak")

    if feedback:
         st.markdown("## Improvement suggestion")
         for tip in feedback:
              st.write(tip)
else:
     st.info("Please enter your password to get started")


st.markdown("&copy; Copyright 2025 Rizwanali2202")              
