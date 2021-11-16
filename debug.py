import streamlit as st

user_input = st.text_input("Enter Movie Name")
st.info(user_input)

st.markdown(" ## Hamburger Menu Customization!")

st.write("Here is the new, original hamburger menu without customization in developer mode.")
st.image("original.png")
st.markdown("**As one can see, there is now a developer menu in grey in developer mode!**")

st.write("Here is the new, original hamburger menu without customization as a viewer.")
st.image("original_viewer.png")

st.write(" If one wants to show information about their app, one can do that through this feature!")
st.image("about.jpeg", "This is an example!")

st.code("""about_info = ''' ## My Custom App This app uses our ML model to demostrate churn prediction '''
menu_items = {'About': about_info}
st.set_page_config(menu_items=menu_items)""")

st.write("If one wants to change the link, one can do that through the 'Get help' or 'Report a bug' key")
st.code("""
get_help_link = https://support.google.com/googlenest/troubleshooter/7211062?hl=en
menu_items = {'Get help': get_help_link}
st.set_page_config(menu_items=menu_items) """)
