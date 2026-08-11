import streamlit as st
import pandas as pd
import plotly.express as px

def render_home_page():
    # --------------------------------------------------------------------------
    # 1. IMMERSIVE INTERACTIVE HERO CANVAS (PARTICLE NETWORK)
    # --------------------------------------------------------------------------
    hero_canvas_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <style>
            body, html { margin: 0; padding: 0; width: 100%; height: 100%; overflow: hidden; background-color: #0b1121; font-family: 'Inter', sans-serif; }
            #canvas1 { position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; }
            .hero-content {
                position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
                text-align: center; z-index: 2; pointer-events: none; width: 100%;
            }
            .title { font-size: 3.5rem; font-weight: 800; color: #ffffff; margin: 0; letter-spacing: -1px; text-shadow: 0px 4px 20px rgba(59, 130, 246, 0.5); }
            .subtitle { font-size: 1.1rem; color: #94A3B8; font-family: monospace; letter-spacing: 3px; margin-top: 10px; }
            .badge { display: inline-block; background: rgba(37, 99, 235, 0.2); border: 1px solid rgba(37, 99, 235, 0.5); padding: 6px 16px; border-radius: 20px; color: #60A5FA; font-size: 0.8rem; font-weight: 700; margin-bottom: 15px; }
        </style>
    </head>
    <body>
        <canvas id="canvas1"></canvas>
        <div class="hero-content">
            <div class="badge">● AI ENGINE ONLINE</div>
            <h1 class="title">SENTINEL</h1>
            <div class="subtitle">NATIONAL ENVIRONMENTAL TRADE INTELLIGENCE HUB</div>
        </div>
        <script>
            const canvas = document.getElementById("canvas1");
            const ctx = canvas.getContext("2d");
            canvas.width = window.innerWidth; canvas.height = window.innerHeight;
            let particlesArray;
            let mouse = { x: null, y: null, radius: 120 };

            window.addEventListener('mousemove', function(event) {
                mouse.x = event.x; mouse.y = event.y;
            });
            window.addEventListener('mouseout', function() {
                mouse.x = undefined; mouse.y = undefined;
            });

            class Particle {
                constructor(x, y, directionX, directionY, size, color) {
                    this.x = x; this.y = y; this.directionX = directionX; this.directionY = directionY; this.size = size; this.color = color;
                }
                draw() {
                    ctx.beginPath(); ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2, false);
                    ctx.fillStyle = '#3b82f6'; ctx.fill();
                }
                update() {
                    if (this.x > canvas.width || this.x < 0) this.directionX = -this.directionX;
                    if (this.y > canvas.height || this.y < 0) this.directionY = -this.directionY;
                    let dx = mouse.x - this.x; let dy = mouse.y - this.y;
                    let distance = Math.sqrt(dx*dx + dy*dy);
                    if (distance < mouse.radius + this.size){
                        if (mouse.x < this.x && this.x < canvas.width - this.size * 10) this.x += 2;
                        if (mouse.x > this.x && this.x > this.size * 10) this.x -= 2;
                        if (mouse.y < this.y && this.y < canvas.height - this.size * 10) this.y += 2;
                        if (mouse.y > this.y && this.y > this.size * 10) this.y -= 2;
                    }
                    this.x += this.directionX; this.y += this.directionY;
                    this.draw();
                }
            }
            function init() {
                particlesArray = [];
                let numberOfParticles = (canvas.height * canvas.width) / 8000;
                for (let i = 0; i < numberOfParticles; i++) {
                    let size = (Math.random() * 2) + 1;
                    let x = (Math.random() * ((innerWidth - size * 2) - (size * 2)) + size * 2);
                    let y = (Math.random() * ((innerHeight - size * 2) - (size * 2)) + size * 2);
                    let directionX = (Math.random() * 1.5) - 0.75;
                    let directionY = (Math.random() * 1.5) - 0.75;
                    particlesArray.push(new Particle(x, y, directionX, directionY, size, '#3b82f6'));
                }
            }
            function connect() {
                let opacityValue = 1;
                for (let a = 0; a < particlesArray.length; a++) {
                    for (let b = a; b < particlesArray.length; b++) {
                        let distance = ((particlesArray[a].x - particlesArray[b].x) * (particlesArray[a].x - particlesArray[b].x))
                        + ((particlesArray[a].y - particlesArray[b].y) * (particlesArray[a].y - particlesArray[b].y));
                        if (distance < (canvas.width/7) * (canvas.height/7)) {
                            opacityValue = 1 - (distance/15000);
                            ctx.strokeStyle = 'rgba(59, 130, 246,' + opacityValue + ')';
                            ctx.lineWidth = 1.2; ctx.beginPath();
                            ctx.moveTo(particlesArray[a].x, particlesArray[a].y);
                            ctx.lineTo(particlesArray[b].x, particlesArray[b].y); ctx.stroke();
                        }
                    }
                }
            }
            function animate() {
                requestAnimationFrame(animate);
                ctx.clearRect(0, 0, innerWidth, innerHeight);
                for (let i = 0; i < particlesArray.length; i++) particlesArray[i].update();
                connect();
            }
            window.addEventListener('resize', function() { canvas.width = innerWidth; canvas.height = innerHeight; init(); });
            init(); animate();
        </script>
    </body>
    </html>
    """
    # Render the interactive canvas (Hide Streamlit's default padding to make it flush)
    st.components.v1.html(hero_canvas_html, height=380)

    # --------------------------------------------------------------------------
    # 2. CLEAR TIER DEFINITIONS (Overrides the visual gap seamlessly)
    # --------------------------------------------------------------------------
    role = st.session_state.get("user_role", "Public (Free)")
    
    if role == "Public (Free)":
        st.markdown("""
        <div class="tier-card tier-public">
            <div class="tier-title">🟢 Public Transparency Access</div>
            <div class="tier-desc">Welcome to SENTINEL. You are viewing public compliance data, regional threat mapping, and inter-agency enforcement statistics. This tier promotes national accountability and environmental treaty transparency.</div>
        </div>
        """, unsafe_allow_html=True)
    elif role == "Gov Agency":
        st.markdown("""
        <div class="tier-card tier-gov">
            <div class="tier-title">🔵 Inter-Agency Operational Access</div>
            <div class="tier-desc">Welcome Officer. SENTINEL empowers JKDM, JAS, MITI, and PERHILITAN with live AI anomaly scanners, OCR manifest extraction, and the Human-in-the-Loop multi-agency incident escalation queue.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="tier-card tier-admin">
            <div class="tier-title">🔴 Root Admin Governance Access</div>
            <div class="tier-desc">Governance Hub Unlocked. You have full systemic clearance to audit the BigQuery 2020-2026 data warehouse, verify ML SHA-256 cryptographic signatures, and recalibrate enforcement contamination thresholds.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # 3. EXECUTIVE PLATFORM METRICS
    # --------------------------------------------------------------------------
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Audited Declarations", "142,890", "↑ 12.4% YoY")
    m2.metric("Overall Anomaly Rate", "4.12%", "↓ 0.8% YoY")
    m3.metric("Container Interceptions", "382 Holds", "JKDM / JAS Actions")
    m4.metric("Active ML Models", "3 Live Pipelines", "2 In Sandbox")

    st.markdown("---")

    # --------------------------------------------------------------------------
    # 4. SIDE-BY-SIDE: MEAs & DATA STUDIO EMBED
    # --------------------------------------------------------------------------
    st.markdown("### 📜 Multilateral Environmental Agreements (MEAs)")
    st.caption("SENTINEL enforces intelligence protocols across four international environmental treaties.")

    col_meas, col_chart = st.columns([1, 1.2])

    with col_meas:
        st.markdown("""
        <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px; margin-bottom:12px; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
            <div style="font-size:1.0rem; font-weight:800; color:#0F172A;">♻️ Basel Convention</div>
            <div style="font-size:0.8rem; color:#475569;"><b>Focus:</b> Plastic Scrap (HS 3915) & E-Waste (HS 8548)</div>
        </div>
        <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px; margin-bottom:12px; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
            <div style="font-size:1.0rem; font-weight:800; color:#0F172A;">❄️ Montreal Protocol</div>
            <div style="font-size:0.8rem; color:#475569;"><b>Focus:</b> Ozone Depleting Substances (HS 2903)</div>
        </div>
        <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px; margin-bottom:12px; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
            <div style="font-size:1.0rem; font-weight:800; color:#0F172A;">🌿 CITES Framework</div>
            <div style="font-size:0.8rem; color:#475569;"><b>Focus:</b> Wildlife & Protected Timber (HS 4403)</div>
        </div>
        <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:8px; padding:14px; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
            <div style="font-size:1.0rem; font-weight:800; color:#0F172A;">🧪 Stockholm & Rotterdam</div>
            <div style="font-size:0.8rem; color:#475569;"><b>Focus:</b> POPs & Hazardous Toxic Chemicals</div>
        </div>
        """, unsafe_allow_html=True)

    with col_chart:
        # Trade Dip Analytics for Banned HS Code (Basel Convention)
        st.markdown("<div style='font-size:1rem; font-weight:700; color:#0F172A; margin-bottom:10px;'>📊 Public Analytics: Enforcement Impact on HS 3915.10</div>", unsafe_allow_html=True)
        
        dip_df = pd.DataFrame({
            "Month": ["Jan", "Feb", "Mar", "Apr (AI Live)", "May", "Jun", "Jul"],
            "Import Volume (Metric Tons)": [14200, 15800, 13900, 4100, 1200, 850, 410]
        })

        fig_dip = px.area(
            dip_df, 
            x="Month", 
            y="Import Volume (Metric Tons)",
            markers=True,
            color_discrete_sequence=["#10B981"]
        )
        fig_dip.update_layout(
            height=280, 
            margin=dict(l=0, r=0, t=10, b=0),
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            yaxis=dict(gridcolor='#E2E8F0')
        )
        st.plotly_chart(fig_dip, use_container_width=True)

    st.markdown("---")

    # --------------------------------------------------------------------------
    # 5. ANIMATED SOFT-GLOW LEAFLET THREAT MAP
    # --------------------------------------------------------------------------
    st.markdown("### 🌍 Real-Time Regional Threat Radar")
    st.caption("Hover over pulsing nodes to inspect active anomalies at Malaysian ports.")

    leaflet_map_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
        <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
        <style>
            #map { height: 420px; width: 100%; border-radius: 12px; border: 1px solid #E2E8F0; }
            .pulse-icon {
                background: rgba(220, 38, 38, 1);
                border-radius: 50%;
                box-shadow: 0 0 0 rgba(220, 38, 38, 0.7);
                animation: pulse-ring 2s infinite;
            }
            @keyframes pulse-ring {
                0% { box-shadow: 0 0 0 0 rgba(220, 38, 38, 0.7); }
                70% { box-shadow: 0 0 0 18px rgba(220, 38, 38, 0); }
                100% { box-shadow: 0 0 0 0 rgba(220, 38, 38, 0); }
            }
            .leaflet-popup-content { font-family: 'Inter', sans-serif; font-size: 14px; }
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
                var pulseMarker = L.divIcon({ className: 'pulse-icon', iconSize: [12, 12] });
                L.marker([p.lat, p.lon], {icon: pulseMarker}).addTo(map)
                    .bindPopup("<b>" + p.name + "</b><br><span style='color:#DC2626; font-weight:bold;'>" + p.desc + "</span>");
            });
        </script>
    </body>
    </html>
    """
    st.components.v1.html(leaflet_map_html, height=440)

    st.markdown("---")

    # --------------------------------------------------------------------------
    # 6. QUICK LAUNCH DESK
    # --------------------------------------------------------------------------
    st.markdown("### 🚀 Operations Quick Launch")
    
    col_q1, col_q2, col_q3, col_q4 = st.columns(4)
    with col_q1:
        if st.button("🔍 Live Scanner"): st.info("Use the sidebar menu to navigate.")
    with col_q2:
        if st.button("📈 Data Studio"): st.info("Use the sidebar menu to navigate.")
    with col_q3:
        if st.button("🤖 AI Copilot"): st.info("Use the sidebar menu to navigate.")
    with col_q4:
        if st.button("📞 HITL Queue"): st.info("Use the sidebar menu to navigate.")
