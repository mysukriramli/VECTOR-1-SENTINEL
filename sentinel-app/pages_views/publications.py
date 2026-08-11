import streamlit as st

def render_publications_page():
    st.subheader("Research & Scientific Publications")
    st.caption("Peer-reviewed methodologies and arXiv preprints providing the theoretical and mathematical foundation for SENTINEL's trade anomaly detection pipelines.")

    st.markdown("---")

    publications = [
        {
            "id": "arXiv:2511.08638",
            "title": "Pattern Recognition of Scrap Plastic Misclassification in Global Trade Data",
            "author": "Muhammad Sukri Bin Ramli",
            "date": "November 2025",
            "domain": "Basel Convention (HS 3915 Plastic Scrap)",
            "pipeline": "plastic_forensic_pipeline.joblib",
            "arxiv_url": "https://arxiv.org/abs/2511.08638",
            "pdf_url": "https://arxiv.org/pdf/2511.08638",
            "abstract": "We propose an interpretable machine learning framework to help identify trade data discrepancies that are challenging to detect with traditional methods. Our system analyzes trade data to find a novel inverse price-volume signature, a pattern where reported volumes increase as average unit prices decrease. The model achieves 0.9375 accuracy and was validated by comparing large-scale UN data with detailed firm-level data.",
            "bibtex": """@article{ramli2025plastic,
  title={Pattern Recognition of Scrap Plastic Misclassification in Global Trade Data},
  author={Ramli, Muhammad Sukri Bin},
  journal={arXiv preprint arXiv:2511.08638},
  year={2025}
}"""
        },
        {
            "id": "arXiv:2512.07864",
            "title": "Pattern Recognition of Ozone-Depleting Substance Exports in Global Trade Data",
            "author": "Muhammad Sukri Bin Ramli",
            "date": "November 2025",
            "domain": "Montreal Protocol (HS 2903 ODS Refrigerants)",
            "pipeline": "ods_forensic_pipeline.joblib",
            "arxiv_url": "https://arxiv.org/abs/2512.07864",
            "pdf_url": "https://arxiv.org/pdf/2512.07864",
            "abstract": "Introduces an unsupervised machine learning framework to systematically detect suspicious trade patterns under the Montreal Protocol. Applied across 100,000 trade records, combining Unsupervised Clustering (K-Means) and Anomaly Detection (Isolation Forest & IQR) to isolate price-per-kilogram outliers and mega-trades. Validated using Explainable AI (SHAP).",
            "bibtex": """@article{ramli2025ods,
  title={Pattern Recognition of Ozone-Depleting Substance Exports in Global Trade Data},
  author={Ramli, Muhammad Sukri Bin},
  journal={arXiv preprint arXiv:2512.07864},
  year={2025}
}"""
        },
        {
            "id": "arXiv:2509.21395",
            "title": "Pattern Recognition of Illicit E-Waste Misclassification in Global Trade Data",
            "author": "Muhammad Sukri Bin Ramli",
            "date": "September 2025",
            "domain": "Basel Convention (HS 8548/8549 E-Waste Slag)",
            "pipeline": "ewaste_forensic_pipeline.joblib",
            "arxiv_url": "https://arxiv.org/abs/2509.21395",
            "pdf_url": "https://arxiv.org/pdf/2509.21395",
            "abstract": "Proposes an Outlier-Aware Segmentation approach (iterative K-Means with Logistic Regression Waste Scoring) to segment trade products and isolate goods exhibiting an anomalous waste signature. Successfully identifies finished electrical goods traded with scrap price signatures.",
            "bibtex": """@article{ramli2025ewaste,
  title={Pattern Recognition of Illicit E-Waste Misclassification in Global Trade Data},
  author={Ramli, Muhammad Sukri Bin},
  journal={arXiv preprint arXiv:2509.21395},
  year={2025}
}"""
        }
    ]

    for pub in publications:
        with st.container():
            st.markdown(f"""
            <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:5px solid #1A365D; border-radius:8px; padding:20px; margin-bottom:18px; box-shadow:0 2px 8px rgba(15,23,42,0.03);">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                    <span style="background:#EFF6FF; color:#1A365D; font-size:0.75rem; font-weight:800; padding:3px 10px; border-radius:4px; border:1px solid #BFDBFE;">{pub['id']}</span>
                    <span style="font-size:0.8rem; color:#64748B; font-weight:600;">Published: {pub['date']}</span>
                </div>
                <h4 style="margin:6px 0; color:#1A365D; font-size:1.15rem; font-weight:800;">{pub['title']}</h4>
                <div style="font-size:0.85rem; color:#334155; margin-bottom:10px;"><b>Author:</b> {pub['author']}</div>
                <p style="font-size:0.88rem; color:#475569; line-height:1.5; margin-bottom:12px;">{pub['abstract']}</p>
                <div style="display:flex; gap:16px; font-size:0.8rem; color:#64748B;">
                    <span><b>Statutory Scope:</b> {pub['domain']}</span>
                    <span>|</span>
                    <span><b>Model Asset:</b> <code>{pub['pipeline']}</code></span>
                </div>
            </div>
            """, unsafe_allow_html=True)

            col_link1, col_link2, col_cit = st.columns([1, 1, 2])
            with col_link1:
                st.link_button("View on arXiv", pub['arxiv_url'], use_container_width=True)
            with col_link2:
                st.link_button("Download PDF", pub['pdf_url'], use_container_width=True)
            with col_cit:
                with st.expander("Export BibTeX Citation"):
                    st.code(pub['bibtex'], language="latex")

        st.markdown("<br>", unsafe_allow_html=True)
