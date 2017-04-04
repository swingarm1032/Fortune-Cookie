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
import random

def getRandomFortune():
    fortunes = [
        "Investment will pay off for you in the near future",
        "You will eat more fortune cookies",
        "You will soon find true love",
        "You will embark an an exciting journey soon",
        "Follow your hearts desire",
        "You will recieve an unexpected gift",
        "You shall be rewarded greatly for past work",
        "You will find a new hobby at soon",
        "This is not a fortune",
        "You will inherit a great ammount",
        "This is another fake fortune"
    ]
    index = random.randint(0,10)
    return fortunes[index]
class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = '<h1>Fortune Cookie</h1>'
        fortune =  '<strong>' + getRandomFortune() + '</strong>'
        fortune_sentance = 'Your fortune is: ' + fortune
        fortune_para = '<p>' + fortune_sentance + '</p>'
        luckyNum = '<strong>' + str(random.randint(1, 100)) + '</strong>'
        number_sentance = 'Your lucky number is: ' + str(luckyNum)
        number_para ='<p>' + number_sentance + '</p>'
        cookie_button = '<a href= "."><button> "Give me another cookie!"</button></a>'
        content = header + fortune_para + number_para + cookie_button
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
