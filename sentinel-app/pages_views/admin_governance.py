import streamlit as st
from components.auth import can_download_joblib

def render_admin_governance_page():
    st.subheader("⚙️ Admin Model Governance Hub")
    if not can_download_joblib():
        st.error("⛔ Access Restricted: Admin Tier required.")
        return

    st.download_button("⬇️ Download plastic_forensic_pipeline.joblib", b"DUMMY_BIN", "plastic_forensic_pipeline.joblib")
    st.download_button("⬇️ Download ods_forensic_pipeline.joblib", b"DUMMY_BIN", "ods_forensic_pipeline.joblib")
    st.download_button("⬇️ Download ewaste_forensic_pipeline.joblib", b"DUMMY_BIN", "ewaste_forensic_pipeline.joblib")