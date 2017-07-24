#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
import sys

sys.path.append('source/')
from pagepost import PagePost
from pagepost import page_list
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

def constructPageListHTML():
    html_string = "<ul>\n"
    for i in range(0, len(page_list)):
        page_post = page_list[i]
        html_string += "<li>" + page_post.listString(i) + "</li>"
    html_string += "</ul>"
    return html_string

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/index.html')
        template_variables = {"content": constructPageListHTML
        }
        self.response.out.write(template.render(template_variables))

class PostHandler(webapp2.RequestHandler):
    def get(self):
        # This creates and serves the blog post page
        template = jinja_environment.get_template('templates/pages.html')
        page_id = int(self.request.get('page_id'))
        page_post = page_list[page_id]
        template_variables = {"title": page_post.title,
                              "content": page_post.content}
        self.response.out.write(template.render(template_variables))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/brain', PostHandler)
], debug=True)
