import webapp2  #this is a LIBRARY that allows us to set up a WEB APP using HANDLER classes that INHERIT from the library
import random

def randomFortune():
    #list of possible fortunes
    fortunes = [
        "You will have much success in coding",
        "You have a wonderful personality",
        "You have tamed the might Python, now you must free on the Great Spider's web!"
    ]

    #randomly select an index of the list
    index = random.randint(0,2)

    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):                                                              #the GET method here says that "if a GET METHOD REQUEST
                                                                                #comes into the server, here is what you do..."
        header = "<h1>Fortune Cookie</h1>"

        fortune = "<strong>" + randomFortune() + "</strong>"
        fortune_sentence = "Your fortune: " + fortune
        fortune_paragraph = "<p>" + fortune_sentence + "</p>"

        lucky_number = "<strong>" + str(random.randint(1,100)) + "</strong>"
        number_sentence = "Your lucky number is: " + lucky_number
        number_paragraph = "<p>" + number_sentence + "</p>"

        another_cookie_button = "<a href='.'><button>Another cookie please!</button></a>"

        content = header + fortune_paragraph + number_paragraph + another_cookie_button

        self.response.write(content)                                            #note that RESPONSE is a PROPERTY of RequestHandler

class LoginHandler(webapp2.RequestHandler):
    def get(self):

        self.response.write("Thanks for trying to log in!")

#Below is a CONSTRUCTOR that makes a NEW INSTANCE of object, WSGIApplication, called APP.
#The app instance is fed our LIST OF PAIRS of routes and their handlers as the FIRST ARGUMENT.
#The handlers give instructions to the server (telling it what to send back).
#The SECOND ARGUMENT is the boolean, debug=True.
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ("/login", LoginHandler)
], debug=True)
