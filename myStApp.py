#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 12 16:24:48 2022

@author: stephenjoseph
"""
import streamlit as st
import pandas as pd
import numpy as np

st.write(""" #my first app
         """)
         
         
chart_data = pd.DataFrame(
np.random.randn(20, 3),
columns=['a', 'b', 'c'])

st.line_chart(chart_data)