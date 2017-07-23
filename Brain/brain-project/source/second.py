from google.appengine.ext import ndb

class BrainPost():
    def __init__(self, title, content):
        self.title = title
        self.content = content
    def listString(self, page_id):
        return "<a href='brain?page_id=" + str(page_id) + "'>" + self.title + "</a>"

brain_list = [
    BrainPost ("HOME", "This would link to home."),
    BrainPost ("INFO", "This is all the brain info. "),
    BrainPost ("NEWS", "This would contain news."),
    BrainPost ("ABOUT THE CREATORS", "This is about us."),
    BrainPost ("REFERENCES", "This is our citations. ")
]
