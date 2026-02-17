import streamlit as st
import os

import streamlit as st

# Navigation to other pages (if you use multipage structure with `pages/`)
st.sidebar.title("Navigation")
st.sidebar.markdown("Choose a page from the left sidebar")


st.set_page_config(page_title="DiaWatch", layout="centered")

st.title("👋 Welcome to DiaWatch")

st.markdown("""
    DiaWatch helps you assess your diabetes risk using AI.  
    Just enter your health details and receive personalized results and lifestyle tips.

    ---
    ✅ AI-Powered  
    📖 Educational  
    🧠 Easy to Use
""")

st.image(
"pages/Articles_images/satellite-express-3455755_1280.jpg",   
 use_container_width=True,
    caption="Track your health with DiaWatch"
)


st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 0.9em;'>"
    "© 2025 DiaWatch | Built by Team XYZ | Educational use only."
    "</p>",
    unsafe_allow_html=True
)



