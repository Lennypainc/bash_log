import tkinter as tk
from tkinter import filedialog

def recherche_mot(file_path, mot):
    occurrences_info = {'count': 0, 'lines': []}
    try:
        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                if mot.lower() in line.lower():
                    occurrences_info['count'] += 1
                    occurrences_info['lines'].append(line_num)
        return occurrences_info
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")
        return {'count': 0, 'lines': []}

def rechercher():
    mot_a_rechercher = entry_mot.get()
    if mot_a_rechercher:
        file_path = filedialog.askopenfilename()
        if file_path:
            print(f"Fichier sélectionné: {file_path}")
            occurrences_info = recherche_mot(file_path, mot_a_rechercher)
            afficher_resultats(occurrences_info)
    else:
        print("Veuillez entrer un mot à rechercher.")

def afficher_resultats(occurrences_info):
    result_window = tk.Toplevel(root)
    result_window.title("Résultats de la recherche")

    if occurrences_info['count'] > 0:
        result_label = tk.Label(result_window, text=f"Le mot a été trouvé {occurrences_info['count']} fois dans le fichier.")
        result_label.pack(padx=20, pady=10)

        if occurrences_info['count'] > 1:
            lines_label = tk.Label(result_window, text=f"Il apparaît aux lignes suivantes : {', '.join(map(str, occurrences_info['lines']))}")
            lines_label.pack(padx=20, pady=10)
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
