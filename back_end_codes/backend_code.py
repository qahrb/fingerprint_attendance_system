import json
import requests
import htmlPy


class enroll(htmlPy.Object):
    # GUI callable functions have to be inside a class.
    # The class should be inherited from htmlPy.Object.

    def __init__(self,app_gui):
        super(enroll, self).__init__()
        self.app_gui = app_gui
        self.token= None
        # Initialize the class here, if required.
        return

    @htmlPy.Slot(str, result=str)
    def login(self, json_data):
        url="http://127.0.0.1:5000/login"
        # @htmlPy.Slot(arg1_type, arg2_type, ..., result=return_type)
        # This function can be used for GUI forms.
        form_data = json.loads(json_data)
        print form_data
        print (json.dumps(form_data))
        try:
            r=requests.get(url,auth=(form_data['id'],form_data['password']))
            print r.content
            print r.status_code
        except Exception:
            self.app_gui.template = ("./login.html", {"errors": ["serverdown"]})
        
        if r.status_code == 200:
            hello=r.json()
            token=hello['token']
            # print "this is a token"
            # print token
            self.token=token
            # print self.token
            self.app_gui.template = ("./enroll.html", {"template_variable_name": "value"})
        else:
            self.app_gui.template = ("./login.html", {"errors": ["please check your username or password"]})
        return json.dumps(form_data)
    
    @htmlPy.Slot()
    def function_name(self):
        # This is the function exposed to GUI events.
        # You can change app HTML from here.
        # Or, you can do pretty much any python from here.
        #
        # NOTE: @htmlPy.Slot decorater needs argument and return data-types.
        # Refer to API documentation.
        return

    @htmlPy.Slot()
    def javascript_function(self):

        # Any function decorated with @htmlPy.Slot decorater can be called
        # using javascript in GUI

        print "mama helwa"
        return
