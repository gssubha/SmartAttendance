import tkinter as tk
import subprocess
from export_attendance import export_attendance

def launch_recognition():
    subprocess.Popen(["python", "recognize_faces.py"])

def launch_view():
    subprocess.Popen(["python", "view_attendance.py"])

def export_data():
    export_attendance()

root = tk.Tk()
root.title("Smart Attendance Dashboard")
root.geometry("300x200")

tk.Button(root, text="Start Face Recognition", command=launch_recognition, width=30).pack(pady=10)
tk.Button(root, text="View Attendance", command=launch_view, width=30).pack(pady=10)
tk.Button(root, text="Export Attendance", command=export_data, width=30).pack(pady=10)

root.mainloop()
