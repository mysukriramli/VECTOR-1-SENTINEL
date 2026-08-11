import streamlit as st

def render_about_page():
    st.subheader("ℹ️ About SENTINEL & Multilateral Environmental Agreements (MEAs)")
    st.write("SENTINEL empowers Malaysian enforcement agencies with real-time ML trade intelligence.")

    t1, t2, t3, t4 = st.tabs(["♻️ Basel Convention", "❄️ Montreal Protocol", "🌿 CITES Framework", "🧪 Stockholm & Rotterdam"])
    with t1:
        st.info("Focus: Plastic Scrap (HS 3915) & E-Waste (HS 8548/8549)")
    with t2:
        st.info("Focus: ODS Gases & Refrigerants (HS 2903)")
    with t3:
        st.warning("Focus: Protected Fauna & Timber (Under Construction)")
    with t4:
        st.warning("Focus: POPs & Chemicals (Under Construction)")