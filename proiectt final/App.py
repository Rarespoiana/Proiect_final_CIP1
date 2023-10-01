import tkinter as tk
from tkinter import ttk
from calculate_CIP1 import calculeaza_CIP1, calculeaza_X1, calculeaza_X2, calculeaza_X3, calculeaza_X4, calculeaza_X5
import datetime

def calculate_CIP1():
    varsta = entry_varsta.get()
    cost_mentenanta = entry_cost_mentenanta.get()
    media_cheltuielilor = entry_media_cheltuielilor.get()
    timp_indisponibilitate = entry_timp_indisponibilitate.get()
    timp_mediu_indisponibilitate = entry_timp_mediu_indisponibilitate.get()
    scop_utilizare = entry_scop_utilizare.get()
    sprijin_producator = entry_sprijin_producator.get()
    serviciu_mentenanta = entry_serviciu_mentenanta.get()
    asigurare_consumabile = entry_asigurare_consumabile.get()


    varsta = datetime.datetime.now().year - int(varsta)  # Calculăm varsta din anul curent și anul fabricației
    cost_mentenanta = float(cost_mentenanta)
    media_cheltuielilor = float(media_cheltuielilor)
    timp_indisponibilitate = int(timp_indisponibilitate)
    timp_mediu_indisponibilitate = int(timp_mediu_indisponibilitate)

    X1 = calculeaza_X1(varsta)
    X2 = calculeaza_X2(cost_mentenanta, media_cheltuielilor)
    X3 = calculeaza_X3(timp_indisponibilitate, timp_mediu_indisponibilitate)
    X4 = calculeaza_X4(scop_utilizare)
    X5 = calculeaza_X5(sprijin_producator, serviciu_mentenanta, asigurare_consumabile)

    CIP1 = calculeaza_CIP1(X1, X2, X3, X4, X5)


    label_result.config(text=f"Raspuns: {CIP1}")

root = tk.Tk()
root.title("Valoare CIP")


labels = ["X1 (Anul fabricatiei):", "X2 (Pret achizitie):", "Media cheltuielilor:", "X3 (Timp indisponibilitate):",
          "Timp mediu indisponibilitate:", "X4 (Scopul utilizarii):", "X5 (Sprijin producator):",
          "Serviciu mentenanta:", "Asigurare consumabile:"]

for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0)

entry_varsta = tk.Entry(root)
entry_varsta.grid(row=0, column=1)

entry_cost_mentenanta = tk.Entry(root)
entry_cost_mentenanta.grid(row=1, column=1)

entry_media_cheltuielilor = tk.Entry(root)
entry_media_cheltuielilor.grid(row=2, column=1)

entry_timp_indisponibilitate = tk.Entry(root)
entry_timp_indisponibilitate.grid(row=3, column=1)

entry_timp_mediu_indisponibilitate = tk.Entry(root)
entry_timp_mediu_indisponibilitate.grid(row=4, column=1)

entry_scop_utilizare = tk.Entry(root)
entry_scop_utilizare.grid(row=5, column=1)

entry_sprijin_producator = tk.Entry(root)
entry_sprijin_producator.grid(row=6, column=1)

entry_serviciu_mentenanta = tk.Entry(root)
entry_serviciu_mentenanta.grid(row=7, column=1)

entry_asigurare_consumabile = tk.Entry(root)
entry_asigurare_consumabile.grid(row=8, column=1)


calculate_button = tk.Button(root, text="Calculeaza", command=calculate_CIP1)
calculate_button.grid(row=9, column=0, columnspan=2)


label_result = tk.Label(root, text="Raspuns:")
label_result.grid(row=10, column=0, columnspan=2)

root.mainloop()