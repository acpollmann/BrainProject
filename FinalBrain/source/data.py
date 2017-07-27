from google.appengine.ext import ndb


class Data(ndb.Model):
    brain_part = ndb.StringProperty()
    brain_description = ndb.StringProperty()

class NewsData(ndb.Model):
    news_title = ndb.StringProperty()
    news_preview = ndb.StringProperty()
    news_link = ndb.StringProperty()

class NewsPost():
    def __init__ (self, news_title, news_preview, news_link):
        self.news_title = news_title
        self.news_preview = news_preview
        self.news_link = news_link
    def store(self):
        new_news_entry = NewsData(news_title = self.news_title, news_preview = self.news_preview, news_link = self.news_link)
        new_news_entry.put()

def newsAsHTML():
    news_query = NewsData.query().iter();
    if news_query == None:
        return "<p> No news yet. </p>"

    html_string = ""
    while (news_query.has_next()):
        news_item = news_query.next();
        html_string += "<hr> <a class = 'news' href =\"" + news_item.news_link + "\"><h2>" + news_item.news_title + "</h2></a>" #</a><h2 style=color:white >" + news_item.news_title + "</h2>"
        html_string += " <p class= 'news_snippets' >" + news_item.news_preview + "</p>"
        html_string += "<p class='show-more'> <a href=\"" + news_item.news_link + "\"> Read More...</a></p>"
    return html_string
