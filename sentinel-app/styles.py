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

    /* 2. MAIN CONTAINER & BACKGROUND GRID */
    .main .block-container {
        padding-top: 4.0rem !important;
        padding-bottom: 2.5rem !important;
        max-width: 95% !important;
    }

    .stApp {
        background-color: #F8FAFC !important;
        background-image: 
            radial-gradient(at 0% 0%, rgba(37, 99, 235, 0.03) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(30, 58, 138, 0.03) 0px, transparent 50%),
            linear-gradient(to right, rgba(226, 232, 240, 0.35) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(226, 232, 240, 0.35) 1px, transparent 1px) !important;
        background-size: 100% 100%, 100% 100%, 30px 30px, 30px 30px !important;
    }

    /* 3. HIDE DEFAULT CHROME */
    footer {visibility: hidden !important;}
    #MainMenu {visibility: hidden !important;}
    .stDeployButton {display: none !important;}

    /* 4. DYNAMIC ROLE/TIER VISUAL BANNERS */
    .tier-banner-public {
        background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%);
        border: 1px solid #A7F3D0;
        border-left: 6px solid #10B981;
        padding: 12px 18px;
        border-radius: 10px;
        color: #065F46;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    .tier-banner-gov {
        background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
        border: 1px solid #BFDBFE;
        border-left: 6px solid #2563EB;
        padding: 12px 18px;
        border-radius: 10px;
        color: #1E3A8A;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    .tier-banner-admin {
        background: linear-gradient(135deg, #FEF2F2 0%, #FEE2E2 100%);
        border: 1px solid #FECACA;
        border-left: 6px solid #EF4444;
        padding: 12px 18px;
        border-radius: 10px;
        color: #991B1B;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    /* 5. HERO BOX DEFINITION */
    .hero-container {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 24px 28px;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.03);
        margin-bottom: 1.5rem;
    }
    .hero-title {
        font-size: 1.8rem;
        font-weight: 800;
        color: #0F172A;
        letter-spacing: -0.5px;
        margin-bottom: 6px;
    }
    .hero-subtitle {
        font-size: 1.0rem;
        color: #475569;
        line-height: 1.5;
    }

    /* 6. SIDEBAR LIGHT THEME */
    section[data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E2E8F0 !important;
    }
    section[data-testid="stSidebar"] * {
        color: #0F172A !important;
    }

    section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {
        background-color: #EFF6FF !important;
        border-left: 4px solid #1E3A8A !important;
    }

    /* 7. FORM INPUTS & SELECTBOXES */
    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div,
    input {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }

    /* 8. METRIC CARDS */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 12px !important;
        padding: 16px 20px !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03) !important;
    }

    /* 9. SHIMMER BUTTONS */
    .stButton>button {
        border-radius: 8px !important;
        font-weight: 600 !important;
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.6rem 1.2rem !important;
        width: 100% !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 14px rgba(37, 99, 235, 0.3) !important;
    }

    /* Pulse Dot for Header */
    .intel-status-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background-color: #ECFDF5;
        border: 1px solid #A7F3D0;
        color: #065F46;
        font-size: 0.78rem;
        font-weight: 700;
        padding: 4px 12px;
        border-radius: 20px;
    }
    .pulse-dot {
        width: 8px;
        height: 8px;
        background-color: #10B981;
        border-radius: 50%;
    }
    </style>
    """, unsafe_allow_html=True)
