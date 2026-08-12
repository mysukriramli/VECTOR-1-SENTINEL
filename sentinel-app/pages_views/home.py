import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def render_home_page():
    
    # --------------------------------------------------------------------------
    # 1. HERO SECTION: INTERACTIVE HTML5 NEURAL CANVAS
    # --------------------------------------------------------------------------
    html_hero = """
    <div style="position: relative; width: 100%; height: 320px; border-radius: 12px; overflow: hidden; background: linear-gradient(135deg, #FFFFFF 0%, #F1F5F9 100%); border: 1px solid #E2E8F0; margin-bottom: 1.5rem; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.03);">
        <canvas id="neuralCanvas" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></canvas>
        
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; pointer-events: none; width: 88%;">
            <div style="margin-bottom: 12px;">
                <span style="background: #FFFFFF; color: #1A365D; border: 1px solid #CBD5E1; padding: 5px 14px; border-radius: 4px; font-size: 0.75rem; font-weight: 700; font-family: 'JetBrains Mono', monospace; text-transform: uppercase; letter-spacing: 0.5px; box-shadow: 0 1px 2px rgba(0,0,0,0.04);">
                    NATIONAL ENVIRONMENTAL TRADE COMPLIANCE ENGINE &middot; VERSION 2.4
                </span>
            </div>
            
            <h1 style="font-size: 2.3rem; font-weight: 800; color: #1A365D; margin: 0; letter-spacing: -0.5px; line-height: 1.2;">
                SENTINEL Trade Intelligence
            </h1>
            
            <p style="font-size: 1.05rem; color: #475569; margin-top: 10px; font-weight: 500; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.5;">
                Smart Environmental Nexus for Trade Intelligence and Networked Enforcement Logic
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
    # 2. DYNAMIC ACCESS LEVEL BANNER & METRICS
    # --------------------------------------------------------------------------
    role = st.session_state.get("user_role", "Public (Free)")
    
    if role == "Public (Free)":
        st.markdown("<div class='tier-pill-public'><b>Access Clearance Level 1: Public Transparency Access</b> &mdash; Public statistics, treaty metrics, and threat mapping.</div>", unsafe_allow_html=True)
    elif role == "Gov Agency":
        st.markdown("<div class='tier-pill-gov'><b>Access Clearance Level 2: Inter-Agency Operational Access (JKDM/JAS/MITI)</b> &mdash; Unlocked ML Scanner, OCR Parser, and Escalation Queue.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='tier-pill-admin'><b>Access Clearance Level 3: Root Admin Access</b> &mdash; Unlocked BigQuery Warehouse (2020&ndash;2026), SHA-256 Checksums, and Model Controls.</div>", unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Audited Declarations", "142,890", "12.4% YoY")
    m2.metric("Overall Anomaly Rate", "4.12%", "-0.8% YoY")
    m3.metric("Container Interceptions", "382 Holds", "JKDM / JAS Actions")
    m4.metric("Active ML Models", "3 Live Pipelines", "2 In Sandbox")

    st.markdown("---")

    # --------------------------------------------------------------------------
    # 3. REAL LOOKER STUDIO MEA ENFORCEMENT IMPACT STUDIO
    # --------------------------------------------------------------------------
    st.markdown("### Interactive MEA Enforcement Impact Studio")
    st.caption("Select a treaty framework below to dynamically load enforcement parameters, target tariff domains, and live Looker Studio analytics dashboards:")

    selected_mea = st.radio(
        "Choose MEA Framework to Inspect:",
        ["Basel Convention", "Montreal Protocol", "CITES Framework", "Stockholm / Rotterdam"],
        horizontal=True
    )

    col_info, col_chart = st.columns([1, 1.6])

    # Dynamic Metadata Card (Left Column)
    with col_info:
        if "Basel" in selected_mea:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:4px solid #1A365D; border-radius:8px; padding:20px; box-shadow:0 1px 3px rgba(0,0,0,0.03);">
                <div class="figma-badge" style="margin-bottom:8px;">Protocol Scope: Hazardous Waste</div>
                <h4 style="margin:0 0 8px 0; color:#1A365D; font-size:1.15rem; font-weight:800;">Basel Convention</h4>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:8px;"><b>Target Tariff Domains:</b> HS 3915 (Plastic Scrap), HS 8548/8549 (E-Waste Slag)</p>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:8px;"><b>Lead Enforcement Agency:</b> Department of Environment (JAS) & JKDM Customs</p>
                <p style="font-size:0.82rem; color:#475569; margin:0;"><b>Inference Pipeline:</b> <code>plastic_forensic_pipeline.joblib</code></p>
            </div>
            """, unsafe_allow_html=True)

        elif "Montreal" in selected_mea:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:4px solid #2563EB; border-radius:8px; padding:20px; box-shadow:0 1px 3px rgba(0,0,0,0.03);">
                <div class="figma-badge" style="margin-bottom:8px;">Protocol Scope: Ozone Layer</div>
                <h4 style="margin:0 0 8px 0; color:#1A365D; font-size:1.15rem; font-weight:800;">Montreal Protocol</h4>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:8px;"><b>Target Tariff Domains:</b> HS 2903 (CFCs, HCFCs, HFC Refrigerants)</p>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:8px;"><b>Lead Enforcement Agency:</b> JAS & MITI</p>
                <p style="font-size:0.82rem; color:#475569; margin:0;"><b>Inference Pipeline:</b> <code>ods_forensic_pipeline.joblib</code></p>
            </div>
            """, unsafe_allow_html=True)

        elif "CITES" in selected_mea:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:4px solid #334155; border-radius:8px; padding:20px; box-shadow:0 1px 3px rgba(0,0,0,0.03);">
                <div class="figma-badge" style="margin-bottom:8px;">Protocol Scope: Species Protection</div>
                <h4 style="margin:0 0 8px 0; color:#1A365D; font-size:1.15rem; font-weight:800;">CITES Framework</h4>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:8px;"><b>Target Tariff Domains:</b> HS 0106 (Fauna), HS 4403 (Timber)</p>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:8px;"><b>Lead Enforcement Agency:</b> PERHILITAN & MAQIS</p>
                <p style="font-size:0.82rem; color:#475569; margin:0;"><b>Inference Pipeline:</b> <code>species_discrepancy.joblib</code></p>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:4px solid #64748B; border-radius:8px; padding:20px; box-shadow:0 1px 3px rgba(0,0,0,0.03);">
                <div class="figma-badge" style="margin-bottom:8px;">Protocol Scope: Chemical Safety</div>
                <h4 style="margin:0 0 8px 0; color:#1A365D; font-size:1.15rem; font-weight:800;">Stockholm & Rotterdam</h4>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:8px;"><b>Target Tariff Domains:</b> POPs & Toxic Pesticides</p>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:8px;"><b>Lead Enforcement Agency:</b> Dept of Agriculture & JAS</p>
                <p style="font-size:0.82rem; color:#475569; margin:0;"><b>Inference Pipeline:</b> <code>chemical_index.joblib</code></p>
            </div>
            """, unsafe_allow_html=True)

    # Embedded Real Looker Studio Dashboards (Right Column)
    with col_chart:
        if "Basel" in selected_mea:
            tab_plastic, tab_ewaste = st.tabs(["Plastic Waste (HS 3915)", "E-Waste (HS 8548/8549)"])
            
            with tab_plastic:
                st.components.v1.iframe(
                    "https://datastudio.google.com/embed/reporting/02b9ef5e-618a-470c-bcaf-30d6ffd23487/page/HsE6F",
                    height=300,
                    scrolling=True
                )
            
            with tab_ewaste:
                st.components.v1.iframe(
                    "https://datastudio.google.com/embed/reporting/ac96d48a-de4a-487c-801d-0bf7e8c5b131/page/qzF6F",
                    height=300,
                    scrolling=True
                )

        elif "Montreal" in selected_mea:
            st.components.v1.iframe(
                "https://datastudio.google.com/embed/reporting/8092b01a-d260-434c-8ae1-8df045e4402c/page/x1F6F",
                height=300,
                scrolling=True
            )

        elif "CITES" in selected_mea:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px dashed #CBD5E1; border-radius:8px; padding:40px; text-align:center; min-height:380px; display:flex; flex-direction:column; justify-content:center; align-items:center;">
                <div style="font-size:0.85rem; font-weight:800; color:#2563EB; font-family:'JetBrains Mono', monospace; text-transform:uppercase; letter-spacing:1px; margin-bottom:8px;">
                    SYSTEM STATUS: UNDER CONSTRUCTION
                </div>
                <div style="font-size:1.1rem; font-weight:800; color:#1A365D; margin-bottom:6px;">
                    CITES Framework Timber & Wildlife Dashboard
                </div>
                <div style="font-size:0.85rem; color:#64748B; max-width:480px;">
                    Data pipeline synchronization in progress. BigQuery historical tables are active; Looker Studio reporting canvas is currently being provisioned for production release.
                </div>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px dashed #CBD5E1; border-radius:8px; padding:40px; text-align:center; min-height:380px; display:flex; flex-direction:column; justify-content:center; align-items:center;">
                <div style="font-size:0.85rem; font-weight:800; color:#2563EB; font-family:'JetBrains Mono', monospace; text-transform:uppercase; letter-spacing:1px; margin-bottom:8px;">
                    SYSTEM STATUS: UNDER CONSTRUCTION
                </div>
                <div style="font-size:1.1rem; font-weight:800; color:#1A365D; margin-bottom:6px;">
                    Stockholm & Rotterdam POPs Chemical Dashboard
                </div>
                <div style="font-size:0.85rem; color:#64748B; max-width:480px;">
                    Data pipeline synchronization in progress. BigQuery historical tables are active; Looker Studio reporting canvas is currently being provisioned for production release.
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # --------------------------------------------------------------------------
    # 4. MULTI-MEA TACTICAL THREAT MATRIX & INTERACTIVE RADAR CHART
    # --------------------------------------------------------------------------
    st.markdown("### Multi-MEA Tactical Threat Matrix & Interactive Radar")
    st.caption("Cross-treaty multi-variable risk signature mapping active 30-day threat profiles against 5-year BigQuery baseline averages.")

    # Checkpoint Data Dictionary
    radar_port_data = {
        "National Aggregate (Malaysia Border Baseline)": {
            "axes": ["Basel Waste Index", "Montreal Quota Index", "CITES Integrity Index", "Stockholm POPs Index", "OCR Anomaly Score", "Entity Route Risk"],
            "active": [72, 68, 55, 60, 65, 58],
            "baseline": [85, 82, 62, 70, 78, 68],
            "primary_threat": "Multi-MEA Co-occurrence (Basel HS 3915 & Montreal HS 2903)",
            "action": "Maintain Level-2 automated screening across major container hubs. Execute random physical sampling on high-density imports.",
            "law": "Customs Act 1967 & Environmental Quality Act 1974 (Act 127)",
            "health_score": "71.2 / 100"
        },
        "Port Klang (Selangor)": {
            "axes": ["Basel Waste Index", "Montreal Quota Index", "CITES Integrity Index", "Stockholm POPs Index", "OCR Anomaly Score", "Entity Route Risk"],
            "active": [94, 42, 35, 48, 88, 85],
            "baseline": [98, 50, 40, 52, 92, 89],
            "primary_threat": "Critical Basel Convention Violation (HS 3915 Plastic Scrap & E-Waste Slag)",
            "action": "Issue Immediate Physical Detention Order. Dispatch Joint JAS-JKDM Inspection Team with density/value probes.",
            "law": "Environmental Quality Act 1974 (Act 127) Sec 34A & Customs Prohibition Order",
            "health_score": "88.4 / 100"
        },
        "Johor Port (Pasir Gudang)": {
            "axes": ["Basel Waste Index", "Montreal Quota Index", "CITES Integrity Index", "Stockholm POPs Index", "OCR Anomaly Score", "Entity Route Risk"],
            "active": [52, 91, 28, 85, 76, 78],
            "baseline": [60, 95, 30, 88, 80, 82],
            "primary_threat": "Elevated Montreal Protocol & Stockholm POPs Discrepancy (HS 2903 Refrigerants)",
            "action": "Dispatch Field Team with Portable Gas Analyzer. Cross-reference MITI Import Quotas via MyGDX API.",
            "law": "Customs (Prohibition of Imports) Order & Environmental Quality (ODS) Reg 1999",
            "health_score": "79.2 / 100"
        },
        "Penang Port (Butterworth)": {
            "axes": ["Basel Waste Index", "Montreal Quota Index", "CITES Integrity Index", "Stockholm POPs Index", "OCR Anomaly Score", "Entity Route Risk"],
            "active": [86, 38, 22, 40, 82, 80],
            "baseline": [92, 45, 25, 45, 88, 86],
            "primary_threat": "E-Waste Slag Misdeclaration & Unit Value Outlier (HS 8548/8549)",
            "action": "Execute Full Container Inspection. Verify scrap metal vs. electronic waste classification.",
            "law": "Environmental Quality Act 1974 (Act 127) & Customs Act 1967 Sec 133",
            "health_score": "82.1 / 100"
        },
        "Bintulu Port (Sarawak)": {
            "axes": ["Basel Waste Index", "Montreal Quota Index", "CITES Integrity Index", "Stockholm POPs Index", "OCR Anomaly Score", "Entity Route Risk"],
            "active": [25, 20, 82, 30, 62, 55],
            "baseline": [30, 25, 88, 35, 68, 60],
            "primary_threat": "CITES Timber Species Volume Discrepancy (HS 4403/4407)",
            "action": "Verify CITES Export Permits with PERHILITAN/Sarawak Forestry. Conduct Volumetric Timber Audit.",
            "law": "International Trade in Endangered Species Act 2008 (Act 686)",
            "health_score": "64.5 / 100"
        },
        "KLIA Air Cargo Complex": {
            "axes": ["Basel Waste Index", "Montreal Quota Index", "CITES Integrity Index", "Stockholm POPs Index", "OCR Anomaly Score", "Entity Route Risk"],
            "active": [35, 62, 88, 82, 90, 84],
            "baseline": [40, 68, 92, 86, 94, 88],
            "primary_threat": "High-Value CITES Wildlife Contraband & Undeclared Toxic Pesticides",
            "action": "Deploy PERHILITAN K9 Sniffer Unit & DOA Hazardous Substance Inspection Desk.",
            "law": "Act 686 & Pesticides Act 1974 (Act 149)",
            "health_score": "85.0 / 100"
        }
    }

    # Checkpoint Switcher
    col_sel1, col_sel2 = st.columns([2, 1])
    with col_sel1:
        selected_checkpoint = st.selectbox(
            "Select Entry Checkpoint / Jurisdiction:",
            list(radar_port_data.keys()),
            index=1
        )

    port_info = radar_port_data[selected_checkpoint]

    # Layout: Radar Chart (Left) vs. Directive Panel (Right)
    col_radar, col_directive = st.columns([1.3, 1])

    with col_radar:
        axes = port_info["axes"]
        active_val = port_info["active"]
        base_val = port_info["baseline"]

        fig_radar = go.Figure()

        # Historical 5-Year Baseline Polygon
        fig_radar.add_trace(go.Scatterpolar(
            r=base_val + [base_val[0]],
            theta=axes + [axes[0]],
            fill='toself',
            fillcolor='rgba(100, 116, 139, 0.1)',
            line=dict(color='#64748B', width=2, dash='dash'),
            name='5-Year Baseline Avg (2020-2025)'
        ))

        # Active 30-Day Threat Polygon
        fig_radar.add_trace(go.Scatterpolar(
            r=active_val + [active_val[0]],
            theta=axes + [axes[0]],
            fill='toself',
            fillcolor='rgba(26, 54, 93, 0.28)',
            line=dict(color='#1A365D', width=3),
            name='Active 30-Day Risk Level'
        ))

        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                    tickfont=dict(size=10, color="#64748B"),
                    gridcolor="#E2E8F0"
                ),
                angularaxis=dict(
                    tickfont=dict(size=11, color="#0F172A", weight="bold"),
                    gridcolor="#E2E8F0"
                ),
                bgcolor="rgba(255, 255, 255, 0.9)"
            ),
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.2,
                xanchor="center",
                x=0.5
            ),
            margin=dict(l=40, r=40, t=20, b=40),
            height=380,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(fig_radar, use_container_width=True)

    with col_directive:
        st.markdown(f"""
        <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:4px solid #1A365D; border-radius:8px; padding:20px; box-shadow:0 1px 3px rgba(0,0,0,0.03); height:100%;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                <span class="figma-badge">TACTICAL INTERDICTION DIRECTIVE</span>
                <span style="font-size:0.85rem; font-weight:800; color:#1A365D; font-family:'JetBrains Mono', monospace;">RISK INDEX: {port_info['health_score']}</span>
            </div>
            
            <h5 style="margin:0 0 12px 0; color:#1A365D; font-weight:800; font-size:1.1rem;">{selected_checkpoint}</h5>
            
            <div style="margin-bottom:14px;">
                <div style="font-size:0.75rem; font-weight:700; color:#64748B; text-transform:uppercase; letter-spacing:0.5px;">Primary Multi-MEA Threat:</div>
                <div style="font-size:0.88rem; font-weight:700; color:#0F172A; margin-top:3px;">{port_info['primary_threat']}</div>
            </div>

            <div style="margin-bottom:14px;">
                <div style="font-size:0.75rem; font-weight:700; color:#64748B; text-transform:uppercase; letter-spacing:0.5px;">Mandatory Tactical Action:</div>
                <div style="font-size:0.85rem; color:#334155; margin-top:3px; line-height:1.4;">{port_info['action']}</div>
            </div>

            <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:6px; padding:12px; margin-top:16px;">
                <div style="font-size:0.72rem; font-weight:700; color:#475569; text-transform:uppercase; letter-spacing:0.5px;">Statutory Enforcement Authority:</div>
                <div style="font-size:0.82rem; font-weight:700; color:#1E3A8A; margin-top:3px;">{port_info['law']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # --------------------------------------------------------------------------
    # 5. QUICK LAUNCH DESK
    # --------------------------------------------------------------------------
    st.markdown("### Platform Quick Launch Operations")
    st.caption("Instantly navigate to operational modules:")

    btn1, btn2, btn3, btn4 = st.columns(4)

    with btn1:
        st.button("Launch Live Scanner", key="go_scanner")
    with btn2:
        st.button("Launch Data Studio", key="go_studio")
    with btn3:
        st.button("Launch AI Copilot", key="go_copilot")
    with btn4:
        st.button("Launch HITL Queue", key="go_hitl")
