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


# Traffic Light Control
@app.route('/set_trafficlight')
def set_trafficlight():
    light_num = request.args.get('light', type=int)
    state = request.args.get('state', type=int)
    if light_num and state is not None:
        setattr(trafficLight, f'L{light_num}', state)
    return jsonify({'status': 'success'})

# Barcode Scanner Control
@app.route('/set_scanner')
def set_scanner():
    command = request.args.get('command', type=int)
    if command is not None:
        barcodeScanner.scanCommand = command
    return jsonify({'status': 'success'})

# Control Panel Control
@app.route('/set_panel')
def set_panel():
    lamp_num = request.args.get('lamp', type=int)
    state = request.args.get('state', type=int)
    if lamp_num and state is not None:
        controlPanel.lampCommands[lamp_num-1] = state
    return jsonify({'status': 'success'})


@app.route("/")
def startApp():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()