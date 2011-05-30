from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
import os


class template_manager():
	def __init__(self):
	 	self.template_directory = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)),"templates"),"project")
	def getTemplate(self,name):
		return os.path.join(self.template_directory,name+".html")



class create(webapp.RequestHandler):
	def get(self):
		templates = template_manager()
		self.response.out.write(template.render(templates.getTemplate("create"),{}))