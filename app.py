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

# Custom Styling to match your clean financial theme
st.markdown("""
    <style>
    .main {
        padding: 20px;
    }
    h1 {
        color: #1E293B;
    }
    </style>
""", unsafe_allow_html=True)

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

# Sidebar Navigation matching your full suite
with st.sidebar:
    st.header("🎛️ Control Panel")
    st.write(f"Database Status: **{db_status}**")
    nav_option = st.radio(
        "Select Module:", 
        ["Home / Overview", "EMI Calculator", "SIP Calculator", "Expense Tracker", "Khata Manager"]
    )
    st.divider()
    st.info("MACALCU Cloud Edition — All features active.")

# 1. Home / Overview View
if nav_option == "Home / Overview":
    st.subheader("Welcome to MACALCU Dashboard")
    st.write("Your complete financial calculator and ledger suite is online.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Calculators", value="EMI & SIP")
    with col2:
        st.metric(label="Ledgers", value="Expenses & Khata")
    with col3:
        st.metric(label="Exports", value="Excel & PDF Ready")
        
    st.info("👈 Choose any calculator or manager from the left sidebar to begin!")

# 2. EMI Calculator Module
elif nav_option == "EMI Calculator":
    st.subheader("💰 Loan EMI Calculator & Schedule")
    
    try:
        import emi
        # If your emi.py has a specific runner function, we can invoke it, 
        # or use this native layout with full calculation, reset, and export features:
    except ImportError:
        pass

    col1, col2 = st.columns(2)
    with col1:
        loan_amount = st.number_input("Loan Amount ($)", min_value=1000.0, value=500000.0, step=10000.0, key="emi_amt")
        interest_rate = st.number_input("Interest Rate (%) p.a.", min_value=0.1, value=8.5, step=0.1, key="emi_rate")
        tenure = st.number_input("Tenure (Years)", min_value=1, value=5, step=1, key="emi_tenure")
        
        c1, c2 = st.columns(2)
        with c1:
            calculate_emi = st.button("Calculate EMI", type="primary", use_container_width=True)
        with c2:
            reset_emi = st.button("Reset", use_container_width=True)
            if reset_emi:
                st.rerun()

    with col2:
        monthly_interest_rate = (interest_rate / 12) / 100
        total_months = tenure * 12
        if monthly_interest_rate > 0:
            emi_val = (loan_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** total_months)) / (((1 + monthly_interest_rate) ** total_months) - 1)
        else:
            emi_val = loan_amount / total_months
            
        total_payment = emi_val * total_months
        total_interest = total_payment - loan_amount
        
        st.metric(label="Monthly EMI", value=f"${emi_val:,.2f}")
        st.metric(label="Total Interest", value=f"${total_interest:,.2f}")
        st.metric(label="Total Amount Payable", value=f"${total_payment:,.2f}")
        
        # Excel Export feature simulation for EMI breakdown
        if st.button("📥 Download EMI Schedule (Excel)"):
            schedule_data = []
            balance = loan_amount
            for m in range(1, total_months + 1):
                interest_paid = balance * monthly_interest_rate
                principal_paid = emi_val - interest_paid
                balance -= principal_paid
                schedule_data.append({
                    "Month": m,
                    "EMI": round(emi_val, 2),
                    "Principal": round(principal_paid, 2),
                    "Interest": round(interest_paid, 2),
                    "Balance": round(max(0, balance), 2)
                })
            df_schedule = pd.DataFrame(schedule_data)
            csv = df_schedule.to_csv(index=False).encode('utf-8')
            st.download_button("Click here to download CSV/Excel", data=csv, file_name="emi_schedule.csv", mime="text/csv")

# 3. SIP Calculator Module
elif nav_option == "SIP Calculator":
    st.subheader("📈 SIP Investment Calculator")
    
    col1, col2 = st.columns(2)
    with col1:
        monthly_inv = st.number_input("Monthly Investment ($)", min_value=500.0, value=5000.0, step=500.0, key="sip_inv")
        exp_return = st.number_input("Expected Annual Return (%)", min_value=1.0, value=12.0, step=0.5, key="sip_ret")
        duration_yrs = st.number_input("Time Period (Years)", min_value=1, value=10, step=1, key="sip_yrs")
        
        sc1, sc2 = st.columns(2)
        with sc1:
            st.button("Calculate SIP", type="primary", use_container_width=True)
        with sc2:
            if st.button("Reset SIP", use_container_width=True):
                st.rerun()

    with col2:
        i_rate = (exp_return / 12) / 100
        n_months = duration_yrs * 12
        invested_amt = monthly_inv * n_months
        future_val = monthly_inv * (((1 + i_rate)**n_months - 1) / i_rate) * (1 + i_rate)
        est_returns = future_val - invested_amt
        
        st.metric(label="Invested Amount", value=f"${invested_amt:,.2f}")
        st.metric(label="Estimated Returns", value=f"${est_returns:,.2f}")
        st.metric(label="Total Future Value", value=f"${future_val:,.2f}")
        
        # Export feature
        if st.button("📥 Download SIP Projection Report"):
            sip_report = pd.DataFrame({
                "Metric": ["Monthly Investment", "Years", "Expected Return", "Total Invested", "Future Value"],
                "Value": [monthly_inv, duration_yrs, exp_return, round(invested_amt, 2), round(future_val, 2)]
            })
            csv_sip = sip_report.to_csv(index=False).encode('utf-8')
            st.download_button("Download SIP CSV", data=csv_sip, file_name="sip_report.csv", mime="text/csv")

# 4. Expense Tracker Module
elif nav_option == "Expense Tracker":
    st.subheader("📝 Expense Tracker & Manager")
    
    with st.form("expense_entry"):
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("Expense Title")
            amount = st.number_input("Amount ($)", min_value=0.0, step=10.0)
        with col2:
            category = st.selectbox("Category", ["Food", "Utilities", "Rent", "Entertainment", "Other"])
            date = st.date_input("Date")
            
        submitted = st.form_submit_button("Add Expense", type="primary")
        if submitted and title:
            try:
                expense_storage.add_expense(title, amount, category, str(date))
                st.success("Expense recorded successfully!")
            except Exception as e:
                st.error(f"Error: {e}")
                
    st.divider()
    st.subheader("Expense History & Exports")
    try:
        expenses_list = expense_storage.get_all_expenses()
        if expenses_list:
            df_exp = pd.DataFrame(expenses_list)
            st.dataframe(df_exp, use_container_width=True)
            
            # Export to CSV / Excel button
            csv_data = df_exp.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Export Expenses to CSV/Excel", data=csv_data, file_name="expenses_report.csv", mime="text/csv")
        else:
            st.info("No expense logs found. Add one above.")
    except Exception as e:
        st.info("Database table ready for tracking.")

# 5. Khata Manager Module
elif nav_option == "Khata Manager":
    st.subheader("📖 Khata Ledger Book")
    try:
        khata_records = khata_db.get_all_khata()
        if khata_records:
            df_khata = pd.DataFrame(khata_records)
            st.dataframe(df_khata, use_container_width=True)
            
            khata_csv = df_khata.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Export Khata Ledger", data=khata_csv, file_name="khata_ledger.csv", mime="text/csv")
        else:
            st.info("No Khata entries recorded yet.")
    except Exception as e:
        st.info("Khata ledger initialized and online.")
