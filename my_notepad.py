import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename

def saving_file():
    file_location = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"),("All Files", "*.*")])
    if not file_location:
        return
    with open(file_location,"w") as file_output:
        text = text_edit.get(1.0, tk.END)
        file_output.write(text)
    gou.title(f"Notepad Clone - {file_location}")

def opening_file():
    file_location = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not file_location:
        return
    text_edit.delete(1.0, tk.END)
    with open(file_location, "r") as file_input:
        text = file_input.read()
        text_edit.insert(tk.END, text)
    gou.title(f"Notepad Clone - {file_location}")

gou=tk.Tk()
gou.title("Notepad Clone")
gou.rowconfigure(0, minsize=540)
gou.columnconfigure(1, minsize=540)

text_edit= tk.Text(gou)
text_edit.grid(row=0, column=1, sticky="nsew")

frame_button= tk.Frame(gou, relief=tk.RAISED, bd=4)
frame_button.grid(row=0, column=0, sticky="ns")

button_open= tk.Button(frame_button, text="Open File", command = opening_file)
button_open.grid(row=0, column=0, padx=5, pady=5)

button_save= tk.Button(frame_button, text="Save As", command = saving_file)
button_save.grid(row=1, column=0, padx=5)


gou.mainloop()