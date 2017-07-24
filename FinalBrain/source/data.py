from google.appengine.ext import ndb

class Data(ndb.Model):
    brain_part = ndb.StringProperty()
    brain_description = ndb.StringProperty()

brain_data = Data(brain_part ='temporal lobe','This is the temporal lobe')
brain_content = brain_data.put()
