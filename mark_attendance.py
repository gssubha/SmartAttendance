import csv
from datetime import datetime
import os

def mark_attendance(name, filename='Attendance.csv'):
    now = datetime.now()
    date_str = now.strftime('%d-%m-%Y')
    time_str = now.strftime('%H:%M:%S')

    # Check if file exists
    file_exists = os.path.isfile(filename)

    # Read existing records to prevent duplicate entries
    already_marked = set()
    if file_exists:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            for row in reader:
                if row and row[0] == name and row[1] == date_str:
                    already_marked.add(name)

    # Mark attendance if not already marked today
    if name not in already_marked:
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Name', 'Date', 'Time'])  # Header
            writer.writerow([name, date_str, time_str])
            print(f"[INFO] Attendance marked for {name} at {time_str}")
    else:
        print(f"[INFO] {name} is already marked present today.")
