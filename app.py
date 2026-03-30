import streamlit as st
import pandas as pd

df = pd.read_csv("dados.csv")

st.title("📊 Dashboard de Produtividade Logística")
st.markdown("Análise de desempenho operacional em tempo real")
st.dataframe(df)

st.subheader("Resumo")
col1, col2 = st.columns(2)

with col1:
    st.metric("Total de pedidos", df["qtnd"].sum())

with col2:
    st.metric("Tempo médio", round(df["time"].mean(), 2))
  
st.subheader("Pedidos por Funcionário")
st.bar_chart(df.groupby("name")["qtnd"].sum())
