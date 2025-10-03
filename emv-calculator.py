# app.py
import streamlit as st

def calculate_emv(reach: int, cpm: float) -> float:
    """
    Calcola l'Earned Media Value (EMV).
    Formula: (Reach / 1000) * CPM
    """
    return (reach / 1000) * cpm

# Titolo app
st.title("📊 Earned Media Value Calculator")

st.markdown(
    """
    Questa applicazione calcola l'**Earned Media Value (EMV)** a partire da:
    - **Reach** (numero di persone raggiunte)
    - **CPM** (costo per mille impressioni)
    """
)

# Input utente
reach = st.number_input("Reach (numero di persone raggiunte)", min_value=0, step=1000)
cpm = st.number_input("CPM (costo per mille impressioni)", min_value=0.0, step=0.1)

# Bottone calcolo
if st.button("Calcola EMV"):
    emv = calculate_emv(reach, cpm)
    st.success(f"✅ L'Earned Media Value è: **{emv:,.2f}**")
