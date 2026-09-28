import streamlit as st

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="Course Recommendation Expert System",
    page_icon="🎓",
    layout="centered"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #666666;
    font-size: 17px;
}

.result-box {
    padding: 20px;
    border-radius: 12px;
    background-color: #e8f5e9;
    border-left: 6px solid #2e7d32;
}

.info-box {
    padding: 15px;
    border-radius: 10px;
    background-color: #f5f5f5;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# TITLE
# -----------------------------
st.markdown(
    '<div class="main-title">🎓 Course Recommendation Expert System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-based course recommendation using IF-THEN rules</div>',
    unsafe_allow_html=True
)

st.write("")

# -----------------------------
# INTRODUCTION
# -----------------------------
st.info(
    "This Expert System recommends a suitable course based on "
    "the user's interest, skill level, and career goal."
)

st.divider()

# -----------------------------
# USER INPUT
# -----------------------------
st.subheader("👤 Enter Your Details")

interest = st.selectbox(
    "1️⃣ Area of Interest",
    [
        "Programming",
        "Web Development",
        "Data Science",
        "Artificial Intelligence",
        "Cybersecurity"
    ]
)

skill = st.selectbox(
    "2️⃣ Current Skill Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

goal = st.selectbox(
    "3️⃣ Career Goal",
    [
        "Software Developer",
        "Web Developer",
        "Data Analyst",
        "AI Engineer",
        "Cybersecurity Professional"
    ]
)

st.write("")

# -----------------------------
# RECOMMENDATION
# -----------------------------
if st.button("🔍 Recommend Course", use_container_width=True):

    recommendation = ""
    reason = ""

    # Rule 1
    if (
        interest == "Programming"
        and skill == "Beginner"
        and goal == "Software Developer"
    ):
        recommendation = "Python Programming"
        reason = "Python is a good starting course for programming beginners interested in software development."

    # Rule 2
    elif (
        interest == "Programming"
        and skill == "Intermediate"
        and goal == "Software Developer"
    ):
        recommendation = "Data Structures and Algorithms"
        reason = "DSA helps intermediate programmers improve problem-solving and software development skills."

    # Rule 3
    elif (
        interest == "Web Development"
        and skill == "Beginner"
        and goal == "Web Developer"
    ):
        recommendation = "HTML, CSS and JavaScript"
        reason = "These are the fundamental technologies required to start web development."

    # Rule 4
    elif (
        interest == "Web Development"
        and skill in ["Intermediate", "Advanced"]
        and goal == "Web Developer"
    ):
        recommendation = "Full Stack Web Development"
        reason = "Your skill level and career goal match full-stack web development."

    # Rule 5
    elif (
        interest == "Data Science"
        and skill == "Beginner"
        and goal == "Data Analyst"
    ):
        recommendation = "Python for Data Analysis"
        reason = "Python provides a useful foundation for data analysis."

    # Rule 6
    elif (
        interest == "Data Science"
        and skill in ["Intermediate", "Advanced"]
        and goal == "Data Analyst"
    ):
        recommendation = "Data Science and Machine Learning"
        reason = "Your data science interest and skill level match data science and machine learning."

    # Rule 7
    elif (
        interest == "Artificial Intelligence"
        and skill == "Beginner"
        and goal == "AI Engineer"
    ):
        recommendation = "Introduction to Artificial Intelligence"
        reason = "This provides the basic concepts needed to start learning AI."

    # Rule 8
    elif (
        interest == "Artificial Intelligence"
        and skill in ["Intermediate", "Advanced"]
        and goal == "AI Engineer"
    ):
        recommendation = "Machine Learning"
        reason = "Machine Learning is a suitable next step for an intermediate or advanced AI learner."

    # Rule 9
    elif (
        interest == "Cybersecurity"
        and skill == "Beginner"
        and goal == "Cybersecurity Professional"
    ):
        recommendation = "Cybersecurity Fundamentals"
        reason = "Fundamentals provide the basic knowledge required for cybersecurity."

    # Rule 10
    elif (
        interest == "Cybersecurity"
        and skill in ["Intermediate", "Advanced"]
        and goal == "Cybersecurity Professional"
    ):
        recommendation = "Ethical Hacking and Network Security"
        reason = "Your cybersecurity interest and skill level match advanced security topics."

    # General fallback
    else:

        if interest == "Programming":
            recommendation = "Python Programming"
            reason = "Python provides a strong programming foundation."

        elif interest == "Web Development":
            recommendation = "Web Development"
            reason = "Web development matches your selected area of interest."

        elif interest == "Data Science":
            recommendation = "Python for Data Analysis"
            reason = "Python is a useful starting point for data-related careers."

        elif interest == "Artificial Intelligence":
            recommendation = "Introduction to Artificial Intelligence"
            reason = "This course provides a foundation in Artificial Intelligence."

        elif interest == "Cybersecurity":
            recommendation = "Cybersecurity Fundamentals"
            reason = "This course provides basic cybersecurity knowledge."

    # -----------------------------
    # RESULT
    # -----------------------------
    st.write("")
    st.subheader("🎯 Recommendation")

    st.markdown(
        f"""
        <div class="result-box">
        <h3>Recommended Course: {recommendation}</h3>
        <p>{reason}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.success(
        "🤖 Decision generated by the Expert System using IF-THEN rules."
    )

# -----------------------------
# HOW THE SYSTEM WORKS
# -----------------------------
st.divider()

st.subheader("⚙️ How the Expert System Works")

st.markdown("""
**1. User Input**  
User provides interest, skill level and career goal.

**2. Knowledge Base**  
The system contains predefined IF-THEN rules.

**3. Inference**  
The system compares the user's inputs with the rules.

**4. Recommendation**  
The matching rule produces a suitable course recommendation.
""")

st.divider()

# -----------------------------
# PROJECT INFORMATION
# -----------------------------
st.subheader("📌 Project Information")

col1, col2 = st.columns(2)

with col1:
    st.write("**AI Technique:**")
    st.write("Rule-Based Expert System")

with col2:
    st.write("**Number of Main Rules:**")
    st.write("10 IF-THEN Rules")

st.caption(
    "Course Recommendation Expert System | AI Mini Project"
)