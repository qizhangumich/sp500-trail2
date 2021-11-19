# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 16:04:44 2021

@author: ZhangQi
"""

import numpy as np
import pandas as pd
import yfinance as yf
import streamlit as st
import altair as alt



#snp500 = pd.read_csv("Datasets/SP500.csv")
#symbols = snp500['Symbol'].sort_values().tolist()

symbols = ["NET","AAPL","MMM","A"]
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


