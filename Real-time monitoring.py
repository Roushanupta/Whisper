from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class MediaFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        file_path = Path(event.src_path)
        if file_path.suffix.lower() in SUPPORTED_FORMATS:
            print(f"New file detected: {file_path}")
            transcribe_audio(file_path)

def monitor_directory(directory):
    observer = Observer()
    event_handler = MediaFileHandler()
    observer.schedule(event_handler, path=directory, recursive=True)
    
    observer.start()
    print(f"Monitoring {directory} for new media files...")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
