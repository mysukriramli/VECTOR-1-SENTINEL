import streamlit as st

def render_embed_portal_page():
    st.subheader("🔌 Inter-Agency Widget & Embed Generator Portal")
    
    # Access Control Gate
    if st.session_state.get("user_role") == "Public (Free)":
        st.warning("🔒 Access Restricted: Inter-Agency Widget Generation requires Gov Agency or Admin credentials.")
        st.info("Use the sidebar Demo Role Switcher to switch to **Gov Agency** or **Admin**.")
        return

    st.caption("Generate plug-and-play HTML `<iframe>` widgets, Web Components, and MyGDX REST API keys to embed SENTINEL intelligence directly into partner agency systems (e.g., JKDM K1 Portal, JAS e-AlamSekitar).")

    st.markdown("---")

    col_config, col_preview = st.columns([1, 1])

    # --------------------------------------------------------------------------
    # COLUMN 1: INTERACTIVE WIDGET BUILDER CONFIGURATOR
    # --------------------------------------------------------------------------
    with col_config:
        st.markdown("##### ⚙️ Widget Configuration Builder")

        widget_type = st.selectbox(
            "Select Widget Capability:",
            [
                "Real-Time Trade Anomaly Risk Gauge",
                "OCR Shipping Manifest Quick Parser",
                "Live MEA Violation Ticker & Alert Banner"
            ]
        )

        target_agency = st.selectbox(
            "Target Host Agency System:",
            [
                "JKDM Customs K1 Clearance System",
                "JAS e-AlamSekitar Portal",
                "MITI Import Licensing Hub",
                "PERHILITAN Wildlife Permit Portal"
            ]
        )

        widget_theme = st.radio("Widget Visual Theme:", ["Light Executive", "Dark Command"], horizontal=True)
        widget_height = st.slider("Widget Height (Pixels):", min_value=300, max_value=800, value=450, step=50)

        st.markdown("##### 🔑 MyGDX API Key & Authentication Token")
        api_token = st.text_input(
            "Generated Agency JWT Token:", 
            value="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJKS0RNLVBLIiwiaWF0IjoxNzU0ODgwMDAwfQ.SENTINEL_SECRET", 
            type="password"
        )

    # --------------------------------------------------------------------------
    # COLUMN 2: LIVE PREVIEW & CODE GENERATOR
    # --------------------------------------------------------------------------
    with col_preview:
        st.markdown("##### 👁️ Live External Widget Preview")
        
        theme_bg = "#FFFFFF" if widget_theme == "Light Executive" else "#0F172A"
        theme_fg = "#0F172A" if widget_theme == "Light Executive" else "#F8FAFC"
        border_color = "#2563EB" if "Risk" in widget_type else ("#10B981" if "OCR" in widget_type else "#EF4444")

        st.markdown(f"""
        <div style="background:{theme_bg}; color:{theme_fg}; border:2px solid {border_color}; border-radius:12px; padding:20px; box-shadow:0 10px 20px rgba(0,0,0,0.08);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                <span style="font-weight:800; font-size:1.05rem;">🛡️ SENTINEL EMBEDDED WIDGET</span>
                <span style="background:#DBEAFE; color:#1E3A8A; font-size:0.75rem; font-weight:700; padding:2px 8px; border-radius:10px;">{target_agency.split()[0]} PORTAL</span>
            </div>
            <div style="font-weight:700; font-size:0.95rem; margin-bottom:6px;">{widget_type}</div>
            <div style="font-size:0.8rem; opacity:0.8; margin-bottom:16px;">Connected to BigQuery Data Lake via MyGDX</div>
            <div style="background:#F1F5F9; color:#0F172A; border-radius:8px; padding:12px; text-align:center; font-weight:700;">
                {
                    '🚨 High Risk Anomaly Score: 88.4/100 (Plastic Scrap Misdeclaration)' if 'Risk' in widget_type 
                    else ('📄 Drop K1 Form PDF / Image for Instant OCR Field Extraction' if 'OCR' in widget_type 
                    else '⚠️ LIVE TICKER: 12 Containers Detained at Port Klang (HS 3915.10)')
                }
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # --------------------------------------------------------------------------
    # CODE EXPORTER TABS
    # --------------------------------------------------------------------------
    st.markdown("##### 📥 Export Embed Code Snippets")

    tab_html, tab_js, tab_curl = st.tabs([
        "🌐 HTML IFrame Snippet", 
        "⚡ JavaScript Web Component", 
        "📡 REST API / cURL Endpoint"
    ])

    base_embed_url = "https://sentinel-app.streamlit.app/embed"

    with tab_html:
        st.caption("Paste this HTML `<iframe>` snippet directly into any partner government web portal.")
        iframe_code = f"""<!-- SENTINEL Multi-Agency Embedded Widget -->
<iframe
    src="{base_embed_url}?widget={widget_type.lower().replace(' ', '_')}&agency={target_agency.split()[0]}&theme={widget_theme.lower().split()[0]}"
    width="100%"
    height="{widget_height}px"
    frameborder="0"
    style="border: 1px solid #CBD5E1; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);"
    allow="geolocation; microphone; camera">
</iframe>"""
        st.code(iframe_code, language="html")

    with tab_js:
        st.caption("Modern zero-dependency Web Component for single-page applications (React, Vue, Angular).")
        js_code = f"""// Include SENTINEL Web Component JS Script
import {{ SentinelWidget }} from '@jdn/sentinel-embed-sdk';

SentinelWidget.init({{
    targetElement: '#sentinel-container',
    agencyKey: '{target_agency.split()[0]}',
    widgetType: '{widget_type}',
    jwtToken: '{api_token[:20]}...',
    height: {widget_height}
}});"""
        st.code(js_code, language="javascript")

    with tab_curl:
        st.caption("Direct MyGDX REST API endpoint for system-to-system automated backend calls.")
        curl_code = f"""curl -X POST "https://api.sentinel.gov.my/v1/scan/manifest" \\
  -H "Authorization: Bearer {api_token}" \\
  -H "Content-Type: application/json" \\
  -d '{{
    "hs_code": "3915.10",
    "unit_price_usd": 0.15,
    "weight_kg": 25000,
    "volume_m3": 65,
    "host_agency": "{target_agency.split()[0]}"
  }}'"""
        st.code(curl_code, language="bash")
