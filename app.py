import streamlit as st
import google.generativeai as genai

# 1. Paste your API key here
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-3.8-flash")

st.title("PocketSmart AI")
st.write("Your Smart Budget Recommendation Assistant")

budget = st.number_input("Monthly Budget (Rs.)", min_value=100, value=5000)
expenses = st.text_area("Enter expenses", "food 2000, travel 500, recharge 300")

if st.button("Get Smart Advice"):
    with st.spinner("Thinking..."):
        prompt = f"""
        You are PocketSmart AI, a friendly budget assistant for Indian students.
        Monthly Budget: Rs.{budget}
        Expenses: {expenses}
        Give in simple Tamil + English:
        1. Total spent and balance
        2. Overspending warning
        3. 3 smart saving tips
        """
        response = model.generate_content(prompt)
        st.success(response.text)

st.divider()
st.subheader("Ask Pocket AI")
q = st.text_input("Ask anything about money")
if q:
    st.write(model.generate_content(q).text)