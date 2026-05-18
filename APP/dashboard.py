import streamlit as st
from analytics import (
    get_average_bill,
    get_average_energy_usage,
    get_automation_rate,
    get_total_customers,
    get_total_tickets
)
from chatbot_engine import chatbot_response

st.set_page_config(
    page_title="TragerInc Energy Dashboard",
    layout="wide"
)

st.title("⚡ TragerInc Energy Usage Insights Dashboard")

st.write(
    "This dashboard provides key insights into customer energy usage, billing, "
    "support automation, and chatbot performance."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Customers", get_total_customers())

with col2:
    st.metric("Average Energy Usage", f"{get_average_energy_usage()} kWh")

with col3:
    st.metric("Average Bill", f"${get_average_bill()}")

col4, col5 = st.columns(2)

with col4:
    st.metric("Automation Rate", f"{get_automation_rate()}%")

with col5:
    st.metric("Support Tickets", get_total_tickets())

st.divider()

st.subheader("💬 Ask the Energy Chatbot")

query = st.text_input("Enter your question")

if query:
    response = chatbot_response(query)
    st.success(response)