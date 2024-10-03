import streamlit as st
from datetime import datetime
from streamlit_drawable_canvas import st_canvas
import time

# Set the page title and layout
st.set_page_config(page_title="Bruckner Meals :)", layout="centered")

# CSS Styling for title and logo
st.markdown("""
    <style>
    .main-title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #000000;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .logo {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 300px;
        padding-bottom: 20px;
    }
    .sub-title {
        font-size: 22px;
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Display the image in the header
logo_url = "https://th.bing.com/th/id/R.534a3a010f905e2340131ca622c63e27?rik=3gNqUzH%2bfZvtfw&pid=ImgRaw&r=0"
st.markdown(f'<img src="{logo_url}" class="logo">', unsafe_allow_html=True)

# Display the main title and logo
st.markdown('<div class="main-title">Bruckner Meals :)</div>', unsafe_allow_html=True)

# Dictionary for translations of common languages
translations = {
    'English': {
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'room_number': 'Room Number',
        'meal_type': 'Meal Type',
        'quantity': 'Quantity',
        'sign_here': 'Sign Here',
        'submit': 'Submit Order',
        'order_success': 'Order Submitted Successfully for',
        'thank_you': 'Thank you for your order! Redirecting...',
        'required_fields': 'Please fill in all required fields.',
    },
    'Spanish': {
        'first_name': 'Nombre',
        'last_name': 'Apellido',
        'room_number': 'Número de habitación',
        'meal_type': 'Tipo de comida',
        'quantity': 'Cantidad',
        'sign_here': 'Firma aquí',
        'submit': 'Enviar pedido',
        'order_success': 'Pedido enviado con éxito para',
        'thank_you': '¡Gracias por su pedido! Redirigiendo...',
        'required_fields': 'Por favor complete todos los campos requeridos.',
    },
    'French': {
        'first_name': 'Prénom',
        'last_name': 'Nom de famille',
        'room_number': 'Numéro de chambre',
        'meal_type': 'Type de repas',
        'quantity': 'Quantité',
        'sign_here': 'Signez ici',
        'submit': 'Soumettre la commande',
        'order_success': 'Commande soumise avec succès pour',
        'thank_you': 'Merci pour votre commande! Redirection...',
        'required_fields': 'Veuillez remplir tous les champs requis.',
    },
    'Chinese': {
        'first_name': '名字',
        'last_name': '姓',
        'room_number': '房间号',
        'meal_type': '餐种类',
        'quantity': '数量',
        'sign_here': '在此签名',
        'submit': '提交订单',
        'order_success': '订单成功提交',
        'thank_you': '感谢您的订单！正在重定向...',
        'required_fields': '请填写所有必填字段。',
    },
    'Arabic': {
        'first_name': 'الاسم الأول',
        'last_name': 'اسم العائلة',
        'room_number': 'رقم الغرفة',
        'meal_type': 'نوع الوجبة',
        'quantity': 'كمية',
        'sign_here': 'وقع هنا',
        'submit': 'إرسال الطلب',
        'order_success': 'تم تقديم الطلب بنجاح لـ',
        'thank_you': 'شكرا لطلبك! جاري إعادة التوجيه...',
        'required_fields': 'يرجى ملء جميع الحقول المطلوبة.',
    },
    'Hindi': {
        'first_name': 'पहला नाम',
        'last_name': 'अंतिम नाम',
        'room_number': 'कमरा संख्या',
        'meal_type': 'भोजन प्रकार',
        'quantity': 'मात्रा',
        'sign_here': 'यहां हस्ताक्षर करें',
        'submit': 'ऑर्डर सबमिट करें',
        'order_success': 'सफलतापूर्वक ऑर्डर सबमिट किया गया',
        'thank_you': 'आपके ऑर्डर के लिए धन्यवाद! पुनः निर्देशित कर रहे हैं...',
        'required_fields': 'कृपया सभी आवश्यक क्षेत्रों को भरें।',
    },
    'Portuguese': {
        'first_name': 'Primeiro Nome',
        'last_name': 'Sobrenome',
        'room_number': 'Número do quarto',
        'meal_type': 'Tipo de refeição',
        'quantity': 'Quantidade',
        'sign_here': 'Assine aqui',
        'submit': 'Enviar Pedido',
        'order_success': 'Pedido enviado com sucesso para',
        'thank_you': 'Obrigado pelo seu pedido! Redirecionando...',
        'required_fields': 'Por favor, preencha todos os campos obrigatórios.',
    },
    'Russian': {
        'first_name': 'Имя',
        'last_name': 'Фамилия',
        'room_number': 'Номер комнаты',
        'meal_type': 'Тип еды',
        'quantity': 'Количество',
        'sign_here': 'Подпишите здесь',
        'submit': 'Отправить заказ',
        'order_success': 'Заказ успешно отправлен для',
        'thank_you': 'Спасибо за ваш заказ! Перенаправление...',
        'required_fields': 'Пожалуйста, заполните все обязательные поля.',
    },
    'Japanese': {
        'first_name': '名',
        'last_name': '姓',
        'room_number': '部屋番号',
        'meal_type': '食事の種類',
        'quantity': '量',
        'sign_here': 'ここにサインしてください',
        'submit': '注文を送信する',
        'order_success': '注文が正常に送信されました',
        'thank_you': 'ご注文ありがとうございました！リダイレクトしています...',
        'required_fields': 'すべての必須フィールドに入力してください。',
    },
    'German': {
        'first_name': 'Vorname',
        'last_name': 'Nachname',
        'room_number': 'Zimmernummer',
        'meal_type': 'Mahlzeittype',
        'quantity': 'Menge',
        'sign_here': 'Hier unterschreiben',
        'submit': 'Bestellung abschicken',
        'order_success': 'Bestellung erfolgreich aufgegeben für',
        'thank_you': 'Vielen Dank für Ihre Bestellung! Umleiten...',
        'required_fields': 'Bitte füllen Sie alle erforderlichen Felder aus.',
    }
}

# Add a dropdown to select the language
selected_language = st.selectbox("Select Language", options=list(translations.keys()))

# Get the appropriate translation
t = translations[selected_language]

# Create a form for the First Name, Last Name, Room Number, and Quantity
with st.form(key='pos_form'):
    st.subheader(t['first_name'])
    first_name = st.text_input(t['first_name'], placeholder=t['first_name'], max_chars=20)
    
    st.subheader(t['last_name'])
    last_name = st.text_input(t['last_name'], placeholder=t['last_name'], max_chars=20)

    st.subheader(t['room_number'])
    room_number = st.text_input(t['room_number'], placeholder=t['room_number'], max_chars=5)

    # Automatically select Breakfast, Lunch, or Dinner based on the time of day
    current_hour = datetime.now().hour
    if current_hour < 11:
        meal_type = "Breakfast"
    elif current_hour < 17:
        meal_type = "Lunch"
    else:
        meal_type = "Dinner"

    st.subheader(f"{t['meal_type']} (Auto-selected): {meal_type}")

    st.subheader(t['quantity'])
    quantity = st.number_input(t['quantity'], min_value=1, max_value=10)

    st.subheader(t['sign_here'])
    canvas_result = st_canvas(
        stroke_width=2,
        stroke_color="#000000",
        background_color="#ffffff",
        height=200,
        width=400,
        drawing_mode="freedraw",
        key="canvas",
    )

    # Submit button
    submit_button = st.form_submit_button(label=t['submit'])

    if submit_button:
        if first_name and last_name and room_number and quantity:
            st.success(f"{t['order_success']} {first_name} {last_name}!\n{t['room_number']}: {room_number}\n{t['meal_type']}: {meal_type}\n{t['quantity']}: {quantity}")
            
            # Simulate a thank you page for 5 seconds
            with st.spinner(t['thank_you']):
                time.sleep(5)

