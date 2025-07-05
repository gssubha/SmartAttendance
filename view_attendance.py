import tkinter as tk
from tkinter import ttk
import csv

def load_attendance_data():
    data = []
    try:
        with open("attendance.csv", mode="r", newline='') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Skip header row
            for row in reader:
                data.append(row)
        return headers, data
    except FileNotFoundError:
        return ["Name", "Date", "Time"], []

def create_attendance_gui():
    headers, data = load_attendance_data()

    root = tk.Tk()
    root.title("Attendance Records")
    root.geometry("600x400")

    tree = ttk.Treeview(root, columns=headers, show="headings")

    # Set column headings
    for header in headers:
        tree.heading(header, text=header)
        tree.column(header, width=200)

    # Insert data into the table
    for row in data:
        tree.insert("", tk.END, values=row)

    tree.pack(fill=tk.BOTH, expand=True)
    root.mainloop()

if __name__ == "__main__":
    create_attendance_gui()
