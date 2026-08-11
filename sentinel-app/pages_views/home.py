import streamlit as st
import pandas as pd
import plotly.express as px

def render_home_page():
    # --------------------------------------------------------------------------
    # 1. LIVE TELEMETRY TICKER
    # --------------------------------------------------------------------------
    st.markdown("""
    <div class="live-ticker-container">
        <span class="ticker-tag">⚡ Live Telemetry</span>
        <span class="ticker-text">
            [09:14 AM] Container #KLU-8820 Held @ Port Klang (Plastic Scrap HS 3915) &nbsp;|&nbsp; 
            [11:30 AM] ODS Gas Discrepancy Flagged @ Johor Port (HCFC-22) &nbsp;|&nbsp; 
            [01:05 PM] E-Waste Manifest Intercepted @ Penang Port
        </span>
    </div>
    """, unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # 2. HERO DEFINITION NEXUS
    # --------------------------------------------------------------------------
    st.markdown("""
    <div class="hero-nexus">
        <div class="hero-nexus-title">🛡️ SENTINEL Environmental Trade Intelligence Engine</div>
        <div class="hero-nexus-sub">
            Malaysia's central AI-powered command portal for monitoring cross-border trade compliance under 
            <b>Multilateral Environmental Agreements (MEAs)</b>. SENTINEL integrates real-time machine learning, 
            OCR document verification, and inter-agency data sharing across <b>JKDM, JAS, MITI, and PERHILITAN</b>.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # 3. DYNAMIC TIER ACCESS BADGE
    # --------------------------------------------------------------------------
    role = st.session_state.get("user_role", "Public (Free)")
    
    if role == "Public (Free)":
        st.markdown("""
        <div class="tier-badge-public">
            🟢 <b>Tier 1: Public Transparency Access</b> — Inspecting public treaty statistics, environmental trade impact metrics, and port threat heatmaps.
        </div>
        """, unsafe_allow_html=True)
    elif role == "Gov Agency":
        st.markdown("""
        <div class="tier-badge-gov">
            🔵 <b>Tier 2: Inter-Agency Operational Access (JKDM / JAS / MITI)</b> — Unlocked Live .joblib ML Scanner, OCR Form Parser, and Multi-Agency Review Queue.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="tier-badge-admin">
            🔴 <b>Tier 3: Root Admin Governance Access</b> — Unlocked BigQuery Data Warehouse (2020–2026), SHA-256 Checksums, and Model Sensitivity Calibration.
        </div>
        """, unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # 4. EXECUTIVE METRICS CARDS
    # --------------------------------------------------------------------------
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Audited Declarations", "142,890", "↑ 12.4% YoY")
    m2.metric("Overall Anomaly Rate", "4.12%", "↓ 0.8% YoY")
    m3.metric("Container Interceptions", "382 Holds", "JKDM / JAS Actions")
    m4.metric("Active ML Models", "3 Deployed", "2 In Sandbox")

    st.markdown("---")

    # --------------------------------------------------------------------------
    # 5. DYNAMIC INTERACTIVE MEA PROTOCOL IMPACT STUDIO
    # --------------------------------------------------------------------------
    st.markdown("### 📜 Interactive MEA Enforcement Impact Studio")
    st.caption("Select a treaty framework below to view its target HS codes, lead agencies, and real-time import volume dips post-enforcement:")

    # Interactive Protocol Selector Pills
    selected_mea = st.radio(
        "Choose MEA Framework to Inspect:",
        ["♻️ Basel Convention (Plastic & E-Waste)", "❄️ Montreal Protocol (ODS Gases)", "🌿 CITES Framework (Wildlife & Timber)", "🧪 Stockholm & Rotterdam (POPs)"],
        horizontal=True
    )

    col_info, col_chart = st.columns([1, 1.2])

    with col_info:
        if "Basel" in selected_mea:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:5px solid #2563EB; border-radius:10px; padding:18px;">
                <h4 style="margin:0 0 6px 0; color:#0F172A;">♻️ Basel Convention</h4>
                <div style="color:#2563EB; font-weight:700; font-size:0.88rem;">Control of Transboundary Hazardous Wastes</div>
                <hr style="margin:10px 0; border-color:#E2E8F0;">
                <p style="font-size:0.85rem; color:#334155; margin-bottom:6px;"><b>Target Tariff Domains:</b> HS 3915 (Plastic Scrap), HS 8548/8549 (E-Waste Slag)</p>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:6px;"><b>Lead Enforcement Agency:</b> Jabatan Alam Sekitar (JAS) & JKDM Customs</p>
                <p style="font-size:0.82rem; color:#64748B;"><b>AI Model Pipeline:</b> <code>plastic_forensic_pipeline.joblib</code></p>
            </div>
            """, unsafe_allow_html=True)
            
            # Data for Basel
            dip_data = pd.DataFrame({
                "Month": ["Jan", "Feb", "Mar", "Apr (AI Live)", "May", "Jun", "Jul"],
                "Import Volume (Tons)": [14200, 15800, 13900, 4100, 1200, 850, 410]
            })
            chart_title = "HS 3915.10 (Plastic Waste) Import Volume Dip"

        elif "Montreal" in selected_mea:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:5px solid #0284C7; border-radius:10px; padding:18px;">
                <h4 style="margin:0 0 6px 0; color:#0F172A;">❄️ Montreal Protocol</h4>
                <div style="color:#0284C7; font-weight:700; font-size:0.88rem;">Ozone Depleting Substances (ODS)</div>
                <hr style="margin:10px 0; border-color:#E2E8F0;">
                <p style="font-size:0.85rem; color:#334155; margin-bottom:6px;"><b>Target Tariff Domains:</b> HS 2903 (CFCs, HCFCs, HFC Refrigerants)</p>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:6px;"><b>Lead Enforcement Agency:</b> JAS & MITI</p>
                <p style="font-size:0.82rem; color:#64748B;"><b>AI Model Pipeline:</b> <code>ods_forensic_pipeline.joblib</code></p>
            </div>
            """, unsafe_allow_html=True)

            dip_data = pd.DataFrame({
                "Month": ["Jan", "Feb", "Mar", "Apr (AI Live)", "May", "Jun", "Jul"],
                "Import Volume (Tons)": [8500, 9200, 8800, 2900, 950, 420, 180]
            })
            chart_title = "HS 2903.42 (HCFC-22 Gases) Import Volume Dip"

        elif "CITES" in selected_mea:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:5px solid #059669; border-radius:10px; padding:18px;">
                <h4 style="margin:0 0 6px 0; color:#0F172A;">🌿 CITES Framework</h4>
                <div style="color:#059669; font-weight:700; font-size:0.88rem;">Endangered Species & Timber Trade</div>
                <hr style="margin:10px 0; border-color:#E2E8F0;">
                <p style="font-size:0.85rem; color:#334155; margin-bottom:6px;"><b>Target Tariff Domains:</b> HS 0106 (Fauna), HS 4403/4407 (Timber)</p>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:6px;"><b>Lead Enforcement Agency:</b> PERHILITAN & MAQIS</p>
                <p style="font-size:0.82rem; color:#64748B;"><b>AI Model Pipeline:</b> Species Discrepancy Classifier</p>
            </div>
            """, unsafe_allow_html=True)

            dip_data = pd.DataFrame({
                "Month": ["Jan", "Feb", "Mar", "Apr (AI Live)", "May", "Jun", "Jul"],
                "Import Volume (Tons)": [5400, 6100, 5800, 1800, 620, 310, 120]
            })
            chart_title = "HS 4403.49 (Protected Timber) Unlicensed Import Dip"

        else:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:5px solid #7C3AED; border-radius:10px; padding:18px;">
                <h4 style="margin:0 0 6px 0; color:#0F172A;">🧪 Stockholm & Rotterdam</h4>
                <div style="color:#7C3AED; font-weight:700; font-size:0.88rem;">POPs & Hazardous Chemicals</div>
                <hr style="margin:10px 0; border-color:#E2E8F0;">
                <p style="font-size:0.85rem; color:#334155; margin-bottom:6px;"><b>Target Tariff Domains:</b> Persistent Organic Pollutants & Toxic Pesticides</p>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:6px;"><b>Lead Enforcement Agency:</b> Department of Agriculture & JAS</p>
                <p style="font-size:0.82rem; color:#64748B;"><b>AI Model Pipeline:</b> Chemical Index Classifier</p>
            </div>
            """, unsafe_allow_html=True)

            dip_data = pd.DataFrame({
                "Month": ["Jan", "Feb", "Mar", "Apr (AI Live)", "May", "Jun", "Jul"],
                "Import Volume (Tons)": [3200, 3800, 3400, 920, 280, 110, 45]
            })
            chart_title = "Hazardous POP Chemicals Import Volume Dip"

    with col_chart:
        fig_dip = px.line(
            dip_data, 
            x="Month", 
            y="Import Volume (Tons)",
            markers=True,
            title=chart_title,
            color_discrete_sequence=["#2563EB"]
        )
        fig_dip.update_layout(height=260, margin=dict(l=10, r=10, t=35, b=10))
        st.plotly_chart(fig_dip, use_container_width=True)

    st.markdown("---")

    # --------------------------------------------------------------------------
    # 6. ANIMATED SOFT-PULSE THREAT RADAR MAP
    # --------------------------------------------------------------------------
    st.markdown("### 🌍 Real-Time Regional Threat Radar")
    st.caption("Live geographical threat score distribution across Malaysian maritime ports and cargo hubs:")

    leaflet_map_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
        <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
        <style>
            #map { height: 380px; width: 100%; border-radius: 12px; border: 1px solid #CBD5E1; }
            .pulse-icon {
                background: rgba(220, 38, 38, 0.9);
                border-radius: 50%;
                box-shadow: 0 0 0 rgba(220, 38, 38, 0.7);
                animation: pulse-ring 1.8s infinite;
            }
            @keyframes pulse-ring {
                0% { box-shadow: 0 0 0 0 rgba(220, 38, 38, 0.7); }
                70% { box-shadow: 0 0 0 16px rgba(220, 38, 38, 0); }
                100% { box-shadow: 0 0 0 0 rgba(220, 38, 38, 0); }
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
                {name: "Port Klang", lat: 3.00, lon: 101.40, desc: "High Risk Plastic Scrap (HS 3915.10)"},
                {name: "Johor Port", lat: 1.45, lon: 103.75, desc: "Unlicensed ODS Gas (HS 2903.42)"},
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
    # 7. QUICK LAUNCH OPERATIONS DESK
    # --------------------------------------------------------------------------
    st.markdown("### 🚀 Quick Launch Operations Desk")
    st.caption("Launch platform capabilities directly:")

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
