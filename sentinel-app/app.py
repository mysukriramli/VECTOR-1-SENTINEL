import os
import sys

# Resolve current directory on Streamlit Cloud for subfolder module imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from styles import apply_custom_styles
from components.auth import init_auth_session
from components.navbar import render_sidebar

# Page View Renderers
from pages_views.home import render_home_page
from pages_views.about import render_about_page
from pages_views.public_insights import render_public_insights_page
from pages_views.anomaly_inspector import render_anomaly_inspector_page
from pages_views.datastudio_catalog import render_datastudio_catalog_page
from pages_views.embed_portal import render_embed_portal_page
from pages_views.copilot_assistant import render_copilot_assistant_page
from pages_views.training_module import render_training_module_page
from pages_views.admin_governance import render_admin_governance_page
from pages_views.faq import render_faq_page
from pages_views.contact import render_contact_page

# Page Window Configuration
st.set_page_config(
    page_title="SENTINEL - Multi-MEA Trade Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply UI Styling & Initialize Session State
apply_custom_styles()
init_auth_session()

# Render Navigation Sidebar
active_page = render_sidebar()

# Header Accent Banner with PSAINC2026 Badges
col_h1, col_h2 = st.columns([3, 1])
with col_h1:
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 4px; flex-wrap: wrap;">
        <span class="main-header">SENTINEL Platform</span>
        <span class="psainc-badge">🏆 PSAINC2026: VECTOR 1</span>
        <span class="intel-status-pill"><span class="pulse-dot"></span> JDN / NAIO COMPLIANT</span>
    </div>
    <div class="sub-header">National Environmental Security & Trade Compliance Engine</div>
    """, unsafe_allow_html=True)
with col_h2:
    st.info(f"Current Access Tier:\n**{st.session_state['user_role']}**")

st.markdown("---")

# Page Dispatcher Router
if "🏠 Home Overview" in active_page:
    render_home_page()
elif "ℹ️ About SENTINEL" in active_page:
    render_about_page()
elif "🗺️ Public Threat Map" in active_page:
    render_public_insights_page()
elif "🔍 Multi-MEA Live Scanner" in active_page:
    render_anomaly_inspector_page()
elif "📈 Data Studio & Catalogue" in active_page:
    render_datastudio_catalog_page()
elif "🔌 Agency Embed Portal" in active_page:
    render_embed_portal_page()
elif "🤖 AI Legal Copilot" in active_page:
    render_copilot_assistant_page()
elif "🎓 Capacity Training Modules" in active_page:
    render_training_module_page()
elif "⚙️ Admin Model Hub" in active_page:
    render_admin_governance_page()
elif "❓ Guidance & FAQ" in active_page:
    render_faq_page()
elif "📞 Incident Escalation" in active_page:
    render_contact_page()
