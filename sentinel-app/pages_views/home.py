import streamlit as st

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
    # 4. 24/7 CONTINUOUS MEA STREAM SCANNING RADAR & LIVE TRADE COUNTER
    # --------------------------------------------------------------------------
    st.markdown("### 24/7 Continuous MEA Stream Scanning Radar")
    st.caption("Real-time AI pipeline continuously evaluating active customs manifest feeds across five core Multilateral Environmental Agreement (MEA) vectors.")

    html_radar_grid = """
    <div style="position: relative; width: 100%; height: 420px; border-radius: 12px; overflow: hidden; background: #FFFFFF; border: 1px solid #CBD5E1; box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);">
        <canvas id="radarCanvas" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></canvas>
        
        <!-- TOP LEFT STATUS PANEL -->
        <div style="position: absolute; top: 16px; left: 20px; pointer-events: none; z-index: 10;">
            <div style="background: #EFF6FF; border: 1px solid #BFDBFE; color: #1E3A8A; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; font-weight: 700; padding: 4px 10px; border-radius: 4px; text-transform: uppercase; letter-spacing: 0.5px; display: inline-block;">
                LIVE INFERENCE ENGINE &middot; 24/7 ACTIVE STREAM
            </div>
            <div style="font-size: 0.82rem; color: #64748B; font-weight: 600; margin-top: 4px;">
                Latency: <span style="color:#2563EB; font-weight:700;">0.012s</span> &nbsp;|&nbsp; Stream Throughput: <span style="color:#2563EB; font-weight:700;">1,420 msgs/sec</span>
            </div>
        </div>

        <!-- TOP RIGHT LIVE TRADE DATA COUNTER WITH DAILY RESET -->
        <div style="position: absolute; top: 16px; right: 20px; background: rgba(255, 255, 255, 0.95); border: 1px solid #CBD5E1; border-radius: 8px; padding: 12px 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); text-align: right; font-family: 'Plus Jakarta Sans', sans-serif; pointer-events: none; z-index: 10; backdrop-filter: blur(6px);">
            <div style="font-size: 0.7rem; font-weight: 800; color: #64748B; text-transform: uppercase; letter-spacing: 0.5px; font-family: 'JetBrains Mono', monospace;">
                TODAY'S SCANNED TRADE MANIFESTS
            </div>
            <div style="font-size: 1.65rem; font-weight: 800; color: #1A365D; font-family: 'JetBrains Mono', monospace; line-height: 1.1; margin: 2px 0;">
                <span id="scannedCounter">14,289</span> <span style="font-size: 0.8rem; color: #2563EB; font-weight: 700;">MANIFESTS</span>
            </div>
            <div style="font-size: 0.72rem; color: #059669; font-weight: 700; display: flex; align-items: center; justify-content: flex-end; gap: 4px;">
                <span>●</span> AUTO-RESET AT MIDNIGHT (00:00 MYT)
            </div>
        </div>

        <!-- BOTTOM RIGHT LEGEND OVERLAY -->
        <div style="position: absolute; bottom: 16px; right: 20px; background: rgba(255,255,255,0.92); border: 1px solid #CBD5E1; border-radius: 6px; padding: 10px 14px; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #334155; pointer-events: none; backdrop-filter: blur(4px); z-index: 10;">
            <div><span style="color:#2563EB; font-weight:800;">[BASEL PLASTIC]</span> HS 3915 &middot; Auditing Unit Prices</div>
            <div><span style="color:#0284C7; font-weight:800;">[BASEL E-WASTE]</span> HS 8549 &middot; Scrap Density Check</div>
            <div><span style="color:#059669; font-weight:800;">[MONTREAL ODS]</span> HS 2903 &middot; Quota Match Active</div>
            <div><span style="color:#7C3AED; font-weight:800;">[STOCKHOLM POP]</span> Toxic Chemical Index Check</div>
            <div><span style="color:#D97706; font-weight:800;">[CITES FLORA]</span> Timber Volumetric Cross-Check</div>
        </div>
    </div>

    <script>
        const rCanvas = document.getElementById('radarCanvas');
        const rCtx = rCanvas.getContext('2d');
        let rWidth, rHeight, centerX, centerY, maxRadius;
        let angle = 0;

        // Dynamic Scanned Counter Engine
        let scannedCount = 14289;
        const counterEl = document.getElementById('scannedCounter');

        function updateCounter() {
            // Increment randomly between 1 and 4 every 1.5 seconds to simulate incoming stream
            scannedCount += Math.floor(Math.random() * 3) + 1;
            if (counterEl) {
                counterEl.innerText = scannedCount.toLocaleString();
            }
        }
        setInterval(updateCounter, 1400);

        function initRadar() {
            rWidth = rCanvas.width = rCanvas.offsetWidth;
            rHeight = rCanvas.height = rCanvas.offsetHeight;
            centerX = rWidth / 2;
            centerY = rHeight / 2;
            maxRadius = Math.min(rWidth, rHeight) * 0.36;
        }
        window.addEventListener('resize', initRadar);
        initRadar();

        // 5 Core MEA Targets (Radial Distribution)
        const meaNodes = [
            { name: "Basel: Plastic Waste (HS 3915)", dist: 0.72, angleDeg: 30, color: "#2563EB" },
            { name: "Basel: E-Waste Slag (HS 8549)", dist: 0.55, angleDeg: 110, color: "#0284C7" },
            { name: "Montreal: ODS Gas (HS 2903)", dist: 0.85, angleDeg: 190, color: "#059669" },
            { name: "Stockholm: Chemical POPs", dist: 0.65, angleDeg: 260, color: "#7C3AED" },
            { name: "CITES: Timber & Flora (HS 4403)", dist: 0.78, angleDeg: 320, color: "#D97706" }
        ];

        function drawRadarGrid() {
            rCtx.clearRect(0, 0, rWidth, rHeight);

            // Light Matrix Background Bar Lines (Grid Matrix Effect)
            rCtx.lineWidth = 1;
            for (let x = 0; x < rWidth; x += 32) {
                rCtx.beginPath();
                rCtx.moveTo(x, 0);
                rCtx.lineTo(x, rHeight);
                rCtx.strokeStyle = 'rgba(226, 232, 240, 0.4)';
                rCtx.stroke();
            }
            for (let y = 0; y < rHeight; y += 32) {
                rCtx.beginPath();
                rCtx.moveTo(0, y);
                rCtx.lineTo(rWidth, y);
                rCtx.strokeStyle = 'rgba(226, 232, 240, 0.4)';
                rCtx.stroke();
            }

            // Concentric Radar Rings
            const ringCount = 4;
            for (let i = 1; i <= ringCount; i++) {
                rCtx.beginPath();
                rCtx.arc(centerX, centerY, (maxRadius / ringCount) * i, 0, Math.PI * 2);
                rCtx.strokeStyle = 'rgba(203, 213, 225, 0.7)';
                rCtx.setLineDash([4, 4]);
                rCtx.stroke();
                rCtx.setLineDash([]);
            }

            // Crosshair Axis Lines
            rCtx.beginPath();
            rCtx.moveTo(centerX - maxRadius - 20, centerY);
            rCtx.lineTo(centerX + maxRadius + 20, centerY);
            rCtx.moveTo(centerX, centerY - maxRadius - 20);
            rCtx.lineTo(centerX, centerY + maxRadius + 20);
            rCtx.strokeStyle = 'rgba(203, 213, 225, 0.9)';
            rCtx.stroke();

            // Rotating Sweep Beam
            angle += 0.018;
            if (angle > Math.PI * 2) angle = 0;

            const sweepGradient = rCtx.createConicGradient(angle, centerX, centerY);
            sweepGradient.addColorStop(0, 'rgba(37, 99, 235, 0.28)');
            sweepGradient.addColorStop(0.12, 'rgba(37, 99, 235, 0.04)');
            sweepGradient.addColorStop(0.25, 'transparent');

            rCtx.beginPath();
            rCtx.arc(centerX, centerY, maxRadius, 0, Math.PI * 2);
            rCtx.fillStyle = sweepGradient;
            rCtx.fill();

            // Radar Leading Line
            const lineX = centerX + Math.cos(angle) * maxRadius;
            const lineY = centerY + Math.sin(angle) * maxRadius;
            rCtx.beginPath();
            rCtx.moveTo(centerX, centerY);
            rCtx.lineTo(lineX, lineY);
            rCtx.strokeStyle = 'rgba(37, 99, 235, 0.8)';
            rCtx.lineWidth = 2;
            rCtx.stroke();

            // Draw MEA Target Nodes & Scan Hits
            meaNodes.forEach(node => {
                const rad = (node.angleDeg * Math.PI) / 180;
                const nx = centerX + Math.cos(rad) * (maxRadius * node.dist);
                const ny = centerY + Math.sin(rad) * (maxRadius * node.dist);

                // Calculate angular distance to sweep line
                let diff = angle - rad;
                while (diff < 0) diff += Math.PI * 2;
                while (diff > Math.PI * 2) diff -= Math.PI * 2;

                const isSwept = diff < 0.35;

                // Ping Ripple Effect when swept
                if (isSwept) {
                    rCtx.beginPath();
                    rCtx.arc(nx, ny, 16, 0, Math.PI * 2);
                    rCtx.fillStyle = 'rgba(37, 99, 235, 0.15)';
                    rCtx.fill();

                    rCtx.beginPath();
                    rCtx.arc(nx, ny, 24, 0, Math.PI * 2);
                    rCtx.strokeStyle = node.color;
                    rCtx.lineWidth = 1;
                    rCtx.stroke();
                }

                // Core Dot
                rCtx.beginPath();
                rCtx.arc(nx, ny, 5, 0, Math.PI * 2);
                rCtx.fillStyle = node.color;
                rCtx.fill();
                rCtx.strokeStyle = '#FFFFFF';
                rCtx.lineWidth = 1.5;
                rCtx.stroke();

                // Text Label
                rCtx.font = "bold 11px 'Plus Jakarta Sans', sans-serif";
                rCtx.fillStyle = "#1A365D";
                rCtx.fillText(node.name, nx + 10, ny + 4);
            });

            requestAnimationFrame(drawRadarGrid);
        }
        drawRadarGrid();
    </script>
    """
    st.components.v1.html(html_radar_grid, height=440)

    st.markdown("---")

    # --------------------------------------------------------------------------
    # 5. QUICK LAUNCH DESK
    # --------------------------------------------------------------------------
    st.markdown("### Platform Quick Launch Operations")
    st.caption("Navigate to operational modules:")

    btn1, btn2, btn3, btn4 = st.columns(4)

    with btn1:
        st.button("Launch Live Scanner", key="go_scanner")
    with btn2:
        st.button("Launch Data Studio", key="go_studio")
    with btn3:
        st.button("Launch AI Copilot", key="go_copilot")
    with btn4:
        st.button("Launch HITL Queue", key="go_hitl")
