
# import the necessary packages
from flask import Flask, render_template, Response, request
from flask import json
import time
import threading
import os
from bme280 import main

# App Globals (do not edit)
app = Flask(__name__)

@app.route('/data')
def data():
    data = main()
    response = app.response_class(
        response=json.dumps(data),
        mimetype='application/json'
    )
    return response


#this if for prometheus only        
@app.route("/metrics")
def metrics():
    #get Data from BME280
    data = main()
    bme = "# HELP bme280_measuring_temperature Current sensor temperature in celsius. \n"
    bme += "# TYPE bme280_measuring_temperature gauge\n"
    bme += "bme280_measuring_temperature "
    bme += str(data[0])
    bme += "\n"
    bme += "# HELP bme280_measuring_humidity Current sensor humidity in persent. \n"
    bme += "# TYPE bme280_measuring_humidity gauge\n"
    bme += "bme280_measuring_humidity "
    bme += str(data[2])
    bme += "\n"
    bme += "# HELP bme280_measuring_pressure Current sensor Pressure in mmHg. \n"
    bme += "# TYPE bme280_measuring_pressure gauge\n"
    bme += "bme280_measuring_pressure "
    bme += str(data[1])
    bme += "\n"
    
    return f"{bme}", 200, {'Content-Type': 'text/plain; charset=utf-8'}
    return bme


@app.route('/', methods=['GET', 'POST'])
def move():
    result = ""
    if request.method == 'POST':
        
        return render_template('index.html',res_str=result)
                        
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False,threaded=True, port=5000)
    
