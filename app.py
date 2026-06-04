import streamlit as st
import requests

st.set_page_config(page_title="UJIMA Automation", layout="wide")

# Title and description
st.title("🚀 UJIMA Automation Dashboard")
st.markdown("Welcome to the UJIMA Automation project!")

# Sidebar
with st.sidebar:
    st.header("Navigation")
    page = st.radio("Select a page", ["Home", "API Test"])

# Home page
if page == "Home":
    st.header("Welcome to UJIMA Automation")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Status", "Active", "+1")
    
    with col2:
        st.metric("Processes", "5", "+2")
    
    with col3:
        st.metric("Efficiency", "95%", "+3%")
    
    st.markdown("---")
    st.subheader("About this project")
    st.write("""
    This is a Streamlit application for automating UJIMA processes.
    
    **Features:**
    - Real-time monitoring
    - API integration
    - Data visualization
    - Automated workflows
    """)

# API Test page
elif page == "API Test":
    st.header("API Test")
    
    st.write("Test your API endpoints here.")
    
    url = st.text_input("Enter API URL:", placeholder="https://api.example.com/endpoint")
    
    if url:
        if st.button("Send Request"):
            try:
                response = requests.get(url, timeout=5)
                st.success("✅ Request successful!")
                st.write(f"Status Code: {response.status_code}")
                st.json(response.json())
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
