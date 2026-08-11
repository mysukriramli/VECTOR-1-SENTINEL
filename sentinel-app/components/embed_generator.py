def generate_iframe_snippet(space_url="https://sentinel-trade-intelligence.streamlit.app", theme="light", width=500, height=220):
    return f"""<!-- SENTINEL Inter-Agency Widget Embed -->
<iframe 
    src="{space_url}/?embed=true&theme={theme.lower()}" 
    width="{width}" 
    height="{height}" 
    frameborder="0" 
    scrolling="no">
</iframe>"""