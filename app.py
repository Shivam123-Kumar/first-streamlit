import streamlit as st

# App Title
st.title("💻 Basic Streamlit Web App")

# Subtitle
st.subheader("Simple Input and Output Demo")

# Text Input
name = st.text_input("What's your name?")

# Number Input
age = st.number_input("Your age", min_value=0, max_value=100, step=1)

# Dropdown Menu
color = st.selectbox("Choose your favorite color", ["Red", "Blue", "Green", "Yellow"])

# Button
if st.button("Submit"):
    st.success(f"Hello {name}! 👋")
    st.write(f"You're {age} years old and your favorite color is {color}.")
