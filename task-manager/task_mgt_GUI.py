import tkinter as tk
from tkinter import messagebox

def main():
    root = tk.Tk()
    root.title("TASK MANAGER")  # the window title
    
    # the size of window on display
    root.geometry("500x700")
    # creating a label-- this is like header of the page and styling it
    label = tk.Label(root, text="My do To List", font=('Courier', 18))
    label.pack(padx=28, pady=28)
    label.config(fg="#0000FF")
    label.config(bg="Antique white")


    # Entry widget for adding tasks
    entry = tk.Entry(root, width=40)
    entry.pack(pady=20)

    # Listbox for displaying tasks
    listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
    listbox.pack()

    # Buttons for adding and deleting tasks
    add_button = tk.Button(root, text="Add Task", command=add_task)
    add_button.pack(pady=5)

    delete_button = tk.Button(root, text="Delete Task", command=delete_task)
    delete_button.pack(pady=5)

    root.mainloop()

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)  # Clear the entry widget
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")



if __name__ == "__main__":
    main()
