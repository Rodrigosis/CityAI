import os
import subprocess
from watchdog.observers import Observer  # type: ignore
from watchdog.events import FileSystemEventHandler  # type: ignore


class ChangeHandler(FileSystemEventHandler):
    def __init__(self, process):
        self.process = process

    def on_any_event(self, event):
        # Reinicia a aplicação quando qualquer arquivo for modificado
        self.process.kill()
        self.process = subprocess.Popen(["python", "main.py"])

if __name__ == "__main__":
    # Inicializa a aplicação pela primeira vez
    process = subprocess.Popen(["python", "main.py"])
    
    # Configura o observador do Watchdog
    event_handler = ChangeHandler(process)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
        process.kill()

    observer.join()
