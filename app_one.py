# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 09:51:
import streamlit as st

# Page config
st.set_page_config(
    page_title="Profile",
    layout="centered"
)

# Vertical spacing
st.markdown("<br><br><br>", unsafe_allow_html=True)

# Profile card with contact details
st.markdown(
    """
    <div style="
        background-color: #f9f9f9;
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        max-width: 600px;
        margin: auto;
    ">
        <h1> Hi, I'm Tshishonga Charles</h1>
        <h3 style="color: blue;">Welcome to my profile</h3>

        <hr style="margin: 30px 0;">

        <h4>📬 Contact Details</h4>

        <p><strong>Email:</strong> vhulendacharles32@gmail.com</p>
        <p><strong>Phone:</strong> +27 66 427 4152</p>
    </div>
    """,
    unsafe_allow_html=True
)



















