import streamlit as st

foto = st.camera_input("Foto")
st.divider()
st.image(foto)
