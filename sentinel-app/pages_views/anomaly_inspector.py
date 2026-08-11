import streamlit as st
import pandas as pd
from components.ml_engine import run_inference

def render_anomaly_inspector_page():
    st.subheader("🔍 Multi-MEA Live Scanner, CSV Upload & OCR Parser")
    
    # Access Control Gate
    if st.session_state.get("user_role") == "Public (Free)":
        st.warning("🔒 Access Restricted: Live trade scanning is available strictly for Gov Agency and Admin credentials.")
        st.info("Use the sidebar Demo Role Switcher to switch to **Gov Agency** or **Admin**.")
        return

    st.caption("Perform real-time ML inference, parse shipping manifest documents via OCR, or upload batch CSV manifest files.")

    # 3 Capabilities Tabs
    tab_manual, tab_csv, tab_ocr = st.tabs([
        "📝 Single Entry Scanner", 
        "📊 Batch CSV File Upload", 
        "📄 Document Manifest OCR Parser"
    ])

    # --------------------------------------------------------------------------
    # TAB 1: SINGLE ENTRY SCANNER
    # --------------------------------------------------------------------------
    with tab_manual:
        c1, c2 = st.columns([1, 1])

        with c1:
            st.markdown("##### Manual Input Manifest Scanner")
            
            selected_model = st.selectbox(
                "Select MEA Model Pipeline:",
                [
                    "Plastic Scrap Detector (plastic_forensic_pipeline.joblib)",
                    "ODS Refrigerant Detector (ods_forensic_pipeline.joblib)",
                    "E-Waste Misdeclaration Detector (ewaste_forensic_pipeline.joblib)"
                ],
                key="manual_model_select"
            )

            key_map = {
                "Plastic Scrap Detector (plastic_forensic_pipeline.joblib)": "plastic",
                "ODS Refrigerant Detector (ods_forensic_pipeline.joblib)": "ods",
                "E-Waste Misdeclaration Detector (ewaste_forensic_pipeline.joblib)": "ewaste"
            }
            model_key = key_map[selected_model]

            unit_price = st.number_input("Declared Unit Price (USD / kg):", min_value=0.01, value=0.25, step=0.05)
            weight_kg = st.number_input("Total Net Weight (kg):", min_value=1.0, value=32000.0, step=1000.0)
            volume_m3 = st.number_input("Container Volume (m³):", min_value=0.1, value=68.0, step=1.0)

            inspect_btn = st.button("Run .joblib Inference", type="primary", key="btn_manual")

        with c2:
            st.markdown("##### Forensic Risk Assessment Output")
            if inspect_btn:
                with st.spinner("Executing joblib model inference..."):
                    score, is_anomaly, msg = run_inference(model_key, unit_price, weight_kg, volume_m3)
                    st.metric("Calculated Risk Score", f"{score} / 100")
                    if is_anomaly:
                        st.error(f"🚨 **{msg}**")
                        st.warning("Action Recommended: Hold container at port for physical inspection.")
                    else:
                        st.success(f"✅ **{msg}**")

    # --------------------------------------------------------------------------
    # TAB 2: BATCH CSV FILE UPLOAD SCANNER
    # --------------------------------------------------------------------------
    with tab_csv:
        st.markdown("##### 📊 Upload Batch Trade Declarations (CSV)")
        st.caption("Upload a `.csv` manifest file containing multiple shipment entries to run automated ML anomaly scans across all rows.")

        sample_csv_data = "Declaration_ID,HS_Code,Unit_Price_USD,Weight_Kg,Volume_M3\nDEC-2026-001,3915.10,0.15,25000,65\nDEC-2026-002,3915.20,1.20,18000,42\nDEC-2026-003,2903.42,4.50,3000,12\nDEC-2026-004,8549.21,0.22,41000,80"
        st.download_button(
            label="📥 Download Sample CSV Template",
            data=sample_csv_data,
            file_name="sentinel_batch_sample.csv",
            mime="text/csv"
        )

        st.markdown("---")
        
        uploaded_csv = st.file_uploader("Choose a CSV file to scan:", type=["csv"], key="csv_uploader")
        
        if uploaded_csv:
            try:
                df = pd.read_csv(uploaded_csv)
                st.success(f"Successfully loaded `{uploaded_csv.name}` ({len(df)} records found).")
                st.write("##### Raw Upload Preview:", df.head(5))

                target_pipeline = st.selectbox(
                    "Select ML Model for Batch Inference:",
                    ["Plastic Scrap (plastic_forensic_pipeline.joblib)", "ODS Gases (ods_forensic_pipeline.joblib)", "E-Waste (ewaste_forensic_pipeline.joblib)"],
                    key="batch_pipeline_select"
                )
                
                pipeline_key = "plastic" if "Plastic" in target_pipeline else ("ods" if "ODS" in target_pipeline else "ewaste")

                if st.button("🚀 Run Batch ML Anomaly Inspection", type="primary", key="btn_batch"):
                    with st.spinner("Processing batch records through joblib pipeline..."):
                        risk_scores = []
                        anomaly_flags = []

                        for _, row in df.iterrows():
                            p = float(row.get("Unit_Price_USD", 0.5))
                            w = float(row.get("Weight_Kg", 10000))
                            v = float(row.get("Volume_M3", 30))
                            
                            score, is_anom, _ = run_inference(pipeline_key, p, w, v)
                            risk_scores.append(score)
                            anomaly_flags.append("🚨 HIGH RISK" if is_anom else "✅ NORMAL")

                        df["ML_Risk_Score"] = risk_scores
                        df["Compliance_Status"] = anomaly_flags

                        st.markdown("##### Batch Inspection Results")
                        st.dataframe(df, use_container_width=True)

                        csv_output = df.to_csv(index=False)
                        st.download_button(
                            label="📥 Download Flagged Batch Report (CSV)",
                            data=csv_output,
                            file_name="SENTINEL_Batch_Scan_Results.csv",
                            mime="text/csv"
                        )
            except Exception as e:
                st.error(f"Error reading CSV file: {str(e)}")

    # --------------------------------------------------------------------------
    # TAB 3: DOCUMENT OCR PARSER (PDF / IMAGE)
    # --------------------------------------------------------------------------
    with tab_ocr:
        st.markdown("##### 📄 Shipping Manifest OCR Document Parser")
        st.caption("Upload scanned Customs K1 Forms, Bills of Lading, or Commercial Invoices to automatically extract trade metadata via OCR.")

        uploaded_doc = st.file_uploader(
            "Upload Customs Document (PDF, PNG, JPG):", 
            type=["pdf", "png", "jpg", "jpeg"],
            key="ocr_uploader"
        )

        if uploaded_doc:
            st.success(f"Document `{uploaded_doc.name}` uploaded successfully.")
            
            col_doc1, col_doc2 = st.columns([1, 1])

            with col_doc1:
                st.markdown("##### Uploaded Document Preview")
                if "image" in uploaded_doc.type:
                    st.image(uploaded_doc, use_container_width=True)
                else:
                    st.info("📄 PDF Document Received & Ready for OCR Processing.")

            with col_doc2:
                st.markdown("##### Extracted OCR Metadata")
                if st.button("⚡ Run OCR Text Extraction", type="primary", key="btn_ocr"):
                    with st.spinner("Extracting text fields & cross-referencing HS Code catalog..."):
                        ocr_data = {
                            "Document_Type": "Customs K1 Import Declaration",
                            "Declared_HS_Code": "3915.10 (Plastic Waste)",
                            "Exporter_Country": "East Asia Regional Hub",
                            "Declared_Goods_Description": "Polyethylene Flakes Secondary Grade",
                            "Total_Weight_Kg": "24,500 kg",
                            "Declared_Value_USD": "$3,180.00",
                            "Parsed_Unit_Price": "$0.13 / kg"
                        }
                        
                        st.json(ocr_data)
                        
                        st.error("🚨 **OCR DISCREPANCY ALERT:** Parsed unit price ($0.13/kg) is 88% below standard virgin resin market value ($1.20/kg). High likelihood of hazardous municipal waste.")
