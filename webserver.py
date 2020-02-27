from flask import (Flask,  # used for the general flask app
                  render_template,  # used to send html files
                  request)  # used to get GET requests
#import leds

app = Flask(__name__)

# Flask works by defining routes. Routes are
# subsections of a website: "ieeeucr.org/members",
# "ieeeucr.org/about-us", and "ieeeucr.org/workshops"
# are all examples of routes. When a route is visited,
# the code in the function underneath is run. You can
# have as few or many routes as you like!


# The / route is called the index route!
#    The launch_control.html file is shown
#    when the user visits this device's IP address
#    ex: when visiting "ieeeucr.org"
@app.route("/")
def index():  # this function can be called whatever
    return render_template("launch_control.html")


# Here we have another route, which flashes the
# nuclear activation LEDs three times
@app.route("/activate")
def activate():
    #leds.flash_activation_led()
    #leds.flash_activation_led()
    #leds.flash_activation_led()
    return "Activated!"

# Here we have a third route, which takes in a
# super secret password and flashes the confirm
# LED if the password is correct
@app.route("/confirm", methods=["GET"])
def confirm():
    password = request.args.get("password")
    # i heard you were missing some code...
    #   - RCC <3
    return "uh oh"

# example route from Jack's slides
@app.route("/example")
def example():
    return render_template("example.html")



# Here is our last route, which writes the target
# input name to a file, using a GET request
# <>< LOL Y'all make this too easy - RCC
with open("target", "w") as target_file:
    target_file.write("target!")


# change this port to a unique port so you don't
# interfere with others
app.run(host="0.0.0.0", port=5000)
