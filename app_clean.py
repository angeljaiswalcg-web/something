import math
import streamlit as st
from tools.calculator import calculate
st.set_page_config(page_title="SmartCalc AI", page_icon="🧮")

st.title("🧮 SmartCalc AI")
st.write("Your Python-powered calculator!")

if "history" not in st.session_state:
    st.session_state.history = []


def to_number(text):
    """Turn the typed text into a float. Empty box = 0.0.
    Returns None if the text is not a valid number."""
    text = text.strip().replace(",", "")
    if text == "":
        return 0.0
    try:
        value = float(text)
    except ValueError:
        return None
    if not math.isfinite(value):   # rejects "nan" and "inf"
        return None
    return value


st.divider()

text1 = st.text_input("Enter first number", placeholder="0", key="num1_text")
text2 = st.text_input("Enter second number", placeholder="0", key="num2_text")

operation = st.selectbox(
    "Choose operation",
    ["Addition", "Subtraction", "Multiplication", "Division"],
)


if st.button("Calculate", use_container_width=True):
    number1 = to_number(text1)
    number2 = to_number(text2)

    if number1 is None or number2 is None:
        st.error("Please enter valid numbers only.")

    else:
        try:
            result, symbol = calculate(number1, number2, operation)

            st.success(f"Result: {result:,.2f}")

            st.session_state.history.append(
                f"{number1:,.2f} {symbol} {number2:,.2f} = {result:,.2f}"
            )

        except ValueError as error:
            st.error(str(error))


st.divider()
st.subheader("📜 Calculation History")

for item in reversed(st.session_state.history):
    st.write(item)

if st.button("Clear History"):
    st.session_state.history = []
    st.rerun()