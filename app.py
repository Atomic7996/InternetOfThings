from flask import Flask, request, render_template
import devices as devices


app = Flask(__name__)

robotGripper = devices.RobotGripper("Gripper Robot")
robotVacuum = devices.RobotVacuum("Vacuum Robot")
trafficLight = devices.TrafficLight("Traffic light")
barcodeScanner = devices.BarcodeScanner("Scanner")
controlPanel = devices.ControlPanel("Control panel")


@app.route("/robot_gripper_connect")
def robotGripperConnect():
    return robotGripper.connect()


@app.route("/robot_vacuum_connect")
def robotVacuumConnect():
    return robotVacuum.connect()


@app.route('/connect_trafficlight')
def connect_trafficlight():
    return trafficLight.connect()


@app.route('/connect_scanner')
def connect_scanner():
    return barcodeScanner.connect()


@app.route('/connect_panel')
def connect_panel():
    return controlPanel.connect()


# Control endpoints
@app.route('/set_trafficlight', methods=['POST'])
def set_trafficlight():
    return trafficLight.set_properties(request)


@app.route('/set_scanner', methods=['POST'])
def set_scanner():
    return barcodeScanner.set_properties(request)


@app.route('/set_panel', methods=['POST'])
def set_panel():
    return controlPanel.set_properties(request)


@app.route("/")
def startApp():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()