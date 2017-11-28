import htmlPy
import json
import os,sys

#This part helps in importing the main module from the parent directory by
#adding the directory the system path 
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
parentdir = os.path.dirname(BASE_DIR)
sys.path.append(parentdir)
print parentdir
print BASE_DIR

from main import app as htmlPy_app

class ClassName(htmlPy.Object):
    # GUI callable functions have to be inside a class.
    # The class should be inherited from htmlPy.Object.

    def __init__(self):
        super(ClassName. self).__init__()
        # Initialize the class here, if required.
        return

    @htmlPy.Slot()
    def function_name(self):
        # This is the function exposed to GUI events.
        # You can change app HTML from here.
        # Or, you can do pretty much any python from here.
        #
        # NOTE: @htmlPy.Slot decorater needs argument and return data-types.
        # Refer to API documentation.
        return

    @htmlPy.Slot(str, result=str)
    def form_function_name(self, json_data):
        # @htmlPy.Slot(arg1_type, arg2_type, ..., result=return_type)
        # This function can be used for GUI forms.
        #
        form_data = json.loads(json_data)
        return json.dumps(form_data)

    @htmlPy.Slot()
    def javascript_function(self):
        # Any function decorated with @htmlPy.Slot decorater can be called
        # using javascript in GUI
        return


## You have to bind the class instance to the AppGUI instance to be
## callable from GUI
# htmlPy_app.bind(ClassName())