import os
import streamlit as st
from components.auth import set_user_role

def render_sidebar():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    logo_path = os.path.join(base_dir, "logo.png")
    
    if os.path.exists(logo_path):
        st.sidebar.image(logo_path, width=110)
    elif os.path.exists("logo.png"):
        st.sidebar.image("logo.png", width=110)
    else:
        st.sidebar.markdown("## VECTOR-1")

    st.sidebar.title("SENTINEL Engine")
    st.sidebar.caption("Smart Environmental Nexus for Trade Intelligence")

    st.sidebar.markdown("---")
    st.sidebar.subheader("Demo Role Switcher")
    
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
        "Home Overview",
        "About SENTINEL",
        "Publications & Research",
        "Public Threat Map"
    ]
    
    if selected_role in ["Gov Agency", "Admin"]:
        pages.extend([
            "Live Scanner",
            "Data Studio & Catalogue",
            "Embed Portal",
            "AI Legal Copilot",
            "Training Modules"
        ])
        
    if selected_role == "Admin":
        pages.append("Admin Model Hub")
        
    pages.extend(["Guidance & FAQ", "Incident Escalation"])
    
    selected_page = st.sidebar.radio("Navigation Menu", pages)
    return selected_page
