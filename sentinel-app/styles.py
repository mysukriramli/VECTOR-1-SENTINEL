import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
    /* 1. TYPOGRAPHY & INTERACTION ENGINE */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
        scroll-behavior: smooth !important;
        color: #0F172A !important;
    }

    /* 2. LAYOUT & CANVAS BACKGROUND */
    .main .block-container {
        padding-top: 2.2rem !important;
        padding-bottom: 2.5rem !important;
        max-width: 96% !important;
    }

    .stApp {
        background-color: #F8FAFC !important;
        background-image: 
            radial-gradient(at 0% 0%, rgba(26, 54, 93, 0.03) 0px, transparent 40%),
            radial-gradient(at 100% 100%, rgba(37, 99, 235, 0.03) 0px, transparent 40%),
            linear-gradient(to right, rgba(226, 232, 240, 0.35) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(226, 232, 240, 0.35) 1px, transparent 1px) !important;
        background-size: 100% 100%, 100% 100%, 32px 32px, 32px 32px !important;
    }

    /* 3. HIDE STREAMLIT CHROME */
    footer {visibility: hidden !important;}
    #MainMenu {visibility: hidden !important;}
    .stDeployButton {display: none !important;}
    header {background-color: transparent !important;}

    /* 4. FIGMA BENTO GRID CARDS */
    .bento-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 20px 24px;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04), 0 1px 2px rgba(15, 23, 42, 0.02);
        transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        height: 100%;
    }
    .bento-card:hover {
        border-color: #CBD5E1;
        box-shadow: 0 8px 16px -4px rgba(26, 54, 93, 0.08);
        transform: translateY(-2px);
    }

    /* 5. MICRO BADGES & STATUS PILLS */
    .figma-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #F1F5F9;
        border: 1px solid #CBD5E1;
        color: #1A365D;
        font-size: 0.72rem;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 4px;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        font-family: 'JetBrains Mono', monospace;
    }

    .tier-pill-public {
        background: #F8FAFC; border: 1px solid #CBD5E1; border-left: 4px solid #64748B; color: #334155;
        padding: 8px 14px; border-radius: 6px; font-size: 0.82rem; font-weight: 600; margin-bottom: 1.2rem;
    }
    .tier-pill-gov {
        background: #EFF6FF; border: 1px solid #BFDBFE; border-left: 4px solid #2563EB; color: #1E3A8A;
        padding: 8px 14px; border-radius: 6px; font-size: 0.82rem; font-weight: 600; margin-bottom: 1.2rem;
    }
    .tier-pill-admin {
        background: #F8FAFC; border: 1px solid #E2E8F0; border-left: 4px solid #0F172A; color: #0F172A;
        padding: 8px 14px; border-radius: 6px; font-size: 0.82rem; font-weight: 600; margin-bottom: 1.2rem;
    }

    /* 6. FIGMA METRIC BLOCK */
    div[data-testid="stMetric"] {
        background: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 10px !important;
        padding: 18px 20px !important;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04) !important;
        transition: all 0.25s ease !important;
    }
    div[data-testid="stMetric"]:hover {
        border-color: #93C5FD !important;
        box-shadow: 0 8px 16px rgba(26, 54, 93, 0.08) !important;
        transform: translateY(-2px) !important;
    }
    div[data-testid="stMetricLabel"] {
        font-size: 0.78rem !important;
        font-weight: 700 !important;
        color: #64748B !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
    }
    div[data-testid="stMetricValue"] {
        font-size: 2.1rem !important;
        font-weight: 800 !important;
        color: #1A365D !important;
        letter-spacing: -0.5px !important;
    }

    /* 7. SIDEBAR STYLING */
    section[data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E2E8F0 !important;
    }
    section[data-testid="stSidebar"] * {
        color: #0F172A !important;
    }
    section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {
        background-color: #EFF6FF !important;
        border-left: 4px solid #1A365D !important;
    }

    /* 8. BUTTON SYSTEM */
    .stButton>button {
        border-radius: 6px !important;
        font-weight: 600 !important;
        background: linear-gradient(135deg, #1A365D 0%, #2563EB 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.7rem 1.4rem !important;
        width: 100% !important;
        box-shadow: 0 2px 6px rgba(26, 54, 93, 0.15) !important;
        transition: all 0.2s ease !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 16px rgba(26, 54, 93, 0.25) !important;
    }

    /* HEADERS */
    .main-header {
        font-size: 1.8rem; font-weight: 800; color: #1A365D; margin-bottom: 0rem; letter-spacing: -0.5px;
    }
    .sub-header {
        font-size: 0.95rem; color: #475569; margin-bottom: 1.2rem; font-weight: 500;
    }
    .intel-status-pill {
        display: inline-flex; align-items: center; gap: 8px; background-color: #F8FAFC; 
        border: 1px solid #E2E8F0; color: #334155; font-size: 0.75rem; font-weight: 700; 
        padding: 4px 12px; border-radius: 4px; text-transform: uppercase;
    }
    .pulse-dot {
        width: 8px; height: 8px; background-color: #2563EB; border-radius: 50%;
    }
    </style>
    """, unsafe_allow_html=True)
