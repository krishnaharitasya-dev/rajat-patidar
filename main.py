import streamlit as st
#title of app
st.title("my first streamlit app")
#adding text
st.write("hello! creating a simple webapplication using streamlit library")
#text input
name=st.text_input("enter your name:")
#number input
age=st.number_input("enter your age:")
#display a message when button is clicked
if st.button("submit"):
    st.write("helo,{name}! welcome to streamlit.")
