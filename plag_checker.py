# Import necessary modules
import tkinter as tk
from tkinter import filedialog
import string
import re

# Create a new tkinter window
root = tk.Tk()
root.title("Plagiarism Checker")
root.configure(bg="#7EBEEB")

# Function to open file dialog and select file 1
def open_file1():  
    filepath = filedialog.askopenfilename()
    file1_entry.delete(0, tk.END)
    file1_entry.insert(0, filepath)

# Function to open file dialog and select file 2
def open_file2():
    filepath = filedialog.askopenfilename()
    file2_entry.delete(0, tk.END)
    file2_entry.insert(0, filepath)

# Function to clean text by removing punctuation and spaces and converting to lowercase
def clean_text(text):
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", "", text)
    return text.lower()

# Function to view the content of a selected file in a new window
def view_file_content(filepath):
    with open(filepath, "r") as file:
        file_content = file.read()
    file_content_window = tk.Toplevel()
    file_content_window.title("File Content")
    file_content_label = tk.Label(file_content_window, text=file_content)
    file_content_label.pack()

# Function to compare the contents of two selected files for plagiarism
def compare_files():
    file1_path = file1_entry.get()
    file2_path = file2_entry.get()

    # Open and read the contents of the two files
    with open(file1_path, "r") as file1, open(file2_path, "r") as file2:
        file1_text = file1.read()
        file2_text = file2.read()

    # Clean the text of the two files
    file1_text = clean_text(file1_text)
    file2_text = clean_text(file2_text)

    # Calculate the similarity between the two files based on common characters
    if len(file1_text) == 0 or len(file2_text) == 0:
        result_label.config(text="Error: One or both files are empty.")
    else:
        common_chars = set(file1_text) & set(file2_text)
        similarity = (len(common_chars) / len(file1_text)) * 100

        # Update the result label with the similarity percentage and color code based on level of similarity
        if similarity < 30:
            result_label.config(text=f"Similarity: {similarity:.2f}%", bg="#a7c957")
        elif similarity >= 30 and similarity <= 60:
            result_label.config(text=f"Similarity: {similarity:.2f}%", bg="#f77f00")
        else:
            result_label.config(text=f"Similarity: {similarity:.2f}%", bg="#c9184a")

# Create labels and buttons for the tkinter window
title_label = tk.Label(root, text="Plagiarism Checker", font=("Calibri", 28), fg="#333333", bg="#7EBEEB")
title_label.grid(row=0, column=0, columnspan=6, pady=(50, 20))

file1_label = tk.Label(root, text="File 1:", font='Caliberi 19',bg="#7EBEEB")
file1_label.grid(row=1, column=0,pady=25,columnspan=2)

file1_entry = tk.Entry(root,width=50)
file1_entry.grid(row=2, column=0,padx=50,pady=50,columnspan=2)

file1_button = tk.Button(root, text="Select File", command=open_file1,font='Caliberi 14')
file1_button.grid(row=3, column=0)

view_file1_button = tk.Button(root, text="View Content",font='Caliberi 14', command=lambda: view_file_content(file1_entry.get()))
view_file1_button.grid(row=3, column=1,padx=10,pady=15)



file2_label = tk.Label(root, text="File 2:", font='Caliberi 19',bg="#7EBEEB")
file2_label.grid(row=1, column=3,pady=25,columnspan=2)

file2_entry = tk.Entry(root, width=50)
file2_entry.grid(row=2, column=3,padx=50,pady=50,columnspan=2)

file2_button = tk.Button(root, text="Select File", command=open_file2,font='Caliberi 14')
file2_button.grid(row=3, column=3)

view_file2_button = tk.Button(root, text="View Content",font='Caliberi 14', command=lambda: view_file_content(file2_entry.get()))
view_file2_button.grid(row=3, column=4, padx=10,pady=15)

compare_button = tk.Button(root, text="Compare Files", command=compare_files,font='Caliberi 14')
compare_button.grid(row=4, column=2,padx=50,pady=50)



result_label = tk.Label(root, text=" ",font='Caliberi 20 bold', bg='red')
result_label.grid(row=5, column=2,padx=10,pady=50)

#run the program
root.mainloop()
