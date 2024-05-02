import streamlit as st

foto = st.camera_input("Foto")
st.divider()
if foto is not None:
  st.image(foto)
