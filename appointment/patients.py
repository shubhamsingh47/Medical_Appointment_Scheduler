import streamlit as st
from database.appointment_operations import (
    time_slot_availability,
    book_appointment,
    reschedule_appointment,
    check_existing_appointment
)
from authentication import signup_and_login
import datetime


def patients_dashboard():
    """This function gives out patient dashboard"""
    st.write(f"*Welcome, {st.session_state.user_id[2]}..* :sparkles:")
    # Setting up two tabs for booking and rescheduling separately for better user experience
    Booking_tab, Reschedule_tab = st.tabs(["Book Appointment", "Reschedule Appointment"])

    with Booking_tab:
        st.subheader("Book an appointment for an in-clinic consultation..")
        st.text_input("Enter the patient name", placeholder="Enter patients full name here",
                      key="Booking_name_key")
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        appointment_date = st.date_input("Enter the Appointment date", min_value=tomorrow,
                                         key='Booking_date_key')
        appointment_time = st.selectbox("Enter the Appointment time",
                                        options=['12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00',
                                                 '15:30', '16:00', '16:30', '17:00', '17:30', '18:00'],
                                        key="Booking_time_key")
        Appointment_button = st.button("Book Appointment")

        if Appointment_button:  # Functioning Book appointment button
            if check_existing_appointment(st.session_state.user_id):
                st.error("You already have an appointment, To reschedule go to 'Reschedule Appointment' Tab.")
            else:
                if time_slot_availability(appointment_date=appointment_date, appointment_time=appointment_time):
                    book_appointment(st.session_state.user_id[0], appointment_date, appointment_time)
                    st.success(f"Successfully booked appointment  on {appointment_date} at {appointment_time}")
                else:
                    st.error(f"The time slot on {appointment_date} at {appointment_time} is already booked")

        if st.session_state.logged_in:
            if st.button("Logout", key="appointment_logout_button"):
                signup_and_login.handle_logout()
                st.rerun()

    with Reschedule_tab:
        st.subheader("Reschedule your Appointment Here..")
        st.text_input("Enter the patient name", placeholder="Enter patients full name here",
                      key="Reschedule_name_key")
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        reschedule_appointment_date = st.date_input("Enter new Appointment Date", min_value=tomorrow,
                                                    key='Reschedule_date_key')
        reschedule_appointment_time = st.selectbox("Enter new Appointment Time",
                                                   options=['12:00', '12:30', '13:00', '13:30', '14:00',
                                                            '14:30', '15:00',
                                                            '15:30', '16:00', '16:30', '17:00', '17:30',
                                                            '18:00'], key='Reschedule_time_key')
        Reschedule_Button = st.button("Reschedule Appointment")

        if Reschedule_Button:  # Functioning Appointment Rescheduling button
            if time_slot_availability(appointment_date=reschedule_appointment_date,
                                      appointment_time=reschedule_appointment_time):
                # noinspection PyUnresolvedReferences
                reschedule_appointment(st.session_state.user_id[0], reschedule_appointment_date,
                                       reschedule_appointment_time)
                st.success(
                    f"Great news! We've rescheduled your appointment to {reschedule_appointment_date}, at {reschedule_appointment_time} PM.  See you then!")
            else:
                st.error(
                    f"Uh-oh! {reschedule_appointment_date} at {reschedule_appointment_time} is booked. Let's find another slot for you!")

        if st.session_state.logged_in:
            if st.button("Logout", key="reschedule_logout_button"):
                signup_and_login.handle_logout()
                st.rerun()
