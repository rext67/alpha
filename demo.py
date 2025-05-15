from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# MySQL config (you will update with your credentials)
db_config = {
    'host': 'localhost',
    'user': 'your_mysql_user',
    'password': 'your_mysql_password',
    'database': 'clinic_db'
}

def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

@app.route('/')
def index():
    return "Clinic Appointment API running"

# Example route to add appointment
@app.route('/appointments', methods=['POST'])
def add_appointment():
    data = request.json
    patient_name = data.get('patient_name')
    doctor_name = data.get('doctor_name')
    date = data.get('date')
    time = data.get('time')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "INSERT INTO appointments (patient_name, doctor_name, date, time) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (patient_name, doctor_name, date, time))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Appointment added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)


