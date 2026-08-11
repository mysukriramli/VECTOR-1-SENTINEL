import streamlit as st
import pandas as pd
from datetime import datetime

def init_data_request_state():
    """Initializes session state for inter-agency data access requests."""
    if "agency_data_requests" not in st.session_state:
        st.session_state["agency_data_requests"] = [
            {
                "Request_ID": "REQ-MYGDX-2026-081",
                "Requesting_Agency": "JAS (Jabatan Alam Sekitar)",
                "Dataset": "sentinel_sec.declarations_2020_2026 (Plastic Scrap & E-Waste)",
                "Access_Level": "Real-Time API Stream",
                "Statutory_Justification": "Cross-referencing Pasir Gudang port manifests against illegal recycling factory operating licenses.",
                "Status": "APPROVED",
                "Approved_Date": "2026-08-01",
                "MyGDX_Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJKQVMtSEsiLCJpYXQiOjE3NTQ4ODAwMDB9.SENTINEL_JAS_AUTH"
            },
            {
                "Request_ID": "REQ-MYGDX-2026-082",
                "Requesting_Agency": "MITI (Ministry of Investment, Trade & Industry)",
                "Dataset": "sentinel_sec.hs_code_intelligence_index",
                "Access_Level": "Monthly Bulk CSV Export",
                "Statutory_Justification": "Annual tariff impact assessment and import quota recalculation for Montreal Protocol chemicals.",
                "Status": "PENDING_JDN_APPROVAL",
                "Approved_Date": "-",
                "MyGDX_Token": "PENDING"
            },
            {
                "Request_ID": "REQ-MYGDX-2026-083",
                "Requesting_Agency": "PERHILITAN",
                "Dataset": "sentinel_sec.mea_violation_audit_logs (CITES Fauna/Flora)",
                "Access_Level": "Embedded Portal Widget",
                "Statutory_Justification": "Wildlife contraband alert feed for airport cargo inspections at KLIA Terminal 1 & 2.",
                "Status": "APPROVED",
                "Approved_Date": "2026-08-10",
                "MyGDX_Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJQRVJISUxJVEFOIiwiaWF0IjoxNzU0OTY2NDAwfQ.SENTINEL_PERHILITAN_AUTH"
            }
        ]

def render_embed_portal_page():
    st.subheader("🔌 Inter-Agency Data Sharing & MyGDX Portal")
    
    # Access Control Gate
    if st.session_state.get("user_role") == "Public (Free)":
        st.warning("🔒 Access Restricted: Inter-agency dataset requesting requires Gov Agency or Admin credentials.")
        st.info("Use the sidebar Demo Role Switcher to switch to **Gov Agency** or **Admin**.")
        return

    init_data_request_state()
    st.caption("Browse SENTINEL enterprise datasets, submit formal data sharing requests via MyGDX frameworks, and export API keys or embedded widgets for partner agency portals.")

    # Top Status Metrics
    reqs = st.session_state["agency_data_requests"]
    approved_cnt = sum(1 for r in reqs if r["Status"] == "APPROVED")
    pending_cnt = sum(1 for r in reqs if "PENDING" in r["Status"])

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Available Datasets", "4 BigQuery Tables", "2020 – 2026 Lake")
    m2.metric("Approved Access Grants", f"{approved_cnt} Active Grants", "MyGDX Synchronized")
    m3.metric("Pending Approvals", f"{pending_cnt} In Queue", "JDN / NAIO Desk")
    m4.metric("Security Compliance", "SPA Bil 2/2021", "OAuth 2.0 / JWT")

    st.markdown("---")

    tab_cat, tab_request, tab_tokens, tab_embed = st.tabs([
        "🗂️ Inter-Agency Data Catalogue",
        "📝 Submit Dataset Access Request",
        "🔑 Approved MyGDX Tokens & Stream Keys",
        "🔌 Widget & API Integration SDK"
    ])

    # --------------------------------------------------------------------------
    # TAB 1: INTER-AGENCY DATA CATALOGUE
    # --------------------------------------------------------------------------
    with tab_cat:
        st.markdown("##### 🗄️ Available SENTINEL Data Assets (2020–2026)")
        st.caption("Databases hosted in BigQuery, available for inter-agency requisition under Malaysia's MyGDX Data Sharing Policy.")

        datasets = [
            {
                "ID": "DS-01",
                "Table Name": "sentinel_sec.declarations_2020_2026",
                "Domain": "Customs Manifests & HS Code Audit",
                "Primary Custodian": "JKDM / JAS",
                "Records": "14.82 Million Rows",
                "Sensitivity": "CONFIDENTIAL (Gov Only)",
                "Description": "Historical national trade manifest declarations containing unit prices, net weights, volume, and ML risk scores."
            },
            {
                "ID": "DS-02",
                "Table Name": "sentinel_sec.ocr_manifest_extracts",
                "Domain": "Unstructured Manifest OCR Parser",
                "Primary Custodian": "JKDM",
                "Records": "2.41 Million Rows",
                "Sensitivity": "CONFIDENTIAL (Gov Only)",
                "Description": "Parsed JSON metadata from scanned Customs K1 forms, Bills of Lading, and commercial invoices."
            },
            {
                "ID": "DS-03",
                "Table Name": "sentinel_sec.mea_violation_audit_logs",
                "Domain": "Judicial Enforcement & Seizures",
                "Primary Custodian": "JAS / PERHILITAN",
                "Records": "382.9 Thousand Rows",
                "Sensitivity": "RESTRICTED (Enforcement Agencies)",
                "Description": "Judicial chain-of-custody audit trail for physical container holds, confiscation orders, and officer overrides."
            },
            {
                "ID": "DS-04",
                "Table Name": "sentinel_sec.hs_code_intelligence_index",
                "Domain": "Global Market Price & Tariff Index",
                "Primary Custodian": "MITI / JAS",
                "Records": "18.4 Thousand Rows",
                "Sensitivity": "OPEN GOV DATA",
                "Description": "Benchmark global resin prices, chemical formula indices, and risk weights per HS Code."
            }
        ]

        for ds in datasets:
            with st.expander(f"📦 [{ds['ID']}] {ds['Table Name']} ({ds['Domain']})"):
                col_a, col_b = st.columns([2, 1])
                with col_a:
                    st.markdown(f"**Description:** {ds['Description']}")
                    st.markdown(f"**Primary Custodian:** {ds['Primary Custodian']}")
                    st.markdown(f"**Total Record Volume:** `{ds['Records']}`")
                with col_b:
                    st.markdown(f"**Security Tier:** `{ds['Sensitivity']}`")
                    st.info("Available for MyGDX API streaming or batch CSV delivery.")

    # --------------------------------------------------------------------------
    # TAB 2: SUBMIT DATASET ACCESS REQUEST
    # --------------------------------------------------------------------------
    with tab_request:
        st.markdown("##### 📝 Formal Inter-Agency Data Request Desk")
        st.caption("Submit an official request to access SENTINEL datasets for agency enforcement or analytical operations.")

        with st.form("form_data_request"):
            col_f1, col_f2 = st.columns(2)

            with col_f1:
                req_agency = st.selectbox(
                    "Requesting Department / Ministry:",
                    [
                        "JAS (Jabatan Alam Sekitar)",
                        "JKDM (Jabatan Kastam Diraja Malaysia)",
                        "MITI (Ministry of Investment, Trade & Industry)",
                        "PERHILITAN (Wildlife & National Parks)",
                        "MAQIS (Malaysian Agricultural Quarantine)",
                        "Department of Agriculture (DOA)"
                    ]
                )

                target_dataset = st.selectbox(
                    "Target Dataset Requested:",
                    [
                        "sentinel_sec.declarations_2020_2026 (14.82M Rows)",
                        "sentinel_sec.ocr_manifest_extracts (2.41M Rows)",
                        "sentinel_sec.mea_violation_audit_logs (382.9K Rows)",
                        "sentinel_sec.hs_code_intelligence_index (18.4K Rows)"
                    ]
                )

            with col_f2:
                access_type = st.selectbox(
                    "Requested Data Exchange Mode:",
                    [
                        "Real-Time MyGDX REST API Stream",
                        "Monthly Automated Bulk CSV / Parquet Export",
                        "Embedded Dashboard Widget (IFrame)",
                        "Direct BigQuery Data Sharing (Read-Only Replica)"
                    ]
                )

                officer_contact = st.text_input("Requesting Officer Email & Title:", value="officer.azman@jas.gov.my")

            statutory_purpose = st.text_area(
                "Statutory Purpose & Legal Justification:",
                placeholder="Specify regulatory mandate or active investigation requiring this data feed (e.g. Cross-referencing Pasir Gudang chemical import manifests)..."
            )

            submit_req = st.form_submit_button("🚀 Submit Formal MyGDX Data Request", type="primary")

            if submit_req:
                if not statutory_purpose.strip():
                    st.error("Please provide a valid statutory purpose before submitting.")
                else:
                    new_id = f"REQ-MYGDX-2026-0{len(st.session_state['agency_data_requests']) + 84}"
                    st.session_state["agency_data_requests"].append({
                        "Request_ID": new_id,
                        "Requesting_Agency": req_agency,
                        "Dataset": target_dataset.split(" (")[0],
                        "Access_Level": access_type,
                        "Statutory_Justification": statutory_purpose,
                        "Status": "PENDING_JDN_APPROVAL",
                        "Approved_Date": "-",
                        "MyGDX_Token": "PENDING"
                    })
                    st.success(f"Request `{new_id}` submitted successfully! Track status in the 'Approved Tokens' tab.")

    # --------------------------------------------------------------------------
    # TAB 3: APPROVED MYGDX TOKENS & STREAM KEYS
    # --------------------------------------------------------------------------
    with tab_tokens:
        st.markdown("##### 🔑 Agency Data Sharing Grants & Token Desk")
        st.caption("View real-time status of inter-agency data requests and copy approved MyGDX OAuth2 Bearer tokens.")

        df_reqs = pd.DataFrame(st.session_state["agency_data_requests"])
        st.dataframe(df_reqs[["Request_ID", "Requesting_Agency", "Dataset", "Access_Level", "Status", "Approved_Date"]], use_container_width=True)

        st.markdown("---")
        st.markdown("##### 🔐 Active Token Inspection")

        approved_list = [r for r in st.session_state["agency_data_requests"] if r["Status"] == "APPROVED"]
        
        if approved_list:
            selected_req_id = st.selectbox("Select Approved Request:", [f"{r['Request_ID']} | {r['Requesting_Agency']}" for r in approved_list])
            target_id = selected_req_id.split(" | ")[0]
            req_item = next(r for r in approved_list if r["Request_ID"] == target_id)

            st.success(f"Grant Active for **{req_item['Requesting_Agency']}**")
            st.markdown(f"**Granted Dataset:** `{req_item['Dataset']}`")
            st.markdown(f"**Exchange Mode:** `{req_item['Access_Level']}`")
            st.code(f"MyGDX JWT Bearer Token:\n{req_item['MyGDX_Token']}", language="text")
        else:
            st.info("No approved grants currently available.")

    # --------------------------------------------------------------------------
    # TAB 4: WIDGET & API INTEGRATION SDK
    # --------------------------------------------------------------------------
    with tab_embed:
        st.markdown("##### 🔌 Partner Portal Widget & REST API Generator")
        st.caption("Generate ready-to-use HTML code snippets or cURL requests to embed live SENTINEL alerts directly into partner agency websites.")

        col_w1, col_w2 = st.columns(2)

        with col_w1:
            embed_target = st.selectbox("Embed Target Agency Portal:", ["JKDM K1 Customs Portal", "JAS e-AlamSekitar", "MITI Permit Portal", "PERHILITAN Cargo Desk"])
            widget_kind = st.radio("Widget Capability:", ["Live Anomaly Risk Gauge", "OCR Form Parser Widget", "MEA Violation Alert Ticker"], horizontal=True)

            st.markdown("##### HTML `<iframe>` Code Snippet")
            iframe_snippet = f"""<!-- SENTINEL Inter-Agency Widget for {embed_target.split()[0]} -->
<iframe
    src="https://sentinel-app.streamlit.app/embed?widget={widget_kind.lower().replace(' ', '_')}&agency={embed_target.split()[0]}"
    width="100%"
    height="450px"
    frameborder="0"
    style="border: 1px solid #CBD5E1; border-radius: 12px;">
</iframe>"""
            st.code(iframe_snippet, language="html")

        with col_w2:
            st.markdown("##### cURL REST API Endpoint Snippet")
            curl_snippet = f"""curl -X POST "https://api.sentinel.gov.my/v1/mygdx/stream" \\
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5..." \\
  -H "Content-Type: application/json" \\
  -d '{{
    "agency": "{embed_target.split()[0]}",
    "dataset": "sentinel_sec.declarations_2020_2026",
    "hs_code": "3915.10"
  }}'"""
            st.code(curl_snippet, language="bash")
