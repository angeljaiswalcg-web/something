
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="SmartCalc AI",
    page_icon="🧮"
)

st.title("🧮 SmartCalc AI")
st.write("Your Python-powered calculator!")

st.divider()

# Initialize calculation history
if "history" not in st.session_state:
    st.session_state.history = []

# User inputs
num1 = st.number_input(
    "Enter first number",
    value=0.0,
    format="%.2f"
)

num2 = st.number_input(
    "Enter second number",
    value=0.0,
    format="%.2f"
)

operation = st.selectbox(
    "Choose operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Calculate
if st.button("Calculate", use_container_width=True):

    if operation == "Addition":
        result = num1 + num2
        symbol = "+"

    elif operation == "Subtraction":
        result = num1 - num2
        symbol = "-"

    elif operation == "Multiplication":
        result = num1 * num2
        symbol = "×"

    elif operation == "Division":
        if num2 == 0:
            st.error("Cannot divide by zero!")
            result = None
        else:
            result = num1 / num2
            symbol = "÷"

    if result is not None:

        st.success(f"Result: {result}")

        # Save calculation in history
        st.session_state.history.append({
            "calculation": f"{num1:g} {symbol} {num2:g}",
            "result": result
        })

# Calculation history
st.divider()
st.subheader("📜 Calculation History")

if st.session_state.history:

    for item in reversed(st.session_state.history):
        st.write(
            f"**{item['calculation']} = {item['result']:g}**"
        )

    if st.button("Clear History"):
        st.session_state.history = []
        st.rerun()

else:
    st.info("No calculations yet. Start calculating!")

