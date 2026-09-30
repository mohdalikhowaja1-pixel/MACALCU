import streamlit as st
import flet as ft

st.set_page_config(page_title="MACALCU Financial Suite", page_icon="📊", layout="wide")

st.title("📊 MACALCU Financial Suite")
st.write("Welcome to your cloud financial suite! Loading your Flet application interface below:")

# Option: Run Flet app components directly or via web server configuration
import main  # This imports your main.py logic

st.info("If the application interface does not render automatically below, please ensure your main Flet function is exported or initialized for web view.")
