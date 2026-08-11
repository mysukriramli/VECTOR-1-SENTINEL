import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
    /* 1. IMPORT GOOGLE MODERN FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
        scroll-behavior: smooth !important;
    }

    /* 2. KEYFRAME ANIMATIONS */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(12px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes pulseGlow {
        0% {
            box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.6);
        }
        70% {
            box-shadow: 0 0 0 8px rgba(16, 185, 129, 0);
        }
        100% {
            box-shadow: 0 0 0 0 rgba(16, 185, 129, 0);
        }
    }

    /* 3. MAIN CONTAINER PADDING & ANIMATION */
    .main .block-container {
        animation: fadeInUp 0.45s cubic-bezier(0.16, 1, 0.3, 1) forwards !important;
        padding-top: 4.5rem !important;
        padding-bottom: 2.5rem !important;
        max-width: 95% !important;
    }

    /* 4. HIGH-TECH LIGHT BACKGROUND WITH SUBTLE GRID */
    .stApp {
        background-color: #F8FAFC !important;
        background-image: 
            radial-gradient(at 0% 0%, rgba(37, 99, 235, 0.03) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(30, 58, 138, 0.03) 0px, transparent 50%),
            linear-gradient(to right, rgba(226, 232, 240, 0.35) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(226, 232, 240, 0.35) 1px, transparent 1px) !important;
        background-size: 100% 100%, 100% 100%, 32px 32px, 32px 32px !important;
    }

    /* 5. HIDE DEFAULT STREAMLIT CHROME */
    footer {visibility: hidden !important;}
    #MainMenu {visibility: hidden !important;}
    .stDeployButton {display: none !important;}

    /* 6. CLEAN EXECUTIVE LIGHT SIDEBAR */
    section[data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E2E8F0 !important;
        box-shadow: 4px 0 12px rgba(15, 23, 42, 0.02) !important;
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
    }

    /* Navigation Menu Links with Hover Lift */
    section[data-testid="stSidebar"] div[role="radiogroup"] label {
        background-color: transparent !important;
        padding: 9px 12px !important;
        border-radius: 8px !important;
        transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1) !important;
        margin-bottom: 3px !important;
        border: 1px solid transparent !important;
    }
    section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
        background-color: #F1F5F9 !important;
        border-color: #E2E8F0 !important;
        transform: translateX(3px) !important;
    }
    section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {
        background-color: #EFF6FF !important;
        border-left: 4px solid #1E3A8A !important;
        border-color: #DBEAFE !important;
        box-shadow: 0 2px 4px rgba(37, 99, 235, 0.06) !important;
    }
    section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] * {
        color: #1E3A8A !important;
        font-weight: 700 !important;
    }

    /* 7. HIGH-CONTRAST FORM INPUTS & DROPDOWNS */
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
        transition: border-color 0.2s ease !important;
    }
    div[data-baseweb="input"] > div:focus-within,
    div[data-baseweb="select"] > div:focus-within {
        border-color: #2563EB !important;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15) !important;
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
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1) !important;
    }
    div[data-baseweb="popover"] * {
        color: #0F172A !important;
        background-color: #FFFFFF !important;
    }
    div[data-baseweb="popover"] li[role="option"]:hover {
        background-color: #EFF6FF !important;
    }

    /* 8. METRIC CARDS WITH HOVER LIFT & GLOW */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 12px !important;
        padding: 18px 22px !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03), 0 2px 4px -1px rgba(0, 0, 0, 0.02) !important;
        transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-4px) !important;
        border-color: #BFDBFE !important;
        box-shadow: 0 12px 20px -3px rgba(37, 99, 235, 0.12), 0 4px 6px -2px rgba(37, 99, 235, 0.05) !important;
    }
    div[data-testid="stMetricLabel"] {
        font-size: 0.82rem !important;
        font-weight: 700 !important;
        color: #64748B !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
    }
    div[data-testid="stMetricValue"] {
        font-size: 1.85rem !important;
        font-weight: 800 !important;
        color: #0F172A !important;
    }

    /* 9. BUTTONS */
    .stButton>button {
        border-radius: 8px !important;
        font-weight: 600 !important;
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.65rem 1.3rem !important;
        box-shadow: 0 4px 10px rgba(37, 99, 235, 0.2) !important;
        transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 18px rgba(37, 99, 235, 0.35) !important;
        background: linear-gradient(135deg, #1D4ED8 0%, #3B82F6 100%) !important;
    }

    /* 10. LIVE INTEL RADAR STATUS BADGE */
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
        letter-spacing: 0.5px;
    }
    .pulse-dot {
        width: 8px;
        height: 8px;
        background-color: #10B981;
        border-radius: 50%;
        animation: pulseGlow 1.8s infinite;
    }

    /* 11. HEADERS */
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        color: #0F172A;
        margin-bottom: 0rem;
        line-height: 1.2;
        letter-spacing: -0.5px;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #475569;
        margin-bottom: 1.2rem;
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)
