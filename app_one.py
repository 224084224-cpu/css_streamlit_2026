


import streamlit as st

# Page config
st.set_page_config(page_title="Profile", layout="centered")

# Create tabs
tabs = st.tabs(["Profile", "Education", "Contact", "Skills"])

# ---------------- Profile Tab ----------------
with tabs[0]:
    col1, col2 = st.columns([3, 1])  # text wider than image

    with col1:
        st.subheader("Hi, I'm Charles Tshishonga 👋")
        st.markdown(":blue[Welcome to my profile 🎓]")

    with col2:
        st.image("profile.jpg", width=150)

    st.divider()

# ---------------- Education Tab ----------------
with tabs[1]:
    st.subheader("Education")
    st.write("**School 📕:** Edison Nesengani Secondary")
    st.write("**Institution 🏛:** Vaal University Of Technology")
    st.write("**Department:** Engineering and Technology")

# ---------------- Contact Tab ----------------
with tabs[2]:
    st.subheader("Contact details")
    st.write("**Email address 🖨:** vhulendacharles32@gmail.com")
    st.write("**Contact 📲:** +27 66 427 4152")
    st.write("**Instagram 📸:** @Kadosh1644")

# ---------------- Skills Tab ----------------
with tabs[3]:
    st.subheader("Other Skills")
    st.write("• Python 🐍")
    st.write("• C++ 💻")



































