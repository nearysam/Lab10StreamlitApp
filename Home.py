import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
A Streamlit map template
<https://github.com/nearysam/Lab10StreamlitApp>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://www.google.com/imgres?q=utk%20logo%20direct%20url%20links&imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F8%2F87%2FUT_Knoxville_logo_2015.svg%2F819px-UT_Knoxville_logo_2015.svg.png&imgrefurl=https%3A%2F%2Fcommons.wikimedia.org%2Fwiki%2FFile%3AUT_Knoxville_logo_2015.svg&docid=ZJ2cKfJhmFSTgM&tbnid=oyw_z1t1Ft3QSM&vet=12ahUKEwiH8MXC6-CFAxX3gYQIHSK_BxYQM3oECBMQAA..i&w=819&h=768&hcb=2&ved=2ahUKEwiH8MXC6-CFAxX3gYQIHSK_BxYQM3oECBMQAA"
st.sidebar.image(logo)

# Customize page title
st.title("Streamlit for Geospatial Applications")

st.markdown(
    """
    This multipage app template demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and [leafmap](https://leafmap.org). It is an open-source project and you are very welcome to contribute to the [GitHub repository](https://github.com/nearysam/Lab10StreamlitApp).
    """
)

st.header("Instructions")

markdown = """
1. For the [GitHub repository](https://github.com/nearysam/Lab10StreamlitApp) or [use it as a template](https://github.com/nearysam/Lab10StreamlitApp/generate) for your own project.
2. Customize the sidebar by changing the sidebar text and logo in each Python files.
3. Find your favorite emoji from https://emojipedia.org.
4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.

"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
