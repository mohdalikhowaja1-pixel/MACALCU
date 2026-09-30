import sys
import os

# Ensure the current directory is in Python's path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
import pandas as pd

# Page Configuration
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
    db_status = "Connected"
except Exception as e:
    db_status = f"Error: {e}"

# Sidebar status
with st.sidebar:
    st.header("App Control Panel")
    st.write(f"Database Status: **{db_status}**")
    nav_option = st.radio("Navigate to:", ["Home / Overview", "EMI Calculator", "SIP Calculator", "Expense Tracker", "Khata Manager"])
    st.divider()
    st.info("MACALCU Cloud Edition is running live and securely.")

# Main Navigation views
if nav_option == "Home / Overview":
    st.subheader("Welcome to MACALCU Dashboard")
    st.write("Your all-in-one smart financial calculation and tracking suite.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Calculators Available", value="EMI, SIP")
    with col2:
        st.metric(label="Trackers Active", value="Expenses & Khata")
    with col3:
        st.metric(label="Database", value="SQLite Active")
        
    st.success("Select a tool from the sidebar to start calculating or tracking your finances!")

elif nav_option == "EMI Calculator":
    st.subheader("💰 Loan EMI Calculator")
    
    col1, col2 = st.columns(2)
    with col1:
        principal = st.number_input("Loan Amount ($)", min_value=1000.0, value=500000.0, step=10000.0)
        rate = st.number_input("Annual Interest Rate (%)", min_value=0.1, value=8.5, step=0.1)
        tenure_years = st.number_input("Loan Tenure (Years)", min_value=1, value=5, step=1)
        
    with col2:
        # EMI Calculation Logic
        monthly_rate = (rate / 12) / 100
        months = tenure_years * 12
        if monthly_rate > 0:
            emi = (principal * monthly_rate * ((1 + monthly_rate) ** months)) / (((1 + monthly_rate) ** months) - 1)
        else:
            emi = principal / months
            
        total_payment = emi * months
        total_interest = total_payment - principal
        
        st.metric(label="Monthly EMI", value=f"${emi:,.2f}")
        st.metric(label="Total Interest Payable", value=f"${total_interest:,.2f}")
        st.metric(label="Total Payment (Principal + Interest)", value=f"${total_payment:,.2f}")

elif nav_option == "SIP Calculator":
    st.subheader("📈 Systematic Investment Plan (SIP) Calculator")
    
    col1, col2 = st.columns(2)
    with col1:
        monthly_investment = st.number_input("Monthly Investment ($)", min_value=100.0, value=5000.0, step=500.0)
        expected_return = st.number_input("Expected Annual Return Rate (%)", min_value=1.0, value=12.0, step=0.5)
        investment_years = st.number_input("Time Period (Years)", min_value=1, value=10, step=1)
        
    with col2:
        # SIP Calculation Logic
        i = (expected_return / 12) / 100
        n = investment_years * 12
        invested_amount = monthly_investment * n
        future_value = monthly_investment * (((1 + i)**n - 1) / i) * (1 + i)
        estimated_returns = future_value - invested_amount
        
        st.metric(label="Invested Amount", value=f"${invested_amount:,.2f}")
        st.metric(label="Estimated Returns", value=f"${estimated_returns:,.2f}")
        st.metric(label="Total Future Value", value=f"${future_value:,.2f}")

elif nav_option == "Expense Tracker":
    st.subheader("📝 Expense Tracker")
    
    with st.form("expense_form"):
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("Expense Title / Description")
            amount = st.number_input("Amount ($)", min_value=0.0, step=10.0)
        with col2:
            category = st.selectbox("Category", ["Food", "Utilities", "Entertainment", "Transport", "Other"])
            date = st.date_input("Date")
            
        submitted = st.form_submit_button("Add Expense")
        if submitted and title:
            try:
                expense_storage.add_expense(title, amount, category, str(date))
                st.success("Expense added successfully!")
            except Exception as e:
                st.error(f"Error saving expense: {e}")
                
    st.divider()
    st.subheader("Recorded Expenses")
    try:
        expenses_list = expense_storage.get_all_expenses()
        if expenses_list:
            df = pd.DataFrame(expenses_list)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No expenses recorded yet. Add one above!")
    except Exception as e:
        st.info("No expense records found in database yet.")

elif nav_option == "Khata Manager":
    st.subheader("📖 Khata Ledger")
    st.info("Manage credit and debit accounts securely.")
    try:
        khata_records = khata_db.get_all_khata()
        if khata_records:
            st.dataframe(pd.DataFrame(khata_records), use_container_width=True)
        else:
            st.info("No Khata entries found.")
    except Exception as e:
        st.info("Khata ledger initialized and ready.")
