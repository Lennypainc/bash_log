import tkinter as tk
from tkinter import filedialog, Text

def search_str(file_path, text):
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if (text) in content:
            print('string exist in a file')
        else:
            print('string does not exist in a file')

root = tk.Tk()
root.title("File Dialog Example")

#mettre une zone de texte étitable sur la fenetre pour ecrire error et voir si le code marche

text = Text(root, height=2)
text.pack()

def retrieve_input():
    text = form.get('1.0','end-1c')
    return text 

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Select a File", initialdir= '/home/lenny/Documents/script/python', filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        selected_file_label.config(text=f"Selected File: {file_path}")
        process_file(file_path)

def process_file(file_path):
    # Implement your file processing logic here
    # For demonstration, let's just display the contents of the selected file
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            file_text.delete('1.0', tk.END)
            file_text.insert(tk.END, file_contents)
    except Exception as e:
        selected_file_label.config(text=f"Error: {str(e)}")


open_button = tk.Button(root, text="Open File", command=open_file_dialog)
open_button.pack(padx=20, pady=20)

open_button = tk.Button(root, text="search", command=search_str)
open_button.pack(padx=20, pady=20)

selected_file_label = tk.Label(root, text="Selected File:")
selected_file_label.pack()

file_text = tk.Text(root, wrap=tk.WORD, height=10, width=40)
file_text.pack(padx=20, pady=20)

root.mainloop()

search_str(file_text, 'text')


