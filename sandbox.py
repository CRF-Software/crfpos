import streamlit as st
from datetime import datetime
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

# Function to create an on-screen keyboard
def create_keyboard(keyboard_input):
    keys = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'SPACE', 'BACKSPACE']
    ]

    for row in keys:
        key_row = st.container()
        cols = key_row.columns(len(row))
        for i, key in enumerate(row):
            if key == "SPACE":
                cols[i].button(" ", on_click=lambda: keyboard_input.append(" "))
            elif key == "BACKSPACE":
                cols[i].button("⌫", on_click=lambda: keyboard_input.pop() if keyboard_input else None)
            else:
                cols[i].button(key, on_click=lambda k=key: keyboard_input.append(k))

# Store the keyboard input
first_name_input = []
last_name_input = []
room_number_input = []

# Create a form for the First Name, Last Name, Room Number, and Quantity
with st.form(key='pos_form'):
    st.subheader("First Name")
    create_keyboard(first_name_input)
    first_name = ''.join(first_name_input)
    st.write(f"Typed First Name: {first_name}")

    st.subheader("Last Name")
    create_keyboard(last_name_input)
    last_name = ''.join(last_name_input)
    st.write(f"Typed Last Name: {last_name}")

    st.subheader("Room Number")
    create_keyboard(room_number_input)
    room_number = ''.join(room_number_input)
    st.write(f"Typed Room Number: {room_number}")

    # Automatically select Breakfast, Lunch, or Dinner based on the time of day
    current_hour = datetime.now().hour
    if current_hour < 11:
        meal_type = "Breakfast"
    elif current_hour < 17:
        meal_type = "Lunch"
    else:
        meal_type = "Dinner"

    st.subheader(f"Meal Type (Auto-selected): {meal_type}")

    st.subheader("Quantity")
    quantity = st.number_input("Enter quantity", min_value=1, max_value=10)

    # Submit button
    submit_button = st.form_submit_button(label="Submit Order")

    if submit_button:
        if first_name and last_name and room_number and quantity:
            st.success(f"Order Submitted Successfully for {first_name} {last_name}!\nRoom Number: {room_number}\nMeal Type: {meal_type}\nQuantity: {quantity}")
            
            # Simulate a thank you page for 5 seconds
            with st.spinner('Thank you for your order! Redirecting...'):
                time.sleep(5)

            # Reload the page to reset the form
            st.experimental_rerun()
        else:
            st.error("Please fill in all required fields.")
