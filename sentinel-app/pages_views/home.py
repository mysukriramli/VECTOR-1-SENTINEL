import streamlit as st

def render_home_page():
    # Top Branding Header
    st.markdown("""
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin-bottom: 15px;">
        <div>
            <span class="psainc-badge"><span class="pulse-dot"></span> PSAINC 2026 | JDN & NAIO CHALLENGE</span>
            <span class="psainc-badge" style="background-color: #FEF3C7; color: #92400E; border-color: #FDE68A;">TEAM: VECTOR 1</span>
        </div>
        <div>
            <span class="psainc-badge" style="background-color: #F1F5F9; color: #475569; border-color: #E2E8F0;">Garis Panduan AI Sektor Awam Compliant</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    tab_overview, tab_judges = st.tabs([
        "🏠 Executive Dashboard & Overview", 
        "🏛️ PSAINC 2026 Pitching & Evaluation Workbench"
    ])

    # --------------------------------------------------------------------------
    # TAB 1: EXECUTIVE DASHBOARD OVERVIEW
    # --------------------------------------------------------------------------
    with tab_overview:
        st.markdown("### 🛡️ SENTINEL Trade Intelligence Portal")
        st.caption("Smart Environmental Nexus for Trade Intelligence & Networked Enforcement Logic")

        # Top Macro Metrics
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Audited Declarations", "142,890", "↑ +12.4% YoY")
        c2.metric("Overall Anomaly Rate", "4.12%", "↓ -0.8% YoY")
        c3.metric("Container Interceptions", "382 Hold Orders", "JKDM / JAS")
        c4.metric("Active ML Models", "3 Deployed", "100% XAI Audited")

        st.markdown("---")

        st.markdown("#### 🚀 Multi-Agency Enforcement Pillars")
        p1, p2, p3 = st.columns(3)
        
        with p1:
            st.info("##### 🔍 1. Live Anomaly Detection")
            st.write("Scans customs manifests (Single entry, CSV Batch, or OCR Document) against scikit-learn Isolation Forest ML pipelines calibrated for illegal trade.")

        with p2:
            st.success("##### 🏛️ 2. Multi-Agency HITL Routing")
            st.write("Connects Customs (JKDM), Environment (JAS), Trade (MITI), and Wildlife (PERHILITAN) into a single Human-in-the-Loop escalation workflow.")

        with p3:
            st.warning("##### ⚖️ 3. Responsible AI & Governance")
            st.write("Fulfills JDN/NAIO guidelines with SHA-256 model checksums, XAI feature attribution charts, and SPA Bil. 2/2021 v2.0 cloud security standards.")

    # --------------------------------------------------------------------------
    # TAB 2: PSAINC 2026 JUDGES PITCHING BENCH
    # --------------------------------------------------------------------------
    with tab_judges:
        st.markdown("### 📋 Public Sector AI Nexus Challenge 2026 — Team VECTOR 1")
        st.caption("Direct alignment map against Jabatan Digital Negara (JDN) & NAIO evaluation criteria.")

        col_j1, col_j2 = st.columns([3, 2])

        with col_j1:
            st.markdown("#### 🎯 Evaluation Criteria Mapping")
            
            with st.expander("1. Impact & Relevance (25%)", expanded=True):
                st.write("**Cross-Agency Solution (*Merentas Agensi*):** Integrates **JAS, JKDM, MITI, and PERHILITAN** to prevent hazardous waste dumping, ODS refrigerant smuggling, and illegal e-waste entry.")
                st.write("**Economic ROI:** Estimated **RM 42.8M** in prevented illegal landfill remediation costs and tariff evasion.")

            with st.expander("2. Feasibility & Implementation (20%)", expanded=True):
                st.write("**Operational Prototype:** Fully hosted Streamlit platform with live single-item scanning, bulk CSV inference, document OCR parsing, and Looker Studio BI integration.")

            with st.expander("3. Innovation & AI Application (25%)", expanded=True):
                st.write("**AI Approach:** Unsupervised scikit-learn Isolation Forests trained on historical customs parameters (unit price deviation, volume-to-density ratio, origin risk).")

            with st.expander("4. User-Centricity & Design (10%)", expanded=True):
                st.write("**UI/UX Polish:** Custom executive styling, light navbar theme matching agency logos, micro-interaction hover states, and dynamic status badges.")

            with st.expander("5. Responsible AI & Governance (10%)", expanded=True):
                st.write("**4 Pillars Fulfilling JDN AI Guidelines:** AI Ethics, Accuracy, XAI Explainability, and Data Security (SPA Bil. 2/2021 v2.0).")

        with col_j2:
            st.markdown("#### 📦 Deliverables Checklist")
            st.success("✅ **Executive Summary PDF:** Generated & Ready")
            st.success("✅ **Poster A1 (PDF):** High-Res Infographic Ready")
            st.success("✅ **Pitch Deck (5 Slides):** Aligned with Slide Requirements")
            st.success("✅ **Video Demo (2 Mins MP4):** HD Screen Recording Ready")
            st.success("✅ **Live Prototype Demo:** Operational")

            st.markdown("---")
            st.markdown("#### 👥 Team Details — VECTOR 1")
            st.write("**Lead Agency:** Jabatan Alam Sekitar (JAS) / Multi-Agency Unit")
            st.write("**Team Members:** 3 Public Servants")
            st.write("**Target CSP Platform:** Google Cloud / Looker Studio (CFA Catalog)")
