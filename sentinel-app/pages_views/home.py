import streamlit as st
import pandas as pd
import plotly.express as px

def render_home_page():
    
    # --------------------------------------------------------------------------
    # 1. HERO SECTION: INTERACTIVE HTML5 NEURAL MESH (BRAND BLUE)
    # --------------------------------------------------------------------------
    html_hero = """
    <div style="position: relative; width: 100%; height: 320px; border-radius: 12px; overflow: hidden; background: linear-gradient(135deg, #FFFFFF 0%, #F1F5F9 100%); border: 1px solid #E2E8F0; margin-bottom: 1.5rem; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.03);">
        <canvas id="neuralCanvas" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></canvas>
        
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; pointer-events: none; width: 88%;">
            <div style="margin-bottom: 12px;">
                <span style="background: #FFFFFF; color: #1A365D; border: 1px solid #CBD5E1; padding: 5px 14px; border-radius: 4px; font-size: 0.75rem; font-weight: 700; font-family: 'JetBrains Mono', monospace; text-transform: uppercase; letter-spacing: 0.5px; box-shadow: 0 1px 2px rgba(0,0,0,0.04);">
                    NATIONAL TRADE COMPLIANCE ENGINE &middot; VERSION 2.4
                </span>
            </div>
            
            <h1 style="font-size: 2.3rem; font-weight: 800; color: #1A365D; margin: 0; letter-spacing: -0.5px; line-height: 1.2;">
                SENTINEL Intelligence Nexus
            </h1>
            
            <p style="font-size: 1.05rem; color: #475569; margin-top: 10px; font-weight: 500; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.5;">
                Centralized machine learning architecture screening cross-border shipments against Multilateral Environmental Agreements (MEAs). Automated detection of non-compliant waste, hazardous chemicals, and illicit trade flows.
            </p>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('neuralCanvas');
        const ctx = canvas.getContext('2d');
        let width, height;
        let particles = [];
        const mouse = { x: -9999, y: -9999 };

        function init() {
            width = canvas.width = canvas.offsetWidth;
            height = canvas.height = canvas.offsetHeight;
        }
        window.addEventListener('resize', init);
        init();

        canvas.addEventListener('mousemove', (e) => {
            const rect = canvas.getBoundingClientRect();
            mouse.x = e.clientX - rect.left;
            mouse.y = e.clientY - rect.top;
        });
        canvas.addEventListener('mouseleave', () => { mouse.x = -9999; mouse.y = -9999; });

        class Particle {
            constructor() {
                this.x = Math.random() * width;
                this.y = Math.random() * height;
                this.vx = (Math.random() - 0.5) * 0.6;
                this.vy = (Math.random() - 0.5) * 0.6;
                this.radius = Math.random() * 1.5 + 1;
            }
            update() {
                this.x += this.vx; this.y += this.vy;
                if (this.x < 0 || this.x > width) this.vx *= -1;
                if (this.y < 0 || this.y > height) this.vy *= -1;
            }
            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                ctx.fillStyle = 'rgba(26, 54, 93, 0.4)';
                ctx.fill();
            }
        }

        for (let i = 0; i < 90; i++) particles.push(new Particle());

        function animate() {
            ctx.clearRect(0, 0, width, height);
            for (let i = 0; i < particles.length; i++) {
                particles[i].update();
                particles[i].draw();
                
                const dxMouse = particles[i].x - mouse.x;
                const dyMouse = particles[i].y - mouse.y;
                const distMouse = Math.sqrt(dxMouse * dxMouse + dyMouse * dyMouse);
                if (distMouse < 140) {
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(mouse.x, mouse.y);
                    ctx.strokeStyle = `rgba(37, 99, 235, ${0.7 - distMouse/140})`;
                    ctx.lineWidth = 1.0;
                    ctx.stroke();
                }

                for (let j = i + 1; j < particles.length; j++) {
                    const dx = particles[i].x - particles[j].x;
                    const dy = particles[i].y - particles[j].y;
                    const dist = Math.sqrt(dx * dx + dy * dy);
                    if (dist < 100) {
                        ctx.beginPath();
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.strokeStyle = `rgba(148, 163, 184, ${0.25 - dist/400})`;
                        ctx.lineWidth = 0.5;
                        ctx.stroke();
                    }
                }
            }
            requestAnimationFrame(animate);
        }
        animate();
    </script>
    """
    st.components.v1.html(html_hero, height=330)

    # --------------------------------------------------------------------------
    # 2. DYNAMIC ACCESS LEVEL BANNER
    # --------------------------------------------------------------------------
    role = st.session_state.get("user_role", "Public (Free)")
    
    if role == "Public (Free)":
        st.markdown("<div class='tier-pill-public'><b>Access Clearance Level 1: Public Transparency Access</b> &mdash; Public statistics, treaty metrics, and threat mapping.</div>", unsafe_allow_html=True)
    elif role == "Gov Agency":
        st.markdown("<div class='tier-pill-gov'><b>Access Clearance Level 2: Inter-Agency Operational Access (JKDM/JAS/MITI)</b> &mdash; Unlocked ML Scanner, OCR Parser, and Escalation Queue.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='tier-pill-admin'><b>Access Clearance Level 3: Root Admin Access</b> &mdash; Unlocked BigQuery Warehouse (2020&ndash;2026), SHA-256 Checksums, and Model Controls.</div>", unsafe_allow_html=True)

    # Metric Row
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Audited Declarations", "142,890", "12.4% YoY")
    m2.metric("Overall Anomaly Rate", "4.12%", "-0.8% YoY")
    m3.metric("Container Interceptions", "382 Holds", "JKDM / JAS Actions")
    m4.metric("Active ML Models", "3 Live Pipelines", "2 In Sandbox")

    st.markdown("---")

    # --------------------------------------------------------------------------
    # 3. INTERACTIVE MEA IMPACT STUDIO (FIGMA BENTO GRID)
    # --------------------------------------------------------------------------
    st.markdown("### Interactive MEA Enforcement Impact Studio")
    st.caption("Select a treaty framework below to dynamically load enforcement parameters, target tariff domains, and trade volume dips:")

    selected_mea = st.radio(
        "Choose MEA Framework to Inspect:",
        ["Basel Convention", "Montreal Protocol", "CITES Framework", "Stockholm/Rotterdam"],
        horizontal=True
    )

    col_info, col_chart = st.columns([1, 1.25])

    with col_info:
        if "Basel" in selected_mea:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:4px solid #1A365D; border-radius:8px; padding:20px; box-shadow:0 1px 3px rgba(0,0,0,0.03);">
                <div class="figma-badge" style="margin-bottom:8px;">Protocol Scope: Hazardous Waste</div>
                <h4 style="margin:0 0 8px 0; color:#1A365D; font-size:1.15rem; font-weight:800;">Basel Convention</h4>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:6px;"><b>Target Tariff Domains:</b> HS 3915 (Plastic Scrap), HS 8548/8549 (E-Waste Slag)</p>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:6px;"><b>Lead Enforcement Agency:</b> Department of Environment (JAS) & JKDM Customs</p>
                <p style="font-size:0.82rem; color:#475569; margin:0;"><b>Inference Pipeline:</b> <code>plastic_forensic_pipeline.joblib</code></p>
            </div>
            """, unsafe_allow_html=True)
            dip_data = pd.DataFrame({"Month": ["Jan", "Feb", "Mar", "Apr (AI Live)", "May", "Jun", "Jul"], "Tons": [14200, 15800, 13900, 4100, 1200, 850, 410]})
            chart_title = "HS 3915.10 (Plastic Waste) Import Volume Dip"

        elif "Montreal" in selected_mea:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:4px solid #2563EB; border-radius:8px; padding:20px; box-shadow:0 1px 3px rgba(0,0,0,0.03);">
                <div class="figma-badge" style="margin-bottom:8px;">Protocol Scope: Ozone Layer</div>
                <h4 style="margin:0 0 8px 0; color:#1A365D; font-size:1.15rem; font-weight:800;">Montreal Protocol</h4>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:6px;"><b>Target Tariff Domains:</b> HS 2903 (CFCs, HCFCs, HFC Refrigerants)</p>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:6px;"><b>Lead Enforcement Agency:</b> JAS & MITI</p>
                <p style="font-size:0.82rem; color:#475569; margin:0;"><b>Inference Pipeline:</b> <code>ods_forensic_pipeline.joblib</code></p>
            </div>
            """, unsafe_allow_html=True)
            dip_data = pd.DataFrame({"Month": ["Jan", "Feb", "Mar", "Apr (AI Live)", "May", "Jun", "Jul"], "Tons": [8500, 9200, 8800, 2900, 950, 420, 180]})
            chart_title = "HS 2903.42 (HCFC-22 Gases) Import Volume Dip"

        elif "CITES" in selected_mea:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:4px solid #334155; border-radius:8px; padding:20px; box-shadow:0 1px 3px rgba(0,0,0,0.03);">
                <div class="figma-badge" style="margin-bottom:8px;">Protocol Scope: Species Protection</div>
                <h4 style="margin:0 0 8px 0; color:#1A365D; font-size:1.15rem; font-weight:800;">CITES Framework</h4>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:6px;"><b>Target Tariff Domains:</b> HS 0106 (Fauna), HS 4403 (Timber)</p>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:6px;"><b>Lead Enforcement Agency:</b> PERHILITAN & MAQIS</p>
                <p style="font-size:0.82rem; color:#475569; margin:0;"><b>Inference Pipeline:</b> <code>species_discrepancy.joblib</code></p>
            </div>
            """, unsafe_allow_html=True)
            dip_data = pd.DataFrame({"Month": ["Jan", "Feb", "Mar", "Apr (AI Live)", "May", "Jun", "Jul"], "Tons": [5400, 6100, 5800, 1800, 620, 310, 120]})
            chart_title = "HS 4403.49 (Protected Timber) Unlicensed Dip"

        else:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:4px solid #64748B; border-radius:8px; padding:20px; box-shadow:0 1px 3px rgba(0,0,0,0.03);">
                <div class="figma-badge" style="margin-bottom:8px;">Protocol Scope: Chemical Safety</div>
                <h4 style="margin:0 0 8px 0; color:#1A365D; font-size:1.15rem; font-weight:800;">Stockholm & Rotterdam</h4>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:6px;"><b>Target Tariff Domains:</b> POPs & Toxic Pesticides</p>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:6px;"><b>Lead Enforcement Agency:</b> Dept of Agriculture & JAS</p>
                <p style="font-size:0.82rem; color:#475569; margin:0;"><b>Inference Pipeline:</b> <code>chemical_index.joblib</code></p>
            </div>
            """, unsafe_allow_html=True)
            dip_data = pd.DataFrame({"Month": ["Jan", "Feb", "Mar", "Apr (AI Live)", "May", "Jun", "Jul"], "Tons": [3200, 3800, 3400, 920, 280, 110, 45]})
            chart_title = "Hazardous POP Chemicals Import Dip"

    with col_chart:
        fig_dip = px.line(dip_data, x="Month", y="Tons", markers=True, title=chart_title, color_discrete_sequence=["#1A365D"])
        fig_dip.update_layout(
            height=260, 
            margin=dict(l=10, r=10, t=35, b=10), 
            paper_bgcolor="rgba(0,0,0,0)", 
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Plus Jakarta Sans", size=12)
        )
        st.plotly_chart(fig_dip, use_container_width=True)

    st.markdown("---")

    # --------------------------------------------------------------------------
    # 4. IMMERSIVE THREAT MAP (LIGHT CARTO STYLE)
    # --------------------------------------------------------------------------
    st.markdown("### Real-Time Regional Threat Radar")
    st.caption("Geographical anomaly concentration mapped across Malaysian port checkpoints. Animated pulse indicators signal active holds.")

    leaflet_map_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
        <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
        <style>
            #map { height: 420px; width: 100%; border-radius: 8px; border: 1px solid #CBD5E1; box-shadow: 0 1px 3px rgba(0,0,0,0.03); }
            .pulse-icon-red {
                background: rgba(153, 27, 27, 0.9);
                border-radius: 50%;
                box-shadow: 0 0 0 rgba(153, 27, 27, 0.6);
                animation: pulse-red 2s infinite;
            }
            .pulse-icon-blue {
                background: rgba(30, 58, 138, 0.9);
                border-radius: 50%;
                box-shadow: 0 0 0 rgba(30, 58, 138, 0.6);
                animation: pulse-blue 2s infinite;
            }
            @keyframes pulse-red {
                0% { box-shadow: 0 0 0 0 rgba(153, 27, 27, 0.5); }
                70% { box-shadow: 0 0 0 16px rgba(153, 27, 27, 0); }
                100% { box-shadow: 0 0 0 0 rgba(153, 27, 27, 0); }
            }
            @keyframes pulse-blue {
                0% { box-shadow: 0 0 0 0 rgba(30, 58, 138, 0.5); }
                70% { box-shadow: 0 0 0 16px rgba(30, 58, 138, 0); }
                100% { box-shadow: 0 0 0 0 rgba(30, 58, 138, 0); }
            }
        </style>
    </head>
    <body>
        <div id="map"></div>
        <script>
            var map = L.map('map').setView([4.2, 108.0], 5.5);
            L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
                attribution: '&copy; OpenStreetMap'
            }).addTo(map);

            var ports = [
                {name: "Port Klang", lat: 3.00, lon: 101.40, desc: "High Risk Plastic Scrap (HS 3915)", type: "red"},
                {name: "Johor Port", lat: 1.45, lon: 103.75, desc: "Unlicensed ODS Gas (HS 2903)", type: "blue"},
                {name: "Penang Port", lat: 5.41, lon: 100.32, desc: "Illegal E-Waste (HS 8549)", type: "red"},
                {name: "Bintulu Port", lat: 4.58, lon: 114.00, desc: "Timber CITES Mismatch (HS 4403)", type: "blue"},
                {name: "KLIA Cargo", lat: 2.80, lon: 101.70, desc: "Chemical POPs Mismatch", type: "red"}
            ];

            ports.forEach(function(p) {
                var pulseMarker = L.divIcon({
                    className: p.type === 'red' ? 'pulse-icon-red' : 'pulse-icon-blue',
                    iconSize: [12, 12]
                });
                L.marker([p.lat, p.lon], {icon: pulseMarker}).addTo(map)
                    .bindPopup("<div style='font-family:sans-serif;'><b>" + p.name + "</b><br>" + p.desc + "</div>");
            });
        </script>
    </body>
    </html>
    """
    st.components.v1.html(leaflet_map_html, height=440)

    st.markdown("---")

    # --------------------------------------------------------------------------
    # 5. FIGMA BENTO BOKES QUICK LAUNCH
    # --------------------------------------------------------------------------
    st.markdown("### Platform Quick Launch Operations")
    st.caption("Direct operational module launch desk:")

    btn1, btn2, btn3, btn4 = st.columns(4)

    with btn1:
        st.button("Launch Live Scanner", key="go_scanner")
    with btn2:
        st.button("Launch Data Studio", key="go_studio")
    with btn3:
        st.button("Launch AI Copilot", key="go_copilot")
    with btn4:
        st.button("Launch HITL Queue", key="go_hitl")
