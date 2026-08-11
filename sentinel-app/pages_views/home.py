import streamlit as st
import pandas as pd
import plotly.express as px

def render_home_page():
    # --------------------------------------------------------------------------
    # 1. HERO SECTION: WHAT IS SENTINEL?
    # --------------------------------------------------------------------------
    st.markdown("""
    <div class="hero-container">
        <div class="hero-title">🛡️ SENTINEL Trade Intelligence Engine</div>
        <div class="hero-subtitle">
            Malaysia's central AI/ML platform for screening cross-border shipments against 
            <b>Multilateral Environmental Agreements (MEAs)</b>. SENTINEL automatically detects illegal 
            hazardous waste, misdeclared e-waste, ozone-depleting chemicals, and contraband before port clearance.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # 2. DYNAMIC TIER VISUAL BADGE
    # --------------------------------------------------------------------------
    role = st.session_state.get("user_role", "Public (Free)")
    
    if role == "Public (Free)":
        st.markdown("""
        <div class="tier-banner-public">
            🟢 <b>Tier Level 1: Public Transparency Access</b> — Viewing public treaty statistics, open environmental trade metrics, and regional threat radar.
        </div>
        """, unsafe_allow_html=True)
    elif role == "Gov Agency":
        st.markdown("""
        <div class="tier-banner-gov">
            🔵 <b>Tier Level 2: Inter-Agency Operational Access (JKDM / JAS / MITI)</b> — Unlocked Live .joblib Scanner, OCR Parser, and Multi-Agency Escalation Queue.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="tier-banner-admin">
            🔴 <b>Tier Level 3: Root Admin Governance Access</b> — Unlocked Cryptographic Model Registry, SHA-256 Hashes, and Sensitivity Calibration.
        </div>
        """, unsafe_allow_html=True)

    # Key Metrics
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Audited Declarations", "142,890", "↑ 12.4% YoY")
    m2.metric("Overall Anomaly Rate", "4.12%", "↓ 0.8% YoY")
    m3.metric("Container Interceptions", "382 Holds", "JKDM / JAS Actions")
    m4.metric("Active ML Models", "3 Live Pipelines", "2 In Sandbox")

    st.markdown("---")

    # --------------------------------------------------------------------------
    # 3. SIDE-BY-SIDE: MEA FRAMEWORKS (LEFT) & DATA STUDIO TRADE DIP (RIGHT)
    # --------------------------------------------------------------------------
    col_left, col_right = st.columns([1, 1])

    with col_left:
        st.markdown("### 📜 Multilateral Environmental Agreements (MEAs)")
        st.caption("International treaties enforced by SENTINEL's ML pipelines:")

        st.markdown("""
        <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:10px; padding:14px; margin-bottom:12px;">
            <div style="font-size:1.1rem; font-weight:800; color:#1E3A8A;">♻️ Basel Convention</div>
            <div style="font-size:0.85rem; color:#334155; margin-top:2px;"><b>Focus:</b> Plastic Scrap (HS 3915) & E-Waste (HS 8548/8549)</div>
            <div style="font-size:0.75rem; color:#64748B;"><b>Enforcement Lead:</b> JAS & JKDM</div>
        </div>

        <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:10px; padding:14px; margin-bottom:12px;">
            <div style="font-size:1.1rem; font-weight:800; color:#1E3A8A;">❄️ Montreal Protocol</div>
            <div style="font-size:0.85rem; color:#334155; margin-top:2px;"><b>Focus:</b> Ozone Depleting Refrigerants & Gases (HS 2903)</div>
            <div style="font-size:0.75rem; color:#64748B;"><b>Enforcement Lead:</b> JAS & MITI</div>
        </div>

        <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:10px; padding:14px; margin-bottom:12px;">
            <div style="font-size:1.1rem; font-weight:800; color:#1E3A8A;">🌿 CITES Framework</div>
            <div style="font-size:0.85rem; color:#334155; margin-top:2px;"><b>Focus:</b> Endangered Wildlife, Flora & Timber (HS 0106/4403)</div>
            <div style="font-size:0.75rem; color:#64748B;"><b>Enforcement Lead:</b> PERHILITAN & MAQIS</div>
        </div>

        <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:10px; padding:14px;">
            <div style="font-size:1.1rem; font-weight:800; color:#1E3A8A;">🧪 Stockholm & Rotterdam</div>
            <div style="font-size:0.85rem; color:#334155; margin-top:2px;"><b>Focus:</b> Persistent Organic Pollutants (POPs) & Toxic Pesticides</div>
            <div style="font-size:0.75rem; color:#64748B;"><b>Enforcement Lead:</b> Dept of Agriculture & JAS</div>
        </div>
        """, unsafe_allow_html=True)

    with col_right:
        st.markdown("### 📊 Public MEA Analytics: Impact of Banned HS Codes")
        st.caption("Demonstrating the sharp dip in illegal imports following AI enforcement on HS Code 3915.10:")

        # Simulated Trade Dip Data for Banned HS Code 3915.10
        dip_df = pd.DataFrame({
            "Month": ["Jan 2026", "Feb 2026", "Mar 2026", "Apr 2026 (Enforcement Starts)", "May 2026", "Jun 2026", "Jul 2026"],
            "Import Volume (Metric Tons)": [14200, 15800, 13900, 4100, 1200, 850, 410]
        })

        fig_dip = px.line(
            dip_df, 
            x="Month", 
            y="Import Volume (Metric Tons)",
            markers=True,
            title="HS 3915.10 (Plastic Waste) Import Volume Dip Post-Enforcement",
            color_discrete_sequence=["#DC2626"]
        )
        fig_dip.update_layout(height=340, margin=dict(l=10, r=10, t=40, b=10))
        st.plotly_chart(fig_dip, use_container_width=True)

        st.success("📉 **Enforcement Impact:** Non-compliant plastic waste declarations dropped by **97.1%** within 90 days of SENTINEL pipeline activation.")

    st.markdown("---")

    # --------------------------------------------------------------------------
    # 4. ANIMATED SOFT-PULSE THREAT RADAR MAP
    # --------------------------------------------------------------------------
    st.markdown("### 🌍 Real-Time Regional Threat Radar")
    st.caption("Live geographical anomaly heat map across Malaysian entry points:")

    # Embedded HTML Leaflet Map with glowing animated pulsing rings
    leaflet_map_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
        <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
        <style>
            #map { height: 380px; width: 100%; border-radius: 12px; }
            .pulse-icon {
                background: rgba(220, 38, 38, 0.9);
                border-radius: 50%;
                box-shadow: 0 0 0 rgba(220, 38, 38, 0.7);
                animation: pulse-ring 1.8s infinite;
            }
            @keyframes pulse-ring {
                0% {
                    box-shadow: 0 0 0 0 rgba(220, 38, 38, 0.7);
                }
                70% {
                    box-shadow: 0 0 0 16px rgba(220, 38, 38, 0);
                }
                100% {
                    box-shadow: 0 0 0 0 rgba(220, 38, 38, 0);
                }
            }
        </style>
    </head>
    <body>
        <div id="map"></div>
        <script>
            var map = L.map('map').setView([4.2, 108.0], 5);
            L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
                attribution: '&copy; OpenStreetMap'
            }).addTo(map);

            var ports = [
                {name: "Port Klang", lat: 3.00, lon: 101.40, desc: "High Risk Plastic Scrap (HS 3915)"},
                {name: "Johor Port", lat: 1.45, lon: 103.75, desc: "Unlicensed ODS Gas (HS 2903)"},
                {name: "Penang Port", lat: 5.41, lon: 100.32, desc: "Illegal E-Waste Containers (HS 8549)"},
                {name: "Bintulu Port", lat: 4.58, lon: 114.00, desc: "Timber CITES Mismatch (HS 4403)"},
                {name: "KLIA Cargo", lat: 2.80, lon: 101.70, desc: "Chemical POPs Mismatch"}
            ];

            ports.forEach(function(p) {
                var pulseMarker = L.divIcon({
                    className: 'pulse-icon',
                    iconSize: [14, 14]
                });
                L.marker([p.lat, p.lon], {icon: pulseMarker}).addTo(map)
                    .bindPopup("<b>" + p.name + "</b><br>" + p.desc);
            });
        </script>
    </body>
    </html>
    """
    st.components.v1.html(leaflet_map_html, height=400)

    st.markdown("---")

    # --------------------------------------------------------------------------
    # 5. MOVED DOWN: FUNCTIONAL QUICK LAUNCH DESK WITH WORKING BUTTONS
    # --------------------------------------------------------------------------
    st.markdown("### 🚀 Platform Quick Operations Desk")
    st.caption("Click any button below to instantly launch the corresponding module:")

    btn1, btn2, btn3, btn4 = st.columns(4)

    with btn1:
        st.markdown("**🔍 Live Anomaly Scanner**")
        st.caption("Inspect declarations via .joblib ML, CSV upload, or OCR.")
        if st.button("Launch Live Scanner", key="go_scanner"):
            st.info("💡 Select **🔍 Multi-MEA Live Scanner** from the sidebar menu to proceed.")

    with btn2:
        st.markdown("**📈 Data Studio Catalogue**")
        st.caption("Access interactive Google Looker Studio reports.")
        if st.button("Launch Data Studio", key="go_studio"):
            st.info("💡 Select **📈 Data Studio & Catalogue** from the sidebar menu to proceed.")

    with btn3:
        st.markdown("**🤖 AI Legal Copilot**")
        st.caption("Query treaty statutes and HS Code regulations.")
        if st.button("Launch AI Copilot", key="go_copilot"):
            st.info("💡 Select **🤖 AI Legal Copilot** from the sidebar menu to proceed.")

    with btn4:
        st.markdown("**📞 HITL Review Queue**")
        st.caption("Multi-agency incident adjudication desk.")
        if st.button("Launch HITL Queue", key="go_hitl"):
            st.info("💡 Select **📞 Incident Escalation** from the sidebar menu to proceed.")
