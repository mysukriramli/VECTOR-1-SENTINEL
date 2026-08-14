import streamlit as st

def get_comprehensive_faq_items():
    """
    Returns the comprehensive SENTINEL FAQ corpus covering system architecture, 
    ML pipelines, RBAC access tiers, statutory compliance, and operational SOPs.
    """
    return [
        # CATEGORY 1: PLATFORM OVERVIEW & RBAC ACCESS
        {
            "category": "🛡️ Platform Overview & RBAC Access",
            "q": "What is SENTINEL and who operates it?",
            "a": """**SENTINEL** (**S**mart **E**nvironmental **N**exus for **T**rade **I**ntelligence & **N**etworked **E**nforcement **L**ogic) is Malaysia's central inter-agency AI trade compliance and threat detection engine.

It is operated jointly across multi-agency enforcement bodies[cite: 1]:
* **JKDM:** Jabatan Kastam Diraja Malaysia (Royal Malaysian Customs Department)[cite: 1, 1]
* **JAS:** Jabatan Alam Sekitar (Department of Environment)[cite: 1, 1]
* **MITI:** Ministry of Investment, Trade & Industry[cite: 1, 1]
* **PERHILITAN:** Department of Wildlife & National Parks[cite: 1, 1]
* **MAQIS:** Malaysian Agricultural Quarantine and Inspection Services[cite: 1]"""
        },
        {
            "category": "🛡️ Platform Overview & RBAC Access",
            "q": "How does Role-Based Access Control (RBAC) work in SENTINEL?",
            "a": """SENTINEL enforces a 3-tier clearance hierarchy that dynamically customizes navigation menus and feature availability[cite: 1, 1]:

1. **Public (Free) Tier:** Designed for academic researchers and public transparency. Provides access to anonymized threat maps, open CSV datasets (CC BY 4.0), and peer-reviewed arXiv publications[cite: 1, 1].
2. **Gov Agency Tier:** Tailored for daily port enforcement officers (JKDM/JAS/MITI). Unlocks the **Live Multi-MEA Scanner** (manual entry, batch CSV, OCR manifest parser), **Looker Studio Analytics**, and the **Human-in-the-Loop (HITL) Adjudication Desk**[cite: 1, 1].
3. **Admin Tier:** Restricted to root system governors. Unlocks raw `.joblib` model binary downloads, SHA-256 cryptographic verification, model risk threshold calibration, and direct SQL queries against the 14.82M+ BigQuery Data Lake[cite: 1, 1]."""
        },
        {
            "category": "🛡️ Platform Overview & RBAC Access",
            "q": "Which Multilateral Environmental Agreements (MEAs) are covered?",
            "a": """SENTINEL screens trade manifest flows across four primary treaty frameworks[cite: 1, 1]:

| MEA Treaty Framework | Target Tariff Domain | Primary Model Pipeline Asset | Lead Agency |
| :--- | :--- | :--- | :--- |
| **Basel Convention** | Plastic Scrap (HS 3915) & E-Waste Slag (HS 8548/8549) | `plastic_forensic_pipeline.joblib` & `ewaste_forensic_pipeline.joblib` | JAS / JKDM |
| **Montreal Protocol** | Ozone-Depleting Refrigerants & Gases (HS 2903) | `ods_forensic_pipeline.joblib` | JAS / MITI |
| **CITES Framework** | Protected Fauna & Timber (HS 0106, 4403/4407) | `cites_timber_pipeline.joblib` *(In Dev)* | PERHILITAN / MAQIS |
| **Stockholm & Rotterdam** | POPs & Toxic Industrial Chemicals (HS 29/38) | `pops_chemical_pipeline.joblib` *(In Dev)* | Dept of Agriculture / JAS |"""
        },

        # CATEGORY 2: MACHINE LEARNING & OCR FORENSICS
        {
            "category": "🤖 Machine Learning & OCR Forensics",
            "q": "How does the ML inference engine detect trade anomalies?",
            "a": """The forensic engine evaluates trade declarations using **Scikit-Learn Isolation Forest** algorithms packaged within `StandardScaler` pipelines (`.joblib`)[cite: 1, 1]. 

The model analyzes key trade declaration attributes[cite: 1]:
* **Unit Price Ratio (USD/kg):** Flags declared values deviating significantly below global market virgin resin or chemical benchmarks[cite: 1, 1].
* **Volumetric Density Ratio ($kg/m^3$):** Identifies physical weight discrepancies indicative of unsorted municipal waste or scrap metal misdeclarations[cite: 1, 1].
* **Importer & Origin Risk Indices:** Evaluates historical importer profile deviations and high-risk transshipment routes[cite: 1, 1].

A calculated **Risk Score (0–100)** determines whether a shipment is classified as normal or flagged as a high-risk anomaly requiring physical port intervention[cite: 1, 1]."""
        },
        {
            "category": "🤖 Machine Learning & OCR Forensics",
            "q": "Why are raw `.joblib` model binaries restricted to Admin access?",
            "a": """Model binary files (`.joblib`) are restricted strictly to **Admin** view to preserve operational security[cite: 1, 1]:
* **Adversarial Evasion:** Prevents illegal trade syndicates from reverse-engineering decision boundaries or finding threshold loopholes[cite: 1].
* **Legal Chain of Custody:** Ensures model parameters remain cryptographically signed with SHA-256 checksum hashes before being introduced into judicial enforcement proceedings[cite: 1, 1]."""
        },
        {
            "category": "🤖 Machine Learning & OCR Forensics",
            "q": "How does the Shipping Manifest Document OCR Parser function?",
            "a": """Under the **Live Scanner** tab, officers can upload scanned PDF, PNG, or JPG shipping manifests (e.g., Customs K1 Forms, Bills of Lading, Commercial Invoices)[cite: 1]. 

The OCR engine extracts unstructured textual fields—such as HS Code, declared weight, total value, and exporter origin—and automatically feeds parsed unit values into the `.joblib` pipeline to detect pricing discrepancies[cite: 1, 1]."""
        },

        # CATEGORY 3: HUMAN-IN-THE-LOOP (HITL) & FIELD SOPS
        {
            "category": "👮 Human-in-the-Loop & Field SOPs",
            "q": "What happens when an ML model flags a high-risk anomaly?",
            "a": """Machine learning outputs in SENTINEL serve as non-binding decision-support flags[cite: 1]. High-risk shipments are routed directly to the **Human-in-the-Loop (HITL) Officer Workbench**[cite: 1]:

1. **Physical Port Hold:** Officers issue a temporary container hold at Westports, Northport, or Penang Port[cite: 1, 1].
2. **Officer Adjudication:** Enforcement personnel perform physical spot-checks or chemical sampling[cite: 1, 1].
3. **Binding Decision:** The officer logs a binding decision in the portal[cite: 1]:
   * **Approve & Release:** Overrides false positive flags with written justification[cite: 1].
   * **Detain & Confiscate:** Issues an official **Form K3 Container Detention Order**[cite: 1].
   * **Inter-Agency Escalation:** Re-routes the case file to partner agencies (e.g., JAS, MITI, PERHILITAN) for secondary lab testing[cite: 1, 1]."""
        },
        {
            "category": "👮 Human-in-the-Loop & Field SOPs",
            "q": "How are human officer decisions audited for legal proceedings?",
            "a": """All officer interactions—including false positive overrides, inspection notes, badge IDs, and detention orders—are recorded in the `sentinel_sec.mea_violation_audit_logs` BigQuery table[cite: 1]. 

This creates a legally compliant audit trail meeting ISO/IEC 42001 and SPA Bil 2/2021 standards for judicial prosecution[cite: 1]."""
        },

        # CATEGORY 4: GCP ARCHITECTURE & DATA LAKE
        {
            "category": "☁️ GCP Architecture & BigQuery",
            "q": "What is the underlying cloud architecture powering SENTINEL?",
            "a": """SENTINEL is built on Google Cloud Platform (GCP) hosted within the `asia-southeast1` region[cite: 1]:

* **Data Lake:** Google BigQuery hosting 14.82M+ customs declarations (2020–2026) partitioned daily[cite: 1, 1].
* **Training Layer:** Colab Enterprise / Vertex AI executing scheduled model retraining and SHAP drift monitoring[cite: 1].
* **Analytics Layer:** Google Looker Studio Pro providing embedded real-time dashboards[cite: 1].
* **Delivery Layer:** Streamlit web application secured with OAuth 2.0 and JWT Bearer Tokens[cite: 1]."""
        },
        {
            "category": "☁️ GCP Architecture & BigQuery",
            "q": "How does inter-agency data sharing work via MyGDX?",
            "a": """Partner government agencies can request data streams through the **Inter-Agency Embed Portal**[cite: 1]. Upon administrative approval, SENTINEL generates OAuth 2.0 JWT Bearer tokens, allowing agencies to[cite: 1]:
* Stream real-time BigQuery data feeds via REST API[cite: 1].
* Embed live SENTINEL threat widgets into external portals (e.g., JKDM K1 Customs System, JAS e-AlamSekitar)[cite: 1]."""
        },

        # CATEGORY 5: STATUTORY COMPLIANCE & AI COPILOT
        {
            "category": "📜 Statutory & AI Copilot",
            "q": "Which national statutory acts govern SENTINEL's operations?",
            "a": """SENTINEL operates under the legal authority of Malaysian environmental and trade acts[cite: 1, 1]:
* **Environmental Quality Act 1974 (Act 127):** Section 31A (Detention Orders), Section 34A (Scheduled Plastic Waste), Section 34B (E-Waste Slag)[cite: 1].
* **Customs Act 1967:** Section 114 (Powers of Seizure and Search)[cite: 1].
* **International Trade in Endangered Species Act 2008 (Act 686):** CITES flora and fauna protection[cite: 1].
* **Public Sector AI Governance (SPA Bil 2/2021):** Cloud data security and AI compliance guidelines[cite: 1, 1]."""
        },
        {
            "category": "📜 Statutory & AI Copilot",
            "q": "How does the SENTINEL-01 AI Legal Copilot assist officers?",
            "a": """**SENTINEL-01** is an autonomous compliance copilot featuring dynamic Natural Language Processing (NLP)[cite: 1]. It allows officers to:
* Extract HS codes and valuations directly from conversational input[cite: 1].
* Calculate real-time price deviation risk scores[cite: 1].
* Query statutory provisions in English or Bahasa Melayu[cite: 1].
* Automatically draft official **Form K3 Container Detention Orders** complete with reference numbers and timestamped legal directives[cite: 1]."""
        },

        # CATEGORY 6: TRAINING & ACADEMIC RESEARCH
        {
            "category": "🎓 Training & Academic Research",
            "q": "How can officers obtain SENTINEL certification?",
            "a": """Officers can enroll in structured capacity-building modules (`MOD-101` to `MOD-301`) under the **Training Modules** tab[cite: 1]. Upon completing scenario-based examination questions (achieving an 80%+ passing score), officers receive downloadable digital certificates authenticated by the SENTINEL Governance Registry[cite: 1]."""
        },
        {
            "category": "🎓 Training & Academic Research",
            "q": "Where can academic researchers cite SENTINEL datasets and papers?",
            "a": """Anonymized, open-access time-series trade datasets are downloadable under the **Public Threat Map & Open Data Portal** under a CC BY 4.0 license[cite: 1]. 

Researchers should cite the underlying peer-reviewed arXiv preprints[cite: 1]:
> *Ramli, M. S. B. (2025). Pattern Recognition of Scrap Plastic Misclassification in Global Trade Data. arXiv:2511.08638.*[cite: 1]"""
        }
    ]

def render_faq_page():
    """Renders the comprehensive, interactive Guidance & FAQ page in Streamlit."""
    st.subheader("❓ Guidance & Comprehensive FAQ Hub")
    st.caption("Central knowledge base covering SENTINEL platform operations, machine learning logic, GCP infrastructure, and statutory enforcement SOPs.")
    st.markdown("---")

    # Top System Specifications Metric Bar
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Monitored MEA Treaties", "4 Frameworks", "Basel, Montreal, CITES, POPs")
    m2.metric("ML Forensic Pipelines", "3 Active / 2 Dev", "scikit-learn Isolation Forest")
    m3.metric("BigQuery Data Corpus", "14.82M Records", "2020–2026 Time-Series")
    m4.metric("Governance Standard", "ISO 42001 & SPA 2/2021", "SHA-256 Checksums")
    st.markdown("---")

    # Search & Filter Controls
    col_search, col_cat = st.columns([2, 1])
    
    with col_search:
        search_query = st.text_input(
            "🔍 Search Knowledge Base:", 
            placeholder="e.g. Isolation Forest, Form K3, BigQuery, RBAC, .joblib, Act 127..."
        ).strip().lower()
        
    with col_cat:
        categories = [
            "All Categories",
            "🛡️ Platform Overview & RBAC Access",
            "🤖 Machine Learning & OCR Forensics",
            "👮 Human-in-the-Loop & Field SOPs",
            "☁️ GCP Architecture & BigQuery",
            "📜 Statutory & AI Copilot",
            "🎓 Training & Academic Research"
        ]
        selected_category = st.selectbox("Filter Category:", categories)

    st.markdown("<br>", unsafe_allow_html=True)

    # Load FAQ corpus
    faq_items = get_comprehensive_faq_items()

    # Filter logic
    filtered_faqs = []
    for item in faq_items:
        # Category Filter Match
        category_match = (selected_category == "All Categories") or (item["category"] == selected_category)
        
        # Search Query Match
        search_match = True
        if search_query:
            search_match = (search_query in item["q"].lower()) or (search_query in item["a"].lower()) or (search_query in item["category"].lower())
            
        if category_match and search_match:
            filtered_faqs.append(item)

    # Render Search Results Summary
    if search_query or selected_category != "All Categories":
        st.info(f"Showing **{len(filtered_faqs)}** result(s) matching your criteria.")

    if not filtered_faqs:
        st.warning("No FAQ entries match your search query. Try searching for broader terms like **'ML'**, **'JAS'**, **'BigQuery'**, or **'SOP'**.")
    else:
        # Group entries by Category for cleaner rendering
        current_category = None
        for item in filtered_faqs:
            if item["category"] != current_category and selected_category == "All Categories":
                current_category = item["category"]
                st.markdown(f"### {current_category}")
                
            with st.expander(f"**{item['q']}**"):
                st.markdown(item["a"])
                st.caption(f"Category: `{item['category']}`")

    st.markdown("---")
    
    # Bottom Helpdesk Escalation Card
    st.markdown("""
    <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:4px solid #2563EB; border-radius:8px; padding:18px; box-shadow:0 1px 3px rgba(0,0,0,0.03);">
        <div style="font-size:0.95rem; font-weight:800; color:#1A365D; margin-bottom:4px;">Need additional operational support or custom API integration?</div>
        <div style="font-size:0.85rem; color:#475569;">
            Inter-agency officers can submit dataset requests via the <b>Embed Portal</b> or route live incident queries to the <b>AI Legal Copilot</b>. For technical helpdesk escalations, visit the <b>Incident Escalation</b> workbench.
        </div>
    </div>
    """, unsafe_allow_html=True)
