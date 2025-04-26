import streamlit as st
from ui import navigation
from authentication import signup_and_login
from Support_and_help import help_and_support
from appointment import doctor
from appointment import patients


def setup_session_state():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'user_id' not in st.session_state:
        st.session_state.user_id = None
    if 'is_doctor' not in st.session_state:
        st.session_state.is_doctor = False


def main():
    st.title('Medical Appointment Scheduler')
    setup_session_state()

    selected = navigation.handle_menu_selection()

    if selected == "Sign-in":
        signup_and_login.handle_signup_and_login_flow()

    elif selected == "Appointment":
        if st.session_state.logged_in:
            if st.session_state.is_doctor:
                doctor.doctor_dashboard()
            else:
                patients.patients_dashboard()
        else:
            st.error("Please log in to access the dashboard!")

    elif selected == "Help & Support":
        help_and_support.handle_help_and_support()


if __name__ == "__main__":
    main()
