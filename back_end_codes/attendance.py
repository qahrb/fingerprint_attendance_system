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
        self.lectures_array_edited=None
        # Initialize the class here, if required.
        return

    @htmlPy.Slot()
    def attendance_main(self):
        
        if !self.start:
            self.start=1
            #get the time in alphabetical form
            self.today = datetime.datetime.now()
            self.today.
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

        if self.today != datetime.datetime.now().day:
            self.current_attendance = requests.post(self.url, json.dumps(js))
            self.current_attendance = json.loads(self.current_attendance.content)
            self.lectures_array= self.current_attendance["records"]
            
        self.current_time =datetime.datetime.now()
        ###############################
        i=0
        
        for lecture in self.lectures_array:
            self.current_time =datetime.datetime.now()
            for key in lecture.keys():
                
                if(key != u"instrcutors"):
                    
                    time= key

                    # remove the colon from the time unicode string
                    time=time.replace(":","")
                    # time is in unicode
                    # this line changes time from unicode to ascii
                    time=time.encode('ascii','ignore')
                    
                    self.lecture_time = self.current_time.replace(hour=int(time[0:2]), minute=int(time[3:5]))
                    self.lectures_array_edited[i]=self.lecture_time
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