from flask import Flask, render_template
app = Flask(__name__)

from database import functions as db

@app.route("/")
@app.route("/home")
def rt_home():
    return render_template('home.html', title="Home")

@app.route("/settings")
def rt_settings():
    return render_template('settings.html', title="Settings")
