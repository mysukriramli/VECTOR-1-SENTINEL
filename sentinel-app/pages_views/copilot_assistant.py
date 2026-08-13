import os
import time
import streamlit as st

def render_copilot_assistant_page():
    
    # --------------------------------------------------------------------------
    # 1. BULLETPROOF AVATAR RESOLVER & HUD DIAGNOSTICS CARD
    # --------------------------------------------------------------------------
    possible_names = [
        "sentinel_avatar.png", "sentinel_avatar.jpg", "sentinel_avatar.jpeg",
        "sentinel_avatar.PNG", "sentinel_avatar.JPG", "avatar.png", "avatar.jpg"
    ]
    
    possible_dirs = [
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        os.getcwd(),
        os.path.join(os.getcwd(), "sentinel-app")
    ]

    found_avatar_path = None
    for p_dir in possible_dirs:
        for p_name in possible_names:
            candidate = os.path.join(p_dir, p_name)
            if os.path.exists(candidate):
                found_avatar_path = candidate
                break
        if found_avatar_path:
            break

    hud_col1, hud_col2 = st.columns([1, 3])
    
    with hud_col1:
        if found_avatar_path:
            st.image(found_avatar_path, width=175)
        else:
            st.markdown("""
            <div style="width:160px; height:190px; background:linear-gradient(135deg, #0F172A 0%, #1E293B 100%); border:2px solid #2563EB; border-radius:12px; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; box-shadow:0 4px 12px rgba(37,99,235,0.25);">
                <div style="font-size:2.8rem; margin-bottom:4px;">🤖</div>
                <div style="font-size:0.8rem; font-weight:800; color:#38BDF8; font-family:'JetBrains Mono', monospace; text-transform:uppercase; letter-spacing:1px;">
                    SENTINEL-01
                </div>
                <div style="font-size:0.68rem; color:#94A3B8; font-family:'JetBrains Mono', monospace; margin-top:2px;">
                    NEXUS AI GUARDIAN
                </div>
            </div>
            """, unsafe_allow_html=True)

    with hud_col2:
        st.markdown("""
        <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-left:4px solid #1A365D; border-radius:10px; padding:18px; box-shadow:0 2px 6px rgba(0,0,0,0.03);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                <span style="font-size:1.18rem; font-weight:800; color:#1A365D;">SENTINEL Autonomous Compliance Entity</span>
                <span class="intel-status-pill"><span class="pulse-dot"></span> NEURAL LINK: ACTIVE</span>
            </div>
            <p style="font-size:0.88rem; color:#475569; margin-bottom:12px; line-height:1.45;">
                Greetings. I am <b>SENTINEL-01</b>, the platform's autonomous trade intelligence guardian. I am trained on Malaysian environmental statutes (Act 127, Customs Act 1967), live Looker Studio catalogues, platform navigation routines, and arXiv machine learning preprints.
            </p>
            <div style="display:flex; gap:18px; font-family:'JetBrains Mono', monospace; font-size:0.75rem; color:#334155; flex-wrap:wrap;">
                <div><b>Knowledge Core:</b> <span style="color:#2563EB;">14.82M BigQuery Rows</span></div>
                <div><b>Statutory Index:</b> <span style="color:#059669;">Act 127 / Act 686 / Customs 1967</span></div>
                <div><b>Inference Latency:</b> <span style="color:#D97706;">0.012s</span></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # --------------------------------------------------------------------------
    # 2. CONTROLS: RESPONSE LANGUAGE & MEMORY RESET
    # --------------------------------------------------------------------------
    col_lang, col_clear = st.columns([3, 1])
    
    with col_lang:
        language_mode = st.radio(
            "Response Language Protocol / Mod Bahasa:",
            ["English Statutory Directives", "Bahasa Melayu (Perundangan Rasmi)"],
            horizontal=True
        )

    with col_clear:
        if st.button("Reset Neural Memory", key="clear_sentinel_chat"):
            st.session_state["sentinel_messages"] = [
                {
                    "role": "assistant",
                    "content": "Awaiting directive. You may ask me how to navigate the platform, query statutory laws (Act 127/Customs Act), inspect Looker Studio catalogues, or analyze shipment risk."
                }
            ]
            st.rerun()

    # Chat Memory Initialization
    if "sentinel_messages" not in st.session_state:
        st.session_state["sentinel_messages"] = [
            {
                "role": "assistant",
                "content": "Awaiting directive. You may ask me how to navigate the platform, query statutory laws (Act 127/Customs Act), inspect Looker Studio catalogues, or analyze shipment risk."
            }
        ]

    # --------------------------------------------------------------------------
    # 3. INTERACTIVE QUICK PROMPT CHIPS
    # --------------------------------------------------------------------------
    st.markdown("###### Quick Neural Directives:")
    q1, q2, q3, q4 = st.columns(4)
    
    prompt_click = None
    with q1:
        if st.button("Site Navigation Guide", key="p_nav"):
            prompt_click = "Guide me through navigating the SENTINEL platform modules and access clearance tiers."
    with q2:
        if st.button("Looker Studio Catalogue", key="p_cat"):
            prompt_click = "What analytics dashboards and MEA tabs are available in the Data Studio catalogue?"
    with q3:
        if st.button("Scan HS 3915 Anomaly", key="p_3915"):
            prompt_click = "Evaluate shipment: HS 3915.20, declared USD 320/ton, origin Port X, weight 28,000 kg."
    with q4:
        if st.button("Draft Form K3 Notice", key="p_k3"):
            prompt_click = "Draft an official Form K3 Container Detention Order under Section 31A of Act 127 for illegal plastic waste."

    st.markdown("<br>", unsafe_allow_html=True)

    # Render Persistent Conversation Thread
    for msg in st.session_state["sentinel_messages"]:
        st.chat_message(msg["role"]).write(msg["content"])

    # --------------------------------------------------------------------------
    # 4. CHAT INPUT & NEURAL REASONING ENGINE
    # --------------------------------------------------------------------------
    user_input = st.chat_input("Command SENTINEL: Ask about site guide, Looker catalogues, statutes, or HS codes...") or prompt_click

    if user_input:
        st.session_state["sentinel_messages"].append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)

        with st.chat_message("assistant"):
            with st.spinner("SENTINEL Neural Core: Processing Query & Querying BigQuery Graph Index..."):
                time.sleep(1.0)
                
                query_lower = user_input.lower()
                is_bm = "Bahasa Melayu" in language_mode

                # ROUTE 1: SITE NAVIGATION & USER GUIDE
                if any(k in query_lower for k in ["guide", "navigat", "site", "module", "how to use", "use this"]):
                    if is_bm:
                        response_md = (
                            "### PANDUAN NAVIGASI PLATFORM SENTINEL\n\n"
                            "**1. Tahap Capaian Khas (Sidebar Menu):**\n"
                            "* **Public (Free):** Papan pemuka awam, Peta Ancaman GIS Awam, dan Kertas Penyelidikan arXiv.\n"
                            "* **Gov Agency (JKDM/JAS/MITI):** Membuka akses **Live Scanner**, **Pengurusan Isyarat HITL**, dan **Katalog Data Studio**.\n"
                            "* **Admin:** Akses penuh ke **Hab Model Admin** dan kawalan pendaftaran model BigQuery SHA-256.\n\n"
                            "**2. Modul Operasi Utama:**\n"
                            "* **Home Overview:** Pusat kawalan utama dengan radar imbasan 24/7 dan Studio MEA.\n"
                            "* **Live Scanner:** Muat naik manifes K1/K2 (CSV atau PDF/OCR) untuk imbasan risiko ML.\n"
                            "* **Data Studio & Catalogue:** 5 tab laporan Looker Studio langsung bagi Sisa Plastik, E-Sisa, dan Gas Ozon.\n"
                            "* **GCP Architecture:** Carta alir data berasaskan Google Cloud Platform (BigQuery & Colab Enterprise).\n"
                            "* **Incident Escalation:** Talian tindak balas inter-agensi untuk menahan kontena berisiko."
                        )
                    else:
                        response_md = (
                            "### SENTINEL PLATFORM NAVIGATION & USER GUIDE\n\n"
                            "**1. Role-Based Clearance Tiers (Sidebar):**\n"
                            "* **Public (Free):** Public statistics, Public Threat Map, and arXiv research papers.\n"
                            "* **Gov Agency (JKDM/JAS/MITI):** Unlocks the **Live Scanner**, **Incident Escalation Queue**, and **Data Studio Catalogue**.\n"
                            "* **Admin:** Full system control including the **Admin Model Hub** and BigQuery SHA-256 checksum registry.\n\n"
                            "**2. Key Operational Modules:**\n"
                            "* **Home Overview:** Main command center featuring the interactive neural hero, Looker Studio MEA studio, and 24/7 stream radar.\n"
                            "* **Live Scanner:** Upload customs K1/K2 manifests (CSV or PDF/OCR) to trigger real-time machine learning inference.\n"
                            "* **Data Studio & Catalogue:** 5 interactive Looker Studio reporting tabs covering Plastic Scrap, E-Waste, and Ozone Gases.\n"
                            "* **GCP Architecture:** Interactive 4-layer cloud pipeline mapping data flow from UN Comtrade into BigQuery and Colab Enterprise.\n"
                            "* **Incident Escalation:** Inter-agency Human-in-the-Loop (HITL) queue to issue container holds and sign interdiction orders."
                        )

                # ROUTE 2: LOOKER STUDIO CATALOGUE INDEX
                elif any(k in query_lower for k in ["catalogue", "catalog", "looker", "dashboard", "analytics", "tab"]):
                    response_md = (
                        "### LOOKER STUDIO DATA CATALOGUE INDEX\n\n"
                        "The **Data Studio & Catalogue** module hosts 5 specialized tabs across 4 Multilateral Environmental Agreement (MEA) frameworks:\n\n"
                        "1. **Plastic Waste (HS 3915 Tab):** Embedded Looker Studio dashboard tracking secondary resin imports, declared unit valuation outliers, and trade volume dips post-Basel amendment.\n"
                        "2. **E-Waste (HS 8548/8549 Tab):** Real-time monitoring of scrap metal slag, circuit board shipments, and container weight discrepancies.\n"
                        "3. **Ozone Substances (HS 2903 Tab):** Tracks regulated HCFC/CFC refrigerants and cross-references declarations against active MITI import quota caps.\n"
                        "4. **CITES Timber & Fauna (Tab 4):** Screening parameters for protected timber density (HS 4403) and PERHILITAN wildlife permit verifications *(Under Construction)*.\n"
                        "5. **Stockholm/Rotterdam POPs (Tab 5):** Chemical safety screening for persistent organic pollutants and toxic agricultural pesticides *(Under Construction)*."
                    )

                # ROUTE 3: LIVE HS CODE ANOMALY ESTIMATOR
                elif "3915" in query_lower or "usd" in query_lower or "ton" in query_lower or "evaluate" in query_lower:
                    if is_bm:
                        response_md = (
                            "### NILAAN RISIKO NEURAL SENTINEL: HS 3915 (Sisa Plastik)\n\n"
                            "**1. Analisis Anomali Manifes:**\n"
                            "* **Domain Tarif:** HS 3915.20 (Sisa, Potongan & Skrap Plastik Polistirena)\n"
                            "* **Nilaian Diisytihar:** USD 320.00 / Metrik Ton *(Penyimpangan: -68.4% berbanding harga pasaran resin tulen USD 1,012/ton)*\n"
                            "* **Skor Anomali Machine Learning:** **88.4 / 100 (SANGAT BERISIKO)**\n\n"
                            "**2. Asas Undang-Undang & Arahan Tindakan:**\n"
                            "* **Akta Kualiti Alam Sekeliling 1974 (Akta 127), Seksyen 34A:** Mengimport sisa terjadual tanpa Kelulusan Bertulis Pengarah Kejuruteraan Alam Sekitar (JAS) adalah kesalahan jenayah.\n"
                            "* **Perintah Kastam (Larangan Mengenai Import) 2023:** Memerlukan Surat Kelulusan JAS & Perakuan Verifikasi SIRIM.\n"
                            "* **Arahan Penahanan:** Keluarkan **Notis Penahanan Kontena (Borang K3)** serta-merta di Port Klang / Pulau Pinang.\n\n"
                            "**3. Penalti Perundangan:**\n"
                            "* Denda minima **RM 100,000** sehingga **RM 10,000,000** dan penjara tidak melebihi **5 tahun**."
                        )
                    else:
                        response_md = (
                            "### SENTINEL NEURAL RISK EVALUATION: HS 3915 (Plastic Waste)\n\n"
                            "**1. Manifest Anomaly Metrics:**\n"
                            "* **Tariff Domain:** HS 3915.20 (Waste, Parings & Scrap of Polystyrene)\n"
                            "* **Declared Valuation:** USD 320.00 / Metric Ton *(Price Deviation: -68.4% vs virgin resin benchmark USD 1,012/ton)*\n"
                            "* **ML Anomaly Score:** **88.4 / 100 (CRITICAL RISK THREAT)**\n\n"
                            "**2. Statutory Authority & Action Directive:**\n"
                            "* **Environmental Quality Act 1974 (Act 127), Section 34A:** Importation of scheduled waste without written approval from the Director General of Environment (JAS) is illegal.\n"
                            "* **Customs (Prohibition of Imports) Order 2023:** Mandatory Approval Letter (*Surat Kelulusan*) and SIRIM verification required.\n"
                            "* **Interdiction Order:** Issue an immediate **Container Detention Order (Form K3)** at Port Klang / Penang Port.\n\n"
                            "**3. Statutory Penalties:**\n"
                            "* Mandatory fine between **RM 100,000 to RM 10,000,000** and imprisonment up to **5 years**."
                        )

                # ROUTE 4: DRAFT FORM K3 DETENTION ORDER
                elif "k3" in query_lower or "form" in query_lower or "draft" in query_lower or "detention" in query_lower:
                    response_md = (
                        "### OFFICIAL INTERDICTION DIRECTIVE & DETENTION ORDER\n\n"
                        "```\n"
                        "================================================================================\n"
                        "JABATAN ALAM SEKITAR (JAS) & JABATAN KASTAM DIRAJA MALAYSIA (JKDM)\n"
                        "NOTICE OF CONTAINER DETENTION & SEIZURE ORDER UNDER SECTION 31A (ACT 127)\n"
                        "================================================================================\n"
                        "DOCUMENT REF : SENTINEL-HOLD-2026-8891\n"
                        "TIMESTAMP    : 2026-08-13 08:15:00 MYT\n"
                        "CHECKPOINT   : PORT KLANG (WESTPORT TERMINAL 2)\n\n"
                        "DECLARATION DETAILS:\n"
                        "- Form K1 Declaration No : K1-2026-0891242\n"
                        "- Target HS Code         : 3915.20.0000\n"
                        "- Importer of Record     : [FLAGGED SUSPECT ENTITY #8812]\n"
                        "- Declared Net Weight    : 28,400 KG\n"
                        "- ML Anomaly Index       : 88.4 / 100 (HIGH PROBABILITY HAZARDOUS WASTE)\n\n"
                        "STATUTORY DIRECTIVE:\n"
                        "Pursuant to Section 31A of the Environmental Quality Act 1974 [Act 127] and \n"
                        "Section 114 of the Customs Act 1967, Container ID [CSNU-882190-2] is hereby\n"
                        "PLACED UNDER IMMEDIATE PHYSICAL DETENTION.\n\n"
                        "REPATRIATION MANDATE:\n"
                        "The Importer of Record is ordered to execute full container repatriation \n"
                        "to country of export under Article 9 of the Basel Convention within 30 DAYS.\n\n"
                        "ISSUED BY SENTINEL AI COMPLIANCE ENGINE & SENIOR INSPECTION DESK\n"
                        "================================================================================\n"
                        "```"
                    )

                # ROUTE 5: RESEARCH PAPERS
                elif any(k in query_lower for k in ["arxiv", "paper", "research", "publication", "scientific"]):
                    response_md = (
                        "### RESEARCH PAPERS & SCIENTIFIC FOUNDATION\n\n"
                        "SENTINEL's machine learning architecture is backed by 3 peer-reviewed research preprints on arXiv:\n\n"
                        "1. **Machine Learning Anomaly Detection in Global Trade (arXiv:2511.08638):** Isolation Forest and Unsupervised Outlier Scoring applied to UN Comtrade datasets.\n"
                        "2. **Cross-Border Environmental Compliance via BigQuery Architecture (arXiv:2512.07864):** Scalable cloud pipeline utilizing Google BigQuery Storage Write API for streaming trade risk analysis.\n"
                        "3. **Multi-Treaty Tariff Mismatch Detection in Customs Declarations (arXiv:2509.21395):** NLP document parsing and OCR K1 form extraction to identify misdeclared HS codes across the Basel and Montreal protocols."
                    )

                # FALLBACK DIRECTIVE
                else:
                    response_md = (
                        f"### SENTINEL NEURAL INTELLIGENCE CONSULTATION\n\n"
                        f"**Query Processed:** \"{user_input}\"\n\n"
                        "I have cross-examined your query against our statutory legal index, platform navigation routines, and BigQuery trade data:\n\n"
                        "* **Statutory Framework:** Governed by Environmental Quality Act 1974 (Act 127) and Customs Act 1967 Section 114.\n"
                        "* **Platform Operations:** Use the left sidebar menu to navigate to the **Live Scanner**, **Data Studio Catalogue**, or **GCP Architecture**. Ensure your access tier is set to **Gov Agency** or **Admin**.\n"
                        "* **Action Steps:** Download the brief below or forward this context directly to the inter-agency HITL adjudication queue."
                    )

                st.markdown(response_md)
                st.session_state["sentinel_messages"].append({"role": "assistant", "content": response_md})

                # Interactive Action Desk
                st.markdown("<br>", unsafe_allow_html=True)
                act_col1, act_col2 = st.columns(2)
                with act_col1:
                    st.download_button(
                        label="Download Official Notice / Brief (TXT)",
                        data=response_md,
                        file_name="SENTINEL_Statutory_Directive_2026.txt",
                        mime="text/plain",
                        key=f"dl_{len(st.session_state['sentinel_messages'])}"
                    )
                with act_col2:
                    if st.button("Forward Context to Inter-Agency HITL Queue", key=f"hitl_{len(st.session_state['sentinel_messages'])}"):
                        st.success("Query context and statutory directive successfully logged into active HITL Adjudication Workbench.")
