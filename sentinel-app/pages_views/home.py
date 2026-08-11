import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def render_home_page():
    st.subheader("🏠 National Environmental Trade Intelligence Hub")
    st.caption("Public Portal & Multi-Agency Command Operations")

    # --------------------------------------------------------------------------
    # 1. INTERACTIVE QUICK-NAVIGATION HUB
    # --------------------------------------------------------------------------
    st.markdown("##### 🚀 Platform Quick Launch Desk")
    q_col1, q_col2, q_col3, q_col4 = st.columns(4)

    with q_col1:
        st.markdown("""
        <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:10px; padding:12px; text-align:center; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
            <div style="font-size:1.5rem;">🔍</div>
            <div style="font-weight:700; color:#0F172A; font-size:0.9rem;">Live Anomaly Scanner</div>
            <div style="font-size:0.75rem; color:#64748B;">Inspect HS Codes & Manifests</div>
        </div>
        """, unsafe_allow_html=True)

    with q_col2:
        st.markdown("""
        <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:10px; padding:12px; text-align:center; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
            <div style="font-size:1.5rem;">📈</div>
            <div style="font-weight:700; color:#0F172A; font-size:0.9rem;">Data Studio Hub</div>
            <div style="font-size:0.75rem; color:#64748B;">Embedded Analytics Catalog</div>
        </div>
        """, unsafe_allow_html=True)

    with q_col3:
        st.markdown("""
        <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:10px; padding:12px; text-align:center; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
            <div style="font-size:1.5rem;">🤖</div>
            <div style="font-weight:700; color:#0F172A; font-size:0.9rem;">AI Legal Copilot</div>
            <div style="font-size:0.75rem; color:#64748B;">Query Trade Protocols</div>
        </div>
        """, unsafe_allow_html=True)

    with q_col4:
        st.markdown("""
        <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:10px; padding:12px; text-align:center; box-shadow:0 2px 4px rgba(0,0,0,0.02);">
            <div style="font-size:1.5rem;">📞</div>
            <div style="font-weight:700; color:#0F172A; font-size:0.9rem;">HITL Escalation Queue</div>
            <div style="font-size:0.75rem; color:#64748B;">Multi-Agency Review Desk</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # 2. KEY METRIC CARDS
    # --------------------------------------------------------------------------
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Audited Trade Declarations", "142,890", "↑ 12.4% YoY")
    m2.metric("Overall Anomaly Rate", "4.12%", "↓ 0.8% YoY")
    m3.metric("Container Interceptions", "382 Holds", "JKDM / JAS Actions")
    m4.metric("Active Model Pipelines", "3 Live", "2 In Sandbox")

    st.markdown("---")

    # --------------------------------------------------------------------------
    # 3. MULTILATERAL ENVIRONMENTAL AGREEMENTS (MEAs) DIRECTORY
    # --------------------------------------------------------------------------
    st.markdown("##### 📜 Multilateral Environmental Agreements (MEAs) Framework")
    st.caption("SENTINEL enforces cross-border compliance across four international environmental treaties.")

    mea1, mea2, mea3, mea4 = st.columns(4)

    with mea1:
        st.markdown("""
        <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:12px; padding:16px; min-height:180px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03);">
            <div style="font-size:1.2rem; font-weight:800; color:#1E3A8A;">♻️ Basel Convention</div>
            <div style="font-size:0.8rem; font-weight:700; color:#2563EB; margin-top:4px;">Hazardous Wastes & Plastics</div>
            <hr style="margin:8px 0; border-color:#F1F5F9;">
            <div style="font-size:0.8rem; color:#334155;"><b>Primary Focus:</b> Plastic Scrap (HS 3915) & E-Waste (HS 8548/8549)</div>
            <div style="font-size:0.75rem; color:#64748B; margin-top:6px;"><b>Lead Agency:</b> JAS / JKDM</div>
        </div>
        """, unsafe_allow_html=True)

    with mea2:
        st.markdown("""
        <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:12px; padding:16px; min-height:180px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03);">
            <div style="font-size:1.2rem; font-weight:800; color:#1E3A8A;">❄️ Montreal Protocol</div>
            <div style="font-size:0.8rem; font-weight:700; color:#2563EB; margin-top:4px;">Ozone Depleting Substances</div>
            <hr style="margin:8px 0; border-color:#F1F5F9;">
            <div style="font-size:0.8rem; color:#334155;"><b>Primary Focus:</b> CFCs, HCFCs & HFCs (HS 2903)</div>
            <div style="font-size:0.75rem; color:#64748B; margin-top:6px;"><b>Lead Agency:</b> JAS / MITI</div>
        </div>
        """, unsafe_allow_html=True)

    with mea3:
        st.markdown("""
        <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:12px; padding:16px; min-height:180px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03);">
            <div style="font-size:1.2rem; font-weight:800; color:#1E3A8A;">🌿 CITES Framework</div>
            <div style="font-size:0.8rem; font-weight:700; color:#2563EB; margin-top:4px;">Endangered Species & Timber</div>
            <hr style="margin:8px 0; border-color:#F1F5F9;">
            <div style="font-size:0.8rem; color:#334155;"><b>Primary Focus:</b> Wildlife, Flora & Timber (HS 0106/4403)</div>
            <div style="font-size:0.75rem; color:#64748B; margin-top:6px;"><b>Lead Agency:</b> PERHILITAN / MAQIS</div>
        </div>
        """, unsafe_allow_html=True)

    with mea4:
        st.markdown("""
        <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:12px; padding:16px; min-height:180px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03);">
            <div style="font-size:1.2rem; font-weight:800; color:#1E3A8A;">🧪 Stockholm & Rotterdam</div>
            <div style="font-size:0.8rem; font-weight:700; color:#2563EB; margin-top:4px;">POPs & Hazardous Chemicals</div>
            <hr style="margin:8px 0; border-color:#F1F5F9;">
            <div style="font-size:0.8rem; color:#334155;"><b>Primary Focus:</b> Toxic Pesticides & Industrial Chemicals</div>
            <div style="font-size:0.75rem; color:#64748B; margin-top:6px;"><b>Lead Agency:</b> Department of Agriculture / JAS</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # --------------------------------------------------------------------------
    # 4. PUBLIC REAL-TIME REGIONAL MAP (SOFT GLOW MARKERS)
    # --------------------------------------------------------------------------
    st.markdown("##### 🌍 Real-Time Regional Threat Map")
    st.caption("Live geographical risk distribution across Malaysian container ports and border check-points.")

    map_df = pd.DataFrame({
        'lat': [3.000, 1.450, 5.410, 4.580, 2.800],
        'lon': [101.400, 103.750, 100.320, 114.000, 101.700],
        'Port': ['Port Klang', 'Johor Port / Pasir Gudang', 'Penang Port', 'Bintulu Port', 'KLIA Cargo Complex'],
        'Threat': ['Plastic Scrap Misdeclaration (HS 3915)', 'Unlicensed ODS Gases (HS 2903)', 'Illegal E-Waste Containers (HS 8549)', 'Timber Volume Discrepancy (HS 4403)', 'Chemical POPs Mismatch'],
        'Score': [92, 88, 79, 85, 94]
    })

    fig = go.Figure()

    # Outer Soft Glow Halo Layer
    fig.add_trace(go.Scattermapbox(
        lat=map_df['lat'],
        lon=map_df['lon'],
        mode='markers',
        marker=dict(
            size=map_df['Score'] * 0.45,
            color='rgba(239, 68, 68, 0.28)',
            opacity=0.8
        ),
        hoverinfo='none',
        showlegend=False
    ))

    # Inner High-Contrast Core Layer
    fig.add_trace(go.Scattermapbox(
        lat=map_df['lat'],
        lon=map_df['lon'],
        mode='markers+text',
        marker=dict(
            size=map_df['Score'] * 0.18,
            color='#DC2626',
            opacity=1.0
        ),
        text=map_df['Port'],
        textposition="top center",
        hoverinfo='text',
        hovertext=[f"<b>{p}</b><br>Threat: {t}<br>Risk Score: <b>{s}/100</b>" for p, t, s in zip(map_df['Port'], map_df['Threat'], map_df['Score'])],
        showlegend=False
    ))

    fig.update_layout(
        mapbox=dict(
            style="carto-positron",
            center=dict(lat=4.0, lon=107.5),
            zoom=4.8
        ),
        height=420,
        margin=dict(l=0, r=0, t=0, b=0)
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # --------------------------------------------------------------------------
    # 5. PUBLIC MEA DATA STUDIO EMBED CONTAINER (PLACEHOLDER)
    # --------------------------------------------------------------------------
    st.markdown("##### 📊 Public MEA Analytics Studio & Interactive Dashboards")
    st.caption("Public access tier for live trade statistics, environmental compliance metrics, and treaty analytics.")

    mea_embed_tab1, mea_embed_tab2, mea_embed_tab3, mea_embed_tab4 = st.tabs([
        "♻️ Public Basel Studio", 
        "❄️ Public Montreal Studio", 
        "🌿 Public CITES Studio", 
        "🧪 Public Stockholm Studio"
    ])

    with mea_embed_tab1:
        st.info("💡 **Basel Convention Public Dashboard:** Interactive Google Looker Studio reports for plastic waste and e-waste imports will render here.")
        # Default Public Embed
        st.components.v1.iframe("https://lookerstudio.google.com/embed/reporting/0B5FF2A71111/page/6zB", height=450, scrolling=True)

    with mea_embed_tab2:
        st.info("💡 **Montreal Protocol Public Dashboard:** Ozone depleting chemical tracking reports will render here.")

    with mea_embed_tab3:
        st.info("💡 **CITES Public Dashboard:** Protected timber and wildlife trade statistical reports will render here.")

    with mea_embed_tab4:
        st.info("💡 **Stockholm & Rotterdam Public Dashboard:** POPs chemical tracking reports will render here.")
