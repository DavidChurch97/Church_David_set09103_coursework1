from flask import Flask, render_template
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
	return render_template("ps4.html"), 200

@app.route("/contact")
def Contact():
	return render_template("ps4.html"), 200

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
