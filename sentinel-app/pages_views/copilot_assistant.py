import streamlit as st
import time

def render_copilot_assistant_page():
    st.subheader("SENTINEL Statutory & Legal Copilot")
    st.caption("AI-powered legal query assistant trained on Malaysian statutory frameworks, customs import orders, and multilateral environmental treaties (MEAs).")

    # --------------------------------------------------------------------------
    # 1. KNOWLEDGE DOMAIN SELECTOR & STATUTORY CONTROLS
    # --------------------------------------------------------------------------
    col_domain, col_clear = st.columns([3, 1])
    
    with col_domain:
        selected_framework = st.multiselect(
            "Constrain Legal Retrieval Domains:",
            [
                "Act 127: Environmental Quality Act 1974",
                "Customs Act 1967 & Prohibition Orders",
                "Act 686: International Trade in Endangered Species 2008",
                "Basel Convention Protocols (Waste HS 3915/8549)",
                "Montreal Protocol (ODS HS 2903)"
            ],
            default=[
                "Act 127: Environmental Quality Act 1974",
                "Customs Act 1967 & Prohibition Orders"
            ]
        )
        
    with col_clear:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Clear Chat Memory", key="clear_copilot_chat"):
            st.session_state["copilot_messages"] = [
                {
                    "role": "assistant",
                    "content": "Greetings Officer. I am initialized with Act 127, Customs Act 1967, and international MEA statutes. Submit a tariff query, HS code, or statutory penalty question below."
                }
            ]
            st.rerun()

    st.markdown("---")

    # --------------------------------------------------------------------------
    # 2. CHAT MEMORY INITIALIZATION
    # --------------------------------------------------------------------------
    if "copilot_messages" not in st.session_state:
        st.session_state["copilot_messages"] = [
            {
                "role": "assistant",
                "content": "Greetings Officer. I am initialized with Act 127, Customs Act 1967, and international MEA statutes. Submit a tariff query, HS code, or statutory penalty question below."
            }
        ]

    # --------------------------------------------------------------------------
    # 3. SUGGESTED QUICK PROMPT CHIPS
    # --------------------------------------------------------------------------
    st.markdown("###### Quick Compliance Prompts:")
    q_col1, q_col2, q_col3 = st.columns(3)
    
    prompt_click = None
    with q_col1:
        if st.button("HS 3915 Plastic Detention SOP", key="prompt_1"):
            prompt_click = "What is the legal procedure and penalty for detaining unpermitted HS 3915 plastic scrap under Act 127?"
    with q_col2:
        if st.button("HS 2903 ODS Refrigerant Quota", key="prompt_2"):
            prompt_click = "Explain the MITI import quota requirements for HCFC-22 gases under HS 2903."
    with q_col3:
        if st.button("HITL Judicial Evidence Protocol", key="prompt_3"):
            prompt_click = "What are the legal chain-of-custody requirements when logging officer overrides in the HITL queue?"

    st.markdown("<br>", unsafe_allow_html=True)

    # Render persistent conversation history
    for msg in st.session_state["copilot_messages"]:
        st.chat_message(msg["role"]).write(msg["content"])

    # --------------------------------------------------------------------------
    # 4. CHAT INPUT & INTENT ROUTING ENGINE
    # --------------------------------------------------------------------------
    user_input = st.chat_input("Query statutory provisions, HS code penalties, or border interdiction SOPs...") or prompt_click

    if user_input:
        # Display User Input
        st.session_state["copilot_messages"].append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)

        # Process Query & Generate Structured Response
        with st.chat_message("assistant"):
            with st.spinner("Searching BigQuery Legal Knowledge Graph & Gazette Index..."):
                time.sleep(1.2)  # Simulated vector retrieval latency
                
                query_lower = user_input.lower()

                # Dynamic Scenario 1: Plastic Scrap / Basel / HS 3915
                if "3915" in query_lower or "plastic" in query_lower or "basel" in query_lower:
                    response_md = """
### Statutory Citation Analysis: HS 3915 (Plastic Scrap)

**1. Primary Legal Framework:**
* **Environmental Quality Act 1974 (Act 127), Section 34A:** Strict prohibition on importing scheduled plastic waste without prior written approval from the Director General of Environment (JAS).
* **Customs (Prohibition of Imports) Order 2023:** Item 1, Second Schedule requires a mandatory Approval Letter (*Surat Kelulusan*) and SIRIM verification prior to port arrival.

**2. Enforcement Powers & Interdiction Protocol:**
* **Detention Order (Form K3/JAS):** Under Section 31A, officers may issue an immediate container hold order at Port Klang, Penang Port, or Pasir Gudang.
* **Mandatory Repatriation:** Non-compliant shipments must be returned to the country of origin at the importer's expense within **30 days** under Article 9 of the Basel Convention.

**3. Statutory Penalties:**
* **Fine:** Minimum **RM 100,000** up to **RM 10,000,000** under Section 34A.
* **Imprisonment:** Mandatory maximum term not exceeding **5 years**, or both.
                    """

                # Dynamic Scenario 2: ODS Gases / Montreal / HS 2903
                elif "2903" in query_lower or "refrigerant" in query_lower or "montreal" in query_lower or "ods" in query_lower:
                    response_md = """
### Statutory Citation Analysis: HS 2903 (Ozone-Depleting Substances)

**1. Primary Legal Framework:**
* **Environmental Quality (Refrigerant Management) Regulations 1999:** Mandates MITI import quota allocation and Department of Environment clearance for HCFCs and HFC blends.
* **Customs Act 1967, Section 133:** False declaration of chemical identifiers on Customs Form K1 constitutes a criminal offense.

**2. Physical Inspection Directive:**
* Verify container pressure ratings using field gas analyzers.
* Cross-reference the declaration payload with MITI's electronic licensing portal via **MyGDX API**.

**3. Statutory Penalties:**
* **Fine:** Up to **RM 500,000** under Section 45 of Act 127.
* **Seizure:** Immediate confiscation of cylinders and forfeiture of shipping line bonds under Section 115 of the Customs Act 1967.
                    """

                # Dynamic Scenario 3: Chain of Custody / HITL / Legal Logs
                elif "hitl" in query_lower or "custody" in query_lower or "evidence" in query_lower or "override" in query_lower:
                    response_md = """
### Statutory Compliance: Digital Chain-of-Custody & HITL Overrides

**1. Judicial Standards:**
* **Evidence Act 1950, Section 90A:** Automated machine learning flags and officer overrides are admissible in court provided digital audit logs maintain cryptographic integrity.

**2. Mandated Logging Workflow:**
* **Digital Signature:** Officers overriding a high-risk ML flag ($Score > 85.0$) must sign with their official government Staff ID.
* **SHA-256 Hashing:** Every adjudication note is appended to the BigQuery immutable ledger with an automated SHA-256 hash stamp.
                    """

                # Fallback Generic Statutory Router
                else:
                    response_md = f"""
### Statutory Consultation Summary

**Query Context:** "{user_input}"
**Applied Frameworks:** {', '.join(selected_framework) if selected_framework else 'National Baseline Statutes'}

* **Statutory Authority:** Customs Act 1967 Section 114 (Power to Inspect and Detain) & Act 127 Section 31.
* **Enforcement Directive:** If ML anomaly threshold exceeds **75.0 / 100**, execute physical sampling and log the container ID into the inter-agency escalation queue.
* **Legal Reference:** Consult the official Jabatan Digital Negara (JDN) guidelines or escalate to senior agency counsel.
                    """

                st.markdown(response_md)

                # Store response in session memory
                st.session_state["copilot_messages"].append({"role": "assistant", "content": response_md})

                # Interactive Action Desk
                st.markdown("<br>", unsafe_allow_html=True)
                act_col1, act_col2 = st.columns(2)
                with act_col1:
                    st.button("Export Statutory Legal Brief (PDF)", key=f"export_{len(st.session_state['copilot_messages'])}")
                with act_col2:
                    if st.button("Escalate Query to Inter-Agency HITL Queue", key=f"hitl_{len(st.session_state['copilot_messages'])}"):
                        st.success("Query & statutory analysis appended to active HITL Adjudication Log.")
