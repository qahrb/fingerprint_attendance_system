import requests
import datetime
import os
from pyfingerprint.pyfingerprint import PyFingerprint

#intiate the connection with the server and get the connection token

#infinite loop 
while True:
    
    #Get the current time and make a variable that contains the time 
    #to be checked.
    now = datetime.datetime.now()
    today_8_am = now.replace(hour=8, minute=0, second=0, microsecond=0)

    if now == today_8_am:
        #In this section we will get the attendance data for today
        #from the server using the api
        
        #intiate the connection with the server and get the connection token
        r=requests.get('http://127.0.0.1:5000/login',auth=('Admin','12345'))
        json=r.json()
        token=json['token']
        