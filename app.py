import streamlit as st
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Loan Calculator", page_icon="🏦", layout="centered")

st.title("🏦 Loan Eligibility Calculator")
st.write("Fill your details below:")

# ---------------- INPUTS ---------------- #
age = st.number_input("Enter your Age", min_value=18, max_value=65, value=22)
income = st.number_input("Monthly Income (₹)", min_value=0, value=5000)
credit_score = st.slider("Credit Score", 300, 900, 650)
existing_emi = st.number_input("Existing EMI (₹)", min_value=0, value=1000)

# New Inputs
interest_rate = st.number_input("Interest Rate (%)", value=10.0)
tenure = st.slider("Loan Tenure (Years)", 1, 30, 5)

# ---------------- LOGIC ---------------- #
if st.button("Check Eligibility"):

    # Age check
    if age < 21 or age > 60:
        st.error("❌ Not Eligible: Age criteria not met")

    # Credit score check
    elif credit_score < 650:
        st.error("❌ Not Eligible: Low Credit Score")

    else:
        # EMI calculation eligibility
        max_emi_allowed = income * 0.5
        available_emi = max_emi_allowed - existing_emi

        if available_emi <= 0:
            st.error("❌ Not Eligible: High existing EMI")

        else:
            # Loan amount estimation
            loan_amount = available_emi * 60  # approx for 5 years

            st.success("✅ You are Eligible!")
            st.write(f"💰 Estimated Loan Amount: ₹{int(loan_amount)}")

            # ---------------- EMI CALCULATION ---------------- #
            r = interest_rate / 12 / 100
            n = tenure * 12

            if r > 0:
                emi = loan_amount * r * (1 + r)**n / ((1 + r)**n - 1)
                st.write(f"📊 Estimated EMI: ₹{int(emi)}")
            else:
                st.write("📊 EMI cannot be calculated")

            # ---------------- GRAPH ---------------- #
            st.subheader("📊 EMI Distribution")

            labels = ['Available EMI', 'Existing EMI']
            values = [available_emi, existing_emi]

            fig, ax = plt.subplots()
            ax.pie(values, labels=labels, autopct='%1.1f%%')
            st.pyplot(fig)