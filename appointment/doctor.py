import mysql.connector as connection
import streamlit as st
import pandas as pd
from database.connection import create_connection


def doctor_dashboard():
    """This function gives out the doctor dashboard """""
    st.write(f"*Welcome, Dr. {st.session_state.user_id[2]}..* :sparkles:")
    st.subheader("Information on All Patients Appointments")
    # Fetch patients info from the db
    query = """ select ut.Name,ap.appointment_date,ap.appointment_time
                        from user_table ut
                        join appointments ap
                        on ut.id = ap.user_id"""
    # Creating db connection to fetch real time data
    conn = create_connection('Medical_Scheduler')
    c = conn.cursor()
    try:
        c.execute(query)
        results = c.fetchall()
        if results:
            patients_info = pd.DataFrame(results,
                                         columns=['Patient Name', 'Appointment Date', 'Appointment Time'])
            patients_info.reset_index(drop=True, inplace=True)
            patients_info.index += 1
            st.dataframe(patients_info)
        else:
            st.warning("No patient appointment found")
    except connection.Error as error:
        st.error(f"Error fetching data {error}")
    finally:
        c.close()
        conn.close()
