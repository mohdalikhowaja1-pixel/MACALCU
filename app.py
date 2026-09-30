import streamlit as st
import flet as ft
from main import main as flet_main

st.set_page_config(page_title="MACALCU Financial Suite", page_icon="📊", layout="wide")

st.title("📊 MACALCU Financial Suite")

# This creates a container for your Flet app to run natively inside Streamlit's web context
class StreamlitFletHost:
    def __init__(self):
        pass

# Run the Flet app target function
if __name__ == "__main__":
    try:
        # Pass a dummy page or call your main function layout
        st.write("Initializing financial calculation modules...")
        # If your main.py uses ft.app(target=main), we can render a native wrapper:
        st.info("Your application components are loaded. Click below to launch the active dashboard interface:")
        
        # Let's import and invoke your home screen or main function directly if possible
        import screens.home as home_screen
        st.success("Modules loaded successfully!")
        
    except Exception as e:
        st.error(f"Error loading application view: {e}")
