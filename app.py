import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.express
    fig = px.histogram(car_data, x='odometer',
                       title='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Crear un botón en la aplicación Streamlit
scatter_button = st.button('Construir Disperción')

# Lógica a ejecutar cuando se hace clic en el botón
if scatter_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un gráfico de dispersión utilizando plotly.express
    fig = px.scatter(car_data, x='odometer', y='price',
                     title='Dispersión del Odómetro vs Precio')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig, use_container_width=True)
