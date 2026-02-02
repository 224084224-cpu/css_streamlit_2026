import streamlit as st

# ---------------- Page Config ----------------
st.set_page_config(page_title="Charles | Profile", layout="centered")

# ---------------- Eye-catching Welcome ----------------
st.markdown(
    """
    <h1 style='text-align: center; color: #1f77b4;'>
        👋 Welcome to My Profile
    </h1>
    <h4 style='text-align: center;'>
        Charles Tshishonga | Engineering & Technology 🎓
    </h4>
    <hr>
    """,
    unsafe_allow_html=True
)

# ---------------- Create Tabs ----------------
tabs = st.tabs(["Profile", "Education", "Contact", "Skills"])

# ================= Profile Tab =================
with tabs[0]:
    st.subheader("👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Name:** Charles")
        st.write("**Surname:** Tshishonga")
        st.write("**Gender:** Male")
        st.write("**Race:** African")

    with col2:
        st.checkbox("Show extra info")
        st.success("📍 South Africa")
        st.info("🎯 Aspiring Engineer & Programmer")

# ================= Education Tab =================
with tabs[1]:
    st.subheader("🎓 Education")

    level = st.selectbox(
        "Select education level",
        ["High School", "University"]
    )

    st.write("**School 📕:** Edison Nesengani Secondary")
    st.write("**Institution 🏛:** Vaal University Of Technology")
    st.write("**Department:** Engineering and Technology")

# ================= Contact Tab =================
with tabs[2]:
    st.subheader("📞 Contact Details")

    preferred = st.radio(
        "Preferred contact method:",
        ["Email", "Phone", "Instagram"]
    )

    st.write("📧 vhulendacharles32@gmail.com")
    st.write("📲 +27 66 427 4152")
    st.write("📸 @Kadosh1644")

# ================= Skills Tab =================
with tabs[3]:
    st.subheader("🛠 Skills")

    skills = st.multiselect(
        "Select skills",
        ["Python 🐍", "C++ 💻", "Data Analysis 📊", "Problem Solving 🧠"]
    )

    st.write("### Selected Skills")
    st.write(skills)











































