# -*- coding: utf-8 -*-

import streamlit as st


# =====================================================
# CONFIGURAZIONE PAGINA
# =====================================================
st.set_page_config(
    page_title="Privacy e Cookie",
    layout="centered"
)


# =====================================================
# TITOLO
# =====================================================
st.title("🔐 Informativa Privacy e Cookie")


# =====================================================
# INFORMATIVA PRIVACY
# =====================================================
st.markdown(
    """
## Informativa sul trattamento dei dati personali

La presente informativa è resa ai sensi del Regolamento (UE) 2016/679
(**General Data Protection Regulation – GDPR**) ed è riferita
all’utilizzo della presente applicazione web.

---

### 1. Titolare del trattamento

**Dott. Carlo Rizzoli**  
Dottore Commercialista  
Venezia

Il titolare del trattamento può essere contattato attraverso
i canali professionali utilizzati per la messa a disposizione
della presente applicazione.

---

### 2. Tipologia di dati trattati

La presente applicazione **non raccoglie, non memorizza e non profila dati personali**.

In particolare:
- non vengono richiesti dati anagrafici;
- non vengono acquisiti dati identificativi;
- non vengono salvati i dati inseriti nei campi di simulazione.

I valori eventualmente inseriti dall’utente hanno **finalità esclusivamente
di calcolo e simulazione** e rimangono disponibili solo durante la sessione
di utilizzo dell’applicazione.

---

### 3. Finalità del trattamento

I dati inseriti facoltativamente dall’utente sono utilizzati unicamente per:
- simulare scenari economico‑finanziari;
- consentire la visualizzazione dei risultati del simulatore.

Non sono effettuati trattamenti ulteriori.

---

### 4. Base giuridica del trattamento

Il trattamento si basa sull’art. 6, par. 1, lett. f) GDPR,
in quanto necessario al funzionamento tecnico dell’applicazione
richiesta volontariamente dall’utente.

---

### 5. Modalità del trattamento

Il trattamento avviene con strumenti informatici,
nel rispetto dei principi di liceità, correttezza e trasparenza.
Non viene effettuata alcuna conservazione strutturata dei dati
né archiviazione su database.

---

### 6. Comunicazione e diffusione dei dati

I dati **non vengono comunicati a terzi né diffusi**.
Non è previsto alcun trasferimento verso paesi extra UE.

---

### 7. Diritti dell’interessato

Ai sensi degli articoli 15 e seguenti del GDPR,
l’utente può esercitare i diritti di accesso, rettifica,
limitazione e opposizione al trattamento,
nei limiti compatibili con la natura dell’applicazione.

---

### 8. Natura del conferimento

Il conferimento dei dati è **facoltativo**.
Il mancato inserimento di valori nei campi di input
non pregiudica la possibilità di consultare i contenuti informativi.
"""
)


# =====================================================
# COOKIE
# =====================================================
st.markdown(
    """
## Informativa sui cookie

La presente applicazione utilizza **esclusivamente cookie tecnici**.

### Cookie tecnici
Sono utilizzati cookie necessari al corretto funzionamento
della piattaforma Streamlit, relativi alla gestione della sessione
e all’interazione con l’interfaccia utente.

Non vengono utilizzati:
- cookie di profilazione;
- cookie di marketing;
- cookie di tracciamento comportamentale.

---

### Cookie di terze parti

L’applicazione è ospitata su infrastruttura **Streamlit Cloud**.
Eventuali cookie di terze parti sono gestiti direttamente
dal fornitore della piattaforma secondo le rispettive informative.

---

### Gestione dei cookie

Poiché sono utilizzati esclusivamente cookie tecnici,
non è richiesto il consenso preventivo dell’utente
ai sensi della normativa vigente.
"""
)


# =====================================================
# AVVERTENZA FINALE
# =====================================================
st.divider()

st.markdown(
    """
⚠️ **Avvertenza finale**

La presente informativa è fornita per finalità informative
e deve essere adattata e integrata qualora l’applicazione
venga utilizzata in contesti operativi o con funzionalità
che comportino il trattamento di dati personali.
"""
)