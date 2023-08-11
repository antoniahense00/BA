# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from modell import modell

a = modell()

a.load_data("Speicherdaten_FW.xlsx")

a.add_kennwert("min_Temp", 100, True)
a.add_kennwert("konstante_Temp", "Ja")
a.add_kennwert("max_Temp", 1000, False)


a.add_kennwert("min", 50)


a.create_heatmap()

a.create_list()

