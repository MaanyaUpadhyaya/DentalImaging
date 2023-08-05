import tkinter as tk
from tkinter import filedialog

def button_clicked():
    file_path = filedialog.askopenfilename()
    if file_path:
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, file_path)
        show_remaining_widgets()

def show_remaining_widgets():
    label2.grid(row=0, column=0, padx=10, pady=10)
    radio_yes.grid(row=0, column=1, padx=10, pady=10)
    radio_no.grid(row=0, column=2, padx=10, pady=10)
    button.grid(row=1, column=5, sticky="ns")

def hide_remaining_widgets():
    label2.grid_remove()
    radio_yes.grid_remove()
    radio_no.grid_remove()
    button.grid_remove()


root = tk.Tk()
root.title("Demo")


label1 = tk.Label(root, text="Select the Patient's Folder")
label1.grid(row=1, column=0)
text_area = tk.Text(root, height=3, width=30)
text_area.grid(row=1, column=1, columnspan=3, sticky="ew")

label2 = tk.Label(root, text="Do you want to select the patient?")
radio_var = tk.StringVar()  
radio_var.set("")

radio_yes = tk.Radiobutton(root, text="Yes", variable=radio_var, value="Yes", command=show_remaining_widgets)
radio_no = tk.Radiobutton(root, text="No", variable=radio_var, value="No", command=hide_remaining_widgets)

button = tk.Button(root, text="...", command=button_clicked)


show_remaining_widgets()

root.mainloop()
