import streamlit as st


def handle_help_and_support():
    st.subheader(
        "For urgent medical consultations, please contact doctor at +91-9876543210 ")  # Change contact number accordingly
    st.subheader('Frequently asked questions: ')
    FAQs = {
        "How do I create an account?": "To create an account, go to the 'Sign-in' section, and Sign-up if you don't have an account else enter required credentials, then Login using those credentials",
        "How do I book an appointment?": "To book an appointment, go to the 'SignIn' section, and SignUp if you don't have an account else enter required credentials, and login, then click on 'Appointment' section and After providing the required details then click on 'Book Appointment'.",
        "Can I reschedule my appointment?": "Yes, you can reschedule your appointment by going to the 'Appointments' section and selecting 'Reschedule Appointment' tab.",
        "What should I do if I forgot my password?": "If you forgot your password, unfortunately right now there is no method to reset it, we are working on it until then you can create New account."}
    for question, answer in FAQs.items():
        with st.expander(question):
            st.write(answer)
