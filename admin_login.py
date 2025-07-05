import tkinter as tk
from tkinter import messagebox
import subprocess

# === Globals for windows ===
login_window = None
dashboard = None

# === Admin Credentials ===
def verify_login(username, password):
    # TODO: Replace with secure credential storage
    return username == "admin" and password == "admin123"

# === Launch external scripts ===
def launch_script(script_name):
    subprocess.Popen(["python", f"{script_name}.py"])

# === Logout / Return to Login ===
def do_logout():
    global dashboard, login_window
    if dashboard:
        dashboard.destroy()
    # Clear the login entries
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    login_window.deiconify()  # show login window again
    username_entry.focus_set()

# === Show the Dashboard ===
def show_dashboard():
    global dashboard, login_window
    # Hide login window
    login_window.withdraw()

    dashboard = tk.Toplevel()
    dashboard.title("Smart Attendance System – Admin Panel")
    dashboard.geometry("500x400")
    dashboard.configure(bg="#f0f0f0")

    tk.Label(dashboard, text="Admin Dashboard",
             font=("Helvetica", 20, "bold"), bg="#f0f0f0").pack(pady=20)

    tk.Button(dashboard, text="➕ Capture Faces", width=25,
              command=lambda: launch_script("capture_faces"),
              bg="#4caf50", fg="white").pack(pady=10)

    tk.Button(dashboard, text="📸 Recognize Faces", width=25,
              command=lambda: launch_script("recognize_faces"),
              bg="#2196f3", fg="white").pack(pady=10)

    tk.Button(dashboard, text="📄 View Attendance", width=25,
              command=lambda: launch_script("view_attendance"),
              bg="#ff9800", fg="white").pack(pady=10)

    tk.Button(dashboard, text="⬇️ Export Attendance", width=25,
              command=lambda: launch_script("export_attendance"),
              bg="#9c27b0", fg="white").pack(pady=10)

    tk.Button(dashboard, text="🚪 Logout", width=10,
              command=do_logout, bg="red", fg="white").place(x=10, y=10)

    # Session auto‐timeout after 5 minutes
    dashboard.after(300_000, do_logout)

# === Handle Login Button ===
def do_login():
    user = username_entry.get().strip()
    pwd  = password_entry.get().strip()
    if verify_login(user, pwd):
        show_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# === Build Login Window ===
login_window = tk.Tk()
login_window.title("Admin Login")
login_window.geometry("300x180")
login_window.configure(bg="white")

tk.Label(login_window, text="Username", bg="white").pack(pady=(20, 5))
username_entry = tk.Entry(login_window)
username_entry.pack()
username_entry.focus_set()

tk.Label(login_window, text="Password", bg="white").pack(pady=5)
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

tk.Button(login_window, text="Login", width=20,
          command=do_login).pack(pady=15)

login_window.mainloop()
