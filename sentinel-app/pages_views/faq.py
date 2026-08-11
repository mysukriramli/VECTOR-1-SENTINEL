import streamlit as st
from mock_data import get_faq_items

def render_faq_page():
    st.subheader("❓ Guidance & FAQ")
    for item in get_faq_items():
        with st.expander(item["q"]):
            st.write(item["a"])