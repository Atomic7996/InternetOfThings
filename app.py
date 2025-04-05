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


@app.route("/")
def startApp():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()