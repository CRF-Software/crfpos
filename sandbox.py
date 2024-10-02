import streamlit as st
from datetime import datetime
from streamlit_drawable_canvas import st_canvas
import sqlite3

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

# Set the page title and layout
st.set_page_config(page_title="CRF POS System with On-Screen Keyboard", layout="centered")

# HTML & JavaScript for on-screen keyboard
keyboard_html = """
    <input id="roomNumberInput" name="room_number" type="text" onfocus="showKeyboard()" placeholder="Enter room number" style="width: 100%; padding: 10px; font-size: 16px;">
    <div id="keyboard" style="display:none; padding-top: 20px;">
        <div>
            <button onclick="typeCharacter('1')">1</button>
            <button onclick="typeCharacter('2')">2</button>
            <button onclick="typeCharacter('3')">3</button>
            <button onclick="typeCharacter('4')">4</button>
            <button onclick="typeCharacter('5')">5</button>
            <button onclick="typeCharacter('6')">6</button>
            <button onclick="typeCharacter('7')">7</button>
            <button onclick="typeCharacter('8')">8</button>
            <button onclick="typeCharacter('9')">9</button>
            <button onclick="typeCharacter('0')">0</button>
            <button onclick="clearInput()">Clear</button>
        </div>
    </div>
    <script>
        function showKeyboard() {
            document.getElementById('keyboard').style.display = 'block';
        }
        
        function typeCharacter(char) {
            var inputField = document.getElementById('roomNumberInput');
            inputField.value += char;
        }

        function clearInput() {
            document.getElementById('roomNumberInput').value = '';
        }
    </script>
"""

# Display the keyboard section using Streamlit's `components.html`
st.markdown("### Room Number Input (with On-Screen Keyboard)")
st.components.v1.html(keyboard_html, height=300)

# Create the rest of the form for meal type and quantity
with st.form(key='pos_form'):
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
        room_number = st.session_state.get('room_number', None)
        if room_number and quantity:
            # Insert the order into the SQLite database
            insert_order(room_number, meal_type, quantity)
            st.success(f"Order Submitted Successfully!\nRoom Number: {room_number}\nMeal Type: {meal_type}\nQuantity: {quantity}")
        else:
            st.error("Please fill in all required fields.")
