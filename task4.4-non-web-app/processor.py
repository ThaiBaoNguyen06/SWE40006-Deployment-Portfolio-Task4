import os
import time
from datetime import datetime

DATA_DIR = "/app/data"
LOG_FILE = os.path.join(DATA_DIR, "activity.log")

os.makedirs(DATA_DIR, exist_ok=True)

print("SWE40006 Task 4.4 - Non-Web Docker Application")
print("Student: Thai Bao Nguyen")
print("Service started successfully.")

while True:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"{timestamp} - Background processing completed successfully."

    print(message)

    with open(LOG_FILE, "a") as file:
        file.write(message + "\n")

    time.sleep(10)