import streamlit as st
import pandas as pd

from dsproject import download_data
from dsproject import plot_stock_data   # sua função de plot
from dsproject.utils.get_current_date import get_current_date

# ------------------------------------------
# CONFIG
# ------------------------------------------

st.set_page_config(page_title="Stock Time Series", layout="wide")

st.title("📈 Stock Time Series Viewer")

st.sidebar.header("Parâmetros")

# Inputs
ticker = st.sidebar.text_input("Ticker", value="AAPL")

start_date = st.sidebar.date_input(
    "Data inicial",
    value=pd.to_datetime("2015-01-01")
)

end_date = st.sidebar.date_input(
    "Data final",
    value=pd.to_datetime(get_current_date())
)

btn = st.sidebar.button("Gerar gráfico")

# ------------------------------------------
# LÓGICA DO APP
# ------------------------------------------

if btn:
    with st.spinner("📥 Baixando dados do Yahoo Finance..."):
        df = download_data(
            ticker=ticker,
            start_date=str(start_date),
            end_date=str(end_date)
        )
    
    st.success(f"Dados carregados! {len(df)} linhas.")

    # --- Gráfico ---
    st.subheader(f"Time Series — {ticker}")
    fig = plot_stock_data(
        ticker=ticker,
        start_date=str(start_date),
        end_date=str(end_date)
    )
    st.plotly_chart(fig, use_container_width=True)

    # --- Tabela ---
    st.write("### Prévia dos dados")
    st.dataframe(df, use_container_width=True)

else:
    st.info("👈 Defina o ticker e clique em *Gerar gráfico* para começar.")

