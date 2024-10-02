import streamlit as st
from datetime import datetime
from streamlit_drawable_canvas import st_canvas
import time

# Set the page title and layout
st.set_page_config(page_title="Simple POS System", layout="centered")

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
st.markdown('<div class="main-title">Simple POS System</div>', unsafe_allow_html=True)

# Create a form for the First Name, Last Name, Room Number, and Quantity
with st.form(key='pos_form'):
    st.subheader("First Name")
    first_name = st.text_input("Enter first name", placeholder="First name", max_chars=20)
    
    st.subheader("Last Name")
    last_name = st.text_input("Enter last name", placeholder="Last name", max_chars=20)

    st.subheader("Room Number")
    room_number = st.text_input("Enter room number", placeholder="Room number", max_chars=5)

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

    st.subheader("Sign Here:")
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
    submit_button = st.form_submit_button(label="Submit Order")

    if submit_button:
        if first_name and last_name and room_number and quantity:
            st.success(f"Order Submitted Successfully for {first_name} {last_name}!\nRoom Number: {room_number}\nMeal Type: {meal_type}\nQuantity: {quantity}")
            
            # Simulate a thank you page for 5 seconds
            with st.spinner('Thank you for your order! Redirecting...'):
                time.sleep(5)

            # Use st.experimental_set_query_params to refresh the form
            st.experimental_set_query_params()

        else:
            st.error("Please fill in all required fields.")

# Test the canvas output
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)
