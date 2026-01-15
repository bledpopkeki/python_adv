import streamlit as st

from modul4.loops import user_input


def main():
    st.title("Hello world")

if st.button("clickme"):
    st.write("button clicked!")
st.checkbox("check me")
if st.checkbox("check me to show some text"):
    st.write("you're seeing this text because you checked the checkbox")

user_input = st.text_input("enter text","sample text")
st.write("you have entered: ", user_input)
age = st.number_input("enter your age", min_value=0, max_value=100)
st.write(f"your age is: {age}")

message = st.text_area("enter a message")
st.write(f"your message:{message}")
if st.button("success"):
    st.success("Operation was successful")










if __name__ == __main__:
    main()
