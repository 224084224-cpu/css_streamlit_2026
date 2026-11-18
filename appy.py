
import streamlit as st
from urllib.parse import quote

st.set_page_config(
    page_title="The Best Student Hub",
    page_icon="🎓",
    layout="wide"
)

PHONE = "27664274152"

st.markdown("""
<style>
.stApp {
    background: #0b1020;
    color: white;
}
h1, h2, h3 {
    color: #ffffff !important;
}
.hero {
    padding: 65px 25px;
    text-align: center;
    background: linear-gradient(135deg, #172554, #581c87);
    border-radius: 22px;
    margin-bottom: 35px;
}
.hero h1 {
    font-size: 48px;
    font-weight: 800;
}
.hero p {
    font-size: 19px;
    color: #e2e8f0;
}
.service {
    background: #1e293b;
    padding: 24px;
    border-radius: 16px;
    min-height: 170px;
    border: 1px solid #334155;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🎓 THE BEST STUDENT HUB</h1>
    <p>Your Partner in Academic and Career Success</p>
    <p>Smart Support. Professional Results.</p>
</div>
""", unsafe_allow_html=True)

st.header("🚀 Our Services")

services = [
    ("📚", "Academic Support", "Tutoring, study guidance and research support."),
    ("📄", "CV Writing", "Professional CVs and cover letters."),
    ("📊", "Presentations", "Modern PowerPoint presentations."),
    ("🎨", "Graphic Design", "Posters, flyers and creative designs."),
    ("💻", "Excel Support", "Spreadsheets, formulas and dashboards."),
    ("📝", "Document Formatting", "Professional reports and formatting.")
]

for start in range(0, len(services), 3):
    cols = st.columns(3)
    for col, (emoji, name, desc) in zip(
        cols, services[start:start + 3]
    ):
        with col:
            st.markdown(
                f'<div class="service"><h3>{emoji} {name}</h3>'
                f'<p>{desc}</p></div>',
                unsafe_allow_html=True
            )

st.divider()
st.header("📲 Request a Service")

with st.form("order_form"):
    name = st.text_input("Your name")
    service = st.selectbox(
        "Choose a service",
        [item[1] for item in services]
    )
    details = st.text_area("Describe what you need")
    submitted = st.form_submit_button("Order via WhatsApp")

if submitted:
    if not name.strip() or not details.strip():
        st.warning("Please enter your name and requirements.")
    else:
        message = (
            f"Hello The Best Student Hub!\n"
            f"My name is {name}.\n"
            f"Service: {service}\n"
            f"Requirements: {details}"
        )
        url = f"https://wa.me/{PHONE}?text={quote(message)}"
        st.link_button("💬 Open WhatsApp", url)

st.divider()
st.header("🌟 About Us")
st.write(
    "The Best Student Hub helps students and job seekers "
    "with academic guidance, professional documents, "
    "digital skills and creative services."
)

st.caption("© 2026 The Best Student Hub. All rights reserved.")
