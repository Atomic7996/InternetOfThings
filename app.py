from flask import Flask
import devices as devices

app = Flask(__name__)

robotVacuum = devices.RobotVacuum("VacuumRobot1")
robotMech = devices.RobotMech("MechRobot1")
tempSensor1 = devices.Sensor("Temp1", "Temperature", "C")


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


@app.route("/")
def startApp():
    return testRobotsString


if __name__ == "__main__":
    testRobotsString = testRobots()
    app.run()