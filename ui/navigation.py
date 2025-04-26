from streamlit_option_menu import option_menu


def handle_menu_selection():
    """Handles the navigation panel and its customization"""
    # Default is "vertical", For Horizontal menu
    return option_menu(
        menu_title=None,
        options=["Sign-in", "Appointment", "Help & Support"],
        icons=["person-plus", "house", "info"],
        menu_icon=None,
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#D1D2DC"},
            "icon": {"color": "#F40643", "font-size": "22px"},
            "nav-link": {
                "font-size": "20px",
                "text-align": "left",
                "margin": "0.3px",
                "--hover-color": "#B1FBF5",
                "color": "black",
                "border": "1px solid black",
                "outline": "None",
                "padding": "3px",
            },
            "nav-link-selected": {
                "background-color": "#014132",
                "color": "#FFFFFF",
                "border": "1px solid black",
                "outline": "none",
                "padding": "3px",
            },
            "nav-bar": {
                "width": "100px",
                "background-color": "light green",
                "border": "1px solid #014132",
            },
        }
    )
