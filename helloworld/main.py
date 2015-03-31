# -*- coding: utf-8 -*-
#!/usr/bin/env python2.7
import os
from google.appengine.ext.webapp import template
import webapp2


class Main(webapp2.RequestHandler):
    def get(self):
        render(self, 'main.html', {'hint': '祝好運！'})
        
    def post(self): 
        try:
            guess = int(self.request.get('guess'))
        except:
            guess = -1
        answer = 4
        if guess < 0:
            hint = '請輸入數字'
        elif guess < answer:
            hint = '你的數字太小'
        elif guess == answer:
            hint = '恭喜！'
        else:
            hint = '你的數字太大'
        templateValues = {'hint': hint, 'guess': guess}
        render(self, 'main.html', templateValues)
    
def render(handler, renderFile, templateValues={}):
    path = os.path.join(os.path.dirname(__file__), 'templates/', renderFile)
    handler.response.out.write(template.render(path, templateValues))

app = webapp2.WSGIApplication([
 ('/.*', Main)],
 debug=True)