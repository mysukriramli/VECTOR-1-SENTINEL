import streamlit as st

def render_about_page():
    st.subheader("ℹ️ About SENTINEL Platform")
    st.caption("Smart Environmental Nexus for Trade Intelligence & Networked Enforcement Logic")

    st.markdown("""
    ### System Architecture & National Mandate
    
    **SENTINEL** is a multi-agency environmental trade intelligence platform designed to protect national borders against non-compliant, hazardous, and illegal trade flows.
    
    By combining **machine learning anomaly pipelines (.joblib)**, **OCR document verification**, and **real-time data exchange**, SENTINEL provides enforcement officers with actionable risk scores prior to container clearance.
    """)

    st.markdown("---")

    a1, a2 = st.columns(2)

    with a1:
        st.markdown("#### 🎯 Strategic Objectives")
        st.markdown("""
        * **Automated Risk Scoring:** Screen trade declarations in real-time against historical price, weight, and volume benchmarks.
        * **Inter-Agency Coordination:** Bridge information gaps between Customs (**JKDM**), Environment (**JAS**), Wildlife (**PERHILITAN**), and Trade (**MITI**).
        * **Human-in-the-Loop Governance:** Ensure all high-risk flags undergo qualified human officer review before detention or seizure actions.
        """)

    with a2:
        st.markdown("#### 🔒 Security & Compliance Standards")
        st.markdown("""
        * **Cryptographic Integrity:** All ML pipelines maintain SHA-256 checksum signatures for chain-of-custody verification.
        * **Role-Based Access Control (RBAC):** Tiered data access segregating Public statistics, Agency operational tools, and Admin model hubs.
        * **Explainable AI (XAI):** Feature importance weighting transparently explains risk predictions to officers and auditors.
        """)
