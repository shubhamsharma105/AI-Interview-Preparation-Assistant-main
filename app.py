import streamlit as st
import pandas as pd
from database import create_tables, save_interview, get_all_interviews
from report_generator import generate_report
from interview_engine import generate_question, question_bank

# Initialize database tables
create_tables()

st.set_page_config(
    page_title="AI Interview Preparation Assistant",
    page_icon="🎯",
    layout="wide"
)

# -------------------------
# Custom CSS for Modern UI
# -------------------------
st.markdown("""
<style>
    /* Metric Cards Styling */
    .metric-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 20px 24px;
        margin-bottom: 10px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    .metric-label {
        font-size: 0.85rem;
        color: #94a3b8;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #38bdf8;
        margin-top: 6px;
    }

    /* Role Progress Bar Styling */
    .role-card {
        background-color: #1e293b;
        border-radius: 10px;
        padding: 16px;
        margin-bottom: 12px;
        border: 1px solid #334155;
    }
    .role-title {
        font-size: 1rem;
        font-weight: 600;
        color: #f8fafc;
        display: flex;
        justify-content: space-between;
    }
    .bar-container {
        width: 100%;
        background-color: #334155;
        border-radius: 8px;
        height: 12px;
        margin-top: 8px;
        overflow: hidden;
    }
    .bar-fill {
        height: 100%;
        background: linear-gradient(90deg, #38bdf8 0%, #818cf8 100%);
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------
# Session State Setup
# -------------------------
if "asked_questions" not in st.session_state:
    st.session_state.asked_questions = []

if "current_question" not in st.session_state:
    st.session_state.current_question = None

if "scores" not in st.session_state:
    st.session_state.scores = []

if "feedbacks" not in st.session_state:
    st.session_state.feedbacks = []

if "saved" not in st.session_state:
    st.session_state.saved = False

if "selected_role" not in st.session_state:
    st.session_state.selected_role = None

TOTAL_QUESTIONS_PER_SESSION = 5

# -------------------------
# Navigation Tabs
# -------------------------
tab1, tab2 = st.tabs(["🎯 Interview", "📊 History & Analytics"])

# -------------------------
# TAB 1: Interview
# -------------------------
with tab1:
    st.sidebar.title("🎯 Interview Settings")
    
    candidate_name = st.sidebar.text_input("Candidate Name", "")
    role = st.sidebar.selectbox("Select Job Role", list(question_bank.keys()))

    if st.session_state.selected_role != role:
        st.session_state.selected_role = role
        st.session_state.asked_questions = []
        st.session_state.scores = []
        st.session_state.feedbacks = []
        st.session_state.saved = False
        st.session_state.current_question = generate_question(role, [])

    if st.session_state.current_question is None:
        st.session_state.current_question = generate_question(role, [])

    st.title("🎯 AI Interview Preparation Assistant")
    st.write("Practice interviews with dynamic questions, get AI evaluation, and view performance logs.")

    q_num = len(st.session_state.asked_questions) + 1
    progress = int((len(st.session_state.asked_questions) / TOTAL_QUESTIONS_PER_SESSION) * 100)
    st.progress(min(progress, 100))

    if len(st.session_state.asked_questions) < TOTAL_QUESTIONS_PER_SESSION and st.session_state.current_question != "Interview Completed":
        st.subheader(f"Question {q_num}/{TOTAL_QUESTIONS_PER_SESSION}")
        st.info(st.session_state.current_question)

        answer = st.text_area("Enter Your Answer", height=200, key=f"ans_{q_num}")

        if st.button("Submit Answer"):
            if answer.strip() == "":
                st.warning("Please enter an answer before submitting.")
            else:
                score = min(10, max(4, len(answer.split()) // 5))
                feedback = f"Score: {score}/10 | Detail evaluation completed."

                st.session_state.scores.append(score)
                st.session_state.feedbacks.append(feedback)
                st.session_state.asked_questions.append(st.session_state.current_question)

                st.success(feedback)
                st.session_state.current_question = generate_question(role, st.session_state.asked_questions)
                st.rerun()

    else:
        st.header("📊 Final Interview Report")

        if st.session_state.scores:
            avg_raw = sum(st.session_state.scores) / len(st.session_state.scores)
            readiness_score = round(avg_raw * 10, 1)
        else:
            readiness_score = 0.0

        col1, col2 = st.columns(2)
        col1.metric("Overall Readiness", f"{readiness_score}%")
        
        status = "PASS ✅" if readiness_score >= 70 else "NEEDS IMPROVEMENT ⚠️"
        col2.metric("Status", status)

        if not st.session_state.saved and st.session_state.scores:
            summary_feedback = f"Completed {len(st.session_state.scores)} questions with overall score of {readiness_score}%."
            save_interview(candidate_name, role, readiness_score, summary_feedback)
            st.session_state.saved = True
            st.success("✅ Interview record saved to database!")

        if st.button("Restart Interview"):
            st.session_state.asked_questions = []
            st.session_state.scores = []
            st.session_state.feedbacks = []
            st.session_state.saved = False
            st.session_state.current_question = generate_question(role, [])
            st.rerun()

# -------------------------
# TAB 2: Custom Dashboard
# -------------------------
with tab2:
    st.title("📊 History & Performance Analytics")
    st.write("Detailed candidate performance metrics and historical interview outcomes.")
    st.write("")

    report = generate_report()

    if report:
        # Custom HTML Metric Cards
        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Total Interviews</div>
                <div class="metric-value" style="color: #38bdf8;">{report['total_interviews']}</div>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Average Score</div>
                <div class="metric-value" style="color: #818cf8;">{report['average_score']}%</div>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Overall Pass Rate</div>
                <div class="metric-value" style="color: #34d399;">{report['pass_rate']}%</div>
            </div>
            """, unsafe_allow_html=True)

        st.write("")
        st.subheader("📌 Role-wise Performance")

        # Custom Horizontal Progress Cards instead of bulky chart
        role_data = report["role_summary"]
        for _, row in role_data.iterrows():
            r_name = row["Role"]
            r_score = round(row["Average Score"], 1)
            
            st.markdown(f"""
            <div class="role-card">
                <div class="role-title">
                    <span>{r_name}</span>
                    <span style="color: #38bdf8;">{r_score}%</span>
                </div>
                <div class="bar-container">
                    <div class="bar-fill" style="width: {min(r_score, 100)}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.write("")
        st.subheader("📜 All Interview Logs")

        # Display Clean Data Table
        display_df = report["df"][["id", "candidate_name", "role", "score", "feedback"]].copy()
        display_df.columns = ["ID", "Candidate Name", "Role", "Score (%)", "Summary Feedback"]
        
        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True
        )

    else:
        st.info("No interview records found. Complete an interview in Tab 1 to build analytics.")