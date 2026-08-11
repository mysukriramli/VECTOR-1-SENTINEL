import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
    /* 1. TYPOGRAPHY & SMOOTH SCROLLING */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
        scroll-behavior: smooth !important;
    }

    /* 2. MAIN APP BACKGROUND */
    .stApp {
        background-color: #F4F7F9 !important;
    }

    /* 3. HIDE STREAMLIT CHROME */
    footer {visibility: hidden !important;}
    #MainMenu {visibility: hidden !important;}
    .stDeployButton {display: none !important;}
    header[data-testid="stHeader"] {background: transparent !important;}

    /* 4. TIER DEFINITION CARDS */
    .tier-card {
        padding: 24px;
        border-radius: 16px;
        color: white;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
        margin-top: -20px;
        position: relative;
        z-index: 10;
        backdrop-filter: blur(10px);
    }
    .tier-public { background: linear-gradient(135deg, #10B981 0%, #047857 100%); }
    .tier-gov { background: linear-gradient(135deg, #2563EB 0%, #1E3A8A 100%); }
    .tier-admin { background: linear-gradient(135deg, #EF4444 0%, #991B1B 100%); }
    
    .tier-title {
        font-size: 1.4rem;
        font-weight: 800;
        margin-bottom: 8px;
        letter-spacing: -0.5px;
    }
    .tier-desc {
        font-size: 0.95rem;
        font-weight: 400;
        opacity: 0.9;
        line-height: 1.5;
    }

    /* 5. METRIC CARDS */
    div[data-testid="stMetric"] {
        background: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 12px !important;
        padding: 16px 20px !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03) !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease !important;
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-4px) !important;
        box-shadow: 0 12px 20px -3px rgba(37, 99, 235, 0.1) !important;
        border-color: #BFDBFE !important;
    }
    div[data-testid="stMetricValue"] { color: #0F172A !important; font-weight: 800 !important; }
    div[data-testid="stMetricLabel"] { color: #64748B !important; font-weight: 700 !important; text-transform: uppercase; }

    /* 6. SIDEBAR STYLING */
    section[data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E2E8F0 !important;
    }
    section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {
        background-color: #EFF6FF !important;
        border-left: 4px solid #1E3A8A !important;
    }
    section[data-testid="stSidebar"] * { color: #0F172A !important; }

    /* 7. QUICK LAUNCH BUTTONS */
    .stButton>button {
        border-radius: 8px !important;
        font-weight: 600 !important;
        background: #FFFFFF !important;
        color: #1E3A8A !important;
        border: 1px solid #CBD5E1 !important;
        padding: 0.8rem !important;
        width: 100% !important;
        transition: all 0.2s ease !important;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%) !important;
        color: white !important;
        border: none !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 15px rgba(37, 99, 235, 0.25) !important;
    }
    </style>
    """, unsafe_allow_html=True)
