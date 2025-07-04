
import os
import pandas as pd
import streamlit as st

# Cargar el archivo CSV
df = pd.read_csv("DATA_PRUEBA.csv")

# Título de la aplicación
st.title("Consulta de Empleados")

# Mostrar una vista previa
st.subheader("Vista general de datos")
st.dataframe(df)

# Filtro por departamento
departamentos = df['departamento'].unique()
departamento_seleccionado = st.selectbox("Selecciona un departamento", ["Todos"] + list(departamentos))

# Filtro por salario mínimo
salario_min = st.slider("Salario mínimo", min_value=int(df['salario'].min()), max_value=int(df['salario'].max()), step=100)

# Aplicar filtros
df_filtrado = df.copy()

if departamento_seleccionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado['departamento'] == departamento_seleccionado]

df_filtrado = df_filtrado[df_filtrado['salario'] >= salario_min]

# Mostrar resultados
st.subheader("Resultados filtrados")
st.dataframe(df_filtrado)
