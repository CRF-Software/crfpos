import sqlite3
import streamlit as st
from datetime import datetime

# Set up database connection
def init_db():
    conn = sqlite3.connect('bruckner.db')
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        room_number TEXT,
                        meal_type TEXT,
                        quantity INTEGER,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                      )''')
    conn.commit()
    return conn, cursor

# Insert data into the database
def insert_order(room_number, meal_type, quantity):
    conn, cursor = init_db()
    cursor.execute('''INSERT INTO orders (room_number, meal_type, quantity)
                      VALUES (?, ?, ?)''', (room_number, meal_type, quantity))
    conn.commit()
    conn.close()

# Set page title and layout
st.set_page_config(page_title="CRF POS System", layout="centered")

# Main POS form
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

    # Submit button
    submit_button = st.form_submit_button(label="Submit Order")

    if submit_button:
        if room_number and quantity:
            # Insert the order into the SQLite database
            insert_order(room_number, meal_type, quantity)
            st.success(f"Order Submitted Successfully!\nRoom Number: {room_number}\nMeal Type: {meal_type}\nQuantity: {quantity}")
        else:
            st.error("Please fill in all required fields.")
