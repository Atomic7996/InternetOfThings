from flask import Flask
import devices as devices
import time


app = Flask(__name__)

robotVacuum = devices.RobotVacuum("VacuumRobot1")
robotMech = devices.RobotMech("MechRobot1")
tempSensor1 = devices.Sensor("Temp1", "Temperature", "C")

trafficLight = devices.TrafficLight("Traffic light")
barcodeScanner = devices.BarcodeScanner("Scanner")
controlPanel = devices.ControlPanel("Control panel")


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


def testTrafficLight():
    testString = "Traffic Light test:<br>"
    testString += trafficLight.connect("MainController") + "<br>"

    trafficLight.setRedLamp(1)
    trafficLight.setYellowLamp(1)
    trafficLight.setGreenLamp(0)
    trafficLight.setBlueLamp(0)  # Устанавливаем состояние синей лампы

    testString += "Traffic Light states:<br>"
    testString += f"Red: {trafficLight.redLamp}<br>"
    testString += f"Yellow: {trafficLight.yellowLamp}<br>"
    testString += f"Green: {trafficLight.greenLamp}<br>"
    testString += f"Blue: {trafficLight.blueLamp}<br>"  # Добавляем состояние синей лампы

    trafficLight.getLampStates()

    return testString

def testBarcodeScanner():

    testString = "Barcode Scanner test:<br>"
    testString += barcodeScanner.connect("AssemblyLine") + "<br>"

    barcodeScanner.startScanning()
    testString += "Scanning started...<br>"

    # Имитируем непрерывное сканирование с заданной периодичностью
    for i in range(3):
        code = barcodeScanner.readBarcode()
        if code:
            testString += f"Code read: {code}<br>"
            testString += f"Last Code (Monitoring Parameter): {barcodeScanner.lastCode}<br>"  # Выводим последний штрих-код
        else:
            testString += "No code read.<br>"
        time.sleep(1)  # Пауза в 1 секунду (имитация периодичности)

    barcodeScanner.stopScanning()
    testString += "Scanning stopped.<br>"

    testString += f"Final Last Code: {barcodeScanner.getLastCode()}<br>"  # Проверяем последний штрих-код после остановки

    return testString

def testControlPanel():

    testString = "Control Panel test:<br>"
    testString += controlPanel.connect("ProductionLine") + "<br>"

    # Устанавливаем значения параметров для мониторинга
    controlPanel.setSwitchMode(2)
    controlPanel.incrementButton1Count()
    controlPanel.setButton2Code(789)
    controlPanel.setButton3Code(987)

    # Устанавливаем значения параметров для управления (лампы)
    controlPanel.setBlueLamp(0)
    controlPanel.setRedLamp(1)
    controlPanel.setYellowLamp(0)
    controlPanel.setGreenLamp(1)

    # Выводим состояния параметров в HTML
    testString += "Control Panel states:<br>"
    testString += f"Switch Mode (p): {controlPanel.switchMode}<br>"
    testString += f"Button 1 Count (b1): {controlPanel.button1Count}<br>"
    testString += f"Button 2 Code (b2): {controlPanel.button2Code}<br>"
    testString += f"Button 3 Code (b3): {controlPanel.button3Code}<br>"
    testString += f"Blue Lamp (L1): {'On' if controlPanel.blueLampState else 'Off'}<br>"
    testString += f"Red Lamp (L2): {'On' if controlPanel.redLampState else 'Off'}<br>"
    testString += f"Yellow Lamp (L3): {'On' if controlPanel.yellowLampState else 'Off'}<br>"
    testString += f"Green Lamp (L4): {'On' if controlPanel.greenLampState else 'Off'}<br>"

    controlPanel.getAllStates() #Выводим состояния в консоль

    return testString


@app.route("/")
def startApp():
    return f"{testRobots()} <br><br> {testTrafficLight()} <br><br> {testBarcodeScanner()} <br><br> {testControlPanel()}"


if __name__ == "__main__":
    app.run()