import tkinter as tk
from tkinter import filedialog

def open_file_explorer():
    root = tk.Tk()
    root.withdraw() 
    file_path = filedialog.askopenfilename()
    return file_path

patient_name = input("Enter the patient name: ")
print("Patient name:", patient_name)

selected_file = open_file_explorer()
print("Selected file:", selected_file)
