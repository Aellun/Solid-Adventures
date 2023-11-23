import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql

def main():
    root = tk.Tk()
    root.title("TASK MANAGEMENT APPLICATION")
    root.resizable(0,0)
    root.geometry("800x600+750+250")

    header_frame = tk.Frame(root, bg="#FAEBD7")
    functions_frame = tk.Frame(root, bg="#FAEBD7")
    functions_frame.pack(side='left', expand=True, fill='both')
    header_frame.pack(side ='top',fill='both')
    
    listbox_frame = tk.Frame(root, bg="#FAEBD7")
    listbox_frame.pack(side='right', expand=True, fill='both')

    header_label = tk.Label(
        header_frame,
        text="My To-Do List",
        font=("Helvetica", "25"),
        background="#FAEBD7",
        foreground="#B9D9EB"
    )
    header_label.pack(padx=6, pady=40)

    task_label = tk.Label(
        functions_frame,
        text="Enter the Task:",
        font=("Consolas", "11", "bold"),
        background="#FAEBD7",
        foreground="#000000"
    )
    task_label.place(x=30, y=60)

    task_entry = tk.Entry(
        functions_frame,
        font=("Consolas", "12"),
        width=24,
        background="#FFF8DC",
        foreground="#A52A2A"
    )
    task_entry.place(x=30, y=80)

    tasks = []

    # The database connection
    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('create table if not exists tasks (title text)')

    def add_task():
        task_string = task_entry.get()
        if len(task_string) == 0:
            messagebox.showinfo('Error', 'Field Empty.')
        else:
            tasks.append(task_string)
            the_cursor.execute('insert into tasks values(?)', (task_string,))
            the_connection.commit()
            list_update()
            task_entry.delete(0,'end')

    def list_update():
        clear_list()
        for task in tasks:
            task_listbox.insert('end', task)

    def delete_task():
        try:
            the_value = task_listbox.get(task_listbox.curselection())
            if the_value in tasks:
                tasks.remove(the_value)
                list_update()
                the_cursor.execute('delete from tasks where title = ?', (the_value,))
                the_connection.commit()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def delete_all_tasks():
        message_box = messagebox.askyesno('Delete all', 'Are you sure?')
        if message_box == True:
            while (len(tasks) != 0):
                tasks.pop()
            the_cursor.execute('delete from tasks')
            the_connection.commit()
            list_update()

    def clear_list():
        task_listbox.delete(0, 'end')

    def close():
        print(tasks)
        root.destroy()

    def retrieve_database():
        while (len(tasks) != 0):
            tasks.pop()
        for row in the_cursor.execute('select title from tasks'):
            tasks.append(row[0])

    add_button = tk.Button(
        functions_frame,
        text="Add Task",
        width=24,
        command=add_task
    )
    del_button = tk.Button(
        functions_frame,
        text="Delete Task",
        width=24,
        command=delete_task
    )
    del_all_button = tk.Button(
        functions_frame,
        text="Delete All Tasks",
        width=24,
        command=delete_all_tasks
    )
    exit_button = tk.Button(
        functions_frame,
        text="Exit",
        width=24,
        command=close
    )
    add_button.place(x=30, y=120)
    del_button.place(x=30, y=160)
    del_all_button.place(x=30, y=200)
    exit_button.place(x=30, y=240)

    task_listbox = tk.Listbox(
        listbox_frame,
        width=26,
        height=13,
        selectmode='SINGLE',
        background="#FFFFFF",
        foreground="#000000",
        selectbackground="#CD853F",
        selectforeground="#FFFFFF"
    )
    task_listbox.place(x=10, y=20)

    retrieve_database()
    list_update()

    the_connection.commit()
    

    root.mainloop()
    the_cursor.close()

if __name__ == "__main__":
    main()
