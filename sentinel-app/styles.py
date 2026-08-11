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
        padding-top: 3.8rem !important;
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

    /* 4. LIVE INTERDICTION TICKER BANNER */
    .live-ticker-container {
        background: #0F172A;
        color: #F8FAFC;
        border-radius: 10px;
        padding: 10px 18px;
        display: flex;
        align-items: center;
        gap: 16px;
        margin-bottom: 1.2rem;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.1);
        border: 1px solid #1E293B;
    }
    .ticker-tag {
        background: #2563EB;
        color: #FFFFFF;
        font-size: 0.72rem;
        font-weight: 800;
        padding: 3px 10px;
        border-radius: 6px;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    .ticker-text {
        font-size: 0.85rem;
        font-family: 'JetBrains Mono', monospace;
        color: #94A3B8;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    /* 5. HERO NEXUS CONTAINER */
    .hero-nexus {
        background: linear-gradient(135deg, #FFFFFF 0%, #F1F5F9 100%);
        border: 1px solid #E2E8F0;
        border-left: 6px solid #1E3A8A;
        border-radius: 14px;
        padding: 24px 28px;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.03);
        margin-bottom: 1.2rem;
    }
    .hero-nexus-title {
        font-size: 1.85rem;
        font-weight: 800;
        color: #0F172A;
        letter-spacing: -0.5px;
        margin-bottom: 6px;
    }
    .hero-nexus-sub {
        font-size: 0.98rem;
        color: #475569;
        line-height: 1.5;
    }

    /* 6. DYNAMIC TIER BADGES */
    .tier-badge-public {
        background: #ECFDF5;
        border: 1px solid #A7F3D0;
        color: #065F46;
        padding: 8px 14px;
        border-radius: 8px;
        font-size: 0.85rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    .tier-badge-gov {
        background: #EFF6FF;
        border: 1px solid #BFDBFE;
        color: #1E3A8A;
        padding: 8px 14px;
        border-radius: 8px;
        font-size: 0.85rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    .tier-badge-admin {
        background: #FEF2F2;
        border: 1px solid #FECACA;
        color: #991B1B;
        padding: 8px 14px;
        border-radius: 8px;
        font-size: 0.85rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }

    /* 7. GLASSMORPHISM METRIC CARDS */
    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.9) !important;
        backdrop-filter: blur(8px) !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 12px !important;
        padding: 16px 20px !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03) !important;
        transition: all 0.25s ease !important;
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-3px) !important;
        border-color: #93C5FD !important;
        box-shadow: 0 10px 20px -3px rgba(37, 99, 235, 0.1) !important;
    }

    /* 8. SIDEBAR LIGHT STYLING */
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

    /* Pulse Status Marker */
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
