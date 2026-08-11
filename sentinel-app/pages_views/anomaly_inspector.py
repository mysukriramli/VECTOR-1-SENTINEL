import streamlit as st
from components.ml_engine import run_inference

def render_anomaly_inspector_page():
    st.subheader("🔍 Multi-MEA Live Anomaly Inspector")
    if st.session_state["user_role"] == "Public (Free)":
        st.warning("🔒 Access Restricted to Gov Agency or Admin credentials.")
        return

    selected_model = st.selectbox(
        "Select Pipeline:",
        ["Plastic Scrap Detector (plastic_forensic_pipeline.joblib)", "ODS Refrigerant Detector (ods_forensic_pipeline.joblib)", "E-Waste Detector (ewaste_forensic_pipeline.joblib)"]
    )
    key_map = {
        "Plastic Scrap Detector (plastic_forensic_pipeline.joblib)": "plastic",
        "ODS Refrigerant Detector (ods_forensic_pipeline.joblib)": "ods",
        "E-Waste Detector (ewaste_forensic_pipeline.joblib)": "ewaste"
    }
    
    unit_price = st.number_input("Declared Unit Price (USD/kg):", value=0.25)
    weight_kg = st.number_input("Total Weight (kg):", value=25000.0)
    volume_m3 = st.number_input("Volume (m³):", value=65.0)

    if st.button("Run .joblib Inference", type="primary"):
        score, is_anomaly, msg = run_inference(key_map[selected_model], unit_price, weight_kg, volume_m3)
        st.metric("Risk Score", f"{score} / 100")
        if is_anomaly:
            st.error(f"🚨 {msg}")
        else:
            st.success(f"✅ {msg}")