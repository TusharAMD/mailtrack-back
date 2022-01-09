from flask import Flask, request, send_from_directory,jsonify
import socket
from requests import get
from flask_cors import CORS
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__, static_url_path='/static')
cors = CORS(app)

@app.route('/explorer/<username>/<path>',methods=["GET","POST"])
def explorer(username,path):
    
    ip = get('https://api.ipify.org').text
    print ('My public IP address is:', ip)
    print("Path Name:", path,"\nUserName:", username)
    return send_from_directory('static', f"{username}/{path}")

@app.route('/sendemail',methods=["GET","POST"])    
def sendemail():
   
    print(request.json)
    return jsonify({1:1})
if __name__ == "__main__":
    app.run(debug=True)