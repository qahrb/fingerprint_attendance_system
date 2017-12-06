import htmlPy

web_app = htmlPy.WebAppGUI(title=u"Python Website", maximized=True)
web_app.url = u"https://getbootstrap.com/docs/3.3/css/#forms-control-readonly"

web_app.start()