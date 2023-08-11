# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# %% Import

import pandas as pd
import numpy as np
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt

# %% Main

data = pd.read_excel("Speicherdaten_FW.xlsx")
t = []
k = []
sk = []


#Temperatur
i_temp = input("Welche Temperatur wird benötigt?")
i_temp = int(i_temp)


c_temp = data['max_Temp'].values
c_temp = c_temp.astype('int')

min_temp = data['min_Temp'].values
min_temp = min_temp.astype('int')

for element in c_temp:
    if element > i_temp:
        t.append(1)
    else:
        p_temp = element/i_temp
        t.append(round(p_temp,2))
        
#konstante Temperatur?
i_ktemp = input("Wird eine konstante Temperatur benötigt? (bitte Ja oder Nein schreiben)")



k_temp = data['konstante_Temp'].values


for element in k_temp:
    if element == i_ktemp:
        k.append(1)
    else: 
        k.append(0)


#Speicherkapazität
i_kapa = input("Welche Speicherkapazität wird benötigt? (in MWh)")
i_kapa = int(i_kapa)


kapa = data['Speicherkapazität in MWh'].values
kapa = kapa.astype('int')


for element in kapa:
    if element > i_kapa:
        sk.append(1)
    else: 
        p_kapa= element/i_kapa
        sk.append(round(p_kapa,2))


#heatmap = np.array([[t],[k]])

# %% plot

kenn = ["Temperatur", "konstante Ausspeichertemperatur", "Speicherkapazität"]
speicher = ["Sand","Ziegelstein","Beton","Stahlschlacke","Aluminium in Graphit"]

heatmap = np.array([t,k,sk])


fig, ax = plt.subplots()
im = ax.imshow(heatmap)
ax.imshow(heatmap, cmap = 'RdYlGn')


# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(speicher)), labels=speicher)
ax.set_yticks(np.arange(len(kenn)), labels=kenn)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(kenn)):
    for j in range(len(speicher)):
        text = ax.text(j, i, heatmap[i, j],
                       ha="center", va="center", color="k")

ax.set_title("Heatmap Speicherauswahl")
fig.tight_layout()
plt.show()

# %% Tabelle

summe = []

summe = np.sum(heatmap, axis = 0) 
summe = summe.tolist()

summe_speicher = [summe,speicher]

summe_sortiert = summe.copy()
summe_sortiert.sort(reverse=True)