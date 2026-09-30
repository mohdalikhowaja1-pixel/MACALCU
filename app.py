import streamlit as st
import main

st.set_page_config(page_title="MACALCU Financial Suite", page_icon="📊", layout="wide")

st.title("📊 MACALCU Financial Suite")
st.write("Welcome to your financial web dashboard!")

# Call your main execution logic directly or render interface hints
try:
    st.success("Application modules loaded successfully from repository.")
    # Here you can invoke elements or let Streamlit present the app layout
except Exception as e:
    st.error(f"Error loading application: {e}")
