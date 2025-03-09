from flask import Flask
import devices as devices
import time

app = Flask(__name__)

robotVacuum = devices.RobotVacuum("VacuumRobot1")
robotMech = devices.RobotMech("MechRobot1")
tempSensor1 = devices.Sensor("Temp1", "Temperature", "C")
trafficLight1 = devices.TrafficLight("TrafficLight1")
barcodeScanner1 = devices.BarcodeScanner("Scanner1")
controlPanel1 = devices.ControlPanel("Panel1")


def testRobots():
    conectionString = "Robots connection test:<br>"
    conectionString += robotVacuum.connect("server") + "<br>"
    conectionString += robotMech.connect("server") + "<br>"
    conectionString += tempSensor1.connect(robotVacuum.name) + "<br>"

    robotVacuum.enterCommand(1)
    robotVacuum.enterCommand(3)

    print()
    robotVacuum.getLastCommand()
    robotVacuum.getProcessedCommandsCount()

    print()
    robotMech.getCoordinates()
    robotMech.enterCoords(10, 15)
    robotMech.setInstrumentAngle(35)
    robotMech.getStatus()
    robotMech.getCoordinates()

    return conectionString


# Добавить методы с тестом лампы, камеры и терминала
def testTrafficLight():
    testString = "Traffic Light test:<br>"
    testString += trafficLight1.connect("MainController") + "<br>"

    trafficLight1.set_red_lamp(1)
    trafficLight1.set_yellow_lamp(1)
    trafficLight1.set_green_lamp(0)
    trafficLight1.set_blue_lamp(0)  # Устанавливаем состояние синей лампы

    testString += "Traffic Light states:<br>"
    testString += f"Red: {trafficLight1.red_lamp}<br>"
    testString += f"Yellow: {trafficLight1.yellow_lamp}<br>"
    testString += f"Green: {trafficLight1.green_lamp}<br>"
    testString += f"Blue: {trafficLight1.blue_lamp}<br>"  # Добавляем состояние синей лампы

    trafficLight1.get_lamp_states()

    return testString

def testBarcodeScanner():

    testString = "Barcode Scanner test:<br>"
    testString += barcodeScanner1.connect("AssemblyLine") + "<br>"

    barcodeScanner1.start_scanning()
    testString += "Scanning started...<br>"

    # Имитируем непрерывное сканирование с заданной периодичностью
    for i in range(3):
        code = barcodeScanner1.read_barcode()
        if code:
            testString += f"Code read: {code}<br>"
            testString += f"Last Code (Monitoring Parameter): {barcodeScanner1.last_code}<br>"  # Выводим last_code
        else:
            testString += "No code read.<br>"
        time.sleep(1)  # Пауза в 1 секунду (имитация периодичности)

    barcodeScanner1.stop_scanning()
    testString += "Scanning stopped.<br>"

    testString += f"Final Last Code: {barcodeScanner1.get_last_code()}<br>"  # Проверяем last_code после остановки

    return testString

def testControlPanel():

    testString = "Control Panel test:<br>"
    testString += controlPanel1.connect("ProductionLine") + "<br>"

    # Устанавливаем значения параметров для мониторинга
    controlPanel1.set_switch_mode(2)
    controlPanel1.increment_button1_count()
    controlPanel1.set_button2_code(789)
    controlPanel1.set_button3_code(987)

    # Устанавливаем значения параметров для управления (лампы)
    controlPanel1.set_blue_lamp(0)
    controlPanel1.set_red_lamp(1)
    controlPanel1.set_yellow_lamp(0)
    controlPanel1.set_green_lamp(1)

    # Выводим состояния параметров в HTML
    testString += "Control Panel states:<br>"
    testString += f"Switch Mode (p): {controlPanel1.switch_mode}<br>"
    testString += f"Button 1 Count (b1): {controlPanel1.button1_count}<br>"
    testString += f"Button 2 Code (b2): {controlPanel1.button2_code}<br>"
    testString += f"Button 3 Code (b3): {controlPanel1.button3_code}<br>"
    testString += f"Blue Lamp (L1): {'On' if controlPanel1.blue_lamp_state else 'Off'}<br>"
    testString += f"Red Lamp (L2): {'On' if controlPanel1.red_lamp_state else 'Off'}<br>"
    testString += f"Yellow Lamp (L3): {'On' if controlPanel1.yellow_lamp_state else 'Off'}<br>"
    testString += f"Green Lamp (L4): {'On' if controlPanel1.green_lamp_state else 'Off'}<br>"

    controlPanel1.get_all_states() #Выводим состояния в консоль

    return testString


@app.route("/")
def startApp():
    return (testRobotsString + "<br><br>" + testTrafficLightString + "<br><br>" + testBarcodeScanner() + "<br><br>"
        + testControlPanel())


if __name__ == "__main__":
    testRobotsString = testRobots()
    testTrafficLightString = testTrafficLight()
    testBarcodeScannerString = testBarcodeScanner()
    testControlPanelString = testControlPanel()
    app.run()