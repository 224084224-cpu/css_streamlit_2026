

import streamlit as st

# Page config
st.set_page_config(page_title="Profile", layout="centered")

# Vertical spacing
st.write("")
st.write("")

tabs = st.tabs(["Profile", "Education", "Contact", "Skills"])

# Card container
with tabs[0]:        
        st.subheader(" Hi, I'm Charles Tshishonga")
        st.markdown(":blue[Welcome to my profile🎓]")
    
        st.divider()
with tabs[1]:
        st.subheader("Education")
        st.write("**School📕:** Edison Nesengani Secondary")
        st.write("**Instituition🏛:** Vaal University Of Technology")
        st.write("**Department:** Engineering and Technology")
    
with tabs[2]:
        st.subheader("Contact details")
        st.write("**Email address🖨:** vhulendacharles32@gmail.com")
        st.write("**Contact details📲:** +27 66 427 4152")
        st.write("**Instagram**: @Kadosh1644")

with tabs[3]:
        st.subheader("Other Skills")
        st.write("Python")
        st.write("C++")


































