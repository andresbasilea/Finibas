import streamlit as st
from PIL import Image
 

 

def app():  
    st.title("Finibas")
    st.header("Solución en Finanzas Personales")
    st.subheader("Realizado por Andrés Basile Álvarez")
    imagen1 = Image.open('imagenes/finibasmain.png')
    st.image(imagen1)


    st.markdown("La presente aplicación tiene por objetivo ayudarte a manejar tus finanzas. Acceda a la barra lateral dando click a la flecha en la parte superior izquierda para continuar.")
