# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
from io import BytesIO


# ======================================
# CONFIGURAZIONE PAGINA
# ======================================
st.set_page_config(
    page_title="Piano di Transazione Fiscale – Simulatore",
    layout="centered"
)

st.title("📊 Piano di Transazione Fiscale – Simulatore")


# ======================================
# INTRODUZIONE
# ======================================
st.markdown(
    """
### Introduzione

Questa sezione è dedicata alla rappresentazione e alla verifica della sostenibilità
economico‑finanziaria di un accordo di ristrutturazione dei debiti di un’impresa
individuale, con particolare riferimento alla transazione fiscale e contributiva
prevista dal Codice della Crisi d’Impresa e dell’Insolvenza (CCII).

Il simulatore consente di analizzare in modo dinamico i principali equilibri economici
del piano, verificando la sostenibilità delle rate e valutando l’impatto di variazioni
dei dati di base.

I contenuti hanno finalità informative e non sostituiscono le valutazioni professionali.
"""
)


# ======================================
# AVVERTENZE LEGALI
# ======================================
with st.expander("Avvertenze legali"):
    st.write(
        """
I contenuti presenti su questo sito hanno finalità esclusivamente informative.
Le elaborazioni non costituiscono consulenza professionale, parere legale o fiscale,
né attestazione ai sensi del Codice della Crisi d’Impresa e dell’Insolvenza.
"""
    )


# ======================================
# INPUT DATI ECONOMICI
# ======================================
st.header("1️⃣ Dati economici")

fatturato = st.number_input("Fatturato annuo (€)", value=34000, step=1000)
costo_personale = st.number_input("Costo personale annuo (€)", value=18000, step=1000)
altri_costi = st.number_input("Altri costi annui (€)", value=6000, step=500)


# ======================================
# INPUT DEBITO
# ======================================
st.header("2️⃣ Dati del debito")

capitale = st.number_input(
    "Capitale debito fiscale/contributivo (€)",
    value=70000,
    step=1000
)

percentuale = st.slider(
    "Percentuale di transazione (%)",
    min_value=10,
    max_value=100,
    value=35
) / 100

durata_mesi = st.number_input(
    "Numero rate (mesi)",
    value=84,
    step=12
)


# ======================================
# CALCOLI
# ======================================
margine_annuo = fatturato - costo_personale - altri_costi
margine_mensile = margine_annuo / 12

importo_piano = capitale * percentuale
rata_mensile = importo_piano / durata_mesi
margine_post_rata = margine_mensile - rata_mensile


# ======================================
# RISULTATI
# ======================================
st.header("3️⃣ Risultati del piano")

c1, c2 = st.columns(2)

with c1:
    st.metric("Capitale debito", f"{capitale:,.0f} €")
    st.metric("Percentuale proposta", f"{int(percentuale*100)} %")
    st.metric("Importo piano", f"{importo_piano:,.0f} €")

with c2:
    st.metric("Numero rate", durata_mesi)
    st.metric("Rata mensile", f"{rata_mensile:,.2f} €")
    st.metric("Margine dopo rata", f"{margine_post_rata:,.2f} €")


# ======================================
# VALUTAZIONE SOSTENIBILITÀ
# ======================================
st.header("4️⃣ Valutazione di sostenibilità")

if margine_post_rata >= 0:
    st.success("✅ Piano sostenibile con i flussi dell’attività")
else:
    st.error("❌ Piano NON sostenibile con i flussi attuali")


# ======================================
# CONFRONTO CON LIQUIDAZIONE
# ======================================
st.header("5️⃣ Confronto con liquidazione alternativa")

recupero_liquidazione = st.number_input(
    "Recupero stimato per l’Erario in liquidazione (€)",
    value=24000,
    step=1000
)

if importo_piano > recupero_liquidazione:
    st.success("✅ Continuità e transazione più conveniente per il Fisco")
else:
    st.warning("⚠️ Liquidazione potenzialmente più conveniente")


# ======================================
# RIEPILOGO TABELLA
# ======================================
st.header("6️⃣ Riepilogo numerico")

df = pd.DataFrame({
    "Voce": [
        "Fatturato annuo",
        "Costo personale",
        "Altri costi",
        "Margine mensile",
        "Capitale debito",
        "Percentuale",
        "Numero rate",
        "Rata mensile",
        "Importo piano",
        "Recupero liquidazione"
    ],
    "Valore": [
        fatturato,
        costo_personale,
        altri_costi,
        round(margine_mensile, 2),
        capitale,
        f"{int(percentuale*100)} %",
        durata_mesi,
        round(rata_mensile, 2),
        round(importo_piano, 2),
        recupero_liquidazione
    ]
})

st.dataframe(df, use_container_width=True)


# ======================================
# DOWNLOAD EXCEL
# ======================================
def crea_excel(dataframe: pd.DataFrame) -> BytesIO:
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        dataframe.to_excel(writer, index=False, sheet_name="Piano")
    buffer.seek(0)
    return buffer

st.download_button(
    label="⬇️ Scarica Excel",
    data=crea_excel(df),
    file_name="piano_transazione_fiscale.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)