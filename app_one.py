import streamlit as st
import urllib.parse
import base64

st.set_page_config(page_title="Thee Best Archaar In Town")

# Upload background image
bg_image = st.file_uploader("Upload Background Picture", type=["png","jpg","jpeg"])

if bg_image is not None:
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

st.title("🥭 Thee Best Archaar In Town")
st.subheader("Fresh, Spicy & Delicious Archaar!")

st.write("Select the size you want and add it to your cart.")

# Products
products = {
    "90ML": 8,
    "250ML": 18,
    "350ML": 25,
    "500ML": 30,
    "1L": 50
}

# Cart
if "cart" not in st.session_state:
    st.session_state.cart = []

st.header("Menu")

for item, price in products.items():
    col1, col2 = st.columns([3,1])

    with col1:
        st.write(f"**{item}** - R{price}")

    with col2:
        if st.button(f"Add {item}", key=item):
            st.session_state.cart.append((item, price))
            st.success(f"{item} added!")

st.divider()

st.header("🛒 Cart")

total = 0
order_text = "Hello, I would like to order:\n"

for item, price in st.session_state.cart:
    st.write(f"{item} - R{price}")
    order_text += f"- {item} (R{price})\n"
    total += price

st.write(f"**Total: R{total}**")

order_text += f"\nTotal: R{total}"

encoded_text = urllib.parse.quote(order_text)
whatsapp_link = f"https://wa.me/27664274152?text={encoded_text}"

if st.button("📲 Order on WhatsApp"):
    st.markdown(f"[Click here to place your order]({whatsapp_link})")










































