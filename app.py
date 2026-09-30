import sys
import os

# Ensure the current directory is in Python's path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st

st.set_page_config(
    page_title="MACALCU — Smart Money Calculator", 
    page_icon="📊", 
    layout="wide"
)

st.title("📊 MACALCU — Smart Money Calculator")

# Initialize database modules directly from root files
try:
    import expense_storage
    import khata_db
    expense_storage.init_db()
    khata_db.init_khata_db()
    st.sidebar.success("Database connected successfully!")
except Exception as e:
    st.sidebar.error(f"Database init warning: {e}")

st.write("Welcome to your financial suite dashboard. Select a calculation module below:")

# Streamlit UI tabs matching your calculation modules
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home / Overview", "💰 EMI Calculator", "📈 SIP Calculator", "📝 Expense Tracker"])

with tab1:
    st.subheader("Dashboard Overview")
    try:
        import home
        st.success("Home module loaded successfully.")
    except Exception as ex:
        st.warning(f"Could not load home screen: {ex}")

with tab2:
    st.subheader("EMI Calculation Suite")
    try:
        import emi
        st.success("EMI calculation tools are ready.")
    except Exception as ex:
        st.warning(f"EMI load warning: {ex}")

with tab3:
    st.subheader("SIP Investment Planner")
    try:
        import sip
        st.success("SIP module loaded.")
    except Exception as ex:
        st.warning(f"SIP load warning: {ex}")

with tab4:
    st.subheader("Expense & Khata Tracker")
    try:
        import expenses
        import khata_screen
        st.success("Tracker modules loaded successfully.")
    except Exception as ex:
        st.warning(f"Tracker load warning: {ex}")
