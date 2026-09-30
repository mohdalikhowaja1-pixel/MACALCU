import streamlit as st

st.set_page_config(
    page_title="MACALCU Financial Suite", 
    page_icon="📊", 
    layout="wide"
)

st.title("📊 MACALCU — Smart Money Calculator")

# Replace this placeholder URL with your free Render or Hugging Face public Flet URL
FLET_APP_URL = "https://your-flet-app-name.onrender.com"

# Embed your live Flet application seamlessly into Streamlit
st.components.v1.iframe(FLET_APP_URL, height=850, scrolling=True)
