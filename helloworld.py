# This simple helloworld has 2 things we need in every flask application

from flask import Flask

# 1 There is the application object created by calling the flask constructor
# with the name of our current module.  We will use the applicaton object globally
# in our application.

app = Flask(__name__)

# 2 We define a view function. 1st line is a decorator, which is an attribute of the app object
# app.route It tells flask that any incoming requests for a page at /index will be handled by 
# this view function.  The function itself is also called index by def index(): but this is not
# connected to the fact the route is called index too, we could have called the function anything.
# It simply returns the string Hello World and that is what shows up in the browser.

@app.route('/index')
def index():
  return 'Hello World!'
  
if __name__ == "__main__":
  app.run('0.0.0.0')
