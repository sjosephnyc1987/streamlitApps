#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 12 16:24:48 2022

@author: stephenjoseph
"""
import streamlit as st

st.write(""" #my first app
         """)
         
        
import schedule
import time

def job():
    print("I'm working and the date/time is ",time.ctime())

schedule.every(0.5).minutes.do(job)


while 1:
    schedule.run_pending()
    time.sleep(1)