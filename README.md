# Medical Scheduler with end-to-end modular coding

## Overview
Medical Scheduler is a lightweight yet powerful application designed to simplify appointment management for a doctor and their patients.
#### The project targets single-practice clinics, private doctors, or specialists needing a simple yet effective system to manage patient flow without large hospital systems.
Built with Python (Streamlit) and backed by a MySQL database, it offers a scalable base for real-world production or expansion.

# Problem Statement
In a busy clinic or private practice:

* Managing patient schedules manually is error-prone and tedious.

* Patients face difficulty booking or rescheduling their slots without continuous staff support.

* Doctors lose valuable consultation time handling appointments.

❗ There is a need for a simple, secure, and automated way to manage appointments between a doctor and patients.

# ⚙️ Core Features
👨‍⚕️ Doctor Dashboard – View and manage upcoming patient appointments

👤 Patient Account Creation – Quick sign-up with mobile number and password

📅 Appointment Scheduling – Book available time slots seamlessly

🔄 Appointment Rescheduling – Modify scheduled slots with ease

🔒 Secure Login – Authentication for both doctor and patients

🧭 Smooth Navigation – Easy-to-use horizontal menu

🆘 Help & Support Section – Built-in guidance and contact info

# 🛠️ Tech Stack
Frontend (UI): Streamlit (Python)

Backend Services: Python (Modular Architecture)

Database: MySQL (Localhost / Cloud Ready)

Deployment Ready: Streamlit Sharing

# 🔒 Security Notes
* All passwords are stored as plain text for simplicity in local development. In production, passwords must be hashed (e.g., bcrypt hashing).

* Doctor access is restricted based on a specific mobile number (config.py)

# 🌟 Future Enhancements 
* Adding email verification for sign-up.

* Adding multi-doctor support.

* Enable appointment cancellation with reason.

* Build notifications (email/SMS reminders) for upcoming appointments.

* Add admin panel for superuser control.

* Feature to reset and change passwords.