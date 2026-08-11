import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
    /* 1. IMPORT GOOGLE MODERN FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }

    /* 2. HIDE FOOTER & MAIN MENU ONLY */
    footer {visibility: hidden !important;}
    #MainMenu {visibility: hidden !important;}
    .stDeployButton {display: none !important;}

    /* 3. TOP PADDING FIX FOR HEADER TEXT */
    .block-container {
        padding-top: 4.5rem !important;
        padding-bottom: 2rem !important;
        max-width: 95% !important;
    }

    /* 4. MAIN BACKGROUND */
    .stApp {
        background-color: #F8FAFC !important;
    }

    /* 5. CLEAN LIGHT EXECUTIVE SIDEBAR (MATCHES LOGO PALETTE) */
    section[data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E2E8F0 !important;
    }
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] .stMarkdown p {
        color: #0F172A !important;
    }
    section[data-testid="stSidebar"] .stCaption {
        color: #64748B !important;
    }
    section[data-testid="stSidebar"] hr {
        border-color: #E2E8F0 !important;
        margin: 1rem 0 !important;
    }

    /* 6. SIDEBAR ROLE SWITCHER SELECTBOX */
    section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
        background-color: #F8FAFC !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 8px !important;
    }
    section[data-testid="stSidebar"] div[data-baseweb="select"] span {
        color: #0F172A !important;
        font-weight: 600 !important;
    }
    section[data-testid="stSidebar"] label {
        color: #334155 !important;
        font-weight: 600 !important;
    }

    /* 7. NAVIGATION RADIO MENU ITEMS */
    section[data-testid="stSidebar"] div[role="radiogroup"] label {
        background-color: transparent !important;
        padding: 8px 12px !important;
        border-radius: 8px !important;
        transition: all 0.2s ease-in-out !important;
        margin-bottom: 2px !important;
    }
    section[data-testid="stSidebar"] div[role="radiogroup"] label * {
        color: #334155 !important;
        font-weight: 500 !important;
    }
    section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
        background-color: #F1F5F9 !important;
    }
    /* Active Selected Page Pill */
    section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {
        background-color: #EFF6FF !important;
        border-left: 4px solid #1E3A8A !important;
    }
    section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] * {
        color: #1E3A8A !important;
        font-weight: 700 !important;
    }

    /* 8. MAIN CONTENT INPUT FIELDS & SELECTBOXES */
    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div,
    div[data-testid="stNumberInput"] input,
    div[data-testid="stTextInput"] input,
    input {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }

    div[data-testid="stNumberInput"] button {
        background-color: #F1F5F9 !important;
        color: #0F172A !important;
        border: 1px solid #CBD5E1 !important;
    }

    /* Dropdown Options Popover Menu */
    div[data-baseweb="popover"] {
        background-color: #FFFFFF !important;
        border-radius: 8px !important;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1) !important;
    }
    div[data-baseweb="popover"] * {
        color: #0F172A !important;
        background-color: #FFFFFF !important;
    }
    div[data-baseweb="popover"] li[role="option"]:hover {
        background-color: #EFF6FF !important;
    }

    /* 9. METRIC CARDS */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 12px !important;
        padding: 16px 20px !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05) !important;
    }
    div[data-testid="stMetricLabel"] {
        font-size: 0.85rem !important;
        font-weight: 700 !important;
        color: #64748B !important;
        text-transform: uppercase !important;
    }
    div[data-testid="stMetricValue"] {
        font-size: 1.8rem !important;
        font-weight: 800 !important;
        color: #0F172A !important;
    }

    /* 10. BUTTONS */
    .stButton>button {
        border-radius: 8px !important;
        font-weight: 600 !important;
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.6rem 1.2rem !important;
    }

    /* 11. HEADERS */
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        color: #0F172A;
        margin-bottom: 0rem;
        line-height: 1.2;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #475569;
        margin-bottom: 1.2rem;
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)
