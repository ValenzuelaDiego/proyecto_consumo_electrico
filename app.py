import streamlit as st
import pandas as pd
import joblib
import holidays

st.set_page_config(page_title="Predicción de consumo eléctrico", page_icon="⚡")

@st.cache_resource
def cargar_modelo():
    return joblib.load("model.pkl")

modelo = cargar_modelo()
feriados_py = holidays.Paraguay(years=range(2021, 2028))

st.title("⚡ Predicción de consumo eléctrico diario")
st.write("Ingresá los datos de producción y clima del día a predecir.")

col1, col2 = st.columns(2)
with col1:
    fecha = st.date_input("Fecha")
    prod_a = st.number_input("Producción A (Total Released TA)", min_value=0.0, value=12000.0)
    prod_b = st.number_input("Producción B (TBCS)", min_value=0.0, value=8000.0)
with col2:
    temp_max = st.number_input("Temperatura máxima (°C)", value=30.0)
    temp_min = st.number_input("Temperatura mínima (°C)", value=20.0)
    humedad = st.number_input("Humedad relativa (%)", min_value=0.0, max_value=100.0, value=70.0)

temp_prom = (temp_max + temp_min) / 2  # aproximación; Open-Meteo calcula el promedio con datos horarios

if st.button("Predecir consumo"):
    dia = pd.Timestamp(fecha).day_name()
    entrada = pd.DataFrame({
        "Total Released TA": [prod_a],
        "TBCS": [prod_b],
        "temp_max": [temp_max],
        "temp_min": [temp_min],
        "temp_prom": [temp_prom],
        "humedad": [humedad],
        "dia_semana": [dia],
        "es_feriado": [int(fecha in feriados_py)],
        "es_fin_de_semana": [int(dia in ["Saturday", "Sunday"])],
    })
    pred = modelo.predict(entrada)[0]
    st.success(f"Consumo estimado: **{pred:,.0f} kWh**")