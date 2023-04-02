from flask import Flask, render_template, request
from models import record           # helps in managing the database
from config import locator          # helps in locating the position of the sensor
import config


app = Flask(__name__)

# this is a common variable shared by all the threads to broadcast
# the data to all the clients connected to the server.
config.sensorsData = None


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/toggle')
def toggleSensor():
    sensor_id = request.args.get('id')
    print(sensor_id)
    config.sensorsData = sensor_id
    return {
        "message": "Request Successful!",
        "data": sensor_id
    }


@app.route('/getdata')
def getData():
    return {
        "data": config.sensorsData
    }


if __name__ == '__main__':
    app.run(host='', port=5000)
