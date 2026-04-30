# -*- coding: utf-8 -*-

import streamlit as st
from utils_text_utils import load_txt_ascii_safe


# =====================================================
# CONFIGURAZIONE PAGINA (DEVE ESSERE ALL'INIZIO)
# =====================================================
st.set_page_config(
    page_title="Guida giuridica – Crisi d’impresa",
    layout="centered"
)


# =====================================================
# TITOLO
# =====================================================
st.title("📘 Guida giuridica – Piano e transazione fiscale")


# =====================================================
# STATO SESSIONE
# =====================================================
if "show_approfondimento" not in st.session_state:
    st.session_state.show_approfondimento = False


# =====================================================
# BOTTONE APPROFONDIMENTO
# =====================================================
st.button(
    "📄 Apri approfondimento giuridico",
    on_click=lambda: st.session_state.update(
        {"show_approfondimento": True}
    )
)


# =====================================================
# EXPANDER APPROFONDIMENTO
# =====================================================
with st.expander(
    "Approfondimento giuridico",
    expanded=st.session_state.show_approfondimento
):
    st.markdown(
        load_txt_ascii_safe("texts/approfondimento.txt")
    )


st.divider()


# =====================================================
# INTRODUZIONE GIURIDICA
# =====================================================
st.markdown(
    "### Finalità della guida\n\n"
    "Questa sezione fornisce un inquadramento giuridico essenziale degli istituti "
    "richiamati dal simulatore, con riferimento al Codice della Crisi d’Impresa "
    "e dell’Insolvenza (CCII).\n\n"
    "I contenuti hanno finalità informative e di orientamento e non sostituiscono "
    "la consulenza professionale né le valutazioni degli organi competenti."
)


# =====================================================
# CONTINUITÀ AZIENDALE
# =====================================================
st.header("1️⃣ Continuità aziendale")

st.markdown(
    "Nel contesto del CCII, la continuità aziendale consiste nella prosecuzione "
    "dell’attività economica da parte del debitore, anche in forma ridimensionata.\n\n"
    "La continuità è considerata ammissibile quando l’attività è in grado di generare "
    "flussi di cassa positivi, assolvere regolarmente le obbligazioni correnti e "
    "assicurare un risultato migliore rispetto alla liquidazione.\n\n"
    "Il simulatore è costruito per verificare questi presupposti attraverso l’analisi "
    "dei margini economici e della sostenibilità delle rate."
)


# =====================================================
# TRANSAZIONE FISCALE
# =====================================================
st.header("2️⃣ Transazione fiscale e contributiva (art. 63 CCII)")

st.markdown(
    "La transazione fiscale e contributiva consente di proporre il soddisfacimento "
    "parziale dei crediti tributari e previdenziali nell’ambito degli strumenti di "
    "regolazione della crisi.\n\n"
    "È possibile prevedere la falcidia del capitale nei limiti della sostenibilità, "
    "lo stralcio integrale di sanzioni e interessi e una rateizzazione coerente con "
    "i flussi prospettici dell’impresa."
)


# =====================================================
# CONVENIENZA PER IL FISCO
# =====================================================
st.header("3️⃣ Convenienza rispetto alla liquidazione")

st.markdown(
    "La valutazione di convenienza costituisce un elemento centrale nelle procedure "
    "che coinvolgono crediti pubblici.\n\n"
    "In assenza di beni liquidabili, la liquidazione conduce spesso a realizzi nulli "
    "o minimi; la continuità aziendale consente invece un soddisfacimento programmato "
    "e certo nel tempo.\n\n"
    "Il simulatore consente un confronto immediato tra importo del piano e recupero "
    "stimato in ipotesi di liquidazione."
)


# =====================================================
# MERITEVOLEZZA
# =====================================================
st.header("4️⃣ Meritevolezza del debitore")

st.markdown(
    "La meritevolezza del debitore è valutata sulla base del comportamento tenuto "
    "nella gestione dell’attività e nell’emersione della crisi.\n\n"
    "Assumono rilievo l’assenza di condotte dolose o distrattive, l’adozione di misure "
    "correttive prima del deposito e la collaborazione con i creditori pubblici.\n\n"
    "Il ridimensionamento dell’attività e la costruzione di un piano sostenibile "
    "costituiscono indici positivi ai fini dell’accesso agli strumenti del CCII."
)


# =====================================================
# RUOLO DEL SIMULATORE
# =====================================================
st.header("5️⃣ Ruolo del simulatore")

st.markdown(
    "Il simulatore non ha funzione decisionale né valutativa in senso giuridico.\n\n"
    "Esso rappresenta uno strumento di supporto volto a comprendere i principali "
    "equilibri economici del piano e a verificare la sostenibilità delle rate "
    "in scenari alternativi.\n\n"
    "Le risultanze devono essere integrate da un’analisi completa del caso concreto "
    "e dalle attestazioni previste dalla normativa."
)


# =====================================================
# AVVERTENZE FINALI
# =====================================================
st.divider()

st.markdown(
    "⚠️ **Avvertenza**\n\n"
    "Le informazioni contenute in questa sezione hanno carattere generale e non "
    "sostituiscono la consulenza professionale, le attestazioni e le decisioni "
    "demandate agli organi competenti."
)
