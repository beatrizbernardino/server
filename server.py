from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)

global POT
global BUT
global TS
global ID
POT = 0
BUT = 0
TS = 0
ID = 0

@app.route('/')
def control():
   return render_template('index.html')

@app.route('/status', methods = ['POST', 'GET'])
def status():
   global POT
   global BUT
   global TS
   global ID
   if request.method == 'POST':
      # TS = 15:23:45/11:11:11, POT = 4095, BUT = 1, ID=15; 
      status = request.form
      POT = status['TS']
      TS = POT.split(",", 1)[0]
      ID = POT.split(",")[3].split("=",1)[-1]
      BUT = POT.split(",")[2].split("=",1)[-1]
      POT = POT.split(",")[1].split("=",1)[-1]
      return render_template("status.html", status = status)
   else:
      return jsonify({'TS' : TS, 'POT' : POT,'BUT' : BUT, 'ID' : ID}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
