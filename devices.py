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
class TrafficLight(Device):
    def __init__(self, name):
        super().__init__(name)
        self.blue_lamp = 0  # 0 - выключена, 1 - включена
        self.red_lamp = 0  # 0 - выключена, 1 - включена
        self.yellow_lamp = 0  # 0 - выключена, 1 - включена
        self.green_lamp = 0  # 0 - выключена, 1 - включена

        print(f"Traffic lights created")

    def connect(self, source):
        return super().connect(source)

    def set_blue_lamp(self, state):

        if state in (0, 1):
            self.blue_lamp = state
            print(f"Blue lamp: {'on' if self.blue_lamp else 'off'}")
        else:
            print("Error: Unavailable status.")

    def set_red_lamp(self, state):

        if state in (0, 1):
            self.red_lamp = state
            print(f"Red lamp: {'On' if self.red_lamp else 'Off'}")
        else:
            print("Error: Unavailable status.")

    def set_yellow_lamp(self, state):

        if state in (0, 1):
            self.yellow_lamp = state
            print(f"Yellow lamp: {'On' if self.yellow_lamp else 'Off'}")
        else:
            print("Error: Unavailable status.")

    def set_green_lamp(self, state):

        if state in (0, 1):
            self.green_lamp = state
            print(f"Green lamp: {'On' if self.green_lamp else 'Off'}")
        else:
            print("Error: Unavailable status.")

    def get_lamp_states(self):

        print(f"Lamp status '{self.name}':")
        print(f"  Blue:  {'On' if self.blue_lamp else 'Off'}")
        print(f"  Red: {'On' if self.red_lamp else 'Off'}")
        print(f"  Yellow: {'On' if self.yellow_lamp else 'Off'}")
        print(f"  Green: {'On' if self.green_lamp else 'Off'}")

# Добавить считыватель штрих-кодов (камера)

class BarcodeScanner(Device):
    def __init__(self, name):
        super().__init__(name)
        self.last_code = None  # Последний считанный код
        self.is_scanning = False # Флаг, показывающий, сканирует ли сканер в данный момент

        print(f"Barcode scanner created")

    def connect(self, source):
        return super().connect(source)

    def start_scanning(self):

        self.is_scanning = True
        print(f"Scanner started scanning")

    def stop_scanning(self):

        self.is_scanning = False
        print(f"Scanner ended scanning")

    def read_barcode(self):

        if self.is_scanning:
            # Генерируем случайный штрих-код в качестве примера.
            # В реальной системе здесь будет считывание из камеры.
            self.last_code = "123456789012"
            print(f"The barcode has been read")
            return self.last_code
        else:
            print("The scan is not active")
            return None

    def get_last_code(self):

        return self.last_code #Возвращает последний считанный код

    def set_scanning_mode(self, mode):

        # В этом примере просто выводим сообщение.
        print(f"The scanning mode is: {mode}")


# добавить пульт управления (терминал)

class ControlPanel(Device):

    def __init__(self, name):
        super().__init__(name)
        self.switch_mode = 0  # Режим переключателя (параметр p)
        self.button1_count = 0  # Количество нажатий кнопки 1 (параметр b1)
        self.button2_code = 0  # Код кнопки 2 (параметр b2)
        self.button3_code = 0  # Код кнопки 3 (параметр b3)
        self.blue_lamp_state = 0  # Состояние синей лампы (параметр L1)
        self.red_lamp_state = 0  # Состояние красной лампы (параметр L2)
        self.yellow_lamp_state = 0  # Состояние желтой лампы (параметр L3)
        self.green_lamp_state = 0  # Состояние зеленой лампы (параметр L4)

        print(f"Control panel created")

    def connect(self, source):
        return super().connect(source)

    # Методы для управления лампами (параметры L1-L4)
    def set_blue_lamp(self, state):

        if state in (0, 1):
            self.blue_lamp_state = state
            print(f"Blue lamp: {'on' if self.blue_lamp_state else 'off'}")
        else:
            print("Error: Invalid lamp state. Use 0 or 1.")

    def set_red_lamp(self, state):

        if state in (0, 1):
            self.red_lamp_state = state
            print(f"Red lamp: {'on' if self.red_lamp_state else 'off'}")
        else:
            print("Error: Invalid lamp state. Use 0 or 1.")

    def set_yellow_lamp(self, state):

        if state in (0, 1):
            self.yellow_lamp_state = state
            print(f"Yellow lamp: {'on' if self.yellow_lamp_state else 'off'}")
        else:
            print("Error: Invalid lamp state. Use 0 or 1.")

    def set_green_lamp(self, state):

        if state in (0, 1):
            self.green_lamp_state = state
            print(f"Green lamp: {'on' if self.green_lamp_state else 'off'}")
        else:
            print("Error: Invalid lamp state. Use 0 or 1.")

    # Methods for monitoring (parameters p, b1-b3)
    def set_switch_mode(self, mode):

        self.switch_mode = mode
        print(f"Switch mode set: {self.switch_mode}")

    def increment_button1_count(self):

        self.button1_count += 1
        print(f"Button 1 pressed. Number of presses: {self.button1_count}")

    def set_button2_code(self, code):

        self.button2_code = code
        print(f"Button 2 code set: {self.button2_code}")

    def set_button3_code(self, code):

        self.button3_code = code
        print(f"Button 3 code set: {self.button3_code}")

    # Methods for getting the current state of parameters
    def get_all_states(self):

        print(f"Control panel state '{self.name}':")
        print(f"  Switch mode: {self.switch_mode}")
        print(f"  Button 1 (number of presses): {self.button1_count}")
        print(f"  Button 2 code: {self.button2_code}")
        print(f"  Button 3 code: {self.button3_code}")
        print(f"  Blue lamp: {'on' if self.blue_lamp_state else 'off'}")
        print(f"  Red lamp: {'on' if self.red_lamp_state else 'off'}")
        print(f"  Yellow lamp: {'on' if self.yellow_lamp_state else 'off'}")
        print(f"  Green lamp: {'on' if self.green_lamp_state else 'off'}")