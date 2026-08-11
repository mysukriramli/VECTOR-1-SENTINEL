import streamlit as st
import pandas as pd
from datetime import datetime

def init_incident_queue():
    """Initializes shared session state queue for HITL incidents."""
    if "incident_queue" not in st.session_state:
        st.session_state["incident_queue"] = [
            {
                "Case_ID": "INC-2026-8801",
                "Timestamp": "2026-08-11 09:15",
                "HS_Code": "3915.10 (Plastic Waste)",
                "Risk_Score": 92.4,
                "Primary_Agency": "JAS (Environment)",
                "Co_Agencies": ["JKDM (Customs)"],
                "Declared_Value": "$0.14/kg",
                "Status": "PENDING_REVIEW",
                "Officer_Note": "",
                "Decision_By": "-"
            },
            {
                "Case_ID": "INC-2026-8802",
                "Timestamp": "2026-08-11 11:30",
                "HS_Code": "2903.42 (ODS Refrigerants)",
                "Risk_Score": 88.1,
                "Primary_Agency": "JAS (Environment)",
                "Co_Agencies": ["MITI", "JKDM"],
                "Declared_Value": "$0.85/kg",
                "Status": "PENDING_REVIEW",
                "Officer_Note": "",
                "Decision_By": "-"
            },
            {
                "Case_ID": "INC-2026-8803",
                "Timestamp": "2026-08-11 13:05",
                "HS_Code": "8549.21 (E-Waste)",
                "Risk_Score": 76.5,
                "Primary_Agency": "JKDM (Customs)",
                "Co_Agencies": ["JAS"],
                "Declared_Value": "$0.30/kg",
                "Status": "ESCALATED",
                "Officer_Note": "Referred to JAS Port Klang unit for physical container sampling.",
                "Decision_By": "Officer Azman (JKDM)"
            }
        ]

def render_contact_page():
    st.subheader("📞 Multi-Agency Escalation & Human-in-the-Loop (HITL) Queue")
    
    # Access Control Gate
    if st.session_state.get("user_role") == "Public (Free)":
        st.warning("🔒 Access Restricted: Multi-Agency Escalation Queue requires Gov Agency or Admin credentials.")
        st.info("Use the sidebar Demo Role Switcher to switch to **Gov Agency** or **Admin**.")
        return

    init_incident_queue()
    st.caption("Human Officers review ML anomaly flags, record audit notes, override false positives, or initiate multi-agency interdiction workflows.")

    # Top Status Metrics
    q_data = st.session_state["incident_queue"]
    pending_cnt = sum(1 for x in q_data if x["Status"] == "PENDING_REVIEW")
    escalated_cnt = sum(1 for x in q_data if x["Status"] == "ESCALATED")
    resolved_cnt = sum(1 for x in q_data if x["Status"] in ["APPROVED_RELEASE", "DETAINED_CONFISCATED"])

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Pending Human Review", f"{pending_cnt} Cases", "Action Required")
    c2.metric("Inter-Agency Escalations", f"{escalated_cnt} Active", "JAS / MITI / JKDM")
    c3.metric("Resolved Cases Today", f"{resolved_cnt} Logged", "Audited")
    c4.metric("Active Response SLA", "< 15 Mins", "Target Met")

    st.markdown("---")

    tab_review, tab_matrix, tab_audit = st.tabs([
        "🛡️ HITL Officer Review Workbench",
        "🏛️ Inter-Agency Routing Matrix",
        "📜 Legal Audit Trail & Logs"
    ])

    # --------------------------------------------------------------------------
    # TAB 1: HUMAN-IN-THE-LOOP OFFICER WORKBENCH
    # --------------------------------------------------------------------------
    with tab_review:
        st.markdown("##### Pending Incident Verification Desk")
        
        # Filter Pending Cases
        pending_cases = [c for c in q_data if c["Status"] in ["PENDING_REVIEW", "ESCALATED"]]
        
        if not pending_cases:
            st.success("✅ All flagged anomalies have been reviewed by enforcement officers.")
        else:
            case_options = [f"{c['Case_ID']} | {c['HS_Code']} | Score: {c['Risk_Score']}" for c in pending_cases]
            selected_case_str = st.selectbox("Select Case to Review:", case_options)
            
            selected_id = selected_case_str.split(" | ")[0]
            case = next(c for c in q_data if c["Case_ID"] == selected_id)

            col_case_info, col_action = st.columns([1, 1])

            with col_case_info:
                st.markdown(f"### Case Details: `{case['Case_ID']}`")
                st.markdown(f"**Flagged HS Code:** {case['HS_Code']}")
                st.markdown(f"**ML Calculated Anomaly Score:** `{case['Risk_Score']} / 100`")
                st.markdown(f"**Declared Unit Value:** `{case['Declared_Value']}`")
                st.markdown(f"**Primary Lead Agency:** `{case['Primary_Agency']}`")
                st.markdown(f"**Support Agencies:** `{', '.join(case['Co_Agencies'])}`")
                st.markdown(f"**Current Status:** `{case['Status']}`")

            with col_action:
                st.markdown("### Human Officer Adjudication")
                
                officer_id = st.text_input("Officer Name / ID Badge:", value="Officer Fairuz (JKDM-PK)")
                decision_action = st.radio(
                    "Human Adjudication Action:",
                    [
                        "✅ Approve & Release (Human Override - False Positive)",
                        "🚨 Confirm Anomaly & Detain Container",
                        "🔄 Escalate to Secondary Agency for Sampling"
                    ]
                )

                if "Escalate" in decision_action:
                    target_agency = st.selectbox(
                        "Route Case File To:",
                        ["JAS (Jabatan Alam Sekitar)", "MITI", "PERHILITAN", "JKDM Enforcement Intelligence"]
                    )
                
                action_notes = st.text_area("Enforcement Justification / Inspection Notes:", placeholder="Enter details from physical spot-check or verification call...")

                if st.button("⚖️ Submit Binding Human Decision", type="primary"):
                    if "Approve" in decision_action:
                        case["Status"] = "APPROVED_RELEASE"
                    elif "Detain" in decision_action:
                        case["Status"] = "DETAINED_CONFISCATED"
                    else:
                        case["Status"] = "ESCALATED"
                        case["Primary_Agency"] = target_agency

                    case["Officer_Note"] = action_notes
                    case["Decision_By"] = officer_id
                    case["Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M")

                    st.success(f"Case `{case['Case_ID']}` updated successfully. Legal log appended.")
                    st.rerun()

    # --------------------------------------------------------------------------
    # TAB 2: INTER-AGENCY ROUTING MATRIX
    # --------------------------------------------------------------------------
    with tab_matrix:
        st.markdown("##### Multi-Agency Jurisdictional Matrix")
        st.caption("Automated routing rules dispatch flagged shipments to target enforcement bodies based on Multilateral Environmental Agreements (MEAs).")

        matrix_data = [
            {"MEA Protocol": "Basel Convention", "Tariff Domain": "HS 3915 (Plastics)", "Lead Agency": "JAS", "Secondary Agency": "JKDM", "Escalation Action": "Container Seizure / Re-export"},
            {"MEA Protocol": "Basel Convention", "Tariff Domain": "HS 8548/8549 (E-Waste)", "Lead Agency": "JAS", "Secondary Agency": "JKDM", "Escalation Action": "Physical Demolition / Fine"},
            {"MEA Protocol": "Montreal Protocol", "Tariff Domain": "HS 2903 (ODS Refrigerants)", "Lead Agency": "JAS", "Secondary Agency": "MITI / JKDM", "Escalation Action": "Gas Sampling & Lab Testing"},
            {"MEA Protocol": "CITES Framework", "Tariff Domain": "HS 0106 / 4403 (Flora/Fauna)", "Lead Agency": "PERHILITAN", "Secondary Agency": "JKDM / MAQIS", "Escalation Action": "Quarantine / Species Verification"}
        ]
        
        st.dataframe(pd.DataFrame(matrix_data), use_container_width=True)

    # --------------------------------------------------------------------------
    # TAB 3: LEGAL AUDIT TRAIL
    # --------------------------------------------------------------------------
    with tab_audit:
        st.markdown("##### Chain of Custody & Human Action Audit Logs")
        st.caption("All ML recommendations and human officer overrides are permanently recorded for judicial evidence compliance.")

        df_audit = pd.DataFrame(st.session_state["incident_queue"])
        st.dataframe(df_audit, use_container_width=True)

        csv_audit = df_audit.to_csv(index=False)
        st.download_button(
            label="📥 Download Signed Audit Log (CSV)",
            data=csv_audit,
            file_name="SENTINEL_Human_In_The_Loop_Audit.csv",
            mime="text/csv"
        )
