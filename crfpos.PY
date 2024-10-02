import streamlit as st
from datetime import datetime
from streamlit_drawable_canvas import st_canvas

# Set the page title and layout
st.set_page_config(page_title="Simple POS System", layout="centered")

# Styling for the header
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
    .sub-title {
        font-size: 22px;
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Display the main title and logo
st.markdown('<div class="main-title">Simple POS System</div>', unsafe_allow_html=True)

# Create a form for the Room Number and Quantity
with st.form(key='pos_form'):
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
        if room_number and quantity:
            st.success(f"Room Number: {room_number}\nMeal Type: {meal_type}\nQuantity: {quantity}\nOrder Submitted Successfully!")
        else:
            st.error("Please fill in all required fields.")

# Test the canvas output
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)
