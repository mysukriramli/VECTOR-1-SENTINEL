import streamlit as st

def render_datastudio_catalog_page():
    st.subheader("Google Looker Studio Analytics & MEA Catalogue Hub")
    
    # Access Control Gate
    if st.session_state.get("user_role") == "Public (Free)":
        st.warning("Access Restricted: Interactive Data Studio catalogues require Gov Agency or Admin credentials.")
        st.info("Use the sidebar Clearance Switcher to switch to **Gov Agency** or **Admin**.")
        return

    st.caption("Switch between treaty domain tabs below to inspect embedded Looker Studio dashboards covering active Multilateral Environmental Agreements (MEAs).")

    # --------------------------------------------------------------------------
    # DATA STUDIO EMBED CATALOGUE CONFIGURATION
    # --------------------------------------------------------------------------
    catalogues = {
        "plastic": "https://datastudio.google.com/embed/reporting/0197917c-bdc7-4e41-8834-c85a6dd20763/page/Rre5F",
        "ewaste": "https://datastudio.google.com/embed/reporting/ef840f7e-ae29-44c0-823b-16b6ce1cff59/page/hYG6F",
        "ozone": "https://datastudio.google.com/embed/reporting/f9e9b6a2-6e3f-4c7b-90bb-8b7922e525da/page/MFG6F"
    }

    # Create 5 distinct tabs across the 4 MEA Framework domains
    tab_plastic, tab_ewaste, tab_ozone, tab_cites, tab_stockholm = st.tabs([
        "Plastic Waste (HS 3915)",
        "E-Waste (HS 8548/8549)",
        "Ozone Substances (HS 2903)",
        "CITES Timber & Fauna",
        "Stockholm/Rotterdam POPs"
    ])

    # --------------------------------------------------------------------------
    # TAB 1: BASEL CONVENTION - PLASTIC SCRAP (LIVE EMBED)
    # --------------------------------------------------------------------------
    with tab_plastic:
        st.markdown("##### Basel Convention: Plastic Scrap (HS 3915) Trade Analytics")
        st.caption("Real-time monitoring of imported secondary plastic resin, density benchmarks, and declared unit value anomalies.")
        st.components.v1.iframe(catalogues["plastic"], height=650, scrolling=True)

    # --------------------------------------------------------------------------
    # TAB 2: BASEL CONVENTION - E-WASTE (LIVE EMBED)
    # --------------------------------------------------------------------------
    with tab_ewaste:
        st.markdown("##### Basel Convention: E-Waste & Electrical Scrap (HS 8548/8549)")
        st.caption("Cross-border tracking of electrical scrap metal slag, hazardous e-waste shipments, and container valuation outliers.")
        st.components.v1.iframe(catalogues["ewaste"], height=650, scrolling=True)

    # --------------------------------------------------------------------------
    # TAB 3: MONTREAL PROTOCOL - OZONE DEPLETING SUBSTANCES (LIVE EMBED)
    # --------------------------------------------------------------------------
    with tab_ozone:
        st.markdown("##### Montreal Protocol: Ozone Depleting Substances (HS 2903)")
        st.caption("Monitoring imports of HCFC, CFC, and regulated refrigerant gases against active MITI import quota allocations.")
        st.components.v1.iframe(catalogues["ozone"], height=650, scrolling=True)

    # --------------------------------------------------------------------------
    # TAB 4: CITES FRAMEWORK - TIMBER & FAUNA (UNDER CONSTRUCTION)
    # --------------------------------------------------------------------------
    with tab_cites:
        st.markdown("##### CITES Framework: Protected Timber & Fauna Screening")
        st.caption("Inspection parameters covering HS 4403/4407 timber volumetric density and PERHILITAN species protection orders.")
        
        st.markdown("""
        <div style="background:#FFFFFF; border:1px dashed #CBD5E1; border-radius:8px; padding:60px 40px; text-align:center; min-height:420px; display:flex; flex-direction:column; justify-content:center; align-items:center; margin: 15px 0;">
            <div style="font-size:0.85rem; font-weight:800; color:#2563EB; font-family:'JetBrains Mono', monospace; text-transform:uppercase; letter-spacing:1px; margin-bottom:8px;">
                SYSTEM STATUS: UNDER CONSTRUCTION
            </div>
            <div style="font-size:1.25rem; font-weight:800; color:#1A365D; margin-bottom:8px;">
                CITES Timber & Endangered Species Reporting Canvas
            </div>
            <div style="font-size:0.88rem; color:#64748B; max-width:520px; line-height:1.5;">
                BigQuery data lake pipelines and PERHILITAN permit cross-checks are active. Google Looker Studio reporting canvas is currently being provisioned for production release.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # TAB 5: STOCKHOLM & ROTTERDAM - POPS CHEMICALS (UNDER CONSTRUCTION)
    # --------------------------------------------------------------------------
    with tab_stockholm:
        st.markdown("##### Stockholm & Rotterdam Frameworks: Hazardous Chemical & POPs")
        st.caption("Monitoring persistent organic pollutants, toxic industrial chemicals, and agricultural pesticide tariff compliance.")
        
        st.markdown("""
        <div style="background:#FFFFFF; border:1px dashed #CBD5E1; border-radius:8px; padding:60px 40px; text-align:center; min-height:420px; display:flex; flex-direction:column; justify-content:center; align-items:center; margin: 15px 0;">
            <div style="font-size:0.85rem; font-weight:800; color:#2563EB; font-family:'JetBrains Mono', monospace; text-transform:uppercase; letter-spacing:1px; margin-bottom:8px;">
                SYSTEM STATUS: UNDER CONSTRUCTION
            </div>
            <div style="font-size:1.25rem; font-weight:800; color:#1A365D; margin-bottom:8px;">
                Stockholm & Rotterdam POPs Chemical Safety Dashboard
            </div>
            <div style="font-size:0.88rem; color:#64748B; max-width:520px; line-height:1.5;">
                Department of Agriculture and Department of Environment chemical registry feeds are synchronized. Looker Studio reporting canvas is currently being provisioned for production release.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### Agency Briefing & Catalogue Exports")
    
    cat_col1, cat_col2 = st.columns(2)
    
    with cat_col1:
        st.markdown("##### Executive Summary Briefing (PDF)")
        st.download_button(
            label="Download Executive Briefing (PDF)",
            data=b"MOCK_PDF_EXECUTIVE_SUMMARY_BYTES",
            file_name="SENTINEL_Executive_Briefing_2026.pdf",
            mime="application/pdf"
        )

    with cat_col2:
        st.markdown("##### Raw Anomaly Incident Dataset (CSV)")
        sample_csv = "HS_Code,Declared_Value,Weight_Kg,Risk_Score,Status\n3915.10,1200,25000,88.4,Hold\n8549.21,850,14000,92.1,Hold\n2903.42,4500,3000,91.2,Confiscate"
        st.download_button(
            label="Download Anomaly Dataset (CSV)",
            data=sample_csv,
            file_name="SENTINEL_Flagged_Anomalies_2026.csv",
            mime="text/csv"
        )
