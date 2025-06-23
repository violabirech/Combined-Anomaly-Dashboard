import streamlit as st

# --- Basic password authentication ---
def check_auth():
    st.sidebar.title("🔐 Login Required")
    password = st.sidebar.text_input("Enter password", type="password")
    if password != "admin123":
        st.warning("Access denied. Please enter the correct password.")
        st.stop()
check_auth()


import streamlit as st
from tabs import overview_tab, metrics_tab

st.set_page_config(page_title="Unified Network Anomaly Dashboard", layout="wide")
st.title("Real-Time Network Anomaly Detection")

# Dashboard toggle
dashboard_choice = st.radio("Select a Dashboard:", ["DNS", "DoS"], horizontal=True)

# Sidebar Controls
st.sidebar.header("Settings")
alerts_enabled = st.sidebar.checkbox("Enable Discord Alerts", value=True)
highlight_enabled = st.sidebar.checkbox("Highlight Anomalies", value=True)
highlight_color = st.sidebar.selectbox("Anomaly Highlight Color", ["red", "orange", "yellow", "blue", "green"], index=4)
time_range = st.sidebar.selectbox("Time Range", ["Last 30 min", "Last 1 hour", "Last 24 hours", "Last 7 days"], index=1)
threshold = st.sidebar.slider("Threshold", 0.01, 1.0, 0.1, 0.01)

# Tabs
tabs = st.tabs(["Overview", "Live Stream", "Manual Entry", "Metrics & Alerts", "Historical Data"])

with tabs[0]:
    overview_tab.render(dashboard_choice, time_range)

with tabs[3]:
    metrics_tab.render(dashboard_choice, time_range)
