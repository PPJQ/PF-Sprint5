# Importación de librerías:
import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado de la aplicación:
st.header('Ventas de vehículos')

# Leemos los datos
car_data = pd.read_csv('vehicles_us.csv')

# Creamos un botón para crear un histograma
hist_button = st.button('Construir histograma')

# Al hacer click en el botón se hará lo siguiente
if hist_button:
    # Escribir un mensaje:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Creamos un histograma:
    fig = px.histogram(car_data, x='model')

    # Creamos un gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)

# Creamos una casilla de verificación para crear un gráfico de dispersión
dispersion_check = st.checkbox('Construir gráfico de dispersión')

# Si la casilla "dispersion_check" esta marcada, entonces se creará el gráfico de dispersión
if dispersion_check:
    # Escribir un mensaje:
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Creamos el gráfico de dispersión:
    fig_disp = px.scatter(car_data, x='model', y='price')

    # Creamos un gráfico interactivo
    st.plotly_chart(fig_disp, use_container_width=True)
