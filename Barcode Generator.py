"""
August 2023
Author: Rambod Azimi

How to use:
1. Enter the numbers you want to convert into barcodes, separated by spaces.
2. Choose the barcode type from the available options (EAN13, EAN8, CODE128, etc.).
3. Click the "Generate Barcodes" button to initiate the barcode generation process.

Features:
Supports multiple barcode types: EAN13, EAN8, CODE128, and more.
Fast and efficient barcode generation for multiple numbers.
Barcodes are automatically saved in the "Downloads" folder for easy access.
"""

import os
import barcode
from barcode import generate
from barcode.writer import ImageWriter
import tkinter as tk
from tkinter import filedialog

# This functions inputs a list of numbers (string type) and the barcode type, and generates the image file (png) in the Downloads folder
def generate_barcode(numbers, barcode_type):
    try:
        barcode_class = barcode.get_barcode_class(barcode_type) # Selecting the barcode type

        downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')  # Setting the path

        for number in numbers: # iterate over all the list of numbers

            code = barcode_class(number, writer=ImageWriter())

            # Generate the barcode image and save it in the "Downloads" folder
            filename = f'{barcode_type}_{number}'
            full_path = os.path.join(downloads_path, f"{filename}")
            code.save(full_path)

            print(f"Barcode generated: {full_path}")

        tk.messagebox.showinfo("Barcode Generator", "Barcodes generated successfully!")
    except barcode.errors.BarcodeNotFoundError:
        tk.messagebox.showerror("Barcode Generator", "Selected barcode type not supported.")

# Action button function
def generate_button_click():
    numbers_input = numbers_entry.get()
    numbers = numbers_input.split()
    barcode_type = barcode_type_entry.get()

    generate_barcode(numbers, barcode_type)

root = tk.Tk()
root.title("Barcode Generator")

headline_label = tk.Label(root, text="Barcode Generator", font=("Helvetica", 16, "bold"))
headline_label.pack(pady=10)

numbers_label = tk.Label(root, text="Enter the numbers separated by spaces:")
numbers_label.pack()
numbers_entry = tk.Entry(root, width=50)
numbers_entry.pack()

barcode_type_label = tk.Label(root, text="Enter the barcode type (EAN13, EAN8, CODE128, etc.):")
barcode_type_label.pack()
barcode_type_entry = tk.Entry(root, width=50)
barcode_type_entry.pack()

generate_button = tk.Button(root, text="Generate Barcodes", command=generate_button_click)
generate_button.pack(pady=10)

description_label = tk.Label(root, text="Please enter numbers separated by spaces, and select the barcode type. Then, you images are ready in your Downloads folder!")
description_label.pack(pady=10)

developer_label = tk.Label(root, text="Designed and developed by Rambod Azimi")
developer_label.pack(pady=5)

# Main
root.mainloop()
