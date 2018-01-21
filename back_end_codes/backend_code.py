import json
import PySide.QtCore as q
import PySide.QtWebKit as w

import requests
import htmlPy
from fingerprint import fingerprint as f
import time
import datetime
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
        
        if(form_data['student_id']== u''):
            self.app_gui.template = ("./enroll.html", {"errors": [" Please enter a student id "]})
            return

        try:
            #The following is the request to check if this student is already enrolled or no
            r = requests.post(url, data = json.dumps(form_data))

            self.hello=r.json()
            print self.hello
            if( self.hello["message"] == None):

                if( self.hello["fingerprint_template"]== None ):
                    self.app_gui.template = ("./register_fingerprint.html", self.hello)
                    return
                else:
                    self.app_gui.template = ("./enroll.html", {"errors": [" This student is already registered. "]})
                    return

            else:
                self.app_gui.template = ("./enroll.html", {"errors": [" The Student Id you entered is wrong. Please enter a correct one"]})
                return
        except Exception:
            self.app_gui.template = ("./enroll.html", {"errors": ["Server down :(. Try again later. "]})
            return

########################################################################################################################

    @htmlPy.Slot()
    def register(self):
                            ##################################        
        url="http://localhost/api/student/enroll_add_student_fingerprint.php"
        #creating a finger scanning instance by intiating the connection to the sensor
        self.finger= f()
        #getting the first scan of a fingerprint.
        if(self.finger.get_finger_template_first() == -1):
            self.app_gui.template = ("./enroll.html", {"errors": [" Please try putting your finger better :) "]})
        
        #alerting the user to remove his finger
        # most important thing in the code
        self.app_gui.evaluate_javascript("myFunction1();")

        die_time=q.QTime.currentTime().addSecs(3)
        while q.QTime.currentTime() < die_time:
            q.QCoreApplication.processEvents(q.QEventLoop.AllEvents,100)
        
        time.sleep(3)
        def h():
            print "hello world"

        # this function waits for change to happen in the url to stop further progress in the function
        if self.app_gui.web_app.urlChanged:
            return
        
        #alerting the user to remove his finger
        # most important thing in the code
        self.app_gui.evaluate_javascript("myFunction2();")

        die_time=q.QTime.currentTime().addSecs(1)
        while q.QTime.currentTime() < die_time:
            q.QCoreApplication.processEvents(q.QEventLoop.AllEvents,100)

        if self.app_gui.web_app.urlChanged:
            return

        list=self.finger.get_finger_template_final()
        print "this is the list contents"
        print list
        #if the fingerprint scanning returns 0 it means that the finger prints scanned are not similar and the user need to scan it again
        if(list==0):
            self.app_gui.template = ("./enroll.html", {"errors": [" Fingers doesn't match :) "]})
            return
        # this means that there had been an unknown problem
        if(list== -1):
            self.app_gui.template = ("./enroll.html", {"errors": [" sorry there had been a problem :) "]})
            return
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
            return
        print r.content

        hello=r.json()
                             ##################################       
        if( hello["message"] == "finger Print was recorded." ):
            self.app_gui.template =  ("./enroll.html", {"successes": [" Fingerprint registered sucessfully "]})
            return
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
        self.lectures_array= None
        self.admins_array=None
        self.current_attendance=None
        self.current_time=None
        self.lecture_time=None
        self.url="http://localhost/api/student/attendance.php"
        self.test = 0
        # Initialize the class here, if required.
        return

########################################################################################################################

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
                    return
                if(test==0):
                    self.app_gui.template = ("./test.html", {"errors": [" Fingers doesn't match :)<br>Try licking your finger"]})
                    return
                # this means that there had been an unknown problem
                if(test== -1):
                    self.app_gui.template = ("./test.html", {"errors": [" sorry there had been a problem :) "]})
                    return

            

        else:
            self.app_gui.template = ("./enroll.html", {"errors": [" The Student Id you entered is wrong. Please enter a correct one"]})
            return

########################################################################################################################

    import json
import PySide.QtCore as q
import PySide.QtWebKit as w
import requests
import htmlPy
from fingerprint import fingerprint as f
import time
import datetime
from ast import literal_eval

class attendance(htmlPy.Object):
    
    def __init__(self,app_gui):
        super(attendance, self).__init__()
        self.app_gui = app_gui
        self.token= None
        self.lectures_array= None
        self.admins_array=None
        self.current_attendance=None
        self.current_time=None
        self.lecture_time=None
        self.today=None
        self.url="http://localhost/api/student/attendance.php"
        self.start = 0
        self.lectures_array_edited=[]
        self.time_for_lecture=0
        # Initialize the class here, if required.
        return

    @htmlPy.Slot()
    def attendance_main(self):
        ###############################
        if not self.start:
            self.start=1
            #get the time in alphabetical form
            self.today = datetime.datetime.now()
            
            ###############################
            # please edit this part for saturdays and sundays
            #js = {"day":today.strftime("%a"),"location":"CMPE001"}
            js = {"day":"MON","location":"CMPE001"}
            ###############################
            # try:
                #The following is the request to get attendance data for today
            self.current_attendance = requests.post(self.url, json.dumps(js))
            self.current_attendance = json.loads(self.current_attendance.content)
            # print self.current_attendance
            self.lectures_array= self.current_attendance["records"]
            for lecture in self.lectures_array:
                self.current_time = datetime.datetime.now()
                for key in lecture.keys():
                    if(key != u"instrcutors"):
                        time= key
                        # remove the colon from the time unicode string
                        time=time.replace(":","")
                        # time is in unicode
                        # this line changes time from unicode to ascii
                        time=time.encode('ascii','ignore')
                        # put the recieved time in the time format needed
                        self.lecture_time = self.current_time.replace(hour=int(time[0:2]), minute=int(time[3:5]))
                        self.lectures_array_edited.append(self.lecture_time)

        ###############################
        self.today = datetime.datetime.now().day
        if self.today != datetime.datetime.now().day:
            self.today = datetime.datetime.now()
            # js = {"day":self.today.strftime("%a"),"location":"CMPE001"}
            js = {"day":"MON","location":"CMPE001"}
            self.current_attendance = requests.post(self.url, json.dumps(js))
            self.current_attendance = json.loads(self.current_attendance.content)
            self.lectures_array= self.current_attendance["records"]
            for lecture in self.lectures_array:
                self.current_time = datetime.datetime.now()
                for key in lecture.keys():
                    if(key != u"instrcutors"):
                        time= key
                        time=time.replace(":","")
                        time=time.encode('ascii','ignore')
                        self.lecture_time = self.current_time.replace(hour=int(time[0:2]), minute=int(time[3:5]))
                        self.lectures_array_edited.append(self.lecture_time)

        self.current_time = datetime.datetime.now()
        # for the time being
        self.current_time= self.current_time.replace(hour=11)
        for lecture in self.lectures_array_edited:
            if self.current_time >= lecture   and self.current_time <= (lecture + datetime.timedelta(hours=2) ):
                self.time_for_lecture=1
                self.lecture_time= lecture
                break
            else:
                self.time_for_lecture=0

        if self.time_for_lecture:
            print "hello"
        else:
            return    
        
        ###############################
        
        

                    # print self.lecture_time
                    # print "###"
                    # self.current_time= self.current_time.replace(hour=8)
                    # print "###"
                    # print self.lecture_time + datetime.timedelta(hours=2)
                    # if self.current_time >= self.lecture_time   and self.current_time <= (self.lecture_time + datetime.timedelta(hours=2) ):
                    #     print "kak"
        ###############################
        # except Exception:
        #     self.app_gui.template = ("./attendance/admin_scan.html", {"errors": ["Server down :(. Try again later. "]})
            
        
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
            self.app_gui.template = ("./attendance/admin_scan.html", { })

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