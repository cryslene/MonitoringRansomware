import os
import pyinotify
import sys

x = 0
y = 0

class EventProcessor(pyinotify.ProcessEvent):
    _methods = ["IN_CREATE", "IN_OPEN", "IN_ACCESS", "IN_ATTRIB", "IN_CLOSE_NOWRITE",
                "IN_CLOSE_WRITE", "IN_DELETE", "IN_DELETE_SELF", "IN_IGNORED", "IN_MODIFY",
                "IN_MOVE_SELF", "IN_MOVED_FROM", "IN_MOVED_TO", "IN_Q_OVERFLOW", "IN_UNMOUNT",
                "default"]

def process_generator(cls, method):
    def _method_name(self, event):
        global x, y
        print("{} -> " "{} ".format(event.maskname, event.pathname))
        if (event.maskname == "IN_ACCESS"):
            x = x + 1          
        if (event.maskname == "IN_MODIFY"):
            y = y + 1
        if (x >= 1000 and y >=2000):
            print('''\n \n \n 
		---------------------------------------------------\n \n
			        RANSOMWARE DETECTED\n \n
		---------------------------------------------------
			\n \n \n ''')
            sys.exit() 
    _method_name.__name__ = "process_{}".format(method)
    setattr(cls, _method_name.__name__, _method_name)

for method in EventProcessor._methods:
    process_generator(EventProcessor, method)

watch_manager = pyinotify.WatchManager()
event_notifier = pyinotify.Notifier(watch_manager, EventProcessor())

watch_this = os.path.abspath("notification_dir")
watch_manager.add_watch("/home/user/projetostcc/ransomware/files", pyinotify.ALL_EVENTS)
event_notifier.loop()


