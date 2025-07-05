import os
import shutil
from datetime import datetime

def export_attendance():
    source_file = "attendance.csv"
    backup_dir = "backup"

    # Create backup folder if it doesn't exist
    os.makedirs(backup_dir, exist_ok=True)

    # Create a timestamped backup filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(backup_dir, f"attendance_backup_{timestamp}.csv")

    try:
        shutil.copy(source_file, backup_file)
        print(f"[INFO] Backup created: {backup_file}")
    except FileNotFoundError:
        print("[ERROR] 'attendance.csv' not found.")
    except Exception as e:
        print(f"[ERROR] Failed to export backup: {e}")

# For testing
if __name__ == "__main__":
    export_attendance()
