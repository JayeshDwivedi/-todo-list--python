import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to delete a selected task
def delete_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to save tasks to a file
def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Success", "Tasks saved successfully!")

# Function to load tasks from a file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for task in file.readlines():
                task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No saved tasks found.")

# Create the main application window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x450")

# UI Elements
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
save_button.pack()

load_button = tk.Button(root, text="Load Tasks", command=load_tasks)
load_button.pack()

# Run the Tkinter event loop
root.mainloop()
