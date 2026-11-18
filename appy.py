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
