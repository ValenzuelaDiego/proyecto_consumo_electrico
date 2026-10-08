# Predicción de consumo eléctrico - Planta ubicada en Guarambaré, Central, Paraguay.

## Problema
La planta no cuenta con visibilidad anticipada de su consumo de energía eléctrica, lo que dificulta la planificación y la detección de anomalías respecto al consumo de energía diario esperado según las condiciones climáticas y la producción planificada.

## Objetivo
Definir que variables son considerables importantes para la predicción de consumo de energía eléctrica. 
Crear un modelo capaz de predecir el consumo eléctrico a partir de variables de producción y variables meteorológicas para dar soporte a la planificación energética y para detectar de manera rápida anomalías asociadas al consumo energético.

## Datos
- Periodo: octubre 2021 a octubre 2026 (diario)
- Fuente: datos internos de producción (de dos tipos de productos) y consumo de la empresa, más datos meteorológicos históricos de Guarambaré obtenidos vía API de Open-Meteo.
- Variables: producción de producto tipo A, producción de producto tipo B, temperatura máxima/mínima/promedio, humedad, día de la semana, feriado.
- Se evaluaron dos escenarios: (1) solo producción tipo A + clima, 2021 - 2026; (2) producción tipo A y B + clima, 2024-2026 (periodo con datos reales de B).

## Modelo
RandomForestRegressor dentro de un Pipeline con ColumnTransformer (StandardScaler para variables numéricas, OneHotEncoder para categóricas). 
Se eligió Random Forest por su capacidad de capturar relaciones no lineales y su robustez frente a la multicolinealidad entre variables de temperatura.

## Resultado
#### Escenario 1 (solo producción de producto A más variables meteorológicas)
MAE: 1500.25 KWh; 
RMSE: 2015.18 KWh; 
MAPE: 7.22%
#### Escenario 2 (producción de producto A y producto B más variables meteorológicas)
MAE: 764.88 kWh; 
RMSE: 1018.16 kWh; 
MAPE: 3.77%

Incluir la producción del producto B reduce el error casi a la mitad. El análisis de importancia de variables confirma que producto A (65%) y producto B (17%) son las variables más determinantes, mientras que día de la semana y feriados resultan irrelevantes (consiste que la planta opera de forma continua). Se selecciono el modelo del Escenario 2 como modelo final.
