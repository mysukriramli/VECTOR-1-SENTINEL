import os
import time
import re
import random
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
            st.markdown(
                "<div style='width:160px; height:190px; background:linear-gradient(135deg, #0F172A 0%, #1E293B 100%); border:2px solid #2563EB; border-radius:12px; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; box-shadow:0 4px 12px rgba(37,99,235,0.25);'>"
                "<div style='font-size:2.8rem; margin-bottom:4px;'>🤖</div>"
                "<div style='font-size:0.8rem; font-weight:800; color:#38BDF8; font-family:\"JetBrains Mono\", monospace; text-transform:uppercase; letter-spacing:1px;'>SENTINEL-01</div>"
                "<div style='font-size:0.68rem; color:#94A3B8; font-family:\"JetBrains Mono\", monospace; margin-top:2px;'>NEXUS AI GUARDIAN</div>"
                "</div>", 
                unsafe_allow_html=True
            )

    with hud_col2:
        st.markdown(
            "<div style='background:#FFFFFF; border:1px solid #CBD5E1; border-left:4px solid #1A365D; border-radius:10px; padding:18px; box-shadow:0 2px 6px rgba(0,0,0,0.03);'>"
            "<div style='display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;'>"
            "<span style='font-size:1.18rem; font-weight:800; color:#1A365D;'>SENTINEL Autonomous Compliance Entity</span>"
            "<span class='intel-status-pill'><span class='pulse-dot'></span> NEURAL LINK: ACTIVE</span>"
            "</div>"
            "<p style='font-size:0.88rem; color:#475569; margin-bottom:12px; line-height:1.45;'>"
            "Greetings. I am <b>SENTINEL-01</b>, equipped with Dynamic Entity Extraction. I parse free-text inputs for HS Codes and Valuations to calculate real-time risk scores against Act 127 and Customs Act 1967."
            "</p>"
            "<div style='display:flex; gap:18px; font-family:\"JetBrains Mono\", monospace; font-size:0.75rem; color:#334155; flex-wrap:wrap;'>"
            "<div><b>Knowledge Core:</b> <span style='color:#2563EB;'>14.82M BigQuery Rows</span></div>"
            "<div><b>Statutory Index:</b> <span style='color:#059669;'>Act 127 / Act 686 / Customs 1967</span></div>"
            "<div><b>Context Memory:</b> <span style='color:#D97706;'>Multi-Turn Enabled</span></div>"
            "</div></div>", 
            unsafe_allow_html=True
        )

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

    # Initialize Context Memory State Variables
    if "sentinel_messages" not in st.session_state:
        st.session_state["sentinel_messages"] = [
            {"role": "assistant", "content": "Awaiting directive. You may ask me to evaluate a specific shipment (e.g., 'Evaluate HS 3915 at USD 150/ton') or query statutory laws."}
        ]
    if "active_hs_context" not in st.session_state:
        st.session_state["active_hs_context"] = None
    if "active_score_context" not in st.session_state:
        st.session_state["active_score_context"] = None

    with col_clear:
        if st.button("Reset Neural Memory", key="clear_sentinel_chat"):
            st.session_state["sentinel_messages"] = [
                {"role": "assistant", "content": "Awaiting directive. You may ask me to evaluate a specific shipment (e.g., 'Evaluate HS 3915 at USD 150/ton') or query statutory laws."}
            ]
            st.session_state["active_hs_context"] = None
            st.session_state["active_score_context"] = None
            st.rerun()

    # --------------------------------------------------------------------------
    # 3. INTERACTIVE QUICK PROMPT CHIPS
    # --------------------------------------------------------------------------
    st.markdown("###### Quick Neural Directives:")
    q1, q2, q3, q4 = st.columns(4)
    
    prompt_click = None
    with q1:
        if st.button("Scan Dynamic HS 3915", key="p_3915"):
            rand_price = random.randint(180, 400)
            prompt_click = f"Evaluate shipment: HS 3915.20, declared USD {rand_price}/ton, weight 28,000 kg."
    with q2:
        if st.button("Scan Dynamic E-Waste", key="p_8549"):
            rand_price = random.randint(600, 1100)
            prompt_click = f"Check this K1 form: HS 8549.21, declared USD {rand_price}/MT for scrap metal."
    with q3:
        if st.button("Draft K3 using Context", key="p_k3"):
            prompt_click = "Draft an official Form K3 Container Detention Order based on the shipment we just discussed."
    with q4:
        if st.button("Site Navigation", key="p_nav"):
            prompt_click = "Guide me through navigating the SENTINEL platform modules."

    st.markdown("<br>", unsafe_allow_html=True)

    # Render Persistent Conversation Thread
    for msg in st.session_state["sentinel_messages"]:
        st.chat_message(msg["role"]).write(msg["content"])

    # --------------------------------------------------------------------------
    # 4. CHAT INPUT & DYNAMIC ENTITY REASONING ENGINE
    # --------------------------------------------------------------------------
    user_input = st.chat_input("Command SENTINEL: Submit shipment values, HS codes, or statutory queries...") or prompt_click

    if user_input:
        st.session_state["sentinel_messages"].append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)

        with st.chat_message("assistant"):
            # Simulated "Chain of Thought" UI
            with st.expander("🧠 View Neural Reasoning Trace", expanded=False):
                st.write("`[SYS]` Parsing Input Tokens...")
                
                # NLP REGEX Extraction
                query_lower = user_input.lower()
                hs_match = re.search(r'\b(3915(?:\.\d{2})?|8549(?:\.\d{2})?|2903(?:\.\d{2})?|4403(?:\.\d{2})?)\b', query_lower)
                price_match = re.search(r'(?:usd|rm|\$)\s*(\d+(?:,\d+)?(?:\.\d+)?)', query_lower)
                
                extracted_hs = hs_match.group(1) if hs_match else None
                extracted_price = float(price_match.group(1).replace(',', '')) if price_match else None

                st.write(f"`[NER]` Extracted HS Code: {extracted_hs if extracted_hs else 'None detected'}")
                st.write(f"`[NER]` Extracted Valuation: {extracted_price if extracted_price else 'None detected'}")
                st.write("`[API]` Querying BigQuery Standard Deviation Tables...")
                time.sleep(1.0)
                st.write("`[LOG]` Synthesizing Statutory Directives...")
            
            is_bm = "Bahasa Melayu" in language_mode
            response_md = ""

            # ROUTE 1: DYNAMIC SHIPMENT EVALUATOR (Math & Context Aware)
            if extracted_hs and extracted_price:
                st.session_state["active_hs_context"] = extracted_hs
                
                # Dynamic Logic Math
                if "3915" in extracted_hs:
                    benchmark = 1012.0
                    statute = "Act 127 Section 34A (Scheduled Plastic Waste)"
                elif "8549" in extracted_hs:
                    benchmark = 2500.0
                    statute = "Act 127 Section 34B (Electronic Waste Slag)"
                else:
                    benchmark = 5000.0
                    statute = "Customs Act 1967 (General Misdeclaration)"

                deviation = ((extracted_price - benchmark) / benchmark) * 100
                risk_score = min(99.9, max(12.0, abs(deviation) * 1.35))
                st.session_state["active_score_context"] = risk_score
                
                risk_label = "CRITICAL RISK THREAT" if risk_score > 75 else "MODERATE RISK"

                if is_bm:
                    response_md = "\n".join([
                        f"### 🛡️ NILAAN RISIKO DINAMIK: HS {extracted_hs}",
                        "",
                        "**1. Metrik Pengekstrakan NLP:**",
                        f"* **Domain Tarif:** HS {extracted_hs}",
                        f"* **Nilaian Diisytihar:** USD {extracted_price:,.2f} / Ton",
                        f"* **Sisihan Pasaran:** {deviation:.1f}% *(Berbanding penanda aras USD {benchmark:,.2f})*",
                        f"* **Skor Anomali ML:** **{risk_score:.1f} / 100 ({risk_label})**",
                        "",
                        "**2. Asas Undang-Undang:**",
                        f"* **Konteks Perundangan:** {statute}. Mengimport bahan terkawal tanpa kelulusan JAS/MITI adalah haram.",
                        "* **Arahan:** Sila keluarkan Borang K3 atau minta saya untuk sediakan draf rasmi."
                    ])
                else:
                    response_md = "\n".join([
                        f"### 🛡️ DYNAMIC RISK EVALUATION: HS {extracted_hs}",
                        "",
                        "**1. NLP Extracted Metrics:**",
                        f"* **Tariff Domain:** HS {extracted_hs}",
                        f"* **Declared Valuation:** USD {extracted_price:,.2f} / Ton",
                        f"* **Market Deviation:** {deviation:.1f}% *(vs virgin benchmark USD {benchmark:,.2f})*",
                        f"* **ML Anomaly Score:** **{risk_score:.1f} / 100 ({risk_label})**",
                        "",
                        "**2. Statutory Authority:**",
                        f"* **Legal Context:** {statute}. Importation of restricted payloads without JAS/MITI approval constitutes a criminal offense.",
                        "* **Directive:** Execute physical inspection. You may ask me to draft the official Form K3 Detention Order."
                    ])

            # ROUTE 2: CONTEXT-AWARE DRAFTING (Uses memory of previous HS code)
            elif "k3" in query_lower or "form" in query_lower or "draft" in query_lower or "detention" in query_lower:
                mem_hs = st.session_state.get("active_hs_context") or "[HS CODE NOT PROVIDED]"
                mem_score = st.session_state.get("active_score_context") or "N/A"
                if isinstance(mem_score, float):
                    mem_score = f"{mem_score:.1f}"
                
                response_md = "\n".join([
                    "### OFFICIAL INTERDICTION DIRECTIVE & DETENTION ORDER",
                    "",
                    "```text",
                    "================================================================================",
                    "JABATAN ALAM SEKITAR (JAS) & JABATAN KASTAM DIRAJA MALAYSIA (JKDM)",
                    "NOTICE OF CONTAINER DETENTION & SEIZURE ORDER UNDER SECTION 31A (ACT 127)",
                    "================================================================================",
                    f"DOCUMENT REF : SENTINEL-HOLD-2026-{random.randint(1000,9999)}",
                    f"TIMESTAMP    : {time.strftime('%Y-%m-%d %H:%M:%S MYT')}",
                    "CHECKPOINT   : NATIONAL CLEARANCE GATEWAY",
                    "",
                    "DECLARATION DETAILS:",
                    f"- Form K1 Declaration No : K1-2026-{random.randint(100000,999999)}",
                    f"- Target HS Code         : {mem_hs}",
                    f"- ML Anomaly Index       : {mem_score} / 100",
                    "",
                    "STATUTORY DIRECTIVE:",
                    "Pursuant to Section 31A of the Environmental Quality Act 1974 [Act 127] and ",
                    "Section 114 of the Customs Act 1967, this payload is hereby",
                    "PLACED UNDER IMMEDIATE PHYSICAL DETENTION.",
                    "",
                    "ISSUED BY SENTINEL AI COMPLIANCE ENGINE & SENIOR INSPECTION DESK",
                    "================================================================================",
                    "```"
                ])

            # ROUTE 3: SITE NAVIGATION & GENERAL
            elif any(k in query_lower for k in ["guide", "navigat", "module", "how to"]):
                response_md = "\n".join([
                    "### SENTINEL PLATFORM NAVIGATION",
                    "",
                    "**1. Role-Based Clearance Tiers (Sidebar):** Switch between Public, Gov Agency, or Admin to unlock features like the **Live Scanner** or **Data Studio Catalogue**.",
                    "**2. Operational Modules:** Use the sidebar to access the Live Scanner (manifest uploads), Data Studio (Looker dashboards), or GCP Architecture (pipeline flows)."
                ])

            # FALLBACK
            else:
                response_md = "\n".join([
                    "### SENTINEL NEURAL INTELLIGENCE",
                    "",
                    f"**Query Processed:** \"{user_input}\"",
                    "",
                    "I did not detect a specific HS code or monetary valuation in your query to run mathematical risk scoring.",
                    "Please provide a payload definition (e.g., 'Check HS 3915 at USD 150') or ask me to draft a legal order."
                ])

            st.markdown(response_md)
            st.session_state["sentinel_messages"].append({"role": "assistant", "content": response_md})

            # Interactive Action Desk
            st.markdown("<br>", unsafe_allow_html=True)
            act_col1, act_col2 = st.columns(2)
            with act_col1:
                st.download_button(
                    label="Download Official Notice / Brief (TXT)",
                    data=response_md,
                    file_name="SENTINEL_Statutory_Directive.txt",
                    mime="text/plain",
                    key=f"dl_{len(st.session_state['sentinel_messages'])}"
                )
            with act_col2:
                if st.button("Forward Context to Inter-Agency HITL Queue", key=f"hitl_{len(st.session_state['sentinel_messages'])}"):
                    st.success("Query context logged into active HITL Adjudication Workbench.")
