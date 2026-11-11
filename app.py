
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="SmartCalc AI",
    page_icon="🧮",
    layout="centered"
)

# Application heading
st.title("🧮 SmartCalc AI")
st.write("Your first Python-powered calculator!")

st.divider()

# User inputs
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox(
    "Choose an operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Calculate button
if st.button("Calculate", use_container_width=True):

    if operation == "Addition":
        result = num1 + num2

    elif operation == "Subtraction":
        result = num1 - num2

    elif operation == "Multiplication":
        result = num1 * num2

    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = None
            st.error("Cannot divide by zero!")

    if result is not None:
        st.success(f"Result: {result}")
