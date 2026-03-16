import streamlit as st
import urllib.parse
import base64
import qrcode

st.set_page_config(page_title="Thee Best Archaar In Town", layout="centered")

# ---------- BACKGROUND ----------
def set_bg(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    page_bg = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """

    st.markdown(page_bg, unsafe_allow_html=True)

set_bg("background.jpg")

# ---------- LOGO ----------
st.image("logo.png", width=220)

# ---------- TITLE ----------
st.title("🥭 Thee Best Archaar In Town")
st.subheader("Fresh • Spicy • Homemade")

st.image("archaar.jpg", caption="Our Delicious Archaar")

# ---------- PRODUCTS ----------
products = {
    "90ML": 8,
    "250ML": 18,
    "350ML": 25,
    "500ML": 30,
    "1L": 50
}

st.header("Customer Details")

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
        qty = st.number_input(f"Qty {item}", min_value=0, step=1, key=item)

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

# ---------- QR CODE ----------
st.divider()
st.header("📱 Scan to Order on WhatsApp")

qr = qrcode.make("https://wa.me/27664274152")

st.image(qr, caption="Scan this QR code to order on WhatsApp")

# ---------- REVIEWS ----------
st.divider()
st.header("⭐ Customer Reviews")

st.write("⭐⭐⭐⭐⭐ 'Best archaar I've tasted!'")
st.write("⭐⭐⭐⭐⭐ 'Amazing flavour!'")
st.write("⭐⭐⭐⭐⭐ 'Definitely buying again!'")

st.divider()
st.write("📞 WhatsApp Orders: 066 427 4152")










































