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
    section[data-testid="stSidebar"] .stSelectbox label {
        color: #94A3B8 !important;
        font-weight: 600;
    }

    /* 6. METRIC CARD CONTAINERS */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 12px !important;
        padding: 16px 20px !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03) !important;
    }
    div[data-testid="stMetricLabel"] {
        font-size: 0.85rem !important;
        font-weight: 700 !important;
        color: #64748B !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
    }
    div[data-testid="stMetricValue"] {
        font-size: 1.8rem !important;
        font-weight: 800 !important;
        color: #0F172A !important;
    }

    /* 7. CUSTOM BUTTONS */
    .stButton>button {
        border-radius: 8px !important;
        font-weight: 600 !important;
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.6rem 1.2rem !important;
        box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.2) !important;
        transition: all 0.2s ease-in-out !important;
    }
    .stButton>button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 12px -2px rgba(37, 99, 235, 0.3) !important;
    }

    /* 8. BADGES & PILLS */
    .badge-active {
        background-color: #D1FAE5 !important;
        color: #065F46 !important;
        padding: 4px 10px !important;
        border-radius: 12px !important;
        font-size: 0.82rem !important;
        font-weight: 700 !important;
    }
    .badge-dev {
        background-color: #FEF3C7 !important;
        color: #92400E !important;
        padding: 4px 10px !important;
        border-radius: 12px !important;
        font-size: 0.82rem !important;
        font-weight: 700 !important;
    }

    /* 9. HEADERS */
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        color: #0F172A;
        letter-spacing: -0.5px;
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
