import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

gou=tk.Tk()
gou.title("Notepad Clone")
gou.rowconfigure(0, minsize=540)
gou.columnconfigure(1, minsize=540)

text_edit= tk.Text(gou)
text_edit.grid(row=0, column=1)

frame_button= tk.Frame(gou, relief=tk.RAISED, bd=4)
frame_button.grid(row=0, column=0)

button_open= tk.Button(frame_button, text="Open File")
button_open.grid(row=0, column=0, padx=5, pady=5)

button_save= tk.Button(frame_button, text="Save As")
button_save.grid(row=1, column=0, padx=5)



gou.mainloop()