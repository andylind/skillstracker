from google.appengine.ext import db

class Skill(db.Model):
    user = db.UserProperty()
    name = db.StringProperty()
    category = db.StringProperty()
    proficiency = db.StringProperty()
    dateUpdated = db.DateTimeProperty(auto_now_add=True)
