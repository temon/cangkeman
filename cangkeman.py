import webapp2
import random
import jinja2
import os
import json

with open('cangkems.json') as namefile:
    names =  json.load(namefile) + ["BOSOK", "GAK DI SEKOLAHIN", "GEDI", "JELEK", "KELINDAS TRUCK",
                                    "MEMBLE", "PORNO", "MINTA DIINJAK", "KOYO TELEK",
                                    "MINTA DIPOTONG", "DI CIPOK ULAR", "KEMANA MANA", "TUKANG GOSIP", 
				    "MINTA DIJILAT", "PENGEN DIISEP", "DIEMUT ALUS",
		                    "PENGEN DITARIK", "PENGEN TAK OBRAL", "MANIS KAYAK BOKONG", 
				    "BUTUH BELAIAN ALUS" ]

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'name':random.choice(names)
        }
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))

class Cangkem(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('cangkem.html')
        self.response.out.write(template.render())

app = webapp2.WSGIApplication([('/', MainPage),('/cangkem', Cangkem)],
                              debug=True)

