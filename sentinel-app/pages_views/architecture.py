import streamlit as st
import pandas as pd

def render_architecture_page():
    st.subheader("GCP Cloud Architecture & ML Infrastructure Stack")
    st.caption("Interactive pipeline mapping the end-to-end data ingestion, model training, analytics compilation, and web delivery layers on Google Cloud Platform.")

    st.markdown("---")

    # Metrics Summary
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Central Data Lake", "Google BigQuery", "14.82M Records")
    m2.metric("ML Training Environment", "Colab Enterprise", "Scikit-Learn / PyTorch")
    m3.metric("Embedded Analytics", "Looker & Data Studio", "Real-Time Direct Query")
    m4.metric("Hosting & API Delivery", "Streamlit / Web SDK", "OAuth2 / JWT Secured")

    st.markdown("---")

    # --------------------------------------------------------------------------
    # 1. LIVE ANIMATED CANVAS: 4-LAYER GCP ARCHITECTURE FLOW
    # --------------------------------------------------------------------------
    st.markdown("##### Interactive End-to-End Pipeline Stream")
    st.caption("Hover over connection pathways to observe data particle velocities between Google Cloud Platform services:")

    html_arch_canvas = """
    <div style="position: relative; width: 100%; height: 380px; border-radius: 12px; overflow: hidden; background: linear-gradient(135deg, #FFFFFF 0%, #F8FAFC 100%); border: 1px solid #CBD5E1; box-shadow: 0 4px 12px rgba(15,23,42,0.03);">
        <canvas id="archCanvas" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></canvas>
    </div>

    <script>
        const aCanvas = document.getElementById('archCanvas');
        const aCtx = aCanvas.getContext('2d');
        let aWidth, aHeight;

        function initArch() {
            aWidth = aCanvas.width = aCanvas.offsetWidth;
            aHeight = aCanvas.height = aCanvas.offsetHeight;
        }
        window.addEventListener('resize', initArch);
        initArch();

        // 4 Architectural Layers Positioned Across Canvas
        const nodes = [
            { id: "L1_COMTRADE", name: "UN Comtrade Open Data", sub: "Global Trade Feed", xRatio: 0.12, yRatio: 0.35, color: "#2563EB", icon: "🌐" },
            { id: "L1_BIGQUERY", name: "Google BigQuery", sub: "Central Warehouse", xRatio: 0.28, yRatio: 0.65, color: "#4285F4", icon: "🗄️" },
            { id: "L2_COLAB", name: "Colab Enterprise", sub: "Notebook Training & Tuning", xRatio: 0.50, yRatio: 0.25, color: "#EA4335", icon: "🧪" },
            { id: "L3_LOOKER", name: "Looker & Data Studio", sub: "Compiled ML & Dashboards", xRatio: 0.72, yRatio: 0.65, color: "#FBBC05", icon: "📊" },
            { id: "L4_DELIVERY", name: "Delivery & Web Hosting", sub: "Streamlit / GitHub / Vercel", xRatio: 0.88, yRatio: 0.40, color: "#34A853", icon: "🚀" }
        ];

        // Connection Pipelines
        const pipelines = [
            { from: 0, to: 1, label: "Access Open Data", color: "#2563EB" },
            { from: 1, to: 2, label: "Read Trade Data", color: "#9333EA" },
            { from: 2, to: 1, label: "Write ML Predictions", color: "#9333EA" },
            { from: 1, to: 3, label: "Plug ML Results", color: "#DC2626" },
            { from: 3, to: 4, label: "Embed Dashboards", color: "#16A34A" }
        ];

        // Animated Data Particles
        let particles = [];
        for (let i = 0; i < 35; i++) {
            particles.push({
                pipeIndex: Math.floor(Math.random() * pipelines.length),
                progress: Math.random(),
                speed: 0.003 + Math.random() * 0.004
            });
        }

        function drawArch() {
            aCtx.clearRect(0, 0, aWidth, aHeight);

            // Light Grid Lines
            aCtx.strokeStyle = "rgba(226, 232, 240, 0.5)";
            aCtx.lineWidth = 1;
            for (let x = 0; x < aWidth; x += 30) {
                aCtx.beginPath(); aCtx.moveTo(x, 0); aCtx.lineTo(x, aHeight); aCtx.stroke();
            }
            for (let y = 0; y < aHeight; y += 30) {
                aCtx.beginPath(); aCtx.moveTo(0, y); aCtx.lineTo(aWidth, y); aCtx.stroke();
            }

            // Draw Pipelines (Connecting Lines)
            pipelines.forEach((p, idx) => {
                const n1 = nodes[p.from];
                const n2 = nodes[p.to];
                const x1 = n1.xRatio * aWidth, y1 = n1.yRatio * aHeight;
                const x2 = n2.xRatio * aWidth, y2 = n2.yRatio * aHeight;

                aCtx.beginPath();
                aCtx.moveTo(x1, y1);
                aCtx.lineTo(x2, y2);
                aCtx.strokeStyle = p.color;
                aCtx.lineWidth = 2;
                aCtx.setLineDash([6, 6]);
                aCtx.stroke();
                aCtx.setLineDash([]);
            });

            // Update & Draw Flowing Data Particles
            particles.forEach(pt => {
                pt.progress += pt.speed;
                if (pt.progress > 1) pt.progress = 0;

                const pipe = pipelines[pt.pipeIndex];
                const n1 = nodes[pipe.from];
                const n2 = nodes[pipe.to];
                const px = (n1.xRatio + (n2.xRatio - n1.xRatio) * pt.progress) * aWidth;
                const py = (n1.yRatio + (n2.yRatio - n1.yRatio) * pt.progress) * aHeight;

                aCtx.beginPath();
                aCtx.arc(px, py, 4, 0, Math.PI * 2);
                aCtx.fillStyle = pipe.color;
                aCtx.fill();
                aCtx.strokeStyle = "#FFFFFF";
                aCtx.lineWidth = 1;
                aCtx.stroke();
            });

            // Draw Layer Nodes
            nodes.forEach(n => {
                const nx = n.xRatio * aWidth;
                const ny = n.yRatio * aHeight;

                // Node Card Container
                aCtx.fillStyle = "#FFFFFF";
                aCtx.strokeStyle = "#CBD5E1";
                aCtx.lineWidth = 1.5;
                aCtx.beginPath();
                aCtx.roundRect(nx - 75, ny - 32, 150, 64, 8);
                aCtx.fill();
                aCtx.stroke();

                // Colored Accent Line
                aCtx.fillStyle = n.color;
                aCtx.beginPath();
                aCtx.roundRect(nx - 75, ny - 32, 6, 64, [8, 0, 0, 8]);
                aCtx.fill();

                // Node Header Text
                aCtx.font = "bold 11px 'Plus Jakarta Sans', sans-serif";
                aCtx.fillStyle = "#1A365D";
                aCtx.fillText(n.name, nx - 62, ny - 8);

                // Subtitle Text
                aCtx.font = "10px 'JetBrains Mono', monospace";
                aCtx.fillStyle = "#64748B";
                aCtx.fillText(n.sub, nx - 62, ny + 12);
            });

            requestAnimationFrame(drawArch);
        }
        drawArch();
    </script>
    """
    st.components.v1.html(html_arch_canvas, height=400)

    st.markdown("---")

    # --------------------------------------------------------------------------
    # 2. INTERACTIVE GCP TECH STACK INSPECTOR
    # --------------------------------------------------------------------------
    st.markdown("##### Technical Component Inspector")
    st.caption("Select a GCP architectural component below to inspect specifications, data schemas, and security configurations:")

    selected_tech = st.radio(
        "Choose Infrastructure Component:",
        ["1. Data Layer (BigQuery & UN Comtrade)", "2. Model Training Layer (Colab Enterprise)", "3. Analytics Layer (Looker & Data Studio)", "4. Delivery & Web Hosting"],
        horizontal=True
    )

    col_spec1, col_spec2 = st.columns([1.2, 1])

    with col_spec1:
        if "1. Data Layer" in selected_tech:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:4px solid #4285F4; border-radius:8px; padding:20px;">
                <div class="figma-badge" style="margin-bottom:8px;">GCP SKU: Google BigQuery Enterprise</div>
                <h4 style="margin:0 0 6px 0; color:#1A365D; font-size:1.15rem; font-weight:800;">Google BigQuery Central Warehouse</h4>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:8px;">Houses 14.82M customs declarations (2020–2026) partitioned by trade month and clustered by HS Code.</p>
                <hr style="margin:10px 0; border-color:#E2E8F0;">
                <div style="font-size:0.8rem; color:#475569;">
                    <div><b>Dataset Location:</b> <code>asia-southeast1 (Malaysia / Singapore)</code></div>
                    <div><b>Storage Engine:</b> Columnar Capacitor Format with Automatic Encryption</div>
                    <div><b>Ingestion Latency:</b> Real-Time Streaming Inserts via BigQuery Storage Write API</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        elif "2. Model Training" in selected_tech:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:4px solid #EA4335; border-radius:8px; padding:20px;">
                <div class="figma-badge" style="margin-bottom:8px;">GCP SKU: Vertex AI / Colab Enterprise</div>
                <h4 style="margin:0 0 6px 0; color:#1A365D; font-size:1.15rem; font-weight:800;">Colab Enterprise ML Training Environment</h4>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:8px;">Managed Vertex AI notebook instance executing automated retraining for Isolation Forest and K-Means clustering pipelines.</p>
                <hr style="margin:10px 0; border-color:#E2E8F0;">
                <div style="font-size:0.8rem; color:#475569;">
                    <div><b>Frameworks:</b> <code>Scikit-Learn 1.9</code> &middot; <code>PyTorch</code> &middot; <code>SHAP 0.44</code></div>
                    <div><b>Model Registry Artifacts:</b> <code>plastic_forensic_pipeline.joblib</code>, <code>ods_forensic.joblib</code></div>
                    <div><b>Retraining Trigger:</b> Scheduled Weekly Cron Job + Concept Drift Hook</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        elif "3. Analytics Layer" in selected_tech:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:4px solid #FBBC05; border-radius:8px; padding:20px;">
                <div class="figma-badge" style="margin-bottom:8px;">GCP SKU: Google Looker Studio Pro</div>
                <h4 style="margin:0 0 6px 0; color:#1A365D; font-size:1.15rem; font-weight:800;">Looker & Data Studio Embedding Engine</h4>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:8px;">Direct BigQuery BI Engine connection serving interactive MEA trade volume visualizations and time-series dips.</p>
                <hr style="margin:10px 0; border-color:#E2E8F0;">
                <div style="font-size:0.8rem; color:#475569;">
                    <div><b>Embed Security:</b> Domain-Restricted IFrame Sandboxing</div>
                    <div><b>Data Caching:</b> 15-Minute Looker In-Memory Acceleration</div>
                    <div><b>Active Dashboards:</b> Plastic Scrap (HS 3915), E-Waste (HS 8549), ODS Gases (HS 2903)</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:4px solid #34A853; border-radius:8px; padding:20px;">
                <div class="figma-badge" style="margin-bottom:8px;">Deployment: Streamlit Cloud / Cloud Run</div>
                <h4 style="margin:0 0 6px 0; color:#1A365D; font-size:1.15rem; font-weight:800;">Delivery & Web Application Layer</h4>
                <p style="font-size:0.85rem; color:#334155; margin-bottom:8px;">High-performance web dashboard delivering real-time manifest scanning, OCR extraction, and inter-agency MyGDX portals.</p>
                <hr style="margin:10px 0; border-color:#E2E8F0;">
                <div style="font-size:0.8rem; color:#475569;">
                    <div><b>Runtime Engine:</b> Python 3.14 + Streamlit 1.61 Engine</div>
                    <div><b>Authentication:</b> Role-Based Access Control (RBAC) & OAuth2 JWT Tokens</div>
                    <div><b>Inter-Agency Gateway:</b> MyGDX REST API & JSON Endpoints</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with col_spec2:
        st.markdown("###### GCP Security & Data Flow Specs")
        spec_df = pd.DataFrame({
            "Specification": ["GCP Region", "IAM Security", "Encryption", "Data Lake Sync", "Uptime SLA"],
            "Configuration Value": ["asia-southeast1", "OAuth2 / RBAC Tiered", "AES-256 / SHA-256", "Live BigQuery Storage Write API", "99.95% Enterprise SLA"]
        })
        st.dataframe(spec_df, use_container_width=True)
