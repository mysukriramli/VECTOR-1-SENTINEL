import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
    /* 1. TYPOGRAPHY & SMOOTH SCROLLING */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
        scroll-behavior: smooth !important;
    }

    /* 2. MAIN APP BACKGROUND (CLEAN & BRIGHT) */
    .main .block-container {
        padding-top: 2.0rem !important;
        padding-bottom: 2.5rem !important;
        max-width: 96% !important;
    }

    .stApp {
        background-color: #F8FAFC !important;
        background-image: 
            radial-gradient(at 0% 0%, rgba(37, 99, 235, 0.04) 0px, transparent 40%),
            radial-gradient(at 100% 100%, rgba(14, 165, 233, 0.04) 0px, transparent 40%),
            linear-gradient(to right, rgba(226, 232, 240, 0.4) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(226, 232, 240, 0.4) 1px, transparent 1px) !important;
        background-size: 100% 100%, 100% 100%, 30px 30px, 30px 30px !important;
    }

    /* 3. HIDE DEFAULT STREAMLIT ELEMENTS */
    footer {visibility: hidden !important;}
    #MainMenu {visibility: hidden !important;}
    .stDeployButton {display: none !important;}
    header {background-color: transparent !important;}

    /* 4. DYNAMIC TIER BADGES (LIGHT THEME ONLY) */
    .tier-badge-public {
        background: #ECFDF5; border: 1px solid #A7F3D0; color: #065F46;
        padding: 8px 14px; border-radius: 8px; font-size: 0.85rem; font-weight: 700; margin-bottom: 1rem;
    }
    .tier-badge-gov {
        background: #EFF6FF; border: 1px solid #BFDBFE; color: #1E3A8A;
        padding: 8px 14px; border-radius: 8px; font-size: 0.85rem; font-weight: 700; margin-bottom: 1rem;
    }
    .tier-badge-admin {
        background: #FEF2F2; border: 1px solid #FECACA; color: #991B1B;
        padding: 8px 14px; border-radius: 8px; font-size: 0.85rem; font-weight: 700; margin-bottom: 1rem;
    }

    /* 5. METRIC CARDS (ELEVATION & SHADOW) */
    div[data-testid="stMetric"] {
        background: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 12px !important;
        padding: 18px 20px !important;
        box-shadow: 0 4px 10px rgba(15, 23, 42, 0.03) !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-4px) !important;
        border-color: #93C5FD !important;
        box-shadow: 0 12px 24px rgba(37, 99, 235, 0.1) !important;
    }
    div[data-testid="stMetricLabel"] {
        font-size: 0.85rem !important; font-weight: 700 !important; color: #64748B !important; text-transform: uppercase !important;
    }
    div[data-testid="stMetricValue"] {
        font-size: 2.0rem !important; font-weight: 800 !important; color: #0F172A !important;
    }

    /* 6. SIDEBAR LIGHT STYLING */
    section[data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E2E8F0 !important;
    }
    section[data-testid="stSidebar"] * {
        color: #0F172A !important;
    }
    section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {
        background-color: #EFF6FF !important;
        border-left: 4px solid #2563EB !important;
    }

    /* 7. QUICK LAUNCH BUTTONS */
    .stButton>button {
        border-radius: 10px !important;
        font-weight: 700 !important;
        background: #FFFFFF !important;
        color: #1E3A8A !important;
        border: 1px solid #CBD5E1 !important;
        padding: 0.7rem 1.4rem !important;
        width: 100% !important;
        box-shadow: 0 2px 5px rgba(15, 23, 42, 0.02) !important;
        transition: all 0.2s ease !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 16px rgba(37, 99, 235, 0.1) !important;
        border-color: #2563EB !important;
        color: #2563EB !important;
    }
    </style>
    """, unsafe_allow_html=True)
