#this is the driver file that connects the backend code to the gui
import os
import htmlPy
import sys
from flask import flash
import PySide



# PySide.QtCore.Qt.FramelessWindowHint

#from PyQt4 import QtGui

# Initial confiurations
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# GUI initializations and settings
app = htmlPy.AppGUI(title=u"Application",developer_mode=True)
app.web_app.setMinimumWidth(480)
app.web_app.setMinimumHeight(650)
app.web_app.setMaximumHeight(800)
app.web_app.setMaximumHeight(480)

# app.web_app.update()
# app.maximized = True



# GUI configurations

# Folders location configuration
app.static_path = os.path.join(BASE_DIR, "static/")
app.template_path = os.path.join(BASE_DIR, "templates/")
importPath = os.path.join(BASE_DIR,"back_end_codes")
sys.path.append(importPath)

from content_management import Content
TOPIC_DICT = Content()



# app.window.setWindowFlags(PySide.QtCore.Qt.FramelessWindowHint)
# app.window.setWindowFlags(PySide.QtCore.Qt.WindowFullScreen)
# app.window.showFullScreen()
#app.window.setWindowIcon(QtGui.QIcon(BASE_DIR + "/static/img/icon.png"))

# app.template = ("index.html", TOPIC_DICT)

# Start Template
app.template = ("home.html", TOPIC_DICT)

# # Binding of back-end functionalities with GUI
# Import back-end functionalities
from backend_code import enroll , attendance , routing, attendancee, exam

# Bind and registering of  back-end functionalities
app.bind(enroll(app))
app.bind(exam(app))
app.bind(attendance(app))
app.bind(attendancee(app))
app.bind(routing(app))



# Instructions for running application

if __name__ == "__main__":
    # The driver file will have to be imported everywhere in back-end.
    # So, always keep app.start() in if __name__ == "__main__" conditional
    app.start()