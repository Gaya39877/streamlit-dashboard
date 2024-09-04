# import mysql.connector
# import streamlit as st

# try:
#     # Connection
#     conn = mysql.connector.connect(
#         host='localhost',
#         port='3306',
#         user='root',
#         passwd='',
#         db='mydb'
#     )
#     c = conn.cursor()

#     # fetch
#     def view_all_data():
#         c.execute('SELECT * FROM insurance ORDER BY id ASC')
#         data = c.fetchall()
#         return data

# except mysql.connector.Error as err:
#     st.error(f"Error: {err}")

import mysql.connector

# Function to fetch data
def view_all_data():
    try:
        # Connection
        conn = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            passwd='',
            db='mydb'
        )
        c = conn.cursor()

        # fetch
        c.execute('SELECT * FROM insurance ORDER BY id ASC')
        data = c.fetchall()
        return data

    except mysql.connector.Error as err:
        print(f"Error: {err}")


