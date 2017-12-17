import json
import requests
import htmlPy
from fingerprint import fingerprint as f
import time

class enroll(htmlPy.Object):
    # GUI callable functions have to be inside a class.
    # The class should be inherited from htmlPy.Object.
########################################################################################################################

    def __init__(self,app_gui):
        super(enroll, self).__init__()
        self.app_gui = app_gui
        self.token= None
        # Initialize the class here, if required.
        return

########################################################################################################################

    @htmlPy.Slot(str, result=str)
    def login(self, json_data):
        
        url="http://127.0.0.1:5000/login"
        
        form_data = json.loads(json_data)
        print form_data
        print (json.dumps(form_data))

        try:
            r=requests.get(url,auth=(form_data['user'],form_data['password']))
        except Exception:
            self.app_gui.template = ("./login.html", {"errors": ["serverdown"]})
            
        if r.status_code == 200:
            hello=r.json()
            token=hello['token']
            self.token=token
            self.app_gui.template = ("./enroll.html", {"template_variable_name": "value"})
        else:
            self.app_gui.template = ("./login.html", {"errors": ["please check your username or password"]})

        return json.dumps(form_data)

########################################################################################################################

    @htmlPy.Slot(str, result=str)
    def enroll_function(self, json_data):
        url="http://localhost/api/student/enroll_find_student_fingerprint.php"
        # @htmlPy.Slot(arg1_type, arg2_type, ..., result=return_type)
        # This function can be used for GUI forms.
        form_data = json.loads(json_data)
        #this print the student id given by the client through the api
        print (json.dumps(form_data))

        if(form_data['student_id']==None):
            self.app_gui.template = ("./enroll.html", {"errors": [" Please enter a student id "]})

        try:
            #The following is the request to check if this student is already enrolled or no
            r = requests.post(url, data = json.dumps(form_data))
        except Exception:
            self.app_gui.template = ("./enroll.html", {"errors": ["Server down :(. Try again later. "]})
            
        hello=r.json()
        
        if( hello["message"] == None):

            if( hello["finger_print"]== None ):
                self.app_gui.template = ("./register_fingerprint.html", hello)
            else:
                self.app_gui.template = ("./enroll.html", {"errors": [" This student is already registered. "]})

        else:
            self.app_gui.template = ("./enroll.html", {"errors": [" The Student Id you entered is wrong. Please enter a correct one"]})
        
########################################################################################################################

    @htmlPy.Slot()
    def register_first(self):
        #creating a finger scanning instance by intiating the connection to the sensor
        self.finger= f()
        #getting the first scan of a fingerprint.
        if(self.finger.get_finger_template_first() == -1):
            self.app_gui.template = ("./enroll.html", {"errors": [" Please try putting your fingers better :) "]})
        #alerting the user to remove his finger
        return
########################################################################################################################

    @htmlPy.Slot()
    def sleep(self):
        time.sleep(4)
        return 
########################################################################################################################

    @htmlPy.Slot()
    def register_last(self):
        time.sleep(2)
        list=self.finger.get_finger_template_final()
        #if the fingerprint scanning returns 0 it means that the finger prints scanned are not similar and the user need to scan it again
        if(list==0):
            self.app_gui.template = ("./enroll.html", {"errors": [" Fingers doesn't match :) "]})
        # this means that there had been an unknown problem
        if(list== -1):
            self.app_gui.template = ("./enroll.html", {"errors": [" sorry there had been a problem :) "]})
        print list

        return
########################################################################################################################
    @htmlPy.Slot()
    def javascript_function(self):

        # Any function decorated with @htmlPy.Slot decorater can be called
        # using javascript in GUI

        print "mama helwa"
        return
