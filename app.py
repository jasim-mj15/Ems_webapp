import os
import mysql.connector
from flask import Flask, request, render_template
import time
from mysql.connector import Error, connect

app = Flask(__name__)
def get_db_connection():
    retries = 3
    delay = 5
    for i in range(retries):
        try:
            conn = connect(
                host=os.getenv('DB_HOST', 'mysql'),
                user=os.getenv('DB_USER', 'emsuser'),
                password=os.getenv('DB_PASSWORD', 'emsuser-password'),
                database=os.getenv('DB_NAME', 'employee_db'),
                auth_plugin='mysql_native_password'
            )
            return conn
        except Error as e:
            if i == retries - 1:
                raise
            time.sleep(delay)
# Retrieve the database config from environment variables
db_config = {
    "host": os.getenv('DB_HOST', 'mysql'),
    "user": os.getenv('DB_USER', 'emsuser'),
    "password": os.getenv('DB_PASSWORD', 'emsuser-password'),
    "database": os.getenv('DB_NAME', 'employee_db'),
    "use_pure": True,  # Try pure Python implementation
    "auth_plugin":'mysql_native_password'  # Force native authentication
}


@app.route('/')
def index():
    return render_template('index.html')  # Assuming you have an index.html template

@app.route('/add_employee', methods=['POST'])
def add_employee():
    name = request.form['name']
    email = request.form['email']
    department = request.form['department']
    # Connect to the MySQL database using the configuration
    conn = mysql.connector.connect(db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, email, department) VALUES (%s, %s, %s)", (name, email, department))
    conn.commit()
    cursor.close()
    conn.close()

    return 'Employee added successfully!'

if __name__ == '__main__':
    app.run(debug=True)
