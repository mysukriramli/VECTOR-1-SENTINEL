import streamlit as st

ROLES = ["Public (Free)", "Gov Agency", "Admin"]

def init_auth_session():
    if "user_role" not in st.session_state:
        st.session_state["user_role"] = "Gov Agency"
    if "user_agency" not in st.session_state:
        st.session_state["user_agency"] = "JKDM (Customs)"

def set_user_role(role_name: str):
    if role_name in ROLES:
        st.session_state["user_role"] = role_name

def is_agency_or_admin() -> bool:
    return st.session_state.get("user_role") in ["Gov Agency", "Admin"]

def can_download_joblib() -> bool:
    return st.session_state.get("user_role") == "Admin"