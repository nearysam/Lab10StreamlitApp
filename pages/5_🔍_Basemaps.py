import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/nearysam/Lab10StreamlitApp>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://www.google.com/imgres?q=utk%20logo%20direct%20url%20links&imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F8%2F87%2FUT_Knoxville_logo_2015.svg%2F819px-UT_Knoxville_logo_2015.svg.png&imgrefurl=https%3A%2F%2Fcommons.wikimedia.org%2Fwiki%2FFile%3AUT_Knoxville_logo_2015.svg&docid=ZJ2cKfJhmFSTgM&tbnid=oyw_z1t1Ft3QSM&vet=12ahUKEwiH8MXC6-CFAxX3gYQIHSK_BxYQM3oECBMQAA..i&w=819&h=768&hcb=2&ved=2ahUKEwiH8MXC6-CFAxX3gYQIHSK_BxYQM3oECBMQAA"
st.sidebar.image(logo)


st.title("Searching Basemaps")
st.markdown(
    """
This app is a demonstration of searching and loading basemaps from [xyzservices](https://github.com/geopandas/xyzservices) and [Quick Map Services (QMS)](https://github.com/nextgis/quickmapservices). Selecting from 1000+ basemaps with a few clicks.
"""
)

with st.expander("See demo"):
    st.image("https://i.imgur.com/0SkUhZh.gif")

row1_col1, row1_col2 = st.columns([3, 1])
width = None
height = 800
tiles = None

with row1_col2:

    checkbox = st.checkbox("Search Quick Map Services (QMS)")
    keyword = st.text_input("Enter a keyword to search and press Enter:")
    empty = st.empty()

    if keyword:
        options = leafmap.search_xyz_services(keyword=keyword)
        if checkbox:
            options = options + leafmap.search_qms(keyword=keyword)

        tiles = empty.multiselect("Select XYZ tiles to add to the map:", options)

    with row1_col1:
        m = leafmap.Map()

        if tiles is not None:
            for tile in tiles:
                m.add_xyz_service(tile)

        m.to_streamlit(width, height)
