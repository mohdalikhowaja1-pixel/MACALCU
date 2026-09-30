import sys
import os

# Ensure Python can locate your internal folders (storage, calculations, screens)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
import flet as ft

st.set_page_config(
    page_title="MACALCU — Smart Money Calculator", 
    page_icon="📊", 
    layout="wide"
)

st.title("📊 MACALCU — Smart Money Calculator")

# Initialize database modules safely
try:
    from storage.expense_storage import init_db
    from storage.khata_db import init_khata_db
    init_db()
    init_khata_db()
    st.sidebar.success("Database connected successfully!")
except Exception as e:
    st.sidebar.error(f"Database init warning: {e}")

st.write("Welcome to your financial suite dashboard. Select a calculation module below:")

# Provide native Streamlit quick-access tabs or expanders that trigger your modules
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home / Overview", "💰 EMI Calculator", "📈 SIP Calculator", "📝 Expense Tracker"])

with tab1:
    st.subheader("Dashboard Overview")
    st.info("Your application layout is connected. Use the navigation options below or check out your native panels.")
    try:
        from screens.home import build_home_screen
        st.write("Home module loaded successfully.")
    except Exception as ex:
        st.warning(fCould not load home screen module directly: {ex})

with tab2:
    st.subheader("EMI Calculation Suite")
    try:
        from screens.emi import build_emi_screen
        st.write("EMI calculation tools are ready.")
    except Exception as ex:
        st.warning(f"Module load warning: {ex}")

with tab3:
    st.subheader("SIP Investment Planner")
    try:
        from screens.sip import build_sip_screen
        st.write("SIP module loaded.")
    except Exception as ex:
        st.warning(f"Module load warning: {ex}")

with tab4:
    st.subheader("Expense & Khata Tracker")
    try:
        from screens.expenses import build_tracker_screen
        from screens.khata_screen import KhataScreen
        st.write("Tracker modules loaded successfully.")
    except Exception as ex:
        st.warning(f"Module load warning: {ex}")
