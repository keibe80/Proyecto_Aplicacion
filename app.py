import pandas as pd
import plotly.express as px
import streamlit as st
import plotly as plt

# Cargar los datos una sola vez (si no está cargado en la sesión)
if 'car_data' not in st.session_state:
    st.session_state.car_data = pd.read_csv(r'D:\ProyectosPY\Sprint7\Proyecto\Proyecto_7\vehicles_us.csv')
car_data = st.session_state.car_data

# Título principal
st.title("Datos de anuncios de ventas de automóviles")

# Checkbox para mostrar los primeros 100 datos
data = st.checkbox("Primeros 100 datos")
if data:
    st.write(car_data.head(100))

# Histograma de odómetro
histo = st.checkbox("Valores únicamente del odómetro")
if histo:
    st.header("Distribución de valores obtenidos del odómetro")
    st.write("Este histograma muestra la distribución de los kilometrajes (odómetros) en los anuncios de venta de coches.")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión de kilometraje vs precio
dipe = st.checkbox("Relación kilometraje-precio")
if dipe:
    st.header("Variación del precio en función del kilometraje")
    st.write('Este gráfico muestra cómo varía el precio según el kilometraje de los coches.')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

# Histograma de condición del vehículo
df1 = car_data.groupby("condition")["model_year"].count().reset_index(name="count")
df_1 = st.checkbox("Grafica de condición respecto al modelo")
if df_1:
    st.header("Distribución de autos según la condición")
    fig = px.bar(df1, x="condition", y="count", title="Número de autos por condición",
                 labels={"condition": "Condición del auto", "count": "Número de autos"})
    st.plotly_chart(fig, use_container_width=True)

# Comparación entre dos modelos según el precio
df_2 = st.checkbox("Comparar dos modelos según el precio")
if df_2:
    modelos = car_data["model"].unique()
    st.header("Selecciona dos modelos para comparar")
    
    # Selección de modelos
    modelo_1 = st.selectbox("Selecciona el primer modelo", modelos)
    modelo_2 = st.selectbox("Selecciona el segundo modelo", modelos)
    
    if modelo_1 and modelo_2:
        st.session_state.modelo_1 = modelo_1
        st.session_state.modelo_2 = modelo_2
        
        st.write(f"Has seleccionado {st.session_state.modelo_1} y {st.session_state.modelo_2} para la comparación.")
        
        # Filtrado y gráfico
        df_comparacion = car_data[car_data['model'].isin([st.session_state.modelo_1, st.session_state.modelo_2])]
        fig = px.scatter(df_comparacion, x="model", y="price", color="model", title=f"Comparación de Precios entre {st.session_state.modelo_1} y {st.session_state.modelo_2}")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("Por favor, selecciona ambos modelos para realizar la comparación.")

#Histograma del precio según la transmisión
df3= st.checkbox("Histograma según la transmisión del modelo")
if df3:
    st.header("Distribución de autos según la transmisión")
    fig = px.histogram(car_data, x="price", color="transmission", title="Distribución de precios por tipo de transmisión",  
                       labels={"price": "Precio", "transmission": "Tipo de transmisión"}, barmode='overlay', opacity=0.6)    
    st.plotly_chart(fig, use_container_width=True)