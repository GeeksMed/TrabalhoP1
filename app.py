from flask import Flask, render_template, request, url_for
import os

app = Flask(__name__, template_folder=os.path.abspath('application/view/templates'), static_folder=os.path.abspath('application/view/static'))

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True)