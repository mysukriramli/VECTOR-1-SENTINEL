import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

def render_training_module_page():
    st.subheader("Capacity Training & Officer Certification Hub")
    st.caption("Structured training curricula, statutory enforcement SOPs, and scenario-based competency assessments for inter-agency personnel.")

    st.markdown("---")

    # Top Metric Banner
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Certified Officers", "1,240 Personnel", "JAS / JKDM / MITI")
    m2.metric("Active Modules", "6 Courses", "Multi-MEA Protocols")
    m3.metric("Pass Rate Benchmark", "94.2%", "Min Score: 80%")
    m4.metric("CPD Hours Awarded", "4,960 Hours", "Public Service Alignment")

    st.markdown("---")

    # Main Training Tabs
    tab_courses, tab_assessment, tab_sops, tab_analytics = st.tabs([
        "Interactive Course Catalogue",
        "Competency Assessment & Certification",
        "Field SOPs & Inspection Manuals",
        "Agency Completion Analytics"
    ])

    # --------------------------------------------------------------------------
    # TAB 1: INTERACTIVE COURSE CATALOGUE
    # --------------------------------------------------------------------------
    with tab_courses:
        st.markdown("##### Enforcement Capacity Building Curricula")
        st.caption("Select a course module to review curriculum objectives, target statutory frameworks, and lesson materials.")

        col_filter1, col_filter2 = st.columns([1, 1])
        with col_filter1:
            agency_filter = st.selectbox("Filter Curriculum by Agency Domain:", ["All Agencies", "JKDM (Customs)", "JAS (Environment)", "MITI (Trade)", "PERHILITAN (Wildlife)"])
        with col_filter2:
            level_filter = st.selectbox("Filter Skill Level:", ["All Levels", "Foundational (Level 100)", "Operational (Level 200)", "Advanced Governance (Level 300)"])

        st.markdown("<br>", unsafe_allow_html=True)

        courses = [
            {
                "code": "MOD-101",
                "title": "Basel Convention & Plastic Scrap (HS 3915) Forensic Inspection",
                "agency": "JAS (Environment)",
                "level": "Foundational (Level 100)",
                "duration": "2.5 Hours (1 CPD Credit)",
                "description": "Comprehensive guide to identifying illegal municipal plastic waste misclassified as secondary resin flakes. Covers unit value anomaly detection, weight-to-volume density ratios, and physical sampling procedures.",
                "topics": ["Statutory Scope under Act 127 (Environmental Quality Act)", "Customs K1 Declaration Verification", "Interpreting plastic_forensic_pipeline.joblib Anomaly Scores"]
            },
            {
                "code": "MOD-102",
                "title": "Montreal Protocol & ODS Gas (HS 2903) Border Interdiction",
                "agency": "JKDM (Customs)",
                "level": "Operational (Level 200)",
                "duration": "3.0 Hours (1.5 CPD Credits)",
                "description": "Techniques for detecting unlicensed ozone-depleting refrigerants (HCFC-22, CFC-12). Covers pressure container analysis, chemical name verification, and MITI import quota validation.",
                "topics": ["Quota Verification via MyGDX API", "Gas Cylinder Pressure & Weight Matching", "Handling Hazardous Chemical Samples at Port Terminals"]
            },
            {
                "code": "MOD-201",
                "title": "SENTINEL Human-in-the-Loop (HITL) Incident Adjudication Workflow",
                "agency": "All Agencies",
                "level": "Operational (Level 200)",
                "duration": "2.0 Hours (1 CPD Credit)",
                "description": "Operational protocol for reviewing ML anomaly flags, recording legally auditable inspection notes, overriding false positives, and executing inter-agency detention orders.",
                "topics": ["Adjudication Workbench Interface", "Legal Chain of Custody & Judicial Logs", "Inter-Agency Referral Matrix (JAS-JKDM-PERHILITAN)"]
            },
            {
                "code": "MOD-202",
                "title": "CITES Framework & Timber/Fauna Cargo Verification",
                "agency": "PERHILITAN (Wildlife)",
                "level": "Operational (Level 200)",
                "duration": "4.0 Hours (2 CPD Credits)",
                "description": "Identifying restricted flora and protected timber species under CITES Appendices I & II. Focuses on document verification for HS 4403/4407 timber and airport cargo inspections.",
                "topics": ["CITES Permit Authentication", "Volumetric Timber Density Discrepancies", "Air Cargo Screening at KLIA Terminals 1 & 2"]
            },
            {
                "code": "MOD-301",
                "title": "Explainable AI (XAI) & Model Risk Governance for Senior Officers",
                "agency": "MITI (Trade)",
                "level": "Advanced Governance (Level 300)",
                "duration": "1.5 Hours (1 CPD Credit)",
                "description": "Executive briefing on interpreting Feature Sensitivity (SHAP/LIME) metrics, managing model drift, calibrating contamination thresholds, and complying with SPA Bil 2/2021 cloud security guidelines.",
                "topics": ["Feature Weight Distribution Analysis", "Threshold Tuning vs Inspection Capacity", "Data Security & Governance under JDN Guidelines"]
            }
        ]

        # Apply Filters
        filtered_courses = courses
        if agency_filter != "All Agencies":
            target = agency_filter.split()[0]
            filtered_courses = [c for c in filtered_courses if target in c["agency"] or "All" in c["agency"]]
        if level_filter != "All Levels":
            filtered_courses = [c for c in filtered_courses if level_filter == c["level"]]

        for c in filtered_courses:
            with st.expander(f"[{c['code']}] {c['title']} ({c['agency']})"):
                st.markdown(f"**Skill Level:** `{c['level']}` &nbsp;|&nbsp; **Duration:** `{c['duration']}`")
                st.markdown(f"**Course Description:** {c['description']}")
                st.markdown("**Core Modules Covered:**")
                for t in c["topics"]:
                    st.markdown(f"- {t}")
                
                st.markdown("<br>", unsafe_allow_html=True)
                col_btn1, col_btn2 = st.columns([1, 3])
                with col_btn1:
                    if st.button(f"Start Course {c['code']}", key=f"btn_start_{c['code']}"):
                        st.success(f"Enrolled in {c['code']}. Progress tracked under your active user badge.")

    # --------------------------------------------------------------------------
    # TAB 2: COMPETENCY ASSESSMENT & CERTIFICATION
    # --------------------------------------------------------------------------
    with tab_assessment:
        st.markdown("##### Officer Competency Assessment Engine")
        st.caption("Complete the scenario-based examination below to validate your compliance knowledge and earn a SENTINEL Certified Specialist Credential.")

        with st.form("assessment_form"):
            st.markdown("###### Candidate Registration")
            col_u1, col_u2 = st.columns(2)
            with col_u1:
                officer_name = st.text_input("Full Officer Name:", value="Officer Azman Bin Ishak")
                officer_id = st.text_input("Badge / Government Staff ID:", value="JKDM-PK-88421")
            with col_u2:
                officer_agency = st.selectbox("Primary Agency Branch:", ["JKDM (Customs)", "JAS (Environment)", "MITI (Trade)", "PERHILITAN (Wildlife)"])
                target_cert = st.selectbox("Certification Target:", ["Basel Convention & Plastic Scrap Forensic Specialist", "Montreal Protocol ODS Inspection Specialist", "Multi-MEA HITL Review Specialist"])

            st.markdown("---")
            st.markdown("###### Examination Scenarios (Passing Threshold: 80%)")

            # Question 1
            st.markdown("**Question 1:** You are inspecting a Customs K1 import declaration for HS 3915.10 (Plastic Waste) with a declared value of **$0.12 / kg** and a container volume density of **420 kg / m³**. The SENTINEL ML model calculates an anomaly score of **91.4 / 100**. What is the appropriate enforcement action under JAS/JKDM SOPs?")
            q1_ans = st.radio(
                "Select Action (Q1):",
                [
                    "A) Immediately clear the container as unit price falls below standard resin market benchmarks.",
                    "B) Issue a physical inspection hold order, notify JAS Port Klang, and execute container sampling for municipal contamination.",
                    "C) Unilaterally reject the shipment without logging officer notes in the HITL queue.",
                    "D) Re-classify the shipment under HS 2903 without notification."
                ],
                key="q1"
            )

            st.markdown("<br>", unsafe_allow_html=True)

            # Question 2
            st.markdown("**Question 2:** Under the Montreal Protocol and Malaysian law, what additional verification step is required before clearing shipments containing refrigerants under HS 2903?")
            q2_ans = st.radio(
                "Select Action (Q2):",
                [
                    "A) Verify active import quota allocation issued by MITI via the MyGDX API and cross-reference cylinder pressure ratings.",
                    "B) Rely solely on exporter self-declarations provided in the commercial invoice.",
                    "C) Waive chemical verification if net container weight is under 10,000 kg.",
                    "D) Forward manifest data directly to the public portal without agency review."
                ],
                key="q2"
            )

            st.markdown("<br>", unsafe_allow_html=True)

            # Question 3
            st.markdown("**Question 3:** What is the legal requirement for an enforcement officer executing a Human-in-the-Loop (HITL) override on a high-risk ML flag?")
            q3_ans = st.radio(
                "Select Action (Q3):",
                [
                    "A) No documentation is required if the officer has over 5 years of service.",
                    "B) The officer must provide a digital signature, badge ID, and mandatory written justification in the judicial audit log.",
                    "C) Overrides can only be approved via informal telephone communications.",
                    "D) The ML model automatically locks overrides unless approved by external vendors."
                ],
                key="q3"
            )

            st.markdown("<br>", unsafe_allow_html=True)
            submit_exam = st.form_submit_button("Submit Assessment for Evaluation", type="primary")

        if submit_exam:
            score = 0
            if "B)" in q1_ans: score += 33.33
            if "A)" in q2_ans: score += 33.33
            if "B)" in q3_ans: score += 33.34

            st.markdown("---")
            if score >= 80:
                st.success(f"**PASSED** &mdash; Final Score: **{score:.1f}%**. Candidate {officer_name} ({officer_id}) has met the certification threshold.")
                
                # Certificate Preview Card
                st.markdown(f"""
                <div style="background:#FFFFFF; border:2px solid #1A365D; border-radius:10px; padding:24px; text-align:center; box-shadow:0 4px 12px rgba(26,54,93,0.08); margin-top:15px;">
                    <div style="font-size:0.8rem; font-weight:800; color:#64748B; text-transform:uppercase; letter-spacing:1px;">NATIONAL ENVIRONMENTAL SECURITY & TRADE COMPLIANCE ENGINE</div>
                    <h3 style="color:#1A365D; font-weight:800; margin:10px 0 4px 0;">Certificate of Competency</h3>
                    <div style="font-size:0.9rem; color:#334155;">This is to certify that</div>
                    <h4 style="color:#2563EB; font-weight:800; margin:8px 0;">{officer_name.upper()} ({officer_id})</h4>
                    <div style="font-size:0.88rem; color:#334155;">has successfully passed the rigorous scenario assessment for</div>
                    <div style="font-size:1.0rem; font-weight:700; color:#0F172A; margin:6px 0;">{target_cert}</div>
                    <div style="font-size:0.78rem; color:#64748B; margin-top:12px;">Issued on {datetime.now().strftime('%d %B %Y')} &middot; Authenticated via SENTINEL Governance Registry</div>
                </div>
                """, unsafe_allow_html=True)
                
                cert_text = f"SENTINEL COMPETENCY CERTIFICATE\nCandidate: {officer_name}\nBadge ID: {officer_id}\nAgency: {officer_agency}\nCert: {target_cert}\nScore: {score:.1f}%\nDate: {datetime.now().strftime('%Y-%m-%d')}"
                st.download_button("Download Official Digital Certificate (PDF/TXT)", cert_text, file_name=f"SENTINEL_Cert_{officer_id}.txt")
            else:
                st.error(f"**DID NOT PASS** &mdash; Final Score: **{score:.1f}%** (Passing Score: 80%). Please review the course materials under Tab 1 and re-attempt.")

    # --------------------------------------------------------------------------
    # TAB 3: FIELD SOPS & INSPECTION MANUALS
    # --------------------------------------------------------------------------
    with tab_sops:
        st.markdown("##### Standard Operating Procedures (SOPs) & Field Guidelines")
        st.caption("Official statutory inspection protocols approved by Jabatan Digital Negara (JDN), JKDM, and JAS.")

        sops = [
            {
                "id": "SOP-JKDM-JAS-2026-01",
                "title": "Joint Protocol for Intercepting Illicit Plastic Scrap & E-Waste Shipments",
                "framework": "Basel Convention & Environmental Quality Act 1974 (Act 127)",
                "summary": "Establishes physical sampling timelines, container hold procedures at Port Klang, Penang Port, and Pasir Gudang, and re-export protocol for non-compliant waste."
            },
            {
                "id": "SOP-JAS-MITI-2026-04",
                "title": "Ozone-Depleting Substance (ODS) Chemical Identification & Laboratory Testing",
                "framework": "Montreal Protocol & Customs (Prohibition of Imports) Order",
                "summary": "Step-by-step field guide for using portable chemical gas analyzers on pressurized cylinders under HS 2903 and verifying electronic licenses via MyGDX."
            },
            {
                "id": "SOP-PERHILITAN-2026-02",
                "title": "CITES Permitting & Protected Flora/Fauna Air Cargo Screening",
                "framework": "International Trade in Endangered Species Act 2008 (Act 686)",
                "summary": "Verification guidelines for timber density, species classification cross-checks, and handling suspect shipments at KLIA Cargo Complex."
            },
            {
                "id": "SOP-SENTINEL-GOV-01",
                "title": "Human-in-the-Loop (HITL) Digital Audit Trail & Judicial Evidence Handling",
                "framework": "Public Sector AI Governance Guidelines & SPA Bil 2/2021 v2.0",
                "summary": "Technical security manual detailing digital signature requirements, SHA-256 hash verification, and chain-of-custody logging for legal proceedings."
            }
        ]

        for s in sops:
            with st.container():
                st.markdown(f"""
                <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:4px solid #1A365D; border-radius:6px; padding:16px; margin-bottom:12px;">
                    <div style="font-size:0.75rem; font-weight:800; color:#2563EB; font-family:'JetBrains Mono', monospace;">{s['id']}</div>
                    <h5 style="margin:4px 0; color:#0F172A; font-weight:800;">{s['title']}</h5>
                    <div style="font-size:0.82rem; color:#64748B; margin-bottom:6px;"><b>Statutory Framework:</b> {s['framework']}</div>
                    <p style="font-size:0.85rem; color:#334155; margin-bottom:8px;">{s['summary']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                sop_content = f"{s['id']}\n{s['title']}\nFramework: {s['framework']}\n\n{s['summary']}\n\nOfficial document issued under the SENTINEL Trade Compliance Engine."
                st.download_button(f"Download {s['id']} Document (PDF)", sop_content, file_name=f"{s['id']}.txt", key=f"dl_{s['id']}")

    # --------------------------------------------------------------------------
    # TAB 4: AGENCY COMPLETION ANALYTICS
    # --------------------------------------------------------------------------
    with tab_analytics:
        st.markdown("##### Inter-Agency Training Completion Dashboard")
        st.caption("Monitoring staff certification rates, module engagement, and compliance scores across enforcement bodies.")

        # Analytics Data
        agency_data = pd.DataFrame({
            "Agency": ["JKDM Customs", "JAS Environment", "MITI Trade", "PERHILITAN Wildlife", "MAQIS Quarantine"],
            "Officers Enrolled": [520, 380, 180, 140, 90],
            "Certified Personnel": [485, 362, 168, 128, 81],
            "Completion Rate (%)": [93.2, 95.2, 93.3, 91.4, 90.0]
        })

        col_a1, col_a2 = st.columns([1.2, 1])

        with col_a1:
            fig_bar = px.bar(
                agency_data,
                x="Agency",
                y=["Officers Enrolled", "Certified Personnel"],
                barmode="group",
                title="Personnel Enrollment vs. Active Certification Count",
                color_discrete_sequence=["#94A3B8", "#1A365D"]
            )
            fig_bar.update_layout(height=320, margin=dict(l=10, r=10, t=40, b=10), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig_bar, use_container_width=True)

        with col_a2:
            st.markdown("###### Agency Certification Summary")
            st.dataframe(agency_data, use_container_width=True)
            
            st.markdown("""
            <div style="background:#EFF6FF; border:1px solid #BFDBFE; border-radius:6px; padding:12px; margin-top:10px;">
                <div style="font-size:0.82rem; font-weight:700; color:#1E3A8A;">KPI Milestone Met</div>
                <div style="font-size:0.8rem; color:#334155; margin-top:2px;">Over <b>92.5%</b> of primary port enforcement personnel have completed Level 100 & 200 Multi-MEA inspection tracks.</div>
            </div>
            """, unsafe_allow_html=True)
