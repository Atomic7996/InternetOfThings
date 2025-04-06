from flask import Flask, request, render_template
import devices as devices


app = Flask(__name__)

robotGripper = devices.RobotGripper("GripperRobot")
robotVacuum = devices.RobotVacuum("VacuumRobot")
trafficLight = devices.TrafficLight("Traffic light")
barcodeScanner = devices.BarcodeScanner("Scanner")
controlPanel = devices.ControlPanel("Control panel")


@app.route("/robot_gripper_connect")
def robotGripperConnect():
    return robotGripper.connect()


@app.route("/robot_vacuum_connect")
def robotVacuumConnect():
    return robotVacuum.connect()

# Пример на Flask
@app.route('/connect/trafficlight')
def connect_trafficlight():
    return TrafficLight("tl1").connect()

@app.route('/connect/scanner')
def connect_scanner():
    return BarcodeScanner("bs1").connect()

@app.route('/connect/panel')
def connect_panel():
    return ControlPanel("cp1").connect()

@app.route("/")
def startApp():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()