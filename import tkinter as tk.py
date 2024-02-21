import tkinter as tk

def on_checkbox_click():
    if checkbox_var.get():
        print("Checkbutton is checked")
    else:
        print("Checkbutton is unchecked")


# Create a Tkinter variable to hold the state of the Checkbutton
checkbox_var = tk.IntVar()

# Create the Checkbutton and associate it with the variable
checkbox = tk.Checkbutton(root, text="Check", variable=checkbox_var, command=on_checkbox_click)

# Pack the Checkbutton into the window
checkbox.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
