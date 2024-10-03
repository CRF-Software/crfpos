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
    # Add other languages here...
}

# Add a dropdown to select the language
selected_language = st.selectbox("Select Language", options=list(translations.keys()))

# Get the appropriate translation
t = translations[selected_language]

# Function to simulate an on-screen keyboard
def create_keyboard():
    keys = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'SPACE', 'BACKSPACE']
    ]
    
    keyboard_input = st.empty()
    user_input = []
    
    for row in keys:
        cols = st.columns(len(row))
        for i, key in enumerate(row):
            if key == "SPACE":
                if cols[i].button(" "):
                    user_input.append(" ")
            elif key == "BACKSPACE":
                if cols[i].button("⌫"):
                    if user_input:
                        user_input.pop()
            else:
                if cols[i].button(key):
                    user_input.append(key)
    
    return ''.join(user_input)

# Create a form for the First Name, Last Name, Room Number, and Quantity
with st.form(key='pos_form'):
    st.subheader(t['first_name'])
    first_name = create_keyboard()

    st.subheader(t['last_name'])
    last_name = create_keyboard()

    st.subheader(t['room_number'])
    room_number = create_keyboard()

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

            # Reload the page to reset the form
            st.experimental_rerun()
        else:
            st.error(t['required_fields'])

# Test the canvas output (signature)
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)
