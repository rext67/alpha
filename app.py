from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

db_config = {
    'host': os.environ.get('MYSQL_HOST', 'localhost'),
    'user': os.environ.get('MYSQL_USER', 'your_mysql_user'),
    'password': os.environ.get('MYSQL_PASSWORD', 'your_mysql_password'),
    'database': os.environ.get('MYSQL_DATABASE', 'clinic_db')
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return "Clinic Appointment API running"

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
    