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
        

        # this function waits for change to happen in the url to stop further progress in the function
        # if self.app_gui.web_app.urlChanged:
        #     return
        
        #alerting the user to remove his finger
        # most important thing in the code
        self.app_gui.evaluate_javascript("myFunction2();")

        die_time=q.QTime.currentTime().addSecs(1)
        while q.QTime.currentTime() < die_time:
            q.QCoreApplication.processEvents(q.QEventLoop.AllEvents,100)

        # if self.app_gui.web_app.urlChanged:
        #     return

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


class attendance(htmlPy.Object):
    
    def __init__(self,app_gui):
        super(attendance, self).__init__()
        self.app_gui = app_gui
        self.token= None
        self.lectures_array= None
        self.admins_array=None
        self.admins_fingers=[]
        self.current_attendance=None
        self.current_time=None
        self.lecture_time=None
        self.today=None
        self.url="http://localhost/api/student/attendance.php"
        self.start = 0
        self.lectures_array_edited=[]
        self.time_for_lecture=0
        self.unedited_lecture_time=None
        self.finger= None
        self.students_array=[]
        self.students_fingers=[]
        self.add_template_flag=0
        self.attended=[]
        self.admin_scan_flag=0
        # Initialize the class here, if required.
        return

    @htmlPy.Slot()
    def attendance_main(self):
        self.add_template_flag=0
        self.time_for_lecture=0
        self.today = datetime.datetime.now().day
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
                        self.unedited_lecture_time=time
                        time=time.replace(":","")
                        time=time.encode('ascii','ignore')
                        self.lecture_time = self.current_time.replace(hour=int(time[0:2]), minute=int(time[3:5]))
                        self.current_time = datetime.datetime.now()
                        #remove the following line when finishing
                        self.current_time= self.current_time.replace(hour=22)
                        if self.current_time >= self.lecture_time   and self.current_time <= (self.lecture_time + datetime.timedelta(hours=2) ):
                            self.time_for_lecture=1
                            # self.lecture_time= lecture
                            break
                        else:
                            self.time_for_lecture=0
                if self.time_for_lecture:
                    break

        ###############################
        
        elif self.today != datetime.datetime.now().day:
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
                        self.unedited_lecture_time=time
                        time=time.replace(":","")
                        time=time.encode('ascii','ignore')
                        self.lecture_time = self.current_time.replace(hour=int(time[0:2]), minute=int(time[3:5]))
                        self.current_time = datetime.datetime.now()
                        #remove the following line when finishing
                        self.current_time= self.current_time.replace(hour=11)
                        if self.current_time >= self.lecture_time   and self.current_time <= (self.lecture_time + datetime.timedelta(hours=2) ):
                            self.time_for_lecture=1
                            # self.lecture_time= lecture
                            break
                        else:
                            self.time_for_lecture=0
                if self.time_for_lecture:
                    break
        else:
            for lecture in self.lectures_array:
                self.current_time = datetime.datetime.now()
                for key in lecture.keys():
                    if(key != u"instrcutors"):
                        time= key
                        self.unedited_lecture_time=time
                        time=time.replace(":","")
                        time=time.encode('ascii','ignore')
                        self.lecture_time = self.current_time.replace(hour=int(time[0:2]), minute=int(time[3:5]))
                        self.current_time = datetime.datetime.now()
                        #remove the following line when finishing
                        self.current_time= self.current_time.replace(hour=11)
                        if self.current_time >= self.lecture_time   and self.current_time <= (self.lecture_time + datetime.timedelta(hours=2) ):
                            self.time_for_lecture=1
                            print "choco"
                            # self.lecture_time= lecture
                            break
                        else:
                            self.time_for_lecture=0
                if self.time_for_lecture:
                    break

        # self.current_time = datetime.datetime.now()
        # # for the time being
        # self.current_time= self.current_time.replace(hour=11)
        # for lecture in self.lectures_array_edited:
        #     if self.current_time >= lecture   and self.current_time <= (lecture + datetime.timedelta(hours=2) ):
        #         self.time_for_lecture=1
        #         self.lecture_time= lecture
        #         break
        #     else:
        #         self.time_for_lecture=0

        if self.time_for_lecture:
            self.admins_fingers=[]
            # x= str(self.lecture_time.hour) +":"+ str(self.lecture_time.minute)
            # print self.lectures_array
            # print self.current_attendance
            # get the instructors array from the lecture
            inst=""
            i=0
            # print self.unedited_lecture_time
            # print self.current_attendance["admins"]
            for lecture in self.current_attendance["records"]:
                for key in lecture:
                    if key == self.unedited_lecture_time:
                        print key
                        inst= self.current_attendance["records"][i]["instrcutors"]
                i+=1
            # print inst

            # get the admins array
            self.admins_array=self.current_attendance["admins"]+inst

            for admin in self.admins_array:
                # print type(admin["fingerPrint"][0])
                temp=literal_eval(admin["fingerPrint"])
                # print type(temp)
                # print type(temp[0])
                self.admins_fingers.append(temp)
            
            # for finger in self.admins_fingers:
            #     print finger
            if not self.admin_scan_flag:
                self.finger=f()
                self.finger.f.clearDatabase()
                temp=self.finger.template_add(self.admins_fingers)
                print temp
                self.admin_scan_flag=1

            temp=self.finger.admin_scan()
            print temp
            print len(self.admins_fingers)-1
            if temp >=0 and temp <= len(self.admins_fingers)-1:
                self.app_gui.template= ("./attendance/student_scan.html",{})
            elif temp== -1:
                self.app_gui.template= ("./attendance/admin_scan.html",{"errors":["No match for the fingerprint given "]})
            else:
                self.app_gui.template= ("./attendance/admin_scan.html",{})
            
        else:
            self.app_gui.evaluate_javascript("myFunction1();")
            self.admin_scan_flag=0
            die_time=q.QTime.currentTime().addSecs(3)
            while q.QTime.currentTime() < die_time:
                q.QCoreApplication.processEvents(q.QEventLoop.AllEvents,100)
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
            
    @htmlPy.Slot()
    def student_scan(self):
        print "hi student"
        self.admin_scan_flag=0
        self.current_time = datetime.datetime.now()
        #remove the following line when finishing
        self.current_time= self.current_time.replace(hour=11)

        if not(self.current_time >= self.lecture_time   and self.current_time <= (self.lecture_time + datetime.timedelta(hours=2) )):
            self.app_gui.template= ("./attendance/admin_scan.html",{"errors":["Time finished"]})
            return
        if not self.add_template_flag:
            i=0
            self.students_fingers=[]
            for lecture in self.current_attendance["records"]:
                    for key in lecture:
                        if key == self.unedited_lecture_time:
                            print key
                            inst= self.current_attendance["records"][i][self.unedited_lecture_time]
                    i+=1
            self.students_array=inst
            # for student in self.students_array:
            #     print student
            for student in self.students_array:
                    # print type(admin["fingerPrint"][0])
                    print type(student["fingerPrint"])
                    temp=literal_eval(student["fingerPrint"])
                    # print type(temp)
                    # print type(temp[0])
                    self.students_fingers.append(temp)

            
            self.finger.template_add(self.students_fingers)
            self.add_template_flag=1
            self.attended=[0]*len(self.students_fingers)
            for i in self.attended:
                print i

        time.sleep(0.5)
        temp=self.finger.admin_scan()
        print temp
        check_array= self.admins_array + self.students_array
        
        if temp >=0 and temp <= len(self.admins_fingers)-1:
                self.app_gui.template= ("./attendance/admin_scan.html",{"successes":["attendance ended"]})
                return
        elif temp > len(self.admins_fingers)-1 and temp <= (len(self.admins_fingers)+len(self.students_fingers))-1:
            # attendance taking part
            print "hi"
            datetime.datetime
            # print check_array[temp]
            date= str(datetime.datetime.now())[0:10]

            timee= str(datetime.datetime.now().time())[0:5]

            dic={"Sid":check_array[temp]["id"],"Cid":check_array[temp]["course_id"],"att":"1","t":timee,"d":date}
            url="http://localhost/api/student/write_single_json_input.php"
            r=requests.post(url,json.dumps(dic))
            print r.content
            self.app_gui.template= ("./attendance/student_scan.html",{"successes":["thank you"+check_array[temp]["name"]]})
            
            return
        elif temp== -1:
            self.app_gui.template= ("./attendance/student_scan.html",{"errors":["No match for the fingerprint given "]})
            return
        else:
            self.app_gui.template= ("./attendance/student_scan.html",{})
            return
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