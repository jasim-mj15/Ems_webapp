from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'user': 'root',
    'password': 'password',
    'host': 'db',  # Use the service name from docker-compose.yml
    'database': 'employee_db'
}
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_employee', methods=['POST'])
def add_employee():
    name = request.form['name']
    email = request.form['email']
    department = request.form['department']
    conn = mysql.connector.connect(db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, email, department) VALUES (%s, %s, %s)", (name, email, department))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/employees')
def view_employees():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('employees.html', employees=employees)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
