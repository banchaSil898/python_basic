from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
#pip install watchdog for these package to work

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_any_event(self, event):
        new_name = "new_file_" + str(self.i) + ".txt"
        print("on_any_event")
        for filename in os.listdir(folder_to_track):
            file_exists = os.path.isfile(folder_destination + "\\" + new_name)
            while file_exists:
                self.i+= 1
                new_name = "new_file_" + str(self.i) + ".txt"
                file_exists = os.path.isfile(folder_destination + "\\" + new_name)

            src = folder_to_track + "\\" + filename
            new_destination = folder_destination + "\\" + new_name
            print(src)
            print(new_destination)
            os.rename(src, new_destination)
    
    def on_created(self, event):
        print("on_created")
    
    def on_modified(self, event):
        print("on_modified")

    def on_moved(self, event):
        print("on_moved")

    def on_deleted(self, event):
        print("on_deleted")

folder_to_track = "D:\\test\\source"
folder_destination = "D:\\test\\destination"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive = True)
observer.start()

print("let's do it!!")
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    print("except!!!")
    observer.stop()
observer.join()
            