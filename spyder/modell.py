#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 13:13:28 2023

@author: antoniahense
"""

import pandas as pd
import numpy as np
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt

class modell:
    kennwerte = ["Speicherart","Speichermaterial","konstante_Temp","min_Temp","max_Temp","Speicherkapazität","Speicherzeitraum","Lebensdauer"]
    kennwerte_hm = []
    #art_hm = []
    #temp_hm = []
    data = []
    parameter = []
    heatmap = []
    counter = 0.0
    
    #Methode zum laden der Speicherdaten
    def load_data(self, dateiname):
       self.data = pd.read_excel(dateiname)
       #return self.data
       
    #Methode zum hinzufügen der Kennwerte; erstellt ein 2D-Array 
    def add_kennwert(self, kennwert, inhalt, flag: bool = False):
        
        speicher_vorhanden = False
        for element in self.kennwerte:
            if kennwert == element:
                speicher_vorhanden = True
                if len(self.parameter) == 0:
                    self.parameter = [[kennwert, inhalt, flag]]
                    self.kennwerte_hm =[kennwert]
                else:    
                    self.parameter.append([kennwert, inhalt, flag])
                    self.kennwerte_hm.append(kennwert)
                print("Der Kennwert "+kennwert+" wurde zu deinem Modell hinzugefügt.")
                self.counter = self.counter +1 
        if speicher_vorhanden == False:
            print("Den Kennwert " + kennwert + " gibt es leider nicht. Es gibt die folgenden Kennwerte: ")
            for element in self.kennwerte: print(element)
            print('-----------------------')
            
            
    def add_maxTemp(self):
        print(1)
        max_Temp = []
       
        for i in range(0,len(self.parameter)):
            
            if self.parameter[i][0] == "max_Temp":
               
                for element in self.data['max_Temp'].values.astype('int'):
                    if element > self.parameter[i][1]:
                        max_Temp.append(1)
                        
                    else:
                        p_temp = element/self.parameter[i][1]
                        max_Temp.append(round(p_temp,2))
                        
                if len(self.heatmap) == 0:
                    self.heatmap = max_Temp
                else:
                    self.heatmap = np.vstack([self.heatmap, max_Temp]) 
                    
    def add_minTemp(self):
        min_Temp = []
       
        for i in range(0,len(self.parameter)):
           
            if self.parameter[i][0] == "min_Temp":
               
                for element in self.data['min_Temp'].values.astype('int'):
                    if element < self.parameter[i][1]:
                        min_Temp.append(1)
                        
                    else:
                        p_temp = self.parameter[i][1]/element
                        min_Temp.append(round(p_temp,2))
                        
                if len(self.heatmap) == 0:
                    self.heatmap = min_Temp
                else:
                    self.heatmap = np.vstack([self.heatmap,min_Temp]) 
                    
                    
    def add_konstanteTemp(self):
        k_Temp = []
        for i in range(0,len(self.parameter)):
           
            if self.parameter[i][0] == 'konstante_Temp':
               
                for element in self.data['konstante_Temp'].values:
                    if element == self.parameter[i][1]:
                        k_Temp.append(1)
                        
                    else:
                        k_Temp.append(0)
                        
                if len(self.heatmap) == 0:
                    self.heatmap = k_Temp
                else:
                    self.heatmap = np.vstack([self.heatmap,k_Temp]) 
      
        #%% Methode zur Erstellung der Heatmap
        
    def create_heatmap(self):
        
        for element in self.kennwerte_hm:
            print(2)
            if element == 'max_Temp': 
                print(3)
                self.add_maxTemp()     
            if element == 'min_Temp':
                self.add_minTemp()
            if element == 'konstante_Temp':
                self.add_konstanteTemp()
                
        
                        
            
       # Heatmap Erstellung
       
       # kenn = ["Temperatur", "konstante Ausspeichertemperatur", "Speicherkapazität"]
       # speicher = ["Sand","Ziegelstein","Beton","Stahlschlacke","Aluminium in Graphit"]
        speicher_list = (self.data['Speichermaterial'].values).tolist()
        speicher = speicher_list
        
        #self.heatmap = np.array([max_Temp, min_Temp,k_Temp])


        fig, ax = plt.subplots()
        im = ax.imshow(self.heatmap)
        ax.imshow(self.heatmap, cmap = 'RdYlGn')


        # Show all ticks and label them with the respective list entries
        ax.set_xticks(np.arange(len(speicher)), labels=speicher)
        ax.set_yticks(np.arange(len(self.kennwerte_hm)), labels=self.kennwerte_hm)

        # Rotate the tick labels and set their alignment.
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                 rotation_mode="anchor")

        # Loop over data dimensions and create text annotations.
        for i in range(len(self.kennwerte_hm)):
            for j in range(len(speicher)):
                text = ax.text(j, i, self.heatmap[i, j],
                               ha="center", va="center", color="k")

        ax.set_title("Heatmap Speicherauswahl")
        fig.tight_layout()
        plt.show()
        
        
    #%%    
    def create_list(self):
        
        summe = []
        speicher = ["Sand","Ziegelstein","Beton","Stahlschlacke","Aluminium in Graphit"]

        summe = np.sum(self.heatmap, axis = 0) 
        summe = summe.tolist()

        summe_speicher = [summe,speicher]
        summe_speicher = np.transpose(summe_speicher)
        
  
        sorted_array = sorted(summe_speicher, key=lambda x: x[0],reverse=True)
        
      
       
        print("Die folgenden Speicher erfüllen alle Anforderungen:")
        for i in range(0,len(sorted_array)):
            if sorted_array[i][0].astype('float') == self.counter:
                print(sorted_array[i][1])
        print("Die folgenden Speicher erfüllen nicht alle Anforderungen:")
        for i in range(0,len(sorted_array)):
            if sorted_array[i][0].astype('float') != self.counter:
                print(sorted_array[i][1])
        

"""
    def create_list(self):
        
        summe = []
        speicher = ["Sand","Ziegelstein","Beton","Stahlschlacke","Aluminium in Graphit"]

        summe = np.sum(self.heatmap, axis = 0) 
        summe = summe.tolist()

        summe_speicher = [summe,speicher]
        summe_speicher =  np.transpose(summe_speicher)
        
        #print(np.transpose(summe_speicher1))
        

        # bubble sort list of lists based on second index
        n = len(summe_speicher)
        for i in range(n):
            for j in range(n-1):
                if summe_speicher[j][0] < summe_speicher[j+1][0]:
                    summe_speicher[j], summe_speicher[j+1] = summe_speicher[j+1], summe_speicher[j]
        
        print(summe_speicher)

        #summe_sortiert = summe.copy()
        #summe_sortiert.sort(reverse=True)

    
"""
    
    
    