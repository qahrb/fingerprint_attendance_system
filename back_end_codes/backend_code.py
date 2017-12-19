import json
import requests
import htmlPy
from fingerprint import fingerprint as f
import time
from ast import literal_eval

########################################################################################################################
########################################################################################################################
########################################################################################################################
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
            
        self.hello=r.json()
        print self.hello
        if( self.hello["message"] == None):

            if( self.hello["fingerprint_template"]== None ):
                self.app_gui.template = ("./register_fingerprint.html", self.hello)
            else:
                self.app_gui.template = ("./enroll.html", {"errors": [" This student is already registered. "]})

        else:
            self.app_gui.template = ("./enroll.html", {"errors": [" The Student Id you entered is wrong. Please enter a correct one"]})
        
########################################################################################################################

    @htmlPy.Slot()
    def register(self):
                            ##################################        
        url="http://localhost/api/student/enroll_add_student_fingerprint.php"
        #creating a finger scanning instance by intiating the connection to the sensor
        self.finger= f()
        #getting the first scan of a fingerprint.
        if(self.finger.get_finger_template_first() == -1):
            self.app_gui.template = ("./enroll.html", {"errors": [" Please try putting your fingers better :) "]})
        #alerting the user to remove his finger
        time.sleep(3)
        list=self.finger.get_finger_template_final()
        #if the fingerprint scanning returns 0 it means that the finger prints scanned are not similar and the user need to scan it again
        if(list==0):
            self.app_gui.template = ("./enroll.html", {"errors": [" Fingers doesn't match :) "]})
        # this means that there had been an unknown problem
        if(list== -1):
            self.app_gui.template = ("./enroll.html", {"errors": [" sorry there had been a problem :) "]})
                            ##################################
        #in the following the list is being added to a dictionary function so it can be sended as a json string to the server
        # print list
        fingerprint_template={'fingerprint_template':json.dumps(list)}
        
        #now we are adding the student's dictonary definations to the fingerprint defination so it could be sent to the server 
        z = dict(self.hello.items() + fingerprint_template.items())
        # print json.dumps(z)
                            ##################################
        try:
            #The following is the request to check if this student is already enrolled or no
            r = requests.post(url, data = json.dumps(z))
        except Exception:
            self.app_gui.template = ("./enroll.html", {"errors": ["Server down :( . Try again later. "]})
        print r.content

        hello=r.json()
                             ##################################       
        if( hello["message"] == "finger Print was recorded." ):
            self.app_gui.template =  ("./enroll.html", {"successes": [" Fingerprint registered sucessfully "]})
        else:
            self.app_gui.template = ("./enroll.html", {"errors": [" Some errors on the server side occured.<br>Please try again later."]})

        return 

########################################################################################################################
########################################################################################################################
########################################################################################################################
class attendance(htmlPy.Object):
    
    def __init__(self,app_gui):
        super(attendance, self).__init__()
        self.app_gui = app_gui
        self.token= None
        # Initialize the class here, if required.
        return

    @htmlPy.Slot(str, result=str)
    def test(self, json_data):
        url="http://localhost/api/student/enroll_find_student_fingerprint.php"
        # @htmlPy.Slot(arg1_type, arg2_type, ..., result=return_type)
        # This function can be used for GUI forms.
        form_data = json.loads(json_data)
        #this print the student id given by the client through the api
        print (json.dumps(form_data))

        if(form_data['student_id']==None):
            self.app_gui.template = ("./test.html", {"errors": [" Please enter a student id "]})

        try:
            #The following is the request to check if this student is already enrolled or no
            r = requests.post(url, data = json.dumps(form_data))
        except Exception:
            self.app_gui.template = ("./test.html", {"errors": ["Server down :(. Try again later. "]})

        hello=r.content
        hello= json.loads(hello)
        print type(hello["fingerprint_template"].encode('utf-8'))
        #literal eval is used to change the string from the template and in a python list
        print literal_eval(hello["fingerprint_template"])
        print type(literal_eval(hello["fingerprint_template"]))

        if( hello["message"] == None):

            if( hello["fingerprint_template"]== None ):
                self.app_gui.template = ("./test.html", {"errors": [" This student fingerprint is not registered. "]})
            else:
                
                finger= f()
                test=finger.student_finger_test(literal_eval(hello["fingerprint_template"]))
                #if the fingerprint scanning returns 0 it means that the finger prints scanned are not similar and the user need to scan it again
                if(test==1):
                    self.app_gui.template= ("./test.html",{"successes":["Yay it works!!! :) "]})
                if(test==0):
                    self.app_gui.template = ("./test.html", {"errors": [" Fingers doesn't match :)<br>Try licking your finger"]})
                # this means that there had been an unknown problem
                if(test== -1):
                    self.app_gui.template = ("./test.html", {"errors": [" sorry there had been a problem :) "]})

            

        else:
            self.app_gui.template = ("./enroll.html", {"errors": [" The Student Id you entered is wrong. Please enter a correct one"]})

########################################################################################################################
########################################################################################################################
########################################################################################################################
#routing class for the links in the app
class routing(htmlPy.Object):
    
    def __init__(self,app_gui):

        super(routing, self).__init__()
        self.app_gui = app_gui
        self.token= None
        # Initialize the class here, if required.
        return

########################################################################################################################

    @htmlPy.Slot(str, result=str)
    def home(self, json_data):
    
        form_data = json.loads(json_data)

        if(form_data['route']=="enroll"):
            self.app_gui.template = ("./enroll.html", { })

        if(form_data['route']=="attendance"):
            self.app_gui.template = ("./attendance.html", { })

        if(form_data['route']=="test"):
            self.app_gui.template = ("./test.html", { })
    
        return 
########################################################################################################################    

    @htmlPy.Slot(str, result=str)
    def header(self, json_data):
    
        form_data = json.loads(json_data)

        print form_data['route']
        if(form_data['route']=="home"):
            self.app_gui.template = ("./home.html", { })

        return 

########################################################################################################################
########################################################################################################################
########################################################################################################################