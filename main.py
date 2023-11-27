from gpiozero import Robot
import RPi.GPIO as GPIO
from flask import Flask, jsonify, request
from flask_cors import CORS
from time import sleep

app = Flask(__name__)
CORS(app, resources={r"/": {"origins": "*"}, r"/test": {"origins": "*"}, r"/forward": {"origins": "*"}, r"/backward": {"origins": "*"}, r"/left": {"origins": "*"}, r"/right": {"origins": "*"}, r"/reverse": {"origins": "*"}, r"/stop": {"origins": "*"}})

robot = Robot((4, 14), (17, 27))


from time import sleep

# Needs to be BCM. GPIO.BOARD lets you address GPIO ports by periperal
# connector pin number, and the LED GPIO isn't on the connector
GPIO.setmode(GPIO.BCM)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    print("BOAT says hi!")
    return jsonify({"response": "BOAT says hi!"})


@app.route('/test', methods=['GET', 'POST'])
def test():
    # set up GPIO output channel
    GPIO.setup(16, GPIO.OUT)

    # On
    GPIO.output(16, GPIO.LOW)

    # Wait a bit
    sleep(3)

    # Off
    GPIO.output(16, GPIO.HIGH)

    return jsonify({"response": "BOAT says hi!"})

@app.route('/forward', methods=['GET', 'POST'])
def forward():
    robot.forward()
    return jsonify({"response":"success"})

@app.route('/backward', methods=['GET', 'POST'])
def backward():
    robot.backward()
    return jsonify({"response":"success"})
    
@app.route('/left', methods=['GET', 'POST'])
def left():
    robot.left()
    return jsonify({"response":"success"})

@app.route('/right', methods=['GET', 'POST'])
def right():
    robot.right()
    return jsonify({"response":"success"})

@app.route('/reverse', methods=['GET', 'POST'])
def reverse():
    robot.reverse()
    return jsonify({"response":"success"})

@app.route('/stop', methods=['GET', 'POST'])
def stop():
    robot.stop()
    return jsonify({"response":"success"})

if __name__ == '__main__':
    app.run(debug=True)