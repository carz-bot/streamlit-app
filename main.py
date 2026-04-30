# -*- coding: utf-8 -*-

import streamlit as st


# =====================================================
# CONFIGURAZIONE PAGINA
# =====================================================
st.set_page_config(
    page_title="Simulatore Transazione Fiscale",
    layout="centered"
)


# =====================================================
# HOME PAGE
# =====================================================
st.title("🏛️ Simulatore di Transazione Fiscale")

st.markdown(
    """
### Benvenuto

Questa applicazione consente di:
- simulare un **piano di transazione fiscale e contributiva**
- verificare la **sostenibilità economico-finanziaria**
- consultare una **guida giuridica di inquadramento normativo**

Usa il menu laterale per navigare tra le sezioni.
"""
)

st.divider()

st.markdown(
    """
📄 **Pagine disponibili**
- 📊 Simulatore del piano
- 📘 Guida giuridica
"""
)
