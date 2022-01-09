from flask import Flask, request, send_from_directory,jsonify
import socket
from requests import get

app = Flask(__name__, static_url_path='/static')


@app.route('/explorer/<username>/<path>',methods=["GET","POST"])
def explorer(username,path):
    
    ip = get('https://api.ipify.org').text
    print ('My public IP address is:', ip)
    print("Path Name:", path,"\nUserName:", username)
    return send_from_directory('static', f"{username}/{path}")

@app.route('/sendemail',methods=["GET","POST"])    
def sendemail():
    print(request.json)

if __name__ == "__main__":
    app.run(debug=True)