import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkcalendar import DateEntry
import sqlite3
import psutil

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Process Logger")

        # Create GUI components
        self.tree = ttk.Treeview(self, columns=('timestamp', 'app_name', 'pid'), show='headings', height=20)
        self.tree.heading('timestamp', text='Timestamp')
        self.tree.heading('app_name', text='App Name')
        self.tree.heading('pid', text='PID')

        self.tree.pack(padx=10, pady=10)

        # Date entry fields using DateEntry widget
        self.start_date_label = tk.Label(self, text="Start Date:")
        self.start_date_label.pack()
        self.start_date_entry = DateEntry(self)
        self.start_date_entry.pack()

        self.end_date_label = tk.Label(self, text="End Date:")
        self.end_date_label.pack()
        self.end_date_entry = DateEntry(self)
        self.end_date_entry.pack()

        # Refresh button
        self.refresh_button = tk.Button(self, text="Refresh", command=self.refresh_logs)
        self.refresh_button.pack(pady=5)

        # Initialize the SQLite database
        self.init_database()

        # Initialize the log display
        self.refresh_logs()

    def init_database(self):
        # Connect to SQLite database (or create if it doesn't exist)
        self.connection = sqlite3.connect('process_logs.db')

        # Create a cursor object to execute SQL queries
        self.cursor = self.connection.cursor()

        # Create a table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS process_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                app_name TEXT,
                pid INTEGER
            )
        ''')

        # Commit changes and close the connection
        self.connection.commit()

    def log_running_processes(self):
        logs = []
        for process in psutil.process_iter(['pid', 'name']):
            log_entry = {
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'app_name': process.info['name'],
                'pid': process.info['pid']
            }
            logs.append(log_entry)

        # Insert logs into the database
        self.cursor.executemany('''
            INSERT INTO process_logs (timestamp, app_name, pid)
            VALUES (:timestamp, :app_name, :pid)
        ''', logs)

        # Commit changes to the database
        self.connection.commit()

    def refresh_logs(self):
        try:
            # Retrieve logs from the database within the specified date range
            start_date = self.start_date_entry.get_date()
            end_date = self.end_date_entry.get_date()

            # Convert dates to strings in the format 'YYYY-MM-DD'
            start_date_str = start_date.strftime('%Y-%m-%d')
            end_date_str = end_date.strftime('%Y-%m-%d')

            # Modify the query to use LIKE with '%'
            query = 'SELECT * FROM process_logs WHERE timestamp LIKE ?'
            self.cursor.execute(query, (f'%{start_date_str}%',))
            logs = self.cursor.fetchall()

            if not logs:
                print("No logs found in the specified date range.")

            # Clear existing logs in the GUI
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Display logs in the GUI
            for log_entry in logs:
                self.tree.insert('', 'end', values=(log_entry[1], log_entry[2], log_entry[3]))
        except Exception as e:
            print(f"Error retrieving logs: {e}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
