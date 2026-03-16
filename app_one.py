import streamlit as st
import urllib.parse
import base64

st.set_page_config(page_title="Thee Best Archaar In Town", layout="centered")

# ---------- BACKGROUND ----------
bg_image = st.file_uploader("Upload Background Picture", type=["png","jpg","jpeg"])

if bg_image:
    encoded = base64.b64encode(bg_image.read()).decode()
    page_bg = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

# ---------- LOGO ----------
logo = st.file_uploader("Upload Business Logo", type=["png","jpg","jpeg"])

if logo:
    st.image(logo, width=200)

# ---------- TITLE ----------
st.title(" Thee Best Archaar In Town")
st.subheader("Fresh • Spicy • Homemade")

st.write("Place your order below and it will send directly to WhatsApp.")

# ---------- PRODUCTS ----------
products = {
    "90ML": 8,
    "250ML": 18,
    "350ML": 25,
    "500ML": 30,
    "1L": 50
}

# ---------- CUSTOMER INFO ----------
customer_name = st.text_input("Your Name")

st.header("Menu")

cart = []
total = 0

for item, price in products.items():

    col1, col2, col3 = st.columns([3,2,2])

    with col1:
        st.write(f"**{item}**")

    with col2:
        st.write(f"R{price}")

    with col3:
        qty = st.number_input(
            f"Qty {item}",
            min_value=0,
            step=1,
            key=item
        )

        if qty > 0:
            cart.append((item, price, qty))
            total += price * qty

st.divider()

st.header("🛒 Order Summary")

order_text = f"Hello, my name is {customer_name}. I would like to order:\n\n"

for item, price, qty in cart:
    st.write(f"{item} x{qty} = R{price*qty}")
    order_text += f"{item} x{qty} - R{price*qty}\n"

st.write(f"### Total: R{total}")

order_text += f"\nTotal: R{total}"

# ---------- WHATSAPP ----------
encoded = urllib.parse.quote(order_text)
whatsapp_url = f"https://wa.me/27664274152?text={encoded}"

if st.button("📲 Send Order to WhatsApp"):
    st.markdown(f"[Click here to send order]({whatsapp_url})")










































