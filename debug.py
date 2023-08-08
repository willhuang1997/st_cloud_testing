import streamlit as st


if "logged_in" not in st.session_state:
    form = st.form(key="my_form")

    form.subheader("Login")

    user = form.text_input("Username")
    password = form.text_input("Password", type="password", autocomplete="new-password")

    if form.form_submit_button("Login"):
        # Check if username and password are correct

        st.session_state["user"] = user
        st.session_state["password"] = password
        st.session_state["logged_in"] = True
        st.experimental_rerun()


else:
    st.subheader("Logged in")
    st.write("You are logged in.")

    st.write("username:", st.session_state["user"])
    st.write("password:", st.session_state["password"])

    if st.button("Logout"):
        del st.session_state["logged_in"]
        st.experimental_rerun()
