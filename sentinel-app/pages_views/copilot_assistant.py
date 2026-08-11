import streamlit as st

def render_copilot_assistant_page():
    st.subheader("🤖 SENTINEL Regulatory & Legal Copilot")
    user_input = st.chat_input("Ask about Act 127 or Customs Import Orders...")
    if user_input:
        st.chat_message("user").write(user_input)
        st.chat_message("assistant").write("Based on Act 127: Detention Order under Section 31A applies.")