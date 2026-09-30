import subprocess
import sys
import streamlit as st

st.set_page_config(page_title="MACALCU Web", page_icon="📊", layout="wide")

st.title("MACALCU Financial Suite is Loading...")
st.write("Your application is starting up. If it doesn't appear below shortly, please refresh the page.")

# This runs your existing Flet application backend in the background
@st.cache_resource
def start_flet():
    # Runs main.py on a background port
    subprocess.Popen([sys.executable, "main.py"])

start_flet()

# Embeds the local Flet web server view directly into the Streamlit page
st.components.v1.iframe("http://localhost:8550", height=800, scrolling=True)
