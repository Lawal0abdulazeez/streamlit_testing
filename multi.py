import streamlit as st

def main():
    st.title("Streamlit Multi-Page App")

    # Sidebar navigation
    page = st.sidebar.selectbox("Select Page", ["Home", "About", "Contact"])

    # Display content based on the selected page
    if page == "Home":
        home_page()
    elif page == "About":
        about_page()
    elif page == "Contact":
        contact_page()

def home_page():
    st.header("Home Page")
    st.write("Welcome to the home page!")

def about_page():
    st.header("About Page")
    st.write("This is the about page. Learn more about us.")

def contact_page():
    st.header("Contact Page")
    st.write("Contact us here. Fill out the form.")

if __name__ == "__main__":
    main()
