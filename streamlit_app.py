import streamlit as st

pages = [
    st.Page("about.py", title="About Me"),
    st.Page("skill.py", title="My Skillset"),
    st.Page("exp.py", title="My Experiences")
]

pg = st.navigation(pages)
pg.run()

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)
