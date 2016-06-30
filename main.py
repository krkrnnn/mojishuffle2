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
import cgi

html_body = """
<html><head>
<meta http-equiv="content-type" content="text/html; charset=utf-8">
</head>
<body>
%s
</body></html>"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

        form = cgi.FieldStorage()
        m1 = form['moji1'].value
        m2 = form['moji2'].value
        shufflemoji = ''

        for index in range(0, min(len(m1), len(m2))-1):
            shufflemoji += m1[index]
            shufflemoji += m2[index]


        if len(m1) > len(m2):
            shufflemoji += m1[len(m2):len(m1)-1]
        elif  len(m2) > len(m1):
            shufflemoji += m2[len(m1):len(m2)-1]

        print "Content-type: text/html\n"
        print html_body % shufflemoji


app = webapp2.WSGIApplication([
    ('/', MainHandler)
    ('/mojishuffle', MainHandler)
], debug=True)
