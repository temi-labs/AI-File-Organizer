import tkinter as tk
from tkinter import filedialog, messagebox
from organizer import organize_folder

selected_folder = None

def pick_folder():
    global selected_folder
    selected_folder = filedialog.askdirectory(title="Select a folder to organize")
    if selected_folder:
        folder_label.config(text=f"Selected: {selected_folder}")
        status.config(text="Idle")

def start():
    global selected_folder
    if not selected_folder:
        messagebox.showwarning("Warning", "Please select a folder first!")
        return
    
    status.config(text="Organizing...")
    try:
        organize_folder(selected_folder)
        status.config(text="Folder organized successfully!")
        messagebox.showinfo("Success", "Files organized successfully!")
    except Exception as e:
        status.config(text="Error occurred")
        messagebox.showerror("Error", f"Error: {str(e)}")

app = tk.Tk()
app.title("Smart File Organizer")
app.geometry("450x300")

title = tk.Label(app, text="AI File Organizer", font=("Arial", 18, "bold"))
title.pack(pady=15)

pick_btn = tk.Button(app, text="📁 Pick Folder", command=pick_folder, width=30, padx=10, pady=10)
pick_btn.pack(pady=10)

folder_label = tk.Label(app, text="No folder selected", font=("Arial", 10), fg="gray")
folder_label.pack(pady=5)

start_btn = tk.Button(app, text="🚀 Organize Files", command=start, width=30, padx=10, pady=10, bg="green", fg="white")
start_btn.pack(pady=10)

status = tk.Label(app, text="Idle", font=("Arial", 11))
status.pack(pady=15)

app.mainloop()
