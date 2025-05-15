create database alpha_clinic;
CREATE USER 'alpha_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON alpha_clinic.* TO 'alpha_user'@'localhost';
FLUSH PRIVILEGES;
USE alpha_clinic;

CREATE TABLE appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_name VARCHAR(100),
    doctor_name VARCHAR(100),
    appointment_date DATE,
    appointment_time TIME
);




