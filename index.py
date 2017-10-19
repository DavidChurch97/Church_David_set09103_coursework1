import ConfigParser
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def Index():
  return render_template("index.html"), 200

@app.route("/pc")
def Pc():
	return render_template("pc.html"), 200

@app.route("/xbox")
def Xbox():
	return render_template("xbox.html"), 200

@app.route("/ps4")
def Ps4():
	return render_template("ps4.html"), 200

@app.route("/about")
def About():
	return render_template("about.html"), 200

@app.route("/contact")
def Contact():
	return render_template("contact.html"), 200

@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html"), 200

def init(app):
    config = ConfigParser.ConfigParser()
    try:
        config_location = "etc/defaults.cfg"
        config.read(config_location)
        
        app.config['DEBUG'] = config.get("config", "debug")
        app.config['ip_address'] = config.get("config", "ip_address")
        app.config['port'] = config.get("config", "port")
        app.config['url'] = config.get("config", "url")
    except:
        print "Could not read configs from: ", config_location

if __name__ == '__main__':
    init(app)
    app.run(
        host=app.config['ip_address'], 
        port=int(app.config['port']))
