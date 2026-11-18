
import streamlit as st
import urllib.parse
from pathlib import Path

st.set_page_config(
    page_title="The Best Student Hub",
    
)

WHATSAPP = "27664274152"

CATEGORIES = [
    "The Best Archaar In Town",
    "Cables and Chargers",
    "TB Students Storage",
    "Research and Online Tests Assistance",
    "Graphic Design",
    "Engineering Drawing Equipments"
]

def photo(filename, caption=None):
    path = Path(__file__).parent / filename
    if path.is_file():
        st.image(str(path), use_container_width=True)
    else:
        st.info("Product image coming soon")
    if caption:
        st.caption(caption)

def order_button(label, message):
    encoded = urllib.parse.quote(message)
    url = f"https://wa.me/{WHATSAPP}?text={encoded}"
    st.link_button(label, url, type="primary")

st.title("🎓 The Best Student Hub")
st.markdown("### Your Student Marketplace")
st.write("Affordable products, student services and convenient WhatsApp enquiries.")


st.markdown("## Explore Our Services")

colors = [
    "#F59A23",
    "#17BCC7",
    "#F21E73",
    "#7533B2",
    "#2474D4",
    "#159B78"
]

icons = ["🌶️", "🔌", "📦", "📚", "🎨", "📐"]

for row in range(0, len(CATEGORIES), 2):
    columns = st.columns(2, gap="large")

    for j, col in enumerate(columns):
        i = row + j

        if i < len(CATEGORIES):
            with col:
                st.markdown(
                    f"""
                    <div style="
                        background:{colors[i]};
                        color:white;
                        padding:30px;
                        border-radius:15px;
                        min-height:160px;
                        margin-bottom:8px;
                    ">
                        <div style="font-size:18px;">
                            {i+1:02d} OPTIONS
                        </div>
                        <h3 style="color:white;">
                            {CATEGORIES[i]}
                        </h3>
                        <div style="font-size:35px;">
                            {icons[i]}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if st.button(
                    f"Explore {CATEGORIES[i]}",
                    key=f"category_{i}",
                    use_container_width=True
                ):
                    st.session_state["section"] = CATEGORIES[i]
                    st.rerun()



section = st.session_state.get('section', CATEGORIES[0])
st.divider()

if section == CATEGORIES[0]:
    st.header('🌶️ The Best Archaar In Town')
    a,b=st.columns([1,1.25],gap='large')
    with a: photo('archaar.jpg','Product poster · Orders use +27 66 427 4152 only')
    with b:
        st.markdown('### Retail sizes')
        retail={'90 ml':8.0,'250 ml':18.0,'350 ml':25.0,'500 ml':30.0,'1 L':50.0,'2 L':100.0}
        bulk={'10 L':270.67,'20 L':520.40}
        st.table([{'Size':k,'Price':f'R{v:,.2f}'} for k,v in retail.items()])
        st.markdown('### Commercial Bulk Buy')
        st.table([{'Size':k,'Price':f'R{v:,.2f}'} for k,v in bulk.items()])
        tier=st.radio('Choose order type',['Retail','Commercial Bulk Buy'],horizontal=True)
        options=retail if tier=='Retail' else bulk
        size=st.selectbox('Choose size',list(options))
        qty=st.number_input('Quantity',min_value=1,max_value=1000,value=1,step=1)
        total=options[size]*qty
        st.metric('Estimated product total',f'R{total:,.2f}')
        order_button('Enquire / Order on WhatsApp',f'Hello The Best Student Hub! I would like to order Archaar.\nType: {tier}\nSize: {size}\nQuantity: {qty}\nProduct total: R{total:,.2f}\nPlease confirm availability, collection/delivery and payment.')

elif section == CATEGORIES[1]:
    st.header('🔌 Cables and Chargers')
    st.caption('Select your cable. Stock and specifications will be confirmed on WhatsApp.')
    products=[('Type C to C Cable',55,'cable_usb_c.jpg'),('USB to iPhone Cable',60,'cable_lightning.jpg'),('Type C to iPhone Cable',70,'charger.jpg')]
    cols=st.columns(3)
    for col,(name,price,img) in zip(cols,products):
        with col:
            photo(img)
            st.subheader(name)
            st.markdown(f'**R{price:.2f}**')
    names={name:price for name,price,_ in products}
    choice=st.selectbox('Choose a product',list(names))
    qty=st.number_input('Quantity',min_value=1,max_value=1000,value=1,step=1)
    total=names[choice]*qty
    st.metric('Estimated product total',f'R{total:,.2f}')
    order_button('Order on WhatsApp',f'Hello The Best Student Hub! Is this available?\nProduct: {choice}\nQuantity: {qty}\nProduct total: R{total:,.2f}\nPlease confirm stock and collection/delivery.')

elif section == CATEGORIES[2]:
    st.header('📦 TB Students Storage')
    st.markdown('### SAFE. SECURE. AFFORDABLE.')
    a,b=st.columns([1,1.25],gap='large')
    with a: photo('storage_logo.png','TB Students Storage')
    with b: photo('storage_poster.jpg','We collect · We store · We return. See current prices below.')
    st.info('📅 Storage period: November 2026 to February 2027  |  📍 Bedworth Park and S.E.7')
    packages={'Package 1 — 1–2 Plastics':250,'Package 2 — 1–4 Plastics':300,'Package 3 — 4–7 Plastics':400,'Package 4 — Plastics + Fridge & Microwave':500}
    st.table([{'Package':name,'Price':f'R{price:.2f}'} for name,price in packages.items()])
    with st.form('storage_form'):
        package=st.selectbox('Choose a package',list(packages))
        location=st.selectbox('Preferred area',['Bedworth Park','S.E.7'])
        name=st.text_input('Your name')
        extra=st.text_area('Items or collection details (optional)')
        submitted=st.form_submit_button('Prepare storage enquiry')
    if submitted:
        if not name.strip(): st.warning('Please enter your name.')
        else:
            msg=f'Hello TB Students Storage!\nName: {name}\nPackage: {package}\nPrice: R{packages[package]:.2f}\nPreferred area: {location}\nStorage period: November 2026–February 2027\nDetails: {extra or "Please advise"}\nPlease confirm availability and collection arrangements.'
            order_button('Send storage enquiry on WhatsApp',msg)

elif section == CATEGORIES[3]:
    st.header('📚 Research and Online Tests Assistance')
    st.caption('Tutoring, revision, guided practice, research support and help developing your own work.')
    rates={'ICT Skills 1 Assistance':60,'ICT Skills 1 Reassessment':70,'Advanced ICT Assistance':80,'Advanced ICT Assistance Reassessment':90,'Computing Applications Tests Assistance':100,'Computing Applications Assignments Support':250}
    st.table([{'Service':name,'Listed price':f'R{price:.2f}'} for name,price in rates.items()]+[{'Service':'General Research Assistance','Listed price':'Request a Quote'}])
    st.markdown('### Academic support highlights')
    c1,c2=st.columns(2)
    with c1: photo('ict_word.jpg','Example supplied assessment screenshot')
    with c2: photo('ict_excel.jpg','Example supplied assessment screenshot')
    st.caption('These are examples from supplied screenshots, not a guarantee of marks or outcomes.')
    with st.form('academic_form'):
        service=st.selectbox('Choose assistance',list(rates)+['General Research Assistance'])
        module=st.text_input('Subject / module / research topic')
        description=st.text_area('What guidance or preparation do you need?')
        deadline=st.date_input('Preferred date',value=None)
        submitted=st.form_submit_button('Prepare academic support enquiry')
    if submitted:
        if not module.strip() or not description.strip(): st.warning('Please enter the topic and your requirements.')
        else:
            price=f'R{rates[service]:.2f}' if service in rates else 'Quotation requested'
            msg=f'Hello The Best Student Hub!\nService: {service}\nListed price: {price}\nSubject/topic: {module}\nAssistance requested: {description}\nPreferred date: {deadline or "Flexible"}\nPlease confirm availability.'
            order_button('Enquire on WhatsApp',msg)

elif section == CATEGORIES[4]:
    st.header('🎨 Graphic Design')
    st.markdown('### Tell us what you want to create')
    st.caption('Enter your budget and the design you have in mind. We will confirm the quote on WhatsApp.')
    with st.form('design_form'):
        design=st.selectbox('Type of design',['Event Poster','Business Advertisement','Church Poster','Birthday Poster','Flyer','Logo Design','Other Custom Design'])
        budget=st.number_input('Your budget (R)',min_value=1.0,value=100.0,step=10.0)
        description=st.text_area('Describe the colours, text, theme, size and style')
        deadline=st.date_input('Preferred delivery date',value=None)
        submitted=st.form_submit_button('Prepare design enquiry')
    if submitted:
        if not description.strip(): st.warning('Please describe your design.')
        else:
            msg=f'Hello The Best Student Hub! I need a graphic design.\nDesign type: {design}\nMy budget: R{budget:.2f}\nDescription: {description}\nPreferred date: {deadline or "Flexible"}\nPlease confirm a quotation.'
            order_button('Request design on WhatsApp',msg)

elif section == CATEGORIES[5]:
    st.header('📐 Engineering Drawing Equipments')
    st.caption('Available for purchase subject to stock confirmation. Please enquire for prices.')
    c1,c2,c3=st.columns(3)
    with c1: photo('drawing_set.jpg','Drawing instruments')
    with c2: photo('drawing_pencils.jpg','Mechanical pencils')
    with c3: photo('drawing_template.jpg','Drawing template')
    with st.form('drawing_form'):
        product=st.selectbox('What are you looking for?',['Drawing Boards Full Sets (New & Pre-Owned)','Drawing Equipments'])
        condition=st.selectbox('Preferred condition',['Either','New','Pre-owned']) if product.startswith('Drawing Boards') else 'Not specified'
        details=st.text_area('Specific item or equipment (optional)')
        submitted=st.form_submit_button('Prepare availability enquiry')
    if submitted:
        msg=f'Hello The Best Student Hub! Is this available for purchase?\nProduct: {product}\nCondition: {condition}\nDetails: {details or "Please advise what is in stock"}\nPlease confirm availability and price.'
        order_button('Check availability on WhatsApp',msg)

st.divider()
st.markdown('### 💬 Need help choosing?')
order_button('Contact The Best Student Hub','Hello The Best Student Hub! I would like to enquire about your services.')
st.caption('© 2026 The Best Student Hub · WhatsApp: +27 66 427 4152 · Enquiries are not confirmed orders or bookings.')
