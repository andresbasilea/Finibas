from PIL.Image import init
import streamlit as st
import Portfolio
import Bienvenida
import re

TABS = {"Inicio": Bienvenida, "Portafolio": Portfolio}


st.set_page_config(page_icon=":brain:", page_title="FINIBAS",)

st.sidebar.title('Finanzas Personales')
selection = st.sidebar.radio("Ir a", list(TABS.keys()))
page = TABS[selection]
page.app()




