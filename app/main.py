from flask import Flask
from ch.maxant.itproject.data.user import User
from ch.maxant.itproject.util import json

# here we create an object called app which has the class "Flask".
# Flask is a "framework", or "library" used to build a web server
app = Flask(__name__,
            static_url_path='',
            static_folder='../web')  # everything in the web folder, which is above the folder which this file is in, can be "served" by the web server


# TODO access DB and return data
# the following function will be called when the browser makes a request
# to say "/users/1". The variable "id" will have the value 1
# this function returns JSON, which is a string (lots of characters) like this: {"id": 1, "name": "Ant"}
# the browser knows how to read JSON and the JavaScript will use it to make an object which we can use to read the name
@app.route('/users/<id>', methods=['GET'])
def send_json(id):
    u = User(id, "Ant")  # this line creates a new User object and calls it "u"
    return json(u)  # and this line turns it into JSON and returns it to the browser


# this function returns the index.html page, when the browser requests "/", which is what the browser does when it first goes to a website
@app.route('/')
def root():
    return app.send_static_file('index.html')
    # or could do this, if we didnt have the static folder at the start: return send_from_directory('.', path)


# and now that we have initialised the server and set up some functions, we start the server.
app.run(host='0.0.0.0', port=8080, debug=True)

# 0.0.0.0 tells it that it is allowed to talk to anyone. you could put a specific IP address in here and it would only be allowed to talk to that address
# A port is like a channel or a chat room - the server now listens for requests on that port. the browser makes requests to:
#
#    http://127.0.0.1:8080/
#
# the "http" is the protocol - kind of like a language of how to talk to each other
# 127.0.0.1 is a special IP address of the local machine. you can also replace that with "localhost" and it will work.
# 8080 is the port - see above
# /   is the address of the document which should be shown in the browser. above the "root" function, we tell the server that it should return the index.html file
#
# the index.html file will then go and get "theme.css" and "code.js" like this:
#
#    http://127.0.0.1:8080/theme.css
#    http://127.0.0.1:8080/code.js
#
# the browser also wants to fetch the "favicon" - an icon or little image which it uses to display in the browser tab
#
#    http://127.0.0.1:8080/favicon.ico
#
# the web server can't find the file and so it returns an error like this:
#
#    HTTP/1.1 404 Not Found
#    Date: Sun, 18 Oct 2012 10:36:20 GMT
#    Server: Apache/2.2.14 (Win32)
#    Content-Length: 230
#    Connection: Closed
#    Content-Type: text/html; charset=iso-8859-1
#
# that is HTTP and the browser knows how to read it. it tells the browser that the file was not found. It uses code 404 to say that - the rest is just info.
