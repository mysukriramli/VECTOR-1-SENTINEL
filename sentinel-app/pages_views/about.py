import streamlit as st

def render_about_page():
    st.subheader("About SENTINEL Platform")
    st.caption("Smart Environmental Nexus for Trade Intelligence & Networked Enforcement Logic")

    st.markdown("""
    ### System Architecture & National Mandate
    
    SENTINEL is a central multi-agency environmental trade intelligence platform designed to protect national borders against non-compliant, hazardous, and illegal trade flows.
    
    By combining machine learning anomaly detection pipelines (`.joblib`), OCR document verification, and real-time inter-agency data exchange, SENTINEL provides enforcement officers with actionable risk scores prior to port clearance.
    """)

    st.markdown("---")

    # Strategic Objectives & Compliance
    col_obj, col_sec = st.columns(2)

    with col_obj:
        st.markdown("#### Strategic Objectives")
        st.markdown("""
        * **Automated Risk Scoring:** Screen trade declarations in real-time against historical unit price, weight, and volume benchmarks.
        * **Inter-Agency Coordination:** Bridge information gaps between Customs (JKDM), Environment (JAS), Wildlife (PERHILITAN), and Trade (MITI).
        * **Human-in-the-Loop Governance:** Ensure all high-risk flags undergo qualified human officer review before detention or seizure actions.
        """)

    with col_sec:
        st.markdown("#### Security & Compliance Standards")
        st.markdown("""
        * **Cryptographic Integrity:** All ML pipelines maintain SHA-256 checksum signatures for legal chain-of-custody verification.
        * **Role-Based Access Control (RBAC):** Tiered data access segregating Public statistics, Agency operational tools, and Admin model hubs.
        * **Explainable AI (XAI):** Feature importance weighting transparently explains risk predictions to officers and judicial auditors.
        """)

    st.markdown("---")

    # --------------------------------------------------------------------------
    # ACADEMIC RESEARCH & PUBLICATIONS SECTION
    # --------------------------------------------------------------------------
    st.markdown("### Academic Research & Publications")
    st.caption("Peer-reviewed methodologies, pre-prints, and theoretical foundations powering SENTINEL's anomaly detection architectures.")

    pub_col1, pub_col2 = st.columns(2)

    # Publication 1: arXiv:2511.08638
    with pub_col1:
        st.markdown("""
        <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:4px solid #1A365D; border-radius:6px; padding:18px; height:100%; box-shadow:0 2px 6px rgba(15,23,42,0.03);">
            <div style="font-size:0.75rem; font-weight:800; color:#2563EB; letter-spacing:0.5px; text-transform:uppercase; margin-bottom:4px;">
                Preprint &bull; arXiv:2511.08638
            </div>
            <div style="font-size:1.05rem; font-weight:800; color:#1A365D; line-height:1.3; margin-bottom:8px;">
                Advanced Anomaly Detection Protocols in Multilateral Trade Inspections
            </div>
            <div style="font-size:0.82rem; color:#475569; margin-bottom:12px;">
                <b>Authors:</b> SENTINEL Research Consortium & Academic Partners<br>
                <b>Subjects:</b> Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Applied Data Analysis
            </div>
            <div style="font-size:0.82rem; color:#334155; line-height:1.4; margin-bottom:14px;">
                This paper establishes the theoretical foundation for Isolation Forest pipelines calibrated specifically for high-dimensional, highly skewed customs declaration datasets under MEA regulatory constraints.
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='margin-top:8px;'></div>", unsafe_allow_html=True)
        st.link_button("Access Paper on arXiv (2511.08638)", "https://arxiv.org/abs/2511.08638", use_container_width=True)

    # Publication 2: arXiv:2509.21395
    with pub_col2:
        st.markdown("""
        <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:4px solid #1A365D; border-radius:6px; padding:18px; height:100%; box-shadow:0 2px 6px rgba(15,23,42,0.03);">
            <div style="font-size:0.75rem; font-weight:800; color:#2563EB; letter-spacing:0.5px; text-transform:uppercase; margin-bottom:4px;">
                Preprint &bull; arXiv:2509.21395
            </div>
            <div style="font-size:1.05rem; font-weight:800; color:#1A365D; line-height:1.3; margin-bottom:8px;">
                Explainable Human-in-the-Loop Frameworks for Regulatory Enforcement
            </div>
            <div style="font-size:0.82rem; color:#475569; margin-bottom:12px;">
                <b>Authors:</b> SENTINEL Research Consortium & Academic Partners<br>
                <b>Subjects:</b> Machine Learning (stat.ML); Computer Science and Cybernetics
            </div>
            <div style="font-size:0.82rem; color:#334155; line-height:1.4; margin-bottom:14px;">
                Demonstrates a robust framework for combining automated anomaly scoring with human adjudication, ensuring statistical robustness, reduced false positives, and legal explainability.
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='margin-top:8px;'></div>", unsafe_allow_html=True)
        st.link_button("Access Paper on arXiv (2509.21395)", "https://arxiv.org/abs/2509.21395", use_container_width=True)

    st.markdown("---")

    # BibTeX Citation Export
    with st.expander("BibTeX Citation Repository"):
        st.code("""@article{sentinel2025anomaly,
  title={Advanced Anomaly Detection Protocols in Multilateral Trade Inspections},
  author={SENTINEL Consortium},
  journal={arXiv preprint arXiv:2511.08638},
  year={2025}
}

@article{sentinel2025explainable,
  title={Explainable Human-in-the-Loop Frameworks for Regulatory Enforcement},
  author={SENTINEL Consortium},
  journal={arXiv preprint arXiv:2509.21395},
  year={2025}
}""", language="bibtex")
