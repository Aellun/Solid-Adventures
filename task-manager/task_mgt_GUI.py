import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql

def main():
    root = tk.Tk()
    root.title("TASK MANAGEMENT APPLICATION")  # the window title
    
    # the size of window on display
    root.geometry("500x700")
    # creating a label-- this is like header of the page and styling it
    label = tk.Label(root, text="My do To List", font=('Courier', 18))
    label.pack(padx=28, pady=28)
    label.config(fg="#0000FF")
    label.config(bg="Antique white")


    # Entry widget for adding tasks
    enter_task = tk.Label(root, text="Enter your task below", font=('Courier', 16))
    enter_task.pack(padx=10, pady=10)
    entry = tk.Entry(root, width=40)
    entry.pack(pady=20)

    # Listbox for displaying tasks
    tasks[]
    tasks = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
    tasks.pack()

    # Buttons for adding and deleting tasks
    add_button = tk.Button(root, text="Add Task", command=lambda: add_task(entry, tasks))
    add_button.pack(pady=5)

    delete_button = tk.Button(root, text="Delete Task", command=lambda: delete_task(tasks))
    delete_button.pack(pady=5)

    root.mainloop()

def add_task():
    #getting the string from the entry field
    task_string = task_field.get()
    #check if the string is empty or not
    if len(task_string) == 0:
    #display an error message if the string is empty
        messagebox > showinfo('Error field Empty.')
    else:
        #adding the string to the task list
        task.append(task_string)
        #the cursor execute method to excecute a sql statement
        the_cursor.execute('insert into tasks values(?)', (task_string,))
        list_update()
        task_field.delete(0, 'end')# deleting the entry in the entry field
        
        #listbox.insert(tk.END, task)
        #entry.delete(0, tk.END)  # Clear the entry widget
    #else:
        #messagebox.showwarning("Warning", "Please enter a task.")
def list_update():
    '''This function will update the list'''
    clear_list()  # calling the function to clear the list
    for task in tasks:
        task_listbox.insert('end',task)


def delete_task():
    ''' the delete_task function deletes the selected task from the
    list and database'''
    try:
        the_value = task_listbox.get(listbox > cursorselection())
        if the_value in tasks:
            tasks.remove(the_value)
            list_update()
            the_cursor.execute('delete from the tasks where title =?',(the_value))
        #selected_task_index = listbox.curselection()[0]
        #listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def delete_all_tasks():
    ''' function to delete all tasks from the list'''
    message_box = messagebox.askyesno('Delete all', 'Are you sure?')
    if message_box == = True:
        while (len(tasks) != 0):# Use the loop to iterate thru' the tasks list until its empty
            tasks.pop()  # Pop up the element from the list
        the_cursor.execute('delete from tasks')# Execute the sql statement
        list_update()

def clear_list():
    ''' The function to clear the list using the delete method'''
    task_listbox.delete(0,'end')

def close():
    ''' Function to close the application but prints the task before closing'''
    print(tasks)
    guiWindow.destroy()

def retrieve_database():
    ''' this is a function to retieve data from the database'''
    while (len(tasks) != 0):
        tasks.pop()
    for row in the_cursor.execute('select title from tasks'):
        tasks.append(row[0])# method to insert the titles from the table to the list


if __name__ == "__main__":
    main()
