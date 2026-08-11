import streamlit as st
from components.auth import set_user_role

def render_sidebar():
    st.sidebar.image("https://img.icons8.com/color/96/shield-with-signature.png", width=64)
    st.sidebar.title("SENTINEL Engine")
    st.sidebar.caption("Smart Environmental Nexus for Trade Intelligence")

    st.sidebar.markdown("---")
    st.sidebar.subheader("👤 Demo Role Switcher")
    
    current_role = st.session_state.get("user_role", "Gov Agency")
    role_options = ["Public (Free)", "Gov Agency", "Admin"]
    
    selected_role = st.sidebar.selectbox(
        "Select Session Role:",
        role_options,
        index=role_options.index(current_role),
        help="Switch roles to demonstrate Role-Based Access Control (RBAC)."
    )
    set_user_role(selected_role)

    st.sidebar.markdown("---")
    
    pages = [
        "🏠 Home Overview",
        "ℹ️ About SENTINEL & MEAs",
        "🗺️ Public Threat Map"
    ]
    
    if selected_role in ["Gov Agency", "Admin"]:
        pages.extend([
            "🔍 Multi-MEA Live Scanner",
            "📈 Data Studio & Catalogue",
            "🔌 Agency Embed Portal",
            "🤖 AI Legal Copilot",
            "🎓 Capacity Training Modules"
        ])
        
    if selected_role == "Admin":
        pages.append("⚙️ Admin Model Hub")
        
    pages.extend(["❓ Guidance & FAQ", "📞 Incident Escalation"])
    
    selected_page = st.sidebar.radio("Navigation Menu", pages)
    return selected_page