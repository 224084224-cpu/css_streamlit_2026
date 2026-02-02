


import streamlit as st

# Page config
st.set_page_config(page_title="Profile", layout="centered")

# Create tabs
tabs = st.tabs(["Profile", "Education", "Contact", "Skills"])

st.header("**Welcome to my profile**")

# ---------------- Profile Tab ----------------
with tabs[0]:
    
        st.write("**Name:** Charles")
        st.write("**Surname:** Tshishonga")
        st.write("**Gender:** Male")
        st.write("**Race:** African")
    


   



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







































