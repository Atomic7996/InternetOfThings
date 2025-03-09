import abc


class Device(abc.ABC):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def connect(self, source):
        return f"{self.name} is connected to {source}"


class Sensor(Device):
    def __init__(self, name, param, unit):
        super().__init__(name)
        self.parameter = param
        self.unit = unit
        self.value = 0

    def connect(self, source):
        return super().connect(source)

    def getData(self):
        print(f"{self.parameter}: {self.value} {self.unit}")


class Robot(Device):
    def __init__(self, name):
        super().__init__(name)

        # Management
        self.commandNumber = 0
        self.coordX = 0
        self.coordY = 0

        # Monitoring
        self.lastCommandNumber = 0
        self.status = 0
        self.commandCounter = 0

        # Sensors



    def connect(self, source):
        return super().connect(source)

    def enterCommand(self, commandNumber):
        self.commandNumber = commandNumber

        self.processCommand(self.commandNumber)

    def enterCoords(self, coordX, coordY):
        self.coordX = coordX
        self.coordY = coordY
        print(f"{self.name} coordinates changed X: {self.coordX}, Y: {self.coordY}")

    def getLastCommand(self):
        print(f"{self.name} last command was: {self.lastCommandNumber}")

    def getStatus(self):
        print(f"{self.name} status is : {self.status}")

    def getProcessedCommandsCount(self):
        print(f"{self.name} processed {self.commandCounter} commands")

    def getCoordinates(self):
        print(f"{self.name} coordinates X: {self.coordX}, Y: {self.coordY}")

    def processCommand(self, command):
        print(f"\n{self.name} is processing command:")
        self.status = 1
        self.getStatus()

        print(f"Processing command {self.commandNumber}")

        self.lastCommandNumber = self.commandNumber
        self.commandCounter += 1
        self.status = 0

        self.getStatus()


class RobotMech(Robot):
    def __init__(self, name):
        super().__init__(name)

        self.instrumentAngle = 0
        self.grabLevel = 0

        print("Robot with mechanical created")

    def setInstrumentAngle(self, angle):
        self.instrumentAngle = angle
        print(f"{self.name} instrument angle changed to {self.instrumentAngle}")

    def setGrabLevel(self, level):
        self.grabLevel = level
        print(f"{self.name} grab level changed to {self.grabLevel}")


class RobotVacuum(Robot):
    def __init__(self, name):
        super().__init__(name)

        self.vacuumGrabMode = 0

        print(f"Robot with vacuum created")

    def setVacuumGrabMode(self, mode):
        self.vacuumGrabMode = mode
        print(f"{self.name} vacuum grab mode changed to {self.vacuumGrabMode}")

# Добавить лампу (светофор)
# Добавить считыватель штрих-кодов (камера)
# добавить пульт управления (терминал)
