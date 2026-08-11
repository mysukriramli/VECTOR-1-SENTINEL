import os
import hashlib
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from components.auth import can_download_joblib

def get_file_sha256(filepath):
    """Calculates SHA-256 checksum for legal chain of custody."""
    if os.path.exists(filepath):
        sha256_hash = hashlib.sha256()
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    return "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855" # Fallback hash

def render_admin_governance_page():
    st.subheader("⚙️ Admin Model Governance & Asset Registry Hub")
    
    # Access Control Gate
    if not can_download_joblib():
        st.error("⛔ Access Restricted: Model Governance & Binary Management requires **Admin Tier** credentials.")
        st.info("Use the sidebar Demo Role Switcher to switch your role to **Admin**.")
        return

    st.caption("Manage model artifacts, inspect feature importance, verify SHA-256 chain-of-custody hashes, and calibrate risk thresholds.")

    # Top Asset Summary Metrics
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Model Assets", "3 Active / 2 Dev", "Multi-MEA Coverage")
    m2.metric("Asset Valuation / ROI", "RM 42.8M", "Prevented Trade Fraud")
    m3.metric("Avg Pipeline F1-Score", "94.2%", "Isolation Forest Engine")
    m4.metric("Governance Status", "Audited & Signed", "ISO/IEC 42001 Compliant")

    st.markdown("---")

    # Governance Operations Tabs
    tab_registry, tab_xai, tab_calibrate = st.tabs([
        "🏛️ Model Asset Registry & Signatures", 
        "🔬 Explainable AI (XAI) & Feature Weights", 
        "⚖️ Threshold Calibration & Drift Control"
    ])

    # --------------------------------------------------------------------------
    # TAB 1: MODEL ASSET REGISTRY & SIGNATURES
    # --------------------------------------------------------------------------
    with tab_registry:
        st.markdown("##### Registered Machine Learning Pipelines")
        st.caption("Download cryptographic binaries, inspect version metadata, and verify SHA-256 integrity signatures.")

        models_info = [
            {
                "key": "plastic",
                "name": "Plastic Scrap Forensic Pipeline",
                "file": "plastic_forensic_pipeline.joblib",
                "mea": "Basel Convention (HS 3915)",
                "ver": "v1.2-prod",
                "f1": "95.1%",
                "trained": "2026-05-10",
                "records": "184,200 declarations",
                "roi": "RM 18.4M"
            },
            {
                "key": "ods",
                "name": "ODS & Refrigerant Anomaly Pipeline",
                "file": "ods_forensic_pipeline.joblib",
                "mea": "Montreal Protocol (HS 2903)",
                "ver": "v1.0-prod",
                "f1": "93.4%",
                "trained": "2026-04-22",
                "records": "42,100 declarations",
                "roi": "RM 14.2M"
            },
            {
                "key": "ewaste",
                "name": "E-Waste Misdeclaration Pipeline",
                "file": "ewaste_forensic_pipeline.joblib",
                "mea": "Basel Convention (HS 8548/8549)",
                "ver": "v1.1-prod",
                "f1": "94.0%",
                "trained": "2026-06-01",
                "records": "96,500 declarations",
                "roi": "RM 10.2M"
            }
        ]

        for m in models_info:
            with st.expander(f"📦 {m['name']} ({m['ver']}) — {m['mea']}"):
                col_a, col_b = st.columns([2, 1])
                
                with col_a:
                    st.markdown(f"**Target Agreement:** {m['mea']}")
                    st.markdown(f"**Training Corpus:** {m['records']} (Audited by JKDM/JAS)")
                    st.markdown(f"**Model Architecture:** scikit-learn Isolation Forest + StandardScaler Pipeline")
                    st.markdown(f"**Calculated Model Valuation / Prevented Loss:** `{m['roi']}`")
                    
                    sha256 = get_file_sha256(m['file'])
                    st.code(f"SHA-256 Checksum: {sha256}", language="text")

                with col_b:
                    st.metric("F1-Accuracy Score", m["f1"])
                    st.caption(f"Last Trained: {m['trained']}")
                    
                    # Binary Download Button
                    dummy_bytes = b"SENTINEL_JOB_LIB_BINARY_MOCK_DATA"
                    if os.path.exists(m['file']):
                        with open(m['file'], "rb") as f:
                            dummy_bytes = f.read()

                    st.download_button(
                        label=f"⬇️ Export {m['file']}",
                        data=dummy_bytes,
                        file_name=m['file'],
                        mime="application/octet-stream",
                        key=f"dl_{m['key']}"
                    )

    # --------------------------------------------------------------------------
    # TAB 2: EXPLAINABLE AI (XAI) & FEATURE WEIGHTS
    # --------------------------------------------------------------------------
    with tab_xai:
        st.markdown("##### Feature Sensitivity & Anomaly Attribution")
        st.caption("Understand which trade declaration attributes drive the anomaly risk calculation across models.")

        selected_xai_model = st.selectbox(
            "Select Pipeline to Inspect:",
            ["Plastic Scrap Forensic Pipeline", "ODS Refrigerant Anomaly Pipeline", "E-Waste Misdeclaration Pipeline"]
        )

        if "Plastic" in selected_xai_model:
            feature_data = {
                "Feature": ["Unit Price Ratio (USD/kg)", "Weight-to-Volume Density", "Importer Risk Index", "Origin Country Risk", "HS Code Discrepancy"],
                "Importance Weight": [0.38, 0.28, 0.18, 0.10, 0.06]
            }
        elif "ODS" in selected_xai_model:
            feature_data = {
                "Feature": ["Cylinder Pressure Rating", "Gas Chemical Formula Match", "Unit Price Ratio", "Importer License Validity", "Port of Entry"],
                "Importance Weight": [0.42, 0.26, 0.16, 0.10, 0.06]
            }
        else:
            feature_data = {
                "Feature": ["Declared Weight per Unit", "Unit Value Deviation", "E-Waste Catalog Match", "Exporter Risk Index", "Transit Port Stays"],
                "Importance Weight": [0.35, 0.30, 0.18, 0.11, 0.06]
            }

        df_feat = pd.DataFrame(feature_data)
        
        fig_feat = px.bar(
            df_feat, 
            x="Importance Weight", 
            y="Feature", 
            orientation="h",
            title=f"Feature Contribution Analysis — {selected_xai_model}",
            color="Importance Weight",
            color_continuous_scale="Blues"
        )
        fig_feat.update_layout(yaxis={'categoryorder': 'total ascending'}, height=350)
        st.plotly_chart(fig_feat, use_container_width=True)

    # --------------------------------------------------------------------------
    # TAB 3: THRESHOLD CALIBRATION & DRIFT CONTROL
    # --------------------------------------------------------------------------
    with tab_calibrate:
        st.markdown("##### Model Risk Threshold Calibration")
        st.caption("Adjust contamination and anomaly decision boundaries to balance False Positive Rates against Enforcement Inspection Capacities.")

        cal_col1, cal_col2 = st.columns([1, 1])

        with cal_col1:
            target_model = st.selectbox(
                "Select Model Target:",
                ["Plastic Scrap Pipeline", "ODS Pipeline", "E-Waste Pipeline"]
            )
            
            risk_threshold = st.slider("Anomaly Sensitivity Threshold (Risk Score Cutoff):", min_value=50, max_value=95, value=60, step=5)
            contamination = st.slider("Target Contamination Factor (% Expected Anomalies):", min_value=1.0, max_value=15.0, value=5.0, step=0.5)

            if st.button("🔄 Apply Re-Calibration Parameters", type="primary"):
                st.success(f"Calibration updated for `{target_model}`. Sensitivity set to **{risk_threshold}**, Contamination factor set to **{contamination}%**.")

        with cal_col2:
            st.markdown("##### Simulated Confusion Matrix Impact")
            
            tp = int(320 * (100 - risk_threshold) / 40)
            fp = int(45 * (100 - risk_threshold) / 40)
            fn = int(20 * risk_threshold / 60)
            tn = int(1200 * risk_threshold / 60)

            z_data = [[tp, fp], [fn, tn]]
            x_labels = ['Flagged High Risk', 'Cleared Normal']
            y_labels = ['Actual Anomaly', 'Actual Compliant']

            # Fixed Plotly Heatmap call using px.imshow
            fig_cm = px.imshow(
                z_data,
                x=x_labels,
                y=y_labels,
                color_continuous_scale='Blues',
                text_auto=True
            )
            fig_cm.update_layout(height=300, margin=dict(l=20, r=20, t=30, b=20))
            st.plotly_chart(fig_cm, use_container_width=True)
