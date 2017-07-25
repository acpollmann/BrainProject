from google.appengine.ext import ndb

class Data(ndb.Model):
    brain_part = ndb.StringProperty()
    brain_description = ndb.StringProperty()
