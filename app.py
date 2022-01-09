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
    if request.method=="POST":

        sender_email = request.json["useremail"]
        receiver_email = request.json["recemail"]
        password = request.json["userpass"]

        message = MIMEMultipart("alternative")
        message["Subject"] = request.json["subject"]
        message["From"] = sender_email
        message["To"] = receiver_email
        
        print(os.path.isdir(f"static\{useremail}") )
        
        # Create the plain-text and HTML version of your message
        text = request.json["mailcontent"]
        <html>
          <body>
            <p>
               <img src="https://mailtracktva.herokuapp.com/explorer/tva/myphoto.jpg"></img>
            </p>
          </body>
        </html>
        
        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
    print(request.json)
    return jsonify({1:1})
if __name__ == "__main__":
    app.run(debug=True)