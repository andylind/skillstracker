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
        user = users.get_current_user()
        userNickname = user.nickname()
        
        recentSkillsQuery =  db.GqlQuery("SELECT * FROM Skill " +
                "WHERE user = :1 " +
                "ORDER BY dateUpdated DESC",
                user)
        recentSkills = recentSkillsQuery.fetch(10)
        
        template_values = {
            'recentSkills': recentSkills,
            'user': userNickname,
            'url': url,
            'url_linktext': url_linktext
        }
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

class SkillsUpdater(webapp.RequestHandler):
    def get(self):    
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'        
        user = users.get_current_user()
        userNickname = user.nickname()
        
        uiSkillsQuery =  db.GqlQuery("SELECT * FROM Skill " +
                "WHERE category = :1 AND user = :2 " +
                "ORDER BY name DESC",
                "UI", user)
        uiSkills = uiSkillsQuery.fetch(100)
                
        javaSkillsQuery =  db.GqlQuery("SELECT * FROM Skill " +
                "WHERE category = :1 AND user = :2 " +
                "ORDER BY name DESC",
                "Java", user)

        javaSkills = javaSkillsQuery.fetch(100)
                
        dotNetSkillsQuery =  db.GqlQuery("SELECT * FROM Skill " +
                "WHERE category = :1 AND user = :2 " +
                "ORDER BY name DESC",
                ".NET", user)
        dotNetSkills = dotNetSkillsQuery.fetch(100)
                
        toolsSkillsQuery =  db.GqlQuery("SELECT * FROM Skill " +
                "WHERE category = :1 AND user = :2 " +
                "ORDER BY name DESC",
                "Tools", user)
        toolsSkills = toolsSkillsQuery.fetch(100)
        
        template_values = {
            'uiSkills': uiSkills,
            'javaSkills': javaSkills,
            'dotNetSkills': dotNetSkills,
            'toolsSkills': toolsSkills,
            'user': userNickname,
            'url': url,
            'url_linktext': url_linktext
            }
        path = os.path.join(os.path.dirname(__file__), 'update.html')
        self.response.out.write(template.render(path, template_values))

class AddSkill(webapp.RequestHandler):
    def post(self):
        newSkill = Skill()
        newSkill.name =  self.request.get('skillName')
        newSkill.proficiency = self.request.get('proficiency')
        newSkill.user = users.get_current_user()
        newSkill.put()
        self.redirect('/')

class Setup(webapp.RequestHandler):
    def get(self):
        newSkill = Skill()
        newSkill.name =  'Java'
        newSkill.category =  'Java'
        newSkill.proficiency = '3'
        newSkill.user = users.get_current_user()
        newSkill.put()
        self.redirect('/')

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/update', SkillsUpdater),
                                      ('/setup', Setup),
                                      ('/AddSkill', AddSkill)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
