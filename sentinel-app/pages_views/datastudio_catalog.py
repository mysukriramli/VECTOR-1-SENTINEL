import streamlit as st

def render_datastudio_catalog_page():
    st.subheader("📈 Google Looker Studio Analytics & Catalogue Hub")
    
    # Access Control Gate
    if st.session_state.get("user_role") == "Public (Free)":
        st.warning("🔒 Access Restricted: Interactive Data Studio catalogues require Gov Agency or Admin credentials.")
        st.info("Use the sidebar Demo Role Switcher to switch to **Gov Agency** or **Admin**.")
        return

    st.caption("Switch between catalogue tabs below to view real-time embedded Looker Studio dashboards.")

    # --------------------------------------------------------------------------
    # CONFIGURE YOUR DATA STUDIO EMBED LINKS HERE
    # --------------------------------------------------------------------------
    # Replace URL_2 and URL_3 with your actual Looker Studio embed links
    catalogues = {
        "📊 Catalogue 1: National Trade Overview": "https://datastudio.google.com/embed/reporting/0197917c-bdc7-4e41-8834-c85a6dd20763/page/Rre5F",
        "🚨 Catalogue 2: Anomaly & Risk Metrics": "https://datastudio.google.com/embed/reporting/YOUR_SECOND_CATALOGUE_ID/page/YOUR_PAGE_ID",
        "🛡️ Catalogue 3: MEA Enforcement Reports": "https://datastudio.google.com/embed/reporting/YOUR_THIRD_CATALOGUE_ID/page/YOUR_PAGE_ID"
    }

    # Create 3 distinct tabs for 1-to-1 catalogue embeds
    tab1, tab2, tab3 = st.tabs([
        "📊 Catalogue 1: Trade Overview", 
        "🚨 Catalogue 2: Anomaly Metrics", 
        "🛡️ Catalogue 3: MEA Enforcement"
    ])

    # --------------------------------------------------------------------------
    # TAB 1 EMBED
    # --------------------------------------------------------------------------
    with tab1:
        st.markdown("##### 📊 National Environmental Trade Overview")
        url_1 = catalogues["📊 Catalogue 1: National Trade Overview"]
        st.components.v1.iframe(url_1, height=650, scrolling=True)

    # --------------------------------------------------------------------------
    # TAB 2 EMBED
    # --------------------------------------------------------------------------
    with tab2:
        st.markdown("##### 🚨 Anomaly Detection & Risk Metrics")
        url_2 = catalogues["🚨 Catalogue 2: Anomaly & Risk Metrics"]
        
        if "YOUR_SECOND_CATALOGUE_ID" in url_2:
            st.info("💡 Paste your second Google Looker Studio embed link into line 19 of `datastudio_catalog.py`.")
        else:
            st.components.v1.iframe(url_2, height=650, scrolling=True)

    # --------------------------------------------------------------------------
    # TAB 3 EMBED
    # --------------------------------------------------------------------------
    with tab3:
        st.markdown("##### 🛡️ Multi-MEA Agency Enforcement Reports")
        url_3 = catalogues["🛡️ Catalogue 3: MEA Enforcement Reports"]
        
        if "YOUR_THIRD_CATALOGUE_ID" in url_3:
            st.info("💡 Paste your third Google Looker Studio embed link into line 20 of `datastudio_catalog.py`.")
        else:
            st.components.v1.iframe(url_3, height=650, scrolling=True)

    st.markdown("---")
    st.markdown("#### 📥 Agency Briefing & Catalogue Exports")
    
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
