from docx import Document
from docx.shared import Pt
import re
import os
import tkinter as tk
from tkinter import filedialog

def process_word_document(input_path, output_path):
    pass  # Placeholder for your code

def browse_input_file():
    filename = filedialog.askopenfilename()
    input_path_entry.delete(0, tk.END)
    input_path_entry.insert(0, filename)

def start_processing():
    input_path = input_path_entry.get()
    output_path = os.path.splitext(input_path)[0] + "_output.docx"
    process_word_document(input_path, output_path)

root = tk.Tk()

input_path_label = tk.Label(root, text="Input file:")
input_path_label.pack()

input_path_entry = tk.Entry(root, width=50)
input_path_entry.pack()

input_path_button = tk.Button(root, text="Browse...", command=browse_input_file)
input_path_button.pack()

start_button = tk.Button(root, text="Start processing", command=start_processing)
start_button.pack()

root.mainloop()