import tkinter as tk
from tkinter import filedialog

def recherche_mot(file_path, mot):
    lignes_trouvees = []
    try:
        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                if mot.lower() in line.lower():
                    lignes_trouvees.append(line_num)
        return lignes_trouvees
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")
        return []

def rechercher():
    mot_a_rechercher = entry_mot.get()
    if mot_a_rechercher:
        file_path = filedialog.askopenfilename()
        if file_path:
            print(f"Fichier sélectionné: {file_path}")
            lignes_trouvees = recherche_mot(file_path, mot_a_rechercher)
            afficher_resultats(lignes_trouvees)
    else:
        print("Veuillez entrer un mot à rechercher.")

def afficher_resultats(lignes_trouvees):
    result_window = tk.Toplevel(root)
    result_window.title("Résultats de la recherche")

    if lignes_trouvees:
        result_label = tk.Label(result_window, text=f"Le mot a été trouvé aux lignes suivantes : {', '.join(map(str, lignes_trouvees))}")
        result_label.pack(padx=20, pady=20)
    else:
        result_label = tk.Label(result_window, text="Le mot n'a pas été trouvé dans le fichier.")
        result_label.pack(padx=20, pady=20)

# Interface graphique
root = tk.Tk()
root.title("Recherche de mot dans un fichier")
root.geometry('600x500')

entry_mot = tk.Entry(root, width=40)
entry_mot.pack(pady=10)

btn_search = tk.Button(root, text="Rechercher", command=rechercher)
btn_search.pack(pady=20)

root.mainloop()
