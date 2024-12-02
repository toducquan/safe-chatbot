import os
from datetime import datetime

BASE_PATH = "logs"
LOG_FILE = "chatbot_log.txt"


def log_chat_history(user_id, sentence):
    date_folder = datetime.now().strftime("%Y%m%d")
    time_stamp = datetime.now().strftime("%H:%M:%S")

    folder_path = os.path.join(BASE_PATH, date_folder)

    os.makedirs(folder_path, exist_ok=True)
    log_file_path = os.path.join(folder_path, LOG_FILE)

    with open(log_file_path, "a") as log_file:
        log_file.write(f"{time_stamp} {user_id}: {sentence}\n")
