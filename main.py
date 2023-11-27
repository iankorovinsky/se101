from gpiozero import Robot, LED

from flask import Flask, jsonify, request
from flask_cors import CORS
from time import sleep

app = Flask(__name__)
CORS(app, resources={r"/": {"origins": "*"}, r"/test": {"origins": "*"}, r"/forward": {"origins": "*"}, r"/backward": {"origins": "*"}, r"/left": {"origins": "*"}, r"/right": {"origins": "*"}, r"/reverse": {"origins": "*"}, r"/stop": {"origins": "*"}})

robot = Robot((4, 14), (17, 27))
led = LED(17)


@app.route('/', methods=['GET', 'POST'])
def welcome():
    print("BOAT says hi!")
    return jsonify({"response": "BOAT says hi!"})


@app.route('/test', methods=['GET', 'POST'])
def test():
    led.on()
    sleep(1)
    led.off()
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