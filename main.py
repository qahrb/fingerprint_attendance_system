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

# GUI initializations
app = htmlPy.AppGUI(title=u"Application",developer_mode=True)
# app.maximized = True



# GUI configurations
app.static_path = os.path.join(BASE_DIR, "static/")
app.template_path = os.path.join(BASE_DIR, "templates/")
importPath = os.path.join(BASE_DIR,"back_end_codes")
sys.path.append(importPath)
from content_management import Content
TOPIC_DICT = Content()

app.web_app.setMinimumWidth(300)
app.web_app.setMinimumHeight(500)

# app.window.setWindowFlags(PySide.QtCore.Qt.FramelessWindowHint)
# app.window.setWindowFlags(PySide.QtCore.Qt.WindowFullScreen)
# app.window.showFullScreen()
#app.window.setWindowIcon(QtGui.QIcon(BASE_DIR + "/static/img/icon.png"))

# app.template = ("index.html", TOPIC_DICT)
app.template = ("enroll.html", TOPIC_DICT)

# # Binding of back-end functionalities with GUI
# Import back-end functionalities
from backend_code import enroll

# Register back-end functionalities
app.bind(enroll(app))


# Instructions for running application

if __name__ == "__main__":
    # The driver file will have to be imported everywhere in back-end.
    # So, always keep app.start() in if __name__ == "__main__" conditional
    app.start()