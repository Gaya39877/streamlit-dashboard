import mysql.connector
import streamlit as st
import pandas as pd

# Establish connection
try:
    conn = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        passwd='',
        db='mydb'
    )
    c = conn.cursor()  # Define the cursor globally
except mysql.connector.Error as err:
    st.error(f"Error: {err}")
    conn = None
    c = None

# Function to fetch data
def view_all_data():
    if c:
        try:
            c.execute('SELECT * FROM insurance ORDER BY id ASC')
            data = c.fetchall()
            return data
        except mysql.connector.Error as err:
            st.error(f"Error fetching data: {err}")
            return []
    else:
        st.error("Database connection is not established.")
        return []

# Fetch data using the function
if conn and c:
    result = view_all_data()

    # Check if the result is not empty before converting to a DataFrame
    if result:
        df = pd.DataFrame(result, columns=['Policy', 'Expiry', 'Location', 'State', 'Premium'])
        # Proceed with using df in your Streamlit app
    else:
        st.error("No data retrieved from the database.")
else:
    st.error("Database connection could not be established.")
