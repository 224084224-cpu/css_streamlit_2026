import streamlit as st
import urllib.parse

# ---------- INSERT YOUR ONLINE IMAGE URLs HERE ----------
BACKGROUND_URL = "https://i.imgur.com/YOUR_BACKGROUND_IMAGE.jpg"
LOGO_URL       = "https://i.imgur.com/YOUR_LOGO_IMAGE.png"
ARCHAAR_URL    = "https://i.imgur.com/YOUR_ARCHAAR_IMAGE.jpg"

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Thee Best Archaar In Town", layout="centered")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
body, .stApp {
    font-family: 'Helvetica', 'Arial', sans-serif;
}
h1, h2, h3, h4 {
    color: #1E90FF;
    font-weight: bold;
}
.stButton>button {
    background-color: #1E90FF;
    color: white;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------- BACKGROUND ----------
st.markdown(f"""
<style>
.stApp {{
    background-image: url("{BACKGROUND_URL}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}
</style>
""", unsafe_allow_html=True)

# ---------- LOGO ----------
st.image(LOGO_URL, width=220)

# ---------- TITLE ----------
st.title("🥭 Thee Best Archaar In Town")
st.subheader("Fresh • Spicy • Affordable")

# ---------- ARCHAAAR IMAGE ----------
st.image(ARCHAAR_URL, caption="Our Delicious Archaar")

# ---------- PRODUCTS ----------
products = {
    "90ML": 8,
    "250ML": 18,
    "350ML": 25,
    "500ML": 30,
    "1L": 50
}

# ---------- CUSTOMER DETAILS ----------
st.header("Customer Details")
customer_name = st.text_input("Your Name")
location = st.selectbox("Delivery Area", ["Vanderbijlpark", "Bedworth Park", "Other"])

# ---------- MENU ----------
st.header("Menu")
cart = []
total = 0
for item, price in products.items():
    col1, col2, col3 = st.columns([3,2,2])
    with col1: st.write(f"**{item}**")
    with col2: st.write(f"R{price}")
    with col3:
        qty = st.number_input(f"Qty {item}", min_value=0, step=1, key=item)
        if qty > 0:
            cart.append((item, price, qty))
            total += price * qty

st.divider()

# ---------- ORDER SUMMARY ----------
st.header("🛒 Order Summary")
order_text = f"Hello, my name is {customer_name}. I am in {location}.\n\nI would like to order:\n\n"
for item, price, qty in cart:
    st.write(f"{item} x{qty} = R{price*qty}")
    order_text += f"{item} x{qty} - R{price*qty}\n"
st.write(f"### Total: R{total}")
order_text += f"\nTotal: R{total}"

# ---------- WHATSAPP ORDER ----------
encoded = urllib.parse.quote(order_text)
whatsapp_url = f"https://wa.me/27664274152?text={encoded}"
if st.button("📲 Send Order to WhatsApp"):
    st.markdown(f"[Click here to send your order]({whatsapp_url})")

# ---------- QR CODE ----------
st.divider()
st.header("📱 Scan QR Code to Order")
qr_url = "https://api.qrserver.com/v1/create-qr-code/?size=220x220&data=https://wa.me/27664274152"
st.image(qr_url, caption="Scan to order on WhatsApp")

# ---------- REVIEWS ----------
st.divider()
st.header("⭐ Customer Reviews")
st.write("⭐⭐⭐⭐⭐ 'Best archaar I've tasted!' - Karabo")
st.write("⭐⭐⭐⭐⭐ 'Perfect spice and flavour!' - Thabo")
st.write("⭐⭐⭐⭐⭐ 'I order every week!' - Chantel")

# ---------- FOOTER ----------
st.divider()
st.write("📞 WhatsApp Orders: 066 427 4152")
st.write("📍 Serving Bedworth Park, Vanderbijlpark & surrounding areas")







































