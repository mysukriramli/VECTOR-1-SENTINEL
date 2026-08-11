import os
import streamlit as st
from components.auth import set_user_role

def render_sidebar():
    """Renders sidebar navigation, brand logo, and tier-prioritized menu routing."""
    
    # Path resolution for local logo file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    logo_path = os.path.join(base_dir, "logo.png")
    
    if os.path.exists(logo_path):
        st.sidebar.image(logo_path, width=110)
    elif os.path.exists("logo.png"):
        st.sidebar.image("logo.png", width=110)
    else:
        st.sidebar.markdown("### SENTINEL")

    st.sidebar.title("SENTINEL Engine")
    st.sidebar.caption("National Environmental Security & Trade Compliance Engine")

    st.sidebar.markdown("---")
    st.sidebar.subheader("Access Clearance Tier")
    
    current_role = st.session_state.get("user_role", "Gov Agency")
    role_options = ["Public (Free)", "Gov Agency", "Admin"]
    
    selected_role = st.sidebar.selectbox(
        "Select Active Tier:",
        role_options,
        index=role_options.index(current_role),
        help="Switch roles to demonstrate Role-Based Access Control (RBAC) and dynamic menu prioritization."
    )
    set_user_role(selected_role)

    st.sidebar.markdown("---")
    st.sidebar.caption("PRIORITIZED MENU")

    # --------------------------------------------------------------------------
    # TIER-BASED NAVIGATION PRIORITY HIERARCHY
    # --------------------------------------------------------------------------
    if selected_role == "Admin":
        # ADMIN TIER PRIORITY: Governance, BigQuery Data Lake, Model Assets First
        pages = [
            "Admin Model Hub",            # Priority 1: Model Registry, SHA-256 Hashes, BigQuery Lake
            "Live Scanner",                # Priority 2: Primary Inference Engine (.joblib, CSV, OCR)
            "Incident Escalation",         # Priority 3: Multi-Agency HITL Adjudication Queue
            "Embed Portal",                # Priority 4: MyGDX Tokens & API Key Management
            "Data Studio & Catalogue",     # Priority 5: Analytics & Looker Studio Reports
            "Home Overview",               # Priority 6: Executive Overview Dashboard
            "AI Legal Copilot",            # Priority 7: Regulatory & MEA Statute Queries
            "Public Threat Map",           # Priority 8: GIS Threat Heatmaps
            "Publications & Research",     # Priority 9: Peer-Reviewed arXiv Papers
            "Training Modules",            # Priority 10: Operational Capacity Building
            "About SENTINEL",              # Priority 11: Mandate & Architecture
            "Guidance & FAQ"               # Priority 12: Platform Documentation
        ]

    elif selected_role == "Gov Agency":
        # GOV AGENCY TIER PRIORITY: Operational Enforcement Tools First
        pages = [
            "Live Scanner",                # Priority 1: Core Daily Work (Manifest ML & OCR Scanning)
            "Incident Escalation",         # Priority 2: HITL Officer Review & Interdiction Workbench
            "Home Overview",               # Priority 3: Executive Overview Dashboard
            "Data Studio & Catalogue",     # Priority 4: Embedded Analytics Dashboards
            "AI Legal Copilot",            # Priority 5: Statutory & Legal Query Assistant
            "Embed Portal",                # Priority 6: Inter-Agency MyGDX Data Requests
            "Public Threat Map",           # Priority 7: GIS Regional Threat Radar
            "Publications & Research",     # Priority 8: Peer-Reviewed Scientific Foundations
            "Training Modules",            # Priority 9: Capacity Training Modules
            "About SENTINEL",              # Priority 10: Platform Mandate & System Overview
            "Guidance & FAQ"               # Priority 11: User Guidance & Support
        ]

    else: # Public (Free)
        # PUBLIC TIER PRIORITY: Transparency & High-Level Metrics First
        pages = [
            "Home Overview",               # Priority 1: Public Command Center Landing Page
            "Public Threat Map",           # Priority 2: Regional Threat Heatmap & Public Risk Data
            "Publications & Research",     # Priority 3: Scientific Proof & arXiv Papers
            "About SENTINEL",              # Priority 4: Platform Mandate & Statutory Context
            "Guidance & FAQ",              # Priority 5: Public Guidance & Frequently Asked Questions
            "Incident Escalation"          # Priority 6: Public Hotline & Whistleblower Reporting
        ]

    selected_page = st.sidebar.radio("Navigation", pages)
    return selected_page
