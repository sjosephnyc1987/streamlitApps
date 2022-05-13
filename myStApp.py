#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 12 16:24:48 2022

@author: stephenjoseph
"""
import streamlit as st

st.write(""" #my first app """)
         
        
import time


while True:
    st.write("I'm working and the date/time is ",time.ctime())
    time.sleep(5)
    