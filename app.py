from flask import Flask, request, render_template
import devices as devices


app = Flask(__name__)

robotGripper = devices.RobotGripper("GripperRobot")
robotVacuum = devices.RobotVacuum("VacuumRobot")
trafficlight = devices.TrafficLight("Traffic light")
scanner = devices.BarcodeScanner("Scanner")
panel = devices.ControlPanel("Control panel")


@app.route("/robot_gripper_connect")
def robotGripperConnect():
    return robotGripper.connect()


@app.route("/robot_vacuum_connect")
def robotVacuumConnect():
    return robotVacuum.connect()


# Пример на Flask
@app.route('/connect_trafficlight')
def connect_trafficlight():
    return trafficlight.connect()


@app.route('/connect_scanner')
def connect_scanner():
    return scanner.connect()


@app.route('/connect_panel')
def connect_panel():
    return panel.connect()


@app.route("/")
def startApp():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()