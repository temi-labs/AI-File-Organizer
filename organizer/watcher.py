from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
from .classifier import classify_file
from .mover import move_file
from config import WATCH_FOLDER

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        file_name = os.path.basename(event.src_path)
        category = classify_file(file_name)
        move_file(WATCH_FOLDER, file_name, category)

def start_watching():
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_FOLDER, recursive=False)

    observer.start()
    print("Watching folder:", WATCH_FOLDER)

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
