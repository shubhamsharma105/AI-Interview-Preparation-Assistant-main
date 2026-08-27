import streamlit as st
import pandas as pd
from database import create_tables, save_interview, get_all_interviews

# Ensure DB table exists
create_tables()

st.set_page_config(page_title="AI Interview Preparation Assistant", page_icon="🎯", layout="wide")

# Navigation Tabs
tab1, tab2 = st.tabs(["🎯 Take Interview", "📜 Interview History"])

# -------------------------
# TAB 1: Take Interview
# -------------------------
with tab1:
    st.title("🎯 AI Interview Preparation Assistant")
    
    # Candidate Details
    candidate_name = st.text_input("Enter Candidate Name", "")
    role = st.selectbox("Select Job Role", ["Python Developer", "Data Analyst", "Machine Learning Engineer"])

    # (Your existing interview state logic goes here...)
    
    # Inside your Final Report section, save the result once:
    if st.button("Save Interview Result to DB"):
        overall_score = 8.5 # Example score from your logic
        summary_feedback = "Strong technical core, work on communication."
        save_interview(candidate_name, role, overall_score, summary_feedback)
        st.success("Successfully saved to interview.db!")

# -------------------------
# TAB 2: Interview History
# -------------------------
with tab2:
    st.header("📜 Past Interview Records")
    
    history_data = get_all_interviews()
    
    if history_data:
        df_history = pd.DataFrame(
            history_data, 
            columns=["ID", "Candidate Name", "Role", "Overall Score", "Feedback"]
        )
        st.dataframe(df_history, use_container_width=True)
    else:
        st.info("No past interview history found in database.")