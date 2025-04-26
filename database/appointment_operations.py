from database.connection import create_connection, create_database


def create_appointment_table():
    create_database()
    conn = create_connection('Medical_Scheduler')
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS appointments')
    c.execute('''CREATE TABLE IF NOT EXISTS appointments (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id Integer,
        appointment_date TEXT NOT NULL,
        appointment_time TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES user_table(id))''')
    conn.commit()
    conn.close()


def time_slot_availability(appointment_date, appointment_time):
    create_database()
    conn = create_connection('Medical_Scheduler')
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM appointments WHERE appointment_date = %s AND appointment_time = %s',
              (appointment_date, appointment_time))
    count = c.fetchone()[0]
    conn.close()
    return count == 0


def check_existing_appointment(user_id):
    conn = create_connection('Medical_Scheduler')
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM appointments WHERE user_id = %s', (user_id[0],))
    count = c.fetchone()[0]
    conn.close()
    return count > 0


def book_appointment(user_id, appointment_date, appointment_time):
    conn = create_connection('Medical_Scheduler')
    c = conn.cursor()
    c.execute('INSERT INTO appointments (user_id, appointment_date, appointment_time) VALUES (%s, %s, %s)',
              (user_id, appointment_date, appointment_time))
    conn.commit()
    conn.close()
    print(f"Data successfully inserted: {user_id}, {appointment_date}, {appointment_time}")


def reschedule_appointment(user_id, new_appointment_date, new_appointment_time):
    conn = create_connection('Medical_Scheduler')
    c = conn.cursor()
    c.execute('UPDATE appointments SET appointment_date = %s, appointment_time = %s WHERE user_id = %s',
              (new_appointment_date, new_appointment_time, user_id))
    conn.commit()
    conn.close()
    print(f"Appointment successfully rescheduled: {user_id}, {new_appointment_date}, {new_appointment_time}")
