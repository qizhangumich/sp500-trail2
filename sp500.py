# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 16:04:44 2021

@author: ZhangQi
"""

import pandas as pd
import streamlit as st
import yfinance as yf
import deepl
import datetime as dt
import matplotlib.pyplot as plt
import altair as alt
import translators as ts


snp500 = pd.read_csv("Datasets/SP500.csv")
symbols = snp500['Symbol'].sort_values().tolist()
 
ticker = st.sidebar.selectbox(
    'Choose a S&P 500 Stock',
     symbols)     

stock = yf.Ticker(ticker)
info = stock.info



st.title(info['longName'])
st.image(info['logo_url'])
#subheader() 
st.markdown('** Sector **: ' + info['sector'])
st.markdown('** Industry **: ' + info['industry'])
st.markdown('** Phone **: ' + info['phone'])
st.markdown('** Address **: ' + info['address1'] + ', ' + info['city'] + ', ' + info['zip'] + ', '  +  info['country'])
st.markdown('** Website **: ' + info['website'])
st.markdown('** Business Summary **')


text = info['longBusinessSummary']
#result = translator.translate(text,lang_src="en", lang_tgt="zh")
st.info(text)


start = dt.datetime.today()-dt.timedelta(2 * 365)
end = dt.datetime.today()
df = yf.download(ticker,start,end)
#st.plt.plot(data=df["Close"])
#st.line_chart(data=df["Close"], width=0, height=0, use_container_width=True)
df = df.reset_index()
c = alt.Chart(df).mark_line().encode(x='Date:T', y='Close:Q')
st.altair_chart(c, use_container_width=True)
#bs = stock.get_balance_sheet(proxy="PROXY_SERVER")
#st.dataframe(data=bs)

