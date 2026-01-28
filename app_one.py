# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 09:51:29 2026

@author: MUKWEVHO EVANCE
"""



import streamlit as st

# Page config
st.set_page_config(
    page_title="Profile",
    layout="centered"
)

# Vertical spacing
st.markdown("<br><br><br>", unsafe_allow_html=True)

# Rounded rectangle (card)
st.markdown(
    """
    <div style="
        background-color: #f9f9f9;
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
    ">
        <h1>👋 Hi, I'm Charles Tshishonga</h1>
        <h3 style="color: blue;">Welcome to my profile</h3>
    </div>
    """,
    unsafe_allow_html=True
)


















