import streamlit as st
import pandas as pd

df = pd.read_csv("dados.csv")

st.title("Dashboard Logístico")

st.dataframe(df)

st.subheader("Resumo")
st.write("Total de pedidos:", df["qtnd"].sum())
st.write("Tempo médio:", df["time"].mean())

st.subheader("Pedidos por Funcionário")
st.bar_chart(df.groupby("name")["qtnd"].sum())
