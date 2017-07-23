import jinja2
import webapp2
import os
import sys

sys.path.append('source/')
from second import BrainPost
from second import brain_list

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

def constructBrainListHTML():
    html_string = ""
    for i in range(0, len(brain_list)):
        brain_post = brain_list[i]
        html_string += brain_post.listString(i) + "  |  "
    return html_string

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/Brain.html')
        template_variables = {"brainlist": constructBrainListHTML()}
        self.response.out.write(template.render(template_variables))

class PostHandler(webapp2.RequestHandler):
    def get(self):
        page_id = int(self.request.get('page_id'))
        self.sendResponse(page_id, None)

    def post(self):
        page_id = int(self.request.get("page_id"))
        self.sendResponse(page_id)

    def sendResponse(self, page_id, page):
        template = jinja_environment.get_template('templates/template.html')
        brain_post = brain_list[page_id]
        template_variables = {"title": brain_post.title,
                            "content": brain_post.content}
        self.response.out.write(template.render(template_variables))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/brain', PostHandler)
], debug=True)
