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

    # -----------------------------
    # 30 IF-THEN RULES
    # -----------------------------

    # Rule 1
    if interest == "Programming" and skill == "Beginner" and goal == "Software Developer":
        recommendation = "Python Programming"
        reason = "Python is a good starting course for programming beginners interested in software development."

    # Rule 2
    elif interest == "Programming" and skill == "Intermediate" and goal == "Software Developer":
        recommendation = "Data Structures and Algorithms"
        reason = "DSA helps intermediate programmers improve problem-solving and software development skills."

    # Rule 3
    elif interest == "Programming" and skill == "Advanced" and goal == "Software Developer":
        recommendation = "Advanced Java Programming"
        reason = "Advanced programming skills can be strengthened through advanced Java concepts."

    # Rule 4
    elif interest == "Programming" and skill == "Beginner" and goal == "Data Analyst":
        recommendation = "Python for Data Analysis"
        reason = "Python provides a useful foundation for beginners interested in data analysis."

    # Rule 5
    elif interest == "Programming" and skill == "Intermediate" and goal == "Data Analyst":
        recommendation = "Python and SQL for Data Analysis"
        reason = "Python and SQL are useful skills for intermediate programmers moving into data analysis."

    # Rule 6
    elif interest == "Programming" and skill == "Advanced" and goal == "Data Analyst":
        recommendation = "Advanced Data Analytics"
        reason = "Advanced programming knowledge can support advanced data analytics."

    # Rule 7
    elif interest == "Web Development" and skill == "Beginner" and goal == "Web Developer":
        recommendation = "HTML, CSS and JavaScript"
        reason = "These are the fundamental technologies required to start web development."

    # Rule 8
    elif interest == "Web Development" and skill == "Intermediate" and goal == "Web Developer":
        recommendation = "Full Stack Web Development"
        reason = "Intermediate web skills are suitable for learning full-stack development."

    # Rule 9
    elif interest == "Web Development" and skill == "Advanced" and goal == "Web Developer":
        recommendation = "Advanced Full Stack Development"
        reason = "Advanced learners can improve their skills through advanced full-stack development."

    # Rule 10
    elif interest == "Web Development" and skill == "Beginner" and goal == "Software Developer":
        recommendation = "Frontend Web Development"
        reason = "Frontend development provides a good starting point for software development through web technologies."

    # Rule 11
    elif interest == "Web Development" and skill == "Intermediate" and goal == "Software Developer":
        recommendation = "Backend Web Development"
        reason = "Intermediate learners can build software development skills through backend technologies."

    # Rule 12
    elif interest == "Web Development" and skill == "Advanced" and goal == "Software Developer":
        recommendation = "Full Stack Development"
        reason = "Advanced web development skills can be extended into full-stack software development."

    # Rule 13
    elif interest == "Data Science" and skill == "Beginner" and goal == "Data Analyst":
        recommendation = "Python for Data Analysis"
        reason = "Python provides a useful foundation for beginners interested in data analysis."

    # Rule 14
    elif interest == "Data Science" and skill == "Intermediate" and goal == "Data Analyst":
        recommendation = "Data Science and Machine Learning"
        reason = "Intermediate data science learners can progress to machine learning and data science."

    # Rule 15
    elif interest == "Data Science" and skill == "Advanced" and goal == "Data Analyst":
        recommendation = "Advanced Data Science"
        reason = "Advanced learners can develop deeper data science and analytical skills."

    # Rule 16
    elif interest == "Data Science" and skill == "Beginner" and goal == "AI Engineer":
        recommendation = "Python and Statistics"
        reason = "Python and statistics provide a strong foundation for beginners moving toward AI."

    # Rule 17
    elif interest == "Data Science" and skill == "Intermediate" and goal == "AI Engineer":
        recommendation = "Machine Learning"
        reason = "Machine learning is a suitable next step for intermediate data science learners."

    # Rule 18
    elif interest == "Data Science" and skill == "Advanced" and goal == "AI Engineer":
        recommendation = "Deep Learning"
        reason = "Advanced data science skills provide a suitable foundation for deep learning."

    # Rule 19
    elif interest == "Artificial Intelligence" and skill == "Beginner" and goal == "AI Engineer":
        recommendation = "Introduction to Artificial Intelligence"
        reason = "This provides the basic concepts needed to start learning AI."

    # Rule 20
    elif interest == "Artificial Intelligence" and skill == "Intermediate" and goal == "AI Engineer":
        recommendation = "Machine Learning"
        reason = "Machine learning is a suitable next step for an intermediate AI learner."

    # Rule 21
    elif interest == "Artificial Intelligence" and skill == "Advanced" and goal == "AI Engineer":
        recommendation = "Deep Learning and Neural Networks"
        reason = "Advanced AI learners can progress to deep learning and neural network concepts."

    # Rule 22
    elif interest == "Artificial Intelligence" and skill == "Beginner" and goal == "Software Developer":
        recommendation = "Python Programming"
        reason = "Python provides a strong programming foundation for beginners interested in AI and software development."

    # Rule 23
    elif interest == "Artificial Intelligence" and skill == "Intermediate" and goal == "Software Developer":
        recommendation = "Machine Learning with Python"
        reason = "Intermediate learners can combine software development with machine learning skills."

    # Rule 24
    elif interest == "Artificial Intelligence" and skill == "Advanced" and goal == "Software Developer":
        recommendation = "AI Application Development"
        reason = "Advanced learners can apply AI concepts to software application development."

    # Rule 25
    elif interest == "Cybersecurity" and skill == "Beginner" and goal == "Cybersecurity Professional":
        recommendation = "Cybersecurity Fundamentals"
        reason = "Fundamentals provide the basic knowledge required for cybersecurity."

    # Rule 26
    elif interest == "Cybersecurity" and skill == "Intermediate" and goal == "Cybersecurity Professional":
        recommendation = "Ethical Hacking"
        reason = "Intermediate cybersecurity learners can develop practical ethical hacking skills."

    # Rule 27
    elif interest == "Cybersecurity" and skill == "Advanced" and goal == "Cybersecurity Professional":
        recommendation = "Advanced Network Security"
        reason = "Advanced learners can develop deeper knowledge of network security."

    # Rule 28
    elif interest == "Cybersecurity" and skill == "Beginner" and goal == "Software Developer":
        recommendation = "Computer and Network Security"
        reason = "Basic security knowledge is useful for software developers."

    # Rule 29
    elif interest == "Cybersecurity" and skill == "Intermediate" and goal == "Software Developer":
        recommendation = "Secure Software Development"
        reason = "Intermediate developers can learn how to build more secure software."

    # Rule 30
    elif interest == "Cybersecurity" and skill == "Advanced" and goal == "Software Developer":
        recommendation = "Application Security"
        reason = "Advanced learners can develop application security skills for software development."

    # -----------------------------
    # GENERAL FALLBACK
    # -----------------------------
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
    st.write("30 IF-THEN Rules")

st.caption(
    "Course Recommendation Expert System | AI Mini Project"
)