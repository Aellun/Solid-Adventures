import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import sqlite3 as sql

def main():
    root = tk.Tk()
    root.title("TASK MANAGEMENT APPLICATION")
    root.resizable(True, True)
    root.geometry("1000x600+750+250")
    root.bind('<Return>', lambda event=None: add_task())

    header_frame = tk.Frame(root, bg="#FAEBD7")
    functions_frame = tk.Frame(root, bg="#FAEBD7")
    functions_frame.pack(side='left', expand=True, fill='both')
    header_frame.pack(side='top', fill='both')

    listbox_frame = tk.Frame(root, bg="#FAEBD7")
    listbox_frame.pack(side='right', expand=True, fill='both')

    header_label = tk.Label(
        header_frame,
        text="My Tasks",
        font=("Helvetica", "25"),
        background="#FAEBD7",
        foreground="#B9D9EB"
    )
    header_label.pack(padx=10, pady=10)

    task_label = tk.Label(
        functions_frame,
        text="Enter Task:",
        font=("Consolas", "11", "bold"),
        background="#FAEBD7",
        foreground="#000000",    
    )
    task_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

    task_entry = tk.Entry(
        functions_frame,
        font=("Consolas", "12"),
        width=24,
        background="#FFF8DC",
        foreground="#A52A2A"
    )
    task_entry.focus_set()
    task_entry.grid(row=0, column=1, padx=5, pady=5, sticky='e')

    date_label = tk.Label(
        functions_frame,
        text="Select Date:",
        font=("Consolas", "11", "bold"),
        background="#FAEBD7",
        foreground="#000000"
    )
    date_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')

    date_entry = DateEntry(
        functions_frame,
        font=("Consolas", "12"),
        width=16,
        background="#FFF8DC",
        foreground="#A52A2A"
    )
    date_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')

    time_label = tk.Label(
        functions_frame,
        text="Select Time:",
        font=("Consolas", "11", "bold"),
        background="#FAEBD7",
        foreground="#000000"
    )
    time_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')

    time_values = ['12:00 AM', '12:30 AM', '1:00 AM', '1:30 AM', '2:00 AM', '2:30 AM', '3:00 AM', '3:30 AM',
                   '4:00 AM', '4:30 AM', '5:00 AM', '5:30 AM', '6:00 AM', '6:30 AM', '7:00 AM', '7:30 AM',
                   '8:00 AM', '8:30 AM', '9:00 AM', '9:30 AM', '10:00 AM', '10:30 AM', '11:00 AM', '11:30 AM',
                   '12:00 PM', '12:30 PM', '1:00 PM', '1:30 PM', '2:00 PM', '2:30 PM', '3:00 PM', '3:30 PM',
                   '4:00 PM', '4:30 PM', '5:00 PM', '5:30 PM', '6:00 PM', '6:30 PM', '7:00 PM', '7:30 PM',
                   '8:00 PM', '8:30 PM', '9:00 PM', '9:30 PM', '10:00 PM', '10:30 PM', '11:00 PM', '11:30 PM']
    time_combobox = ttk.Combobox(
        functions_frame,
        values=time_values,
        font=("Consolas", "12"),
        width=16,
    )
    time_combobox.grid(row=2, column=1, padx=10, pady=10, sticky='w')

    tasks = []

    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('DROP TABLE IF EXISTS my_to_do')
    the_cursor.execute('CREATE TABLE my_to_do (todo TEXT, todate TEXT, totime TEXT)')

    def add_task(event=None):
        task_string = task_entry.get()
        selected_date = date_entry.get()
        selected_time = time_combobox.get()
        if len(task_string) == 0 or not selected_date or not selected_time:
            messagebox.showinfo('Error', 'Field Empty.')
        else:
            tasks.append((task_string, selected_date, selected_time))
            the_cursor.execute('INSERT INTO my_to_do VALUES (?, ?, ?)', (task_string, selected_date, selected_time))
            the_connection.commit()
            list_update()
            task_entry.delete(0, 'end')

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
                the_cursor.execute('DELETE FROM my_to_do WHERE todo = ?', (the_value,))
                the_connection.commit()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def delete_all_tasks():
        message_box = messagebox.askyesno('Delete all', 'Are you sure?')
        if message_box == True:
            while (len(tasks) != 0):
                tasks.pop()
            the_cursor.execute('DELETE FROM my_to_do')
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
        for row in the_cursor.execute('SELECT todo FROM my_to_do'):
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
    add_button.place(x=120, y=200)
    del_button.place(x=120, y=250)
    del_all_button.place(x=120, y=300)
    exit_button.place(x=120, y=350)

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
