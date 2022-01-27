#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 15:51:55 2021

@author: stephengood
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataFile = 'GenoHydroHydrograph_Data.csv'
df = pd.read_csv(dataFile); 


basin_area = 156 # squre miles
cfs_to_cms = 0.028316873266469
squaremiles_to_squrekm = 2.58999
basin_area_m2 = basin_area * squaremiles_to_squrekm * 1000**2

day = df['DAY'].values
d2h = df['d2HVSMOW (‰)'].values
d18o = df['d18OVSMOW (‰)'].values
discharge_CFS = df['DISCHARGE [CFS]'].values
flow = discharge_CFS * cfs_to_cms * (60*60*24)/(basin_area_m2) * 1000
ppt = df['ppt (mm)']


d2h_pre_3 = -38.7; d18o_pre_3 = -6.3; pre_3_days = np.array([-1,13])
d2h_pre_4 = -23.3; d18o_pre_4 = -5.0; pre_4_days = np.array([14,33])

d2h_base = np.nanmean(d2h[day<9])

bfi = (d2h - d2h_base)/(d2h_pre_3 - d2h_base)


plt.figure(1, figsize=(10,10))
plt.subplot(2,2,1)
plt.plot(day, d2h,'ro',label='Stream Samples')
plt.plot(pre_3_days, pre_3_days*0+d2h_pre_3,'r-',label='Precip Samples')
plt.plot(pre_4_days, pre_4_days*0+d2h_pre_4,'r-')
plt.ylabel('delta 2H [permil]'); #plt.legend()
plt.xlim(0,31)

plt.subplot(2,2,3)
plt.plot(day, d18o,'bo',label='Stream Samples')
plt.plot(pre_3_days, pre_3_days*0+d18o_pre_3,'b-',label='Precip Samples')
plt.plot(pre_4_days, pre_4_days*0+d18o_pre_4,'b-')
plt.ylabel('delta 18O [permil]'); #plt.legend()
plt.xlim(0,31)

plt.subplot(2,2,2)
plt.bar(day,ppt,color='k')
plt.ylabel('PRISM Precip [mm]')

plt.subplot(2,2,4)
plt.plot(day,discharge_CFS,'k-')
plt.ylabel('USGS Measured Flow [CFS]')
#plt.plot(day,flow*bfi,'r-')
plt.savefig('F1.pdf')
