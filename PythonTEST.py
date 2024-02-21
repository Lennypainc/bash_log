#!/bin/python3
import tkinter as tk
from tkinter import filedialog


file_path = None  # variable du chemin du fichier
show_total_occurrence = None  # BooleanVar for checkbox
result_label = None  # Label to display results

def create_boolean_var():
    global show_total_occurrence
    show_total_occurrence = tk.BooleanVar()
    show_total_occurrence.set(True)  # Initialize the checkbox state to True

def recherche_mot(mot):
    global file_path
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
    global file_path, result_label
    mot_a_rechercher = entry_mot.get()
    if mot_a_rechercher:
        if file_path is None:
            file_path = filedialog.askopenfilename()
            if not file_path:
                return  # User canceled file selection
            print(f"Fichier sélectionné: {file_path}")

        total_occurrences, occurrences_info = recherche_mot(mot_a_rechercher)
        afficher_resultats(total_occurrences, occurrences_info)
    else:
        print("Veuillez entrer un mot à rechercher.")

def changer_dossier():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        print(f"Nouveau fichier sélectionné: {file_path}")

def afficher_resultats(total_occurrences, occurrences_info):
    global result_label
    result_label.pack_forget()  # Forget previous result label

    if occurrences_info and not show_total_occurrence.get():
        result_text = ""
        for group in occurrences_info:
            result_text += f"Le mot a été trouvé {group['count']} fois de la ligne {group['start_line']} à la ligne {group['start_line'] + group['count'] - 1}.\n"
    elif show_total_occurrence.get():
        result_text = f"Le mot a été trouvé {total_occurrences} fois dans le fichier {file_path}."

    result_label = tk.Label(root, text=result_text)
    result_label.pack(padx=20, pady=10)

# Interface graphique
root = tk.Tk()
root.title("Recherche de mot dans un fichier")
root.geometry('600x500')
root.configure(bg='#4fd5ed')

entry_mot = tk.Entry(root, width=40)
entry_mot.pack(pady=10)

btn_search = tk.Button(root, text="Rechercher", command=rechercher)
btn_search.pack(pady=10)

btn_change_folder = tk.Button(root, text="Changer de fichier", command=changer_dossier)
btn_change_folder.pack(pady=10)

create_boolean_var()  # Create BooleanVar after root window is created
checkbox_show_total = tk.Checkbutton(root, text="Afficher le total d'occurrences", variable=show_total_occurrence)
checkbox_show_total.pack(padx=20, pady=10)  # Checkbox in the main window

result_label = tk.Label(root, text="")
result_label.pack(padx=20, pady=10)  # Initial empty label

root.mainloop()
