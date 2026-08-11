import streamlit as st

def render_home_page():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #1E3A8A 0%, #0F172A 100%); padding:25px; border-radius:12px; color:white; margin-bottom:25px;">
        <h2 style="color:#FFFFFF; margin:0; font-size:1.8rem;">🛡️ SENTINEL Trade Intelligence Portal</h2>
        <p style="color:#93C5FD; font-size:1.05rem; margin-top:8px; margin-bottom:0px;">
            Smart Environmental Nexus for Trade Intelligence & Networked Enforcement Logic
        </p>
    </div>
    """, unsafe_allow_html=True)

    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Audited Declarations", "142,890", "+12.4% YoY")
    k2.metric("Overall Anomaly Rate", "4.12%", "-0.8% YoY")
    k3.metric("Container Interceptions", "382 Hold Orders", "JKDM / JAS")
    k4.metric("Active ML Models", "3 Deployed", "2 Under Dev")
    st.markdown("""
<div style="background-color: #EFF6FF; border: 1px solid #BFDBFE; border-radius: 12px; padding: 16px; margin-bottom: 20px;">
    <div style="display: flex; align-items: center; gap: 10px;">
        <span style="background-color: #2563EB; color: white; font-weight: 800; font-size: 0.75rem; padding: 4px 10px; border-radius: 20px;">BONUS ELIGIBLE</span>
        <strong style="color: #1E3A8A; font-size: 1.05rem;">Cross-Agency Interoperability Engine</strong>
    </div>
    <p style="color: #1E3E62; font-size: 0.9rem; margin-top: 8px; margin-bottom: 0px;">
        SENTINEL unifies environmental enforcement across <b>JAS (Environment)</b>, <b>JKDM (Customs)</b>, <b>MITI (Trade)</b>, and <b>PERHILITAN (Wildlife)</b> under a single AI intelligence fabric.
    </p>
</div>
""", unsafe_allow_html=True)
