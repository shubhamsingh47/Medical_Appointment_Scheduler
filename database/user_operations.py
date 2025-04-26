from database.connection import create_connection, create_database


def create_user_table():
    create_database()
    conn = create_connection('Medical_Scheduler')
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS user_table')
    c.execute('''CREATE TABLE IF NOT EXISTS user_table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Mobile_Number VARCHAR(15) UNIQUE NOT NULL,
        Name VARCHAR(100) NOT NULL,
        Password VARCHAR(100) NOT NULL)''')
    conn.commit()
    conn.close()


def create_new_user(Mobile_Number, Name, Password):
    conn = create_connection('Medical_Scheduler')
    c = conn.cursor()
    c.execute('INSERT INTO user_table (Mobile_Number, Name, Password) VALUES (%s, %s, %s)',
              (Mobile_Number, Name, Password))
    conn.commit()
    conn.close()
    print(f"Data inserted: {Mobile_Number}, {Name}, {Password}")


def check_mobile_number_exists(mobile_number):
    conn = create_connection('Medical_Scheduler')
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM user_table WHERE Mobile_Number = %s', (mobile_number,))
    count = c.fetchone()[0]
    conn.close()
    return count > 0


def user_authentication(Mobile_Number, Password):
    conn = create_connection('Medical_Scheduler')
    c = conn.cursor()
    c.execute('SELECT * FROM user_table WHERE Mobile_Number = %s AND Password = %s',
              (Mobile_Number, Password))
    user_match = c.fetchone()
    conn.close()
    return user_match
