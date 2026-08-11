import streamlit as st

def render_datastudio_catalog_page():
    st.subheader("📈 Google Looker Studio Analytics & Catalogue")
    
    if st.session_state.get("user_role") == "Public (Free)":
        st.warning("🔒 Access Restricted: Gov Agency or Admin credentials required.")
        return

    st.caption("Interactive multi-agency analytics powered by embedded Google Looker Studio.")

    # Embedded Looker Studio iframe
    st.markdown("#### Interactive Environmental Trade Dashboard")
    looker_studio_url = "https://lookerstudio.google.com/embed/reporting/0B5FF2A71111/page/6zB"
    st.components.v1.iframe(looker_studio_url, height=600, scrolling=True)

    st.markdown("---")
    st.markdown("#### 📥 Agency Export & Report Catalogue")
    
    cat_col1, cat_col2 = st.columns(2)
    
    with cat_col1:
        st.markdown("##### Executive Summary Briefing (PDF)")
        st.download_button(
            label="📄 Download Executive Briefing (PDF)",
            data=b"MOCK_PDF_EXECUTIVE_SUMMARY_BYTES",
            file_name="SENTINEL_Executive_Briefing_2026.pdf",
            mime="application/pdf"
        )

    with cat_col2:
        st.markdown("##### Raw Anomaly Incident Dataset (CSV)")
        sample_csv = "HS_Code,Declared_Value,Weight_Kg,Risk_Score,Status\n3915.10,1200,25000,88.4,Hold\n2903.42,4500,3000,91.2,Confiscate"
        st.download_button(
            label="📊 Download Anomaly Dataset (CSV)",
            data=sample_csv,
            file_name="SENTINEL_Flagged_Anomalies_2026.csv",
            mime="text/csv"
        )
