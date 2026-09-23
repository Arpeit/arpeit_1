import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles_us.csv")

st.header("Análisis de anuncios de vehículos en EE. UU.")

show_histogram = st.checkbox("Construir histograma de kilometraje")

if show_histogram:
    st.write("Histograma de kilometraje de los vehículos")

    fig = px.histogram(
        car_data,
        x="odometer",
        nbins=50
    )

    st.plotly_chart(fig, use_container_width=True)

show_scatter = st.checkbox(
    "Construir gráfico de dispersión: kilometraje vs. precio"
)

if show_scatter:
    st.write("Relación entre kilometraje y precio de los vehículos")

    fig = px.scatter(
        car_data,
        x="odometer",
        y="price"
    )

    st.plotly_chart(fig, use_container_width=True)