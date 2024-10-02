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

# Create a form for the Room Number first
with st.form(key='pos_form'):
    st.subheader("Room Number")
    room_number = st.text_input("Enter room number", placeholder="Room number", max_chars=5)

    submit_button = st.form_submit_button(label="Submit Room Number")

    if submit_button:
        if room_number:
            st.success(f"Room Number: {room_number} Submitted Successfully!")

            # Simulate a thank you page for 5 seconds
            with st.spinner('Thank you! Refreshing for the next user...'):
                time.sleep(5)

            # Refresh the page for the next user
            st.experimental_set_query_params()
        else:
            st.error("Please fill in the room number.")

