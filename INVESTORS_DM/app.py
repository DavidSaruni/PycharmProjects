from flask import Flask, render_template, request, session, redirect, flash, url_for
import pymysql as pymysql

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def registration():
    if