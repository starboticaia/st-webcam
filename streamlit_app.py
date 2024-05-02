import streamlit as st
from PIL import Image
import numpy as np

# el objeto es de tipo fichero, no imagen
img_file_buffer = st.camera_input("Haz una foto")

if img_file_buffer is not None:
    # convertimos a imagen
    img = Image.open(img_file_buffer)

    # convertimos a array
    img_array = np.array(img)

    # Check the type of img_array:
    # Should output: <class 'numpy.ndarray'>
    #st.write(type(img_array))

    # muestra altura, anchura y canales    
    st.write(img_array.shape)
