import streamlit as st
import pandas as pd
import numpy as np
from data import Seite2

def page1():
    st.title('GirlsTech')
    st.write('Welcome to all our Girlys!')

def page2():
    Seite2()

pages = {
    'Seite 1': page1,
    "Seite 2": page2
}
# ---------------------------------------------------------------   

# Initialisierung der Session State
if 'page' not in st.session_state:
    st.session_state.page = 'Seite 1'

# Sidebar mit Seiten-Navigation
st.sidebar.title('GirlsTech')

selection = st.sidebar.radio("Navigation", list(pages.keys()))

# Aktualisiere die Session State basierend auf der Auswahl
st.session_state.page = selection

# Aufrufen der entsprechenden Seiten-Funktion
pages[st.session_state.page]()
