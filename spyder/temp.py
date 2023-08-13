# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from modell import modell


#Nutze die modell()- Methode um dein Modell zu laden:
a = modell()

#Mit load_data() wird die Speicherdatenbank integriert:
a.load_data("Speicherdaten_FW.xlsx")

# Mit add_kennwert(kennwert, inhalt) können die verschiedenen Kennwerte mit
#jeweiliger Zahl hinzugefügt werden:

a.add_kennwert("min_Temp", 90, True)
#a.add_kennwert("konstante_Temp", "Ja")
a.add_kennwert("max_Temp", 1000)
a.add_kennwert("minTemp", 200)
a.add_kennwert('Speicherart', 'Sensibel')
a.add_kennwert('Speicherkapazität', 2300)

#Mit create_heatmap() wird die heatmap geplottet, es muss vorher die Datenbank
#geladen werden und Kennwerte zum Modell hinzugefügt werden.
a.create_heatmap()

#Mit create_list() wird eine sortierte Liste ausgegeben. Es muss vorher die 
#Heatmap erzeugt werden.
a.create_list()

