import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkcalendar import DateEntry
import sqlite3 as sql
from tkinter import ttk

# Function to define and run the main application
def main():
    # Create the main Tkinter window
    root = tk.Tk()
    root.title("TASK MANAGEMENT APPLICATION")
    root.configure(bg="#2E2E2E")  # Set the background color to a dark

    root.resizable(True, True)
    root.geometry("1000x700+750+250")
    root.bind('<Return>', lambda event=None: add_task())

    # Create the main frame container
    frame_container = tk.Frame(root, bg="#FAEBD7")
    frame_container.pack(side='left', expand=True, fill='both')

    header_frame = tk.Frame(frame_container, bg="#CC7722")
    functions_frame = tk.Frame(frame_container, bg="#DCD7A0")
    #listbox_frame = tk.Frame(functions_frame, bg="#FAEBD7")

    header_frame.pack(side='top', fill='both', pady=10)
    functions_frame.pack(side='bottom', expand=True, fill='both')

    frame_container.grid_columnconfigure(0, weight=1)  # Make column 0 resizable
    frame_container.grid_rowconfigure(0, weight=1)  # Make row 0 resizable
    functions_frame.grid_columnconfigure(0, weight=1)  # Make column 0 resizable
    functions_frame.grid_columnconfigure(1, weight=1)  # Make column 1 resizable
    functions_frame.grid_rowconfigure(0, weight=1)  # Make row 0 resizable
    functions_frame.grid_rowconfigure(1, weight=1)  # Make row 1 resizable
    functions_frame.grid_rowconfigure(2, weight=1)  # Make row 2 resizable

    # Header Label
    header_label = tk.Label(
        header_frame,
        text="My to do list",
        font=("Helvetica", "18"),
        background="#CC7722",
        foreground="#B9D9EB"
    )
    header_label.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky='ew')

    # Frame for task-related widgets
    frame_task = tk.Frame(
        functions_frame,
        borderwidth=2,
        relief="groove",
        background="#FAEBD7"
    )
    frame_task.grid(row=1, column=0, rowspan=1, padx=40, pady=40, sticky='w', columnspan=2)

     # Labels and Entry Widgets for Task Entry
    task_label = tk.Label(
        frame_task,
        text="Enter Task:",
        font=("Consolas", "11", "bold"),
        background="#FAEBD7",
        foreground="#000000",
    )
    task_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

    task_entry = tk.Entry(
        frame_task,
        font=("Consolas", "12"),
        width=16,
        background="#FFF8DC",
        foreground="#A52A2A"
    )
    task_entry.focus_set()
    task_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

    date_label = tk.Label(
        frame_task,
        text="Select Date:",
        font=("Consolas", "11", "bold"),
        background="#FAEBD7",
        foreground="#000000"
    )
    date_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')

    date_entry = DateEntry(
        frame_task,
        font=("Consolas", "12"),
        width=16,
        background="#FFF8DC",
        foreground="#A52A2A"
    )
    date_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')

    time_label = tk.Label(
        frame_task,
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
        frame_task,
        values=time_values,
        font=("Consolas", "12"),
        width=16,
    )
    time_combobox.grid(row=2, column=1, padx=10, pady=10, sticky='w')

    tasks = []
    completed_tasks = []

    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('create table if not exists my_to_do (todo text, todate text, totime text)')

    def add_task(event=None):
        task_string = task_entry.get()
        selected_date = date_entry.get()
        selected_time = time_combobox.get()
        if len(task_string) == 0 or not selected_date or not selected_time:
            messagebox.showinfo('Error', 'Field Empty.')
        else:
            tasks.append((task_string, selected_date, selected_time))
            the_cursor.execute('insert into my_to_do values(?, ?, ?)', (task_string, selected_date, selected_time))
            the_connection.commit()
            list_update()
            task_entry.delete(0, 'end')

    def mark_as_completed(view_listbox):
        try:
            selected_index = int(view_listbox.curselection()[0])
            selected_task = tasks[selected_index - 1]
            
            completed_tasks.append(selected_task)
            tasks.pop(selected_index - 1)

            the_cursor.execute('delete from my_to_do where rowid=?', (selected_index,))
            the_connection.commit()

            list_update(view_listbox)
            list_update()
        except (IndexError, ValueError):
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def view_completed_tasks():
        completed_window = tk.Toplevel(root)
        completed_window.title("Completed Tasks")

        completed_listbox = tk.Listbox(
            completed_window,
            width=45,
            height=13,
            background="#FFFFFF",
            foreground="#000000",
            selectbackground="#CD853F",
            selectforeground="#FFFFFF"
        )
        completed_listbox.pack(padx=10, pady=10)

        completed_listbox.insert('end', 'Task          Date             Time')
        completed_listbox.insert('end', '-' * 45)
        for index, task in enumerate(completed_tasks, start=1):
            completed_listbox.insert('end', f"{index}. {task[0]:<14}{task[1]:<17}{task[2]}")


    def view_tasks():
        view_window = tk.Toplevel(root)
        view_window.title("View Tasks")

        view_listbox = tk.Listbox(
            view_window,
            width=45,
            height=13,
            background="#FFFFFF",
            foreground="#000000",
            selectbackground="#CD853F",
            selectforeground="#FFFFFF"
        )
        view_listbox.pack(padx=10, pady=10)

        view_listbox.insert('end', 'Task          Date             Time')
        view_listbox.insert('end', '-' * 45)
        for index, task in enumerate(tasks, start=1):
            view_listbox.insert('end', f"{index}. {task[0]:<14}{task[1]:<17}{task[2]}")

        modify_button = tk.Button(
            view_window,
            text="Modify Task",
            width=24,
            command=lambda: modify_task(tasks, view_listbox, the_cursor, the_connection)
        )
        modify_button.pack(pady=10)

        mark_completed_button = tk.Button(
            view_window,
            text="Mark as Completed",
            width=24,
            command=lambda: mark_as_completed(view_listbox)
        )
        mark_completed_button.pack(pady=10)

    def modify_task(tasks, view_listbox, the_cursor, the_connection):
        try:
            selected_index = int(view_listbox.curselection()[0])
            selected_task = tasks[selected_index - 1]

            modify_window = tk.Toplevel(root)
            modify_window.title("Modify Task")

            tk.Label(
                modify_window,
                text="Task:",
                font=("Consolas", "11", "bold"),
                background="#FAEBD7",
                foreground="#000000",
            ).grid(row=0, column=0, padx=10, pady=10, sticky='w')

            modified_task_entry = tk.Entry(
                modify_window,
                font=("Consolas", "12"),
                width=24,
                background="#FFF8DC",
                foreground="#A52A2A"
            )
            modified_task_entry.insert(0, selected_task[0])
            modified_task_entry.grid(row=0, column=1, padx=5, pady=5, sticky='E')

            tk.Label(
                modify_window,
                text="Select Date:",
                font=("Consolas", "11", "bold"),
                background="#FAEBD7",
                foreground="#000000"
            ).grid(row=1, column=0, padx=10, pady=10, sticky='w')

            modified_date_entry = DateEntry(
                modify_window,
                font=("Consolas", "12"),
                width=16,
                background="#FFF8DC",
                foreground="#A52A2A"
            )
            modified_date_entry.set_date(selected_task[1])
            modified_date_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')

            tk.Label(
                modify_window,
                text="Select Time:",
                font=("Consolas", "11", "bold"),
                background="#FAEBD7",
                foreground="#000000"
            ).grid(row=2, column=0, padx=10, pady=10, sticky='w')

            modified_time_combobox = ttk.Combobox(
                modify_window,
                values=time_values,
                font=("Consolas", "12"),
                width=16,
            )
            modified_time_combobox.set(selected_task[2])
            modified_time_combobox.grid(row=2, column=1, padx=10, pady=10, sticky='w')

            update_button = tk.Button(
                modify_window,
                text="Update Task",
                width=24,
                command=lambda: update_task(selected_index, modified_task_entry.get(),
                                            modified_date_entry.get(), modified_time_combobox.get(),
                                            view_listbox, modify_window)
            )
            update_button.grid(row=3, columnspan=2, pady=10)

        except (IndexError, ValueError):
            messagebox.showwarning("Warning", "Please select a task to modify.")

    def update_task(selected_index, modified_task, modified_date, modified_time, view_listbox, modify_window):
        tasks[selected_index - 1] = (modified_task, modified_date, modified_time)
        the_cursor.execute('update my_to_do set todo=?, todate=?, totime=? where rowid=?',
                           (modified_task, modified_date, modified_time, selected_index))
        the_connection.commit()
        list_update(view_listbox)
        modify_window.destroy()

    def list_update(view_listbox=None):
        clear_list(view_listbox)
        for index, task in enumerate(tasks, start=1):
            if view_listbox:
                view_listbox.insert('end', f"{index}. {task[0]:<14}{task[1]:<17}{task[2]}")
            else:
                task_listbox.insert('end', task)

    def delete_task():
        try:
            selected_index = int(task_listbox.curselection()[0])
            selected_task = tasks[selected_index - 1]

            tasks.remove(selected_task)
            list_update()
            the_cursor.execute('delete from my_to_do where rowid=?', (selected_index,))
            the_connection.commit()
        except (IndexError, ValueError):
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def delete_all_tasks():
        message_box = messagebox.askyesno('Delete all', 'Are you sure?')
        if message_box == True:
            while (len(tasks) != 0):
                tasks.pop()
            the_cursor.execute('delete from my_to_do')
            the_connection.commit()
            list_update()

    def clear_list(view_listbox=None):
        if view_listbox:
            view_listbox.delete(0, 'end')
        else:
            task_listbox.delete(0, 'end')

    def clear_screen(view_listbox=None):
        if view_listbox:
            view_listbox.delete(0, 'end')
        else:
            task_listbox.delete(0, 'end')
            
    def close():
        root.destroy()

    def retrieve_database():
        while (len(tasks) != 0):
            tasks.pop()
        for row in the_cursor.execute('select todo, todate, totime from my_to_do'):
            tasks.append(row)

    # enclose all buttons on the function_frame
    frame_buttons = tk.Frame(
        functions_frame,
        borderwidth=2,
        relief="groove",
        background="#FAEBD7"
    )
    frame_buttons.grid(row=2, column=0, padx=10, pady=10, sticky='w', columnspan=2)

    add_button = tk.Button(
        frame_buttons,
        text="Add Task",
        width=32,
        command=add_task
    )
    del_button = tk.Button(
        frame_buttons,
        text="Delete Task",
        width=32,
        command=lambda: delete_task()
    )
    del_all_button = tk.Button(
        frame_buttons,
        text="Delete All Tasks",
        width=32,
        command=delete_all_tasks
    )
    view_button = tk.Button(
        frame_buttons,
        text="View Tasks",
        width=32,
        command=view_tasks
    )
    completed_button = tk.Button(
        frame_buttons,
        text="View Completed Tasks",
        width=32,
        command=view_completed_tasks
    )
    exit_button = tk.Button(
        frame_buttons,
        text="Exit",
        width=32,
        command=close
    )
    clear_screen_button = tk.Button(
        frame_buttons,
        text="Clear Screen",
        width=32,
        command=lambda: clear_screen()
    )

    # placing each button on the function_frame
    add_button.grid(row=0, column=0, padx=20, pady=20)
    del_button.grid(row=0, column=1, padx=10, pady=10)
    del_all_button.grid(row=2, column=0, padx=10, pady=10)
    view_button.grid(row=2, column=1, padx=10, pady=10)
    exit_button.grid(row=3, column=1, padx=10, pady=10)
    clear_screen_button.grid(row=3, column=0, padx=10, pady=10)
    completed_button.grid(row=4, column=0, padx=10, pady=10)
    
    task_listbox_frame = ttk.Frame(
    functions_frame,
    style="TFrame",
)
    task_listbox_frame.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    # listbox containing the task entered
    task_listbox = tk.Listbox(
    task_listbox_frame,
    width=35,
    height=15,
    selectmode='SINGLE',
    background="#EBF6F7",
    foreground="#000000",
    selectbackground="#CD853F",
    selectforeground="#FFFFFF"
)
    task_listbox.pack(padx=5, pady=5)


    retrieve_database()
    list_update()

    the_connection.commit()

    # Run the Tkinter main loop
    root.mainloop()
    the_cursor.close()

# Entry point for the script
if __name__ == "__main__":
    main()
