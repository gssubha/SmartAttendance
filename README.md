# Smart Attendance System 🎓📋

Smart Attendance System is a Python‑based solution that automates classroom check‑in by capturing and recognizing student faces via webcam, then logging the exact date and time of each arrival. Administrators access a secure dashboard to start recognition, view and filter records, export data, and manage backups—all with minimal manual effort.

---

## Key Benefits

- 🤖 **Hands‑free attendance** marking in real time  
- ⏰ **Precise time‑stamp** for each entry  
- 🔒 **Secure admin** login, logout and session timeout  
- 📊 **Built‑in viewer** with filtering and export features  
- 💾 **Automatic, timestamped backups** for data integrity  

---

## Core Tools & Libraries

- **OpenCV**  
  Image capture and video processing  
- **face_recognition** (dlib + NumPy)  
  Face encoding and matching  
- **CSV + datetime**  
  Attendance logging  
- **Tkinter + ttk**  
  Graphical dashboards and alert dialogs  
- **os, shutil, subprocess**  
  File operations and script orchestration  

---

## Components at a Glance

| File                         | Functionality                                             | Identifier |
|------------------------------|-----------------------------------------------------------|-------|
| `capture_faces.py`           | Capture 10 clear images per student                       | 📸    |
| `face_recognition_module.py` | Load images and generate numeric face encodings           | 🎯    |
| `recognize_faces.py`         | Real‑time detection, recognition and attendance trigger   | 🤖    |
| `mark_attendance.py`         | Append unique “Name, Date, Time” entries to `attendance.csv` | 📝    |
| `view_attendance.py`         | GUI table to view and filter all records                  | 📋    |
| `export_attendance.py`       | Create timestamped backups in `backup/` directory         | 💾    |
| `smart_attendance_gui.py`    | Unified admin login + dashboard with logout & timeout     | 🛠️    |
| `attendance.csv`             | Master log of all marked attendance                       | 📁    |
| `backup/`                    | Contains daily CSV backups named by date + time           | 📂    |

---

## Flow of Operation

[Admin Login]

↓

[Capture Faces] → [Encode & Store]

↓

[Start Recognition] → [Detect Face] → [Match Encoding]

↓

[Mark Attendance] → [Append CSV]

↓

[View/Filter Records] ↔ [Export Data]

↓

[Automatic Backup]


---

## System Requirements & Setup

- **Python 3.9 or 3.10** (for dlib compatibility)  
- A working USB or built‑in webcam  
- Install dependencies via pip:

```bash
pip install opencv-python face_recognition dlib numpy tkinter
```
---
![Screenshot 2025-07-06 003508](https://github.com/user-attachments/assets/036f61cf-3dcf-4f73-9e87-c4f4571d3f5c)
---
![Screenshot 2025-07-06 003533](https://github.com/user-attachments/assets/706c459b-c434-419a-899a-4fae9c1d7c3c)
---
![Screenshot 2025-07-06 003704](https://github.com/user-attachments/assets/5b6c8a29-9829-487f-b0e3-e2f8b545fc37)
---
![Screenshot 2025-07-06 003726](https://github.com/user-attachments/assets/1a77207b-526f-4eab-900a-e15dd7625fb1)
