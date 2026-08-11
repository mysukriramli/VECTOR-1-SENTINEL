import streamlit as st
from components.embed_generator import generate_iframe_snippet

def render_embed_portal_page():
    st.subheader("🔌 Inter-Agency Widget & Embed Generator")
    snippet = generate_iframe_snippet()
    st.code(snippet, language="html")