from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/")
def Index():
  return render_template("index.html"), 200

@app.route("/pc")
def Pc():
	return render_template("pc.html"), 200

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
