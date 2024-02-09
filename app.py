# ======= Importación de librerías =======
import pandas as pd
import plotly.express as px
import streamlit as st

# ======= Encabezado de la aplicación =======
st.header('Ventas de vehículos')

# ======= Lectura de datos =======
car_data = pd.read_csv('vehicles_us.csv')


# ======= Gráfica 1: Vehículos por Marca =======

# Creamos una casilla de verificación para crear un histograma
histogram_check = st.checkbox('Construir histograma')

# Si la casilla de "histogram_check" esta marcada, se hará un histograma
if histogram_check:
    # Escribir un mensaje:
    st.write(
        'Conteo de Vehículos por Marca')

    # Creamos un histograma:
    fig = px.histogram(car_data, x='model')

    # Creamos un gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)


# ======= Gráfica 2: Costo por Marca =======

# Creamos una casilla de verificación para crear un gráfico de dispersión
dispersion_check = st.checkbox('Construir gráfico de dispersión')

# Si la casilla "dispersion_check" esta marcada, entonces se creará el gráfico de dispersión
if dispersion_check:
    # Escribir un mensaje:
    st.write(
        'Relación Costo por Marca')

    # Creamos el gráfico de dispersión:
    fig_disp = px.scatter(car_data, x='model', y='price')

    # Creamos un gráfico interactivo
    st.plotly_chart(fig_disp, use_container_width=True)


# ======= Gráfica 3: Kilometraje/Precio =======

# Creamos un botón para crear un gráfico de dispersión Kilometraje/Precio
hits_button = st.button('Kilometraje/Precio')

# Si se presiona el botón se creara un gráfico de dispersión relacionando Kilometraje/Precio
if hits_button:
    # Escribir un mensaje:
    st.write(
        'Kilometraje/Precio')

    # Creamos un gráfico de dispersión
    fig_km_price = px.scatter(car_data, x='odometer', y='price')

    # Creamos un gráfico interactivo:
    st.plotly_chart(fig_km_price, use_container_width=True)
