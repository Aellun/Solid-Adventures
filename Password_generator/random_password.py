import tkinter as tk
from tkinter import messagebox
import secrets
import string
import json
import pyperclip

# File to store password data
PASSWORDS_FILE = "passwords.json"

# Function to load passwords from the file
def load_passwords_from_file():
    try:
        with open(PASSWORDS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Load existing passwords from file
passwords_data = load_passwords_from_file()

# Button style
button_style = {'bg': '#E3B778', 'fg': 'white'}

def generate_password():
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    selection_list = letters + digits + special_chars

    # Get the desired password length from the scale widget
    password_len = password_length_scale.get()

    # the for loop for logic to generate password string
    while True:
        password = ''
        for i in range(password_len):
            password += ''.join(secrets.choice(selection_list))
        # the password string must satisfy the following conditions
        if any(char in special_chars for char in password) and sum(char in digits for char in password) >= 2:
            break

    # Get the website or application name from the entry widget
    website_name = website_entry.get()

     # Check if the name is provided
    if not website_name:
        messagebox.showerror("Error", "Please provide a name before generating a password.")
        return  # Stop execution if the name is not provided

    # Store the generated password in the dictionary
    passwords_data[website_name] = password

    # Update the password label and show a message box
    password_label.config(text=f"Password for {website_name}: {password}")
    messagebox.showinfo("Generated Password", f"Password for {website_name}: {password}")

def save_passwords_to_file():
    '''this function writes the password
    and its corresponding application to json file'''
    with open(PASSWORDS_FILE, "w") as file:
        json.dump(passwords_data, file)
    
    # Clear the entry widget
    website_entry.delete(0, 'end')

    # Clear the password label
    password_label.config(text="")

def delete_password(app_name):
    # Delete the password entry for the specified application
    if app_name in passwords_data:
        del passwords_data[app_name]

        # Save the changes immediately
        save_passwords_to_file()

        # Update the view window to reflect the changes
        view_saved_passwords()

def copy_password(app_name, password):
    # Copy the password to the clipboard
    pyperclip.copy(password)
    messagebox.showinfo("Password Copied", f"Password for {app_name} copied to clipboard.")

def view_saved_passwords():
    if hasattr(view_saved_passwords, 'view_window') and view_saved_passwords.view_window:
        # Destroy the existing view window if it exists
        view_saved_passwords.view_window.destroy()

    # Create a new window to display saved passwords
    view_window = tk.Toplevel(window)
    view_window.title("View Passwords")

    # Set the geometry for the "View Passwords" window
    view_window.geometry("500x310")

    # Set the background color for the "View Passwords" window
    view_window.configure(bg="#C9BB8E")

    # Create labels for 'app name' and 'password'
    app_name_label = tk.Label(view_window, text="App Name", font=("Helvetica", 12, "bold"))
    app_name_label.grid(row=0, column=0, padx=10, pady=5)

    password_label = tk.Label(view_window, text="Password", font=("Helvetica", 12, "bold"))
    password_label.grid(row=0, column=1, padx=10, pady=5)

    copy_label = tk.Label(view_window, text="Copy", font=("Helvetica", 12, "bold"))
    copy_label.grid(row=0, column=2, padx=10, pady=5)

    delete_label = tk.Label(view_window, text="Delete", font=("Helvetica", 12, "bold"))
    delete_label.grid(row=0, column=3, padx=10, pady=5)

    # Display saved passwords in three columns
    row_num = 1
    for app_name, password in passwords_data.items():
        tk.Label(view_window, text=app_name).grid(row=row_num, column=0, padx=10, pady=5)
        tk.Label(view_window, text=password).grid(row=row_num, column=1, padx=10, pady=5)
        # Add a button to copy the password to the clipboard
        copy_button = tk.Button(view_window, text="Copy", command=lambda a=app_name, p=password: copy_password(a, p), **button_style)
        copy_button.grid(row=row_num, column=2, padx=10, pady=5)
        delete_button = tk.Button(view_window, text="Delete", command=lambda a=app_name: delete_password(a), **button_style)
        delete_button.grid(row=row_num, column=3, padx=10, pady=5)  # Change column index to 3

        row_num += 1

    # Store the reference to the current view window in the function attribute
    view_saved_passwords.view_window = view_window

# Load passwords from file at the beginning
load_passwords_from_file()

# the main window
window = tk.Tk()
window.title("Password Generator")

# Set the geometry for the main window
window.geometry("350x350")

# Set a dark background for the main window
window.configure(bg="#C9BB8E")

# Create an entry widget for the application name
website_entry_label = tk.Label(window, text="Name:")
website_entry_label.pack(pady=5)

website_entry = tk.Entry(window)
website_entry.pack(pady=5)

# Create a Scale widget for password length
password_length_label = tk.Label(window, text="Password Length:", font=("Helvetica", 12, "bold"), bg="#C9BB8E")
password_length_label.pack(pady=5)

password_length_scale = tk.Scale(window, from_=6, to=20, orient=tk.HORIZONTAL, length=200, bg="#C9BB8E")
password_length_scale.set(12)  # Set default length to 12
password_length_scale.pack(pady=10)

# button to generate the password
generate_button = tk.Button(window, text="Generate Password", command=generate_password, **button_style)
generate_button.pack(pady=10)

# Create buttons to save and view passwords
save_button = tk.Button(window, text="Save Passwords", command=save_passwords_to_file, **button_style)
save_button.pack(pady=5)

view_button = tk.Button(window, text="View Passwords", command=view_saved_passwords, **button_style)
view_button.pack(pady=5)

# Create a label to display the generated password
password_label = tk.Label(window, text="")
password_label.pack(pady=10)

# Start the GUI event loop
window.mainloop()
