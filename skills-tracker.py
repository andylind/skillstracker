import cgi
import os
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from datamodel import Skill

class MainPage(webapp.RequestHandler):
    def get(self):    
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'        
        user = users.get_current_user().nickname()
        
        skillsQuery = Skill.all().order('-dateUpdated')
        currentSkills = skillsQuery.fetch(100)
        
        template_values = {
            'currentSkills': currentSkills,
            'user': user,
            'url': url,
            'url_linktext': url_linktext
            }
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

class AddSkill(webapp.RequestHandler):
    def post(self):
        newSkill = Skill()
        newSkill.name =  self.request.get('skillName')
        newSkill.proficiency = self.request.get('proficiency')
        newSkill.user = users.get_current_user()
        newSkill.put()
        self.redirect('/')

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/AddSkill', AddSkill)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()