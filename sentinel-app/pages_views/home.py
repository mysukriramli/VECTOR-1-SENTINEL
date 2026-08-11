import streamlit as st
import pandas as pd
import plotly.express as px

def render_home_page():
    st.subheader("🏠 National Environmental Trade Intelligence Hub")
    
    # --------------------------------------------------------------------------
    # PSAINC2026 COMPETITION PITCH ROOM TAB (FOR JUDGES)
    # --------------------------------------------------------------------------
    with st.expander("🏆 **PSAINC2026 Judge's Deliverables Desk (Team VECTOR 1)**", expanded=True):
        st.caption("Official competition submission assets for Jabatan Digital Negara (JDN) & NAIO evaluation panel.")
        
        d_tab1, d_tab2, d_tab3, d_tab4 = st.tabs([
            "📑 Executive Summary", 
            "🖼️ A1 Poster", 
            "🎬 2-Min Demo Video", 
            "📊 Pitch Deck (5 Slides)"
        ])
        
        with d_tab1:
            st.markdown("##### 1. Project Executive Summary (Template PDF)")
            st.markdown("""
            * **Project Name:** SENTINEL (Smart Environmental Nexus for Trade Intelligence)
            * **Team Name:** VECTOR 1[cite: 2]
            * **Lead Owner:** Cross-Agency Collaboration (JAS, JKDM, MITI, PERHILITAN)[cite: 2]
            * **AI Approach:** Isolation Forest Anomaly Detection + OCR Manifest Parsing + Google Looker Studio Analytics[cite: 2].
            * **Public Impact:** RM 42.8M prevented revenue fraud, 382 toxic illegal waste containers intercepted[cite: 2].
            """)
            st.download_button("📥 Download Executive Summary (PDF)", b"MOCK_PDF_DATA", "SENTINEL_Executive_Summary_VECTOR1.pdf")

        with d_tab2:
            st.markdown("##### 2. Official Competition Poster (A1 Portrait)[cite: 2]")
            st.info("A1 Poster resolution: 594mm x 841mm, 150+ DPI[cite: 2]. Contains problem statement, AI architecture, UI screens, and team contact[cite: 2].")

        with d_tab3:
            st.markdown("##### 3. Prototype Video Demonstration (2 Mins Max MP4)[cite: 2]")
            st.caption("Highlights problem statement, live .joblib ML inference, and multi-agency escalation workflow[cite: 2].")
            # Sample Video Placeholder
            st.video("https://www.w3schools.com/html/mov_bbb.mp4")

        with d_tab4:
            st.markdown("##### 4. Presentation Slide Deck (5 Core Slides)[cite: 2]")
            st.markdown("""
            1. **Slide 1:** Problem Statement & Multi-MEA Statutory Context[cite: 2]
            2. **Slide 2:** AI Architecture & Cloud Sandbox Integration (Google / TM AIaaS)[cite: 2]
            3. **Slide 3:** Live Prototype Workflow & Feature Set[cite: 2]
            4. **Slide 4:** Public Impact, Economic Value & Citizen ROI[cite: 2]
            5. **Slide 5:** Scalability Roadmap & Expansion Plan[cite: 2]
            """)

    st.markdown("---")

    # Metrics Overview
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Audited Declarations", "142,890", "↑ 12.4% YoY")
    c2.metric("Overall Anomaly Rate", "4.12%", "↓ 0.8% YoY")
    c3.metric("Container Interceptions", "382 Holds", "JKDM / JAS")
    c4.metric("Active ML Models", "3 Deployed", "2 In Sandbox")

    st.markdown("---")

    # Interactive Threat Heatmap
    st.markdown("##### 🌍 Real-Time Regional Environmental Trade Threat Feed")
    
    map_data = pd.DataFrame({
        'lat': [3.0, 1.5, 5.4, 4.5, 2.5],
        'lon': [101.4, 103.8, 100.3, 114.0, 101.8],
        'Risk_Level': ['High Risk Plastic', 'ODS Gas Misdeclaration', 'E-Waste Shipment', 'Timber CITES Deficit', 'Toxic Sludge'],
        'Score': [92, 88, 79, 85, 94]
    })
    
    fig = px.scatter_mapbox(
        map_data, 
        lat="lat", 
        lon="lon", 
        color="Score", 
        size="Score",
        hover_name="Risk_Level",
        color_continuous_scale="Reds",
        zoom=5, 
        height=380
    )
    fig.update_layout(mapbox_style="open-street-map", margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(fig, use_container_width=True)
