import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
    /* 1. IMPORT GOOGLE MODERN FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }

    /* 2. HIDE STREAMLIT DEFAULT CHROME & FOOTER */
    header {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    #MainMenu {visibility: hidden !important;}
    .stDeployButton {display: none !important;}
    div[data-testid="stDecoration"] {display: none !important;}
    div[data-testid="stToolbar"] {visibility: hidden !important;}

    /* 3. OPTIMIZE MAIN CONTAINER PADDING */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 2rem !important;
        max-width: 95% !important;
    }

    /* 4. MAIN APPLICATION BACKGROUND */
    .stApp {
        background-color: #F8FAFC !important;
    }

    /* 5. EXECUTIVE DARK SIDEBAR STYLING */
    section[data-testid="stSidebar"] {
        background-color: #0F172A !important;
        border-right: 1px solid #1E293B !important;
    }
    section[data-testid="stSidebar"] * {
        color: #F8FAFC !important;
    }

    /* 6. BASEWEB DROPDOWN & SELECTBOX TEXT FIX */
    /* Sidebar Selectbox Container */
    section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
        background-color: #1E293B !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
    }
    section[data-testid="stSidebar"] div[data-baseweb="select"] span {
        color: #F8FAFC !important;
    }

    /* Main Content Area Selectbox Container */
    div[data-testid="stMain"] div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 8px !important;
    }
    div[data-testid="stMain"] div[data-baseweb="select"] span {
        color: #0F172A !important;
    }

    /* Dropdown Options Popover Menu (Fixes Invisible Text) */
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
    div[data-baseweb="popover"] li[aria-selected="true"] {
        background-color: #DBEAFE !important;
        font-weight: 600 !important;
    }

    /* 7. METRIC CARD CONTAINERS */
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

    /* 8. BUTTONS */
    .stButton>button {
        border-radius: 8px !important;
        font-weight: 600 !important;
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.6rem 1.2rem !important;
    }

    /* 9. HEADERS */
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        color: #0F172A;
        margin-bottom: 0rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #475569;
        margin-bottom: 1.2rem;
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)
