import streamlit as st
import mysql.connector as connection
from config import AppConfig
from database.user_operations import create_new_user, check_mobile_number_exists, user_authentication


def handle_logout():
    """This function handles the logout"""
    st.session_state.logged_in = False
    st.session_state.user_id = None
    st.session_state.is_doctor = False
    st.success("You have successfully logged out.")


def handle_signup_and_login_flow():
    """ Handles the user signup and login process."""
    signup_tab, login_tab = st.tabs(['SignUp', 'Login'])

    # Set up signup tab
    with signup_tab:
        Mobile_Number = st.number_input("Enter your Phone Number", max_value=9999999999,
                                        format='%i', placeholder="Enter your 10 digits number",
                                        key='signup_mobile_key')
        Name = st.text_input("Enter your Name", key='signup_name_key', placeholder="Enter your full name")
        Password = st.text_input("Enter your password", type='password', key='signup_password_key',
                                 placeholder="Enter your password")
        Sign_up_button = st.button('Sign Up', key='signup_button_key')

        if Sign_up_button:
            if Mobile_Number and len(str(Mobile_Number)) and Name and Password:
                try:
                    create_new_user(Mobile_Number, Name, Password)
                    st.success("Account created successfully! Go to Login Page.")
                except connection.IntegrityError:
                    st.error('Phone Number already exists! Go to Login Page.')
            else:
                if len(str(Mobile_Number)) != 10:
                    st.warning("Phone number must be of 10 digits.")
                else:
                    st.warning("Please provide all the details.")

    # Set up login tab
    with login_tab:
        Mobile_Number = st.number_input("Enter your Phone Number", max_value=9999999999,
                                        format='%i', placeholder="Enter your 10 digits number",
                                        key='login_mobile_key')
        # Name = st.text_input("Enter your Name", key='login_name_key')
        Password = st.text_input("Enter your password", type='password', key='login_password_key',
                                 placeholder="Enter your password")
        Login_button = st.button('Log In', key='login_button_key')

        if Login_button:
            if Mobile_Number and Password:
                if check_mobile_number_exists(Mobile_Number):
                    user_id = user_authentication(Mobile_Number, Password)
                    if user_id:
                        st.session_state.logged_in = True
                        st.session_state.user_id = user_id
                        st.session_state.is_doctor = (Mobile_Number == AppConfig.DOCTOR_MOBILE_NUMBER)
                        st.success(f"Welcome, Successfully logged in!! ")
                    else:
                        st.error("Invalid Credentials")
                else:
                    st.error("Oops! It looks like you don't have an account. Please sign up to create a new one.")
            else:
                st.warning("Please provide all the details")

        if st.session_state.logged_in:
            if st.button("Logout", key="signin_logout_button"):
                handle_logout()
