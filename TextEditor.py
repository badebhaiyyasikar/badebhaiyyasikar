import tkinter as tk
from tkinter import filedialog, massagebox

def new_file():
    text.delete(1.0, tk.END)

    def open_file():
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],)
        if file_path:
                with open(file_path, "r") as file:
                    text.delete(1.0, tk.END)
                    text.insert(tk.End, file.read())

    def save_file():
        file_path = filedialog.asksaveasfilename()
        if file_path:
            with open(file_path, "w") as file:
                file.write(text.get(1.0, tk.END))
def save_file():
    file_path = filedialog.asksaveasfilename( defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))
            massagebox.showinfo("Info", "file saved")

root = tk.Tk()
root.title("simple text  Editor - Badebhaiyya")
root.geometry("800x600")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
#file_menu.add_command(label="Open", command=Open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

text = tk.Text(root, Wrap=tk.word, font=("consolas", 12),fg="black", bg="white")
text.pack(expand=tk.YES, fill=tk.BOTH) 

root.mainloop()