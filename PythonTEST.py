import tkinter as tk
from tkinter import filedialog

file_path = None  # variable du chemin du fichier


def recherche_mot(file_path, mot):
    occurrences_info = []
    current_group = {'start_line': 0, 'count': 0}
    total_occurrences = 0

    try:
        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                if mot.lower() in line.lower():
                    if current_group['count'] == 0:
                        current_group['start_line'] = line_num
                    current_group['count'] += 1
                    total_occurrences += 1
                elif current_group['count'] > 0:
                    occurrences_info.append(current_group)
                    current_group = {'start_line': 0, 'count': 0}

            if current_group['count'] > 0:
                occurrences_info.append(current_group)

        return total_occurrences, occurrences_info
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")
        return 0, []

def rechercher():
    global file_path
    mot_a_rechercher = entry_mot.get()
    if mot_a_rechercher:
        if file_path is None:
            file_path = filedialog.askopenfilename()
            if not file_path:
                return  # User canceled file selection
            print(f"Fichier sélectionné: {file_path}")

        total_occurrences, occurrences_info = recherche_mot(file_path, mot_a_rechercher)
        afficher_resultats(total_occurrences, occurrences_info)
    else:
        print("Veuillez entrer un mot à rechercher.")

def changer_dossier():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        print(f"Nouveau fichier sélectionné: {file_path}")
    
def afficher_resultats(total_occurrences, occurrences_info):
    result_window = tk.Toplevel(root)
    result_window.title("Résultats de la recherche")

    if occurrences_info:
        result_label_total = tk.Label(result_window, text=f"Le mot a été trouvé {total_occurrences} fois dans le fichier{file_path}.")
        result_label_total.pack(padx=20, pady=10)

        for group in occurrences_info:
            result_label_group = tk.Label(result_window, text=f"Le mot a été trouvé {group['count']} fois de la ligne {group['start_line']} à la ligne {group['start_line'] + group['count'] - 1}.")
            result_label_group.pack(padx=20, pady=5)
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
btn_search.pack(pady=10)

btn_change_folder = tk.Button(root, text="Changer de fichier", command=changer_dossier)
btn_change_folder.pack(pady=10)

root.mainloop()