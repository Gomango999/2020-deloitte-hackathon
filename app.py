from flask import Flask, render_template, request
import requests
import json
from src.Bootstrapper import bootstrap_system

app = Flask(__name__)
app.debug = True

system = bootstrap_system()

@app.route('/')
def index():
    return render_template('index.html', a=system.a)
