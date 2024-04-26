import streamlit as st
import leafmap.foliumap as leafmap

markdown = """
A Streamlit map template
<https://github.com/nearysam/Lab10StreamlitApp>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://www.google.com/imgres?q=utk%20logo%20direct%20url%20links&imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F8%2F87%2FUT_Knoxville_logo_2015.svg%2F819px-UT_Knoxville_logo_2015.svg.png&imgrefurl=https%3A%2F%2Fcommons.wikimedia.org%2Fwiki%2FFile%3AUT_Knoxville_logo_2015.svg&docid=ZJ2cKfJhmFSTgM&tbnid=oyw_z1t1Ft3QSM&vet=12ahUKEwiH8MXC6-CFAxX3gYQIHSK_BxYQM3oECBMQAA..i&w=819&h=768&hcb=2&ved=2ahUKEwiH8MXC6-CFAxX3gYQIHSK_BxYQM3oECBMQAA"
st.sidebar.image(logo)


st.title("Interactive Map")

col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")

with col2:

    basemap = st.selectbox("Select a basemap:", options, index)


with col1:

    m = leafmap.Map(
        locate_control=True, latlon_control=True, draw_export=True, minimap_control=True
    )
    m.add_basemap(basemap)
    m.to_streamlit(height=700)
