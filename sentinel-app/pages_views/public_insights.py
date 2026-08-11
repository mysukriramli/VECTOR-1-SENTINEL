import streamlit as st
import pydeck as pdk
import plotly.express as px
from mock_data import get_trade_statistics_df, get_malaysia_port_locations, get_open_data_news

def render_public_insights_page():
    st.subheader("🗺️ Public Open Trade Insights & Interactive Threat Map")
    
    ports_df = get_malaysia_port_locations()
    layer = pdk.Layer(
        "ScatterplotLayer",
        ports_df,
        get_position=["lon", "lat"],
        get_color="[200, 30, 0, 160]",
        get_radius="anomalies * 500",
        pickable=True
    )
    view_state = pdk.ViewState(latitude=4.2105, longitude=101.9758, zoom=5)
    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

    df_trade = get_trade_statistics_df()
    fig = px.bar(df_trade, x="Year", y="Volume (Tonnes)", color="MEA Category", barmode="group")
    st.plotly_chart(fig, use_container_width=True)