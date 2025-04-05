import abc
import json
import random


class Device(abc.ABC):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def connect(self):
        pass


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
        self.t1 = 0
        self.t2 = 0
        self.t3 = 0
        self.t4 = 0
        self.t5 = 0
        self.t6 = 0
        self.m1 = 0
        self.m2 = 0
        self.m3 = 0
        self.m4 = 0
        self.m5 = 0
        self.m6 = 0
        self.l1 = 0
        self.l2 = 0
        self.l3 = 0
        self.l4 = 0
        self.l5 = 0
        self.l6 = 0

    @abc.abstractmethod
    def connect(self, *args):
        self.emulate()


    def emulate(self):
        self.t1 = random.randint(15, 115)
        self.t2 = random.randint(15, 115)
        self.t3 = random.randint(15, 115)
        self.t4 = random.randint(15, 115)
        self.t5 = random.randint(15, 115)
        self.t6 = random.randint(15, 115)
        self.m1 = random.randint(15, 115)
        self.m2 = random.randint(15, 115)
        self.m3 = random.randint(15, 115)
        self.m4 = random.randint(15, 115)
        self.m5 = random.randint(15, 115)
        self.m6 = random.randint(15, 115)
        self.l1 = random.randint(15, 115)
        self.l2 = random.randint(15, 115)
        self.l3 = random.randint(15, 115)
        self.l4 = random.randint(15, 115)
        self.l5 = random.randint(15, 115)
        self.l6 = random.randint(15, 115)

        self.lastCommandNumber = 3
        self.status = 1
        self.commandCounter = 3


class RobotGripper(Robot):
    def __init__(self, name):
        super().__init__(name)

        self.motorMaximum = 4096
        self.instrumentAngle = 0
        self.grabLevel = 0

        print("Robot with gripper created")

    def connect(self):
        super().connect()

        return json.dumps({
            't1': self.t1,
            't2': self.t2,
            't3': self.t3,
            't4': self.t4,
            't5': self.t5,
            't6': self.t6,
            'm1': self.m1,
            'm2': self.m2,
            'm3': self.m3,
            'm4': self.m4,
            'm5': self.m5,
            'm6': self.m6,
            'l1': self.l1,
            'l2': self.l2,
            'l3': self.l3,
            'l4': self.l4,
            'l5': self.l5,
            'l6': self.l6,
            'lastCommandNumber': self.lastCommandNumber,
            'status': self.status,
            'commandCounter': self.commandCounter,
        })

        # Management
        # return json.dumps({
        #     'commandNumber': self.commandNumber,
        #     'coordX': self.coordX,
        #     'coordY': self.coordY,
        #     'instrumentAngle': self.instrumentAngle,
        #     'grabLevel': self.grabLevel
        # })


class RobotVacuum(Robot):
    def __init__(self, name):
        super().__init__(name)

        self.vacuumGrabMode = 0

        print(f"Robot with vacuum created")

    def connect(self):
       super().connect()
       self.status = 0

       return json.dumps({
           't1': self.t1,
           't2': self.t2,
           't3': self.t3,
           't4': self.t4,
           't5': self.t5,
           't6': self.t6,
           'm1': self.m1,
           'm2': self.m2,
           'm3': self.m3,
           'm4': self.m4,
           'm5': self.m5,
           'm6': self.m6,
           'l1': self.l1,
           'l2': self.l2,
           'l3': self.l3,
           'l4': self.l4,
           'l5': self.l5,
           'l6': self.l6,
           'lastCommandNumber': self.lastCommandNumber,
           'status': self.status,
           'commandCounter': self.commandCounter,
       })
       # Management
       # return json.dumps({
       #     'commandNumber': self.commandNumber,
       #     'coordX': self.coordX,
       #     'coordY': self.coordY,
       #     'vacuumGrabMode': self.vacuumGrabMode,
       # })


class TrafficLight(Device):
    def __init__(self, name):
        super().__init__(name)
        self.blueLamp = 0  # 0 - выключена, 1 - включена
        self.redLamp = 0  # 0 - выключена, 1 - включена
        self.yellowLamp = 0  # 0 - выключена, 1 - включена
        self.greenLamp = 0  # 0 - выключена, 1 - включена

        print(f"Traffic light created")

    def connect(self,):
        return super().connect()

    def setBlueLamp(self, state):

        if state in (0, 1):
            self.blueLamp = state
            print(f"Blue lamp: {'on' if self.blueLamp else 'off'}")
        else:
            print("Error: Unavailable status.")

    def setRedLamp(self, state):

        if state in (0, 1):
            self.redLamp = state
            print(f"Red lamp: {'On' if self.redLamp else 'Off'}")
        else:
            print("Error: Unavailable status.")

    def setYellowLamp(self, state):

        if state in (0, 1):
            self.yellowLamp = state
            print(f"Yellow lamp: {'On' if self.yellowLamp else 'Off'}")
        else:
            print("Error: Unavailable status.")

    def setGreenLamp(self, state):

        if state in (0, 1):
            self.greenLamp = state
            print(f"Green lamp: {'On' if self.greenLamp else 'Off'}")
        else:
            print("Error: Unavailable status.")

    def getLampStates(self):

        print(f"Lamp status '{self.name}':")
        print(f"  Blue:  {'On' if self.blueLamp else 'Off'}")
        print(f"  Red: {'On' if self.redLamp else 'Off'}")
        print(f"  Yellow: {'On' if self.yellowLamp else 'Off'}")
        print(f"  Green: {'On' if self.greenLamp else 'Off'}")


class BarcodeScanner(Device):
    def __init__(self, name):
        super().__init__(name)
        self.lastCode = None  # Последний считанный код
        self.isScanning = False # Флаг, показывающий, сканирует ли сканер в данный момент

        print(f"Barcode scanner created")

    def connect(self):
        return super().connect()

    def startScanning(self):

        self.isScanning = True
        print(f"Scanner started scanning")

    def stopScanning(self):

        self.isScanning = False
        print(f"Scanner ended scanning")

    def readBarcode(self):

        if self.isScanning:
            # Генерируем случайный штрих-код в качестве примера.
            # В реальной системе здесь будет считывание из камеры.
            self.lastCode = "123456789012"
            print(f"The barcode has been read")
            return self.lastCode
        else:
            print("The scan is not active")
            return None

    def getLastCode(self):

        return self.lastCode #Возвращает последний считанный код

    def setScanningMode(self, mode):

        # В этом примере просто выводим сообщение.
        print(f"The scanning mode is: {mode}")


class ControlPanel(Device):

    def __init__(self, name):
        super().__init__(name)
        self.switchMode = 0  # Режим переключателя (параметр p)
        self.button1Count = 0  # Количество нажатий кнопки 1 (параметр b1)
        self.button2Code = 0  # Код кнопки 2 (параметр b2)
        self.button3Code = 0  # Код кнопки 3 (параметр b3)
        self.blueLampState = 0  # Состояние синей лампы (параметр L1)
        self.redLampState = 0  # Состояние красной лампы (параметр L2)
        self.yellowLampState = 0  # Состояние желтой лампы (параметр L3)
        self.greenLampState = 0  # Состояние зеленой лампы (параметр L4)

        print(f"Control panel created")

    def connect(self):
        return super().connect()

    # Методы для управления лампами (параметры L1-L4)
    def setBlueLamp(self, state):

        if state in (0, 1):
            self.blueLampState = state
            print(f"Blue lamp: {'on' if self.blueLampState else 'off'}")
        else:
            print("Error: Invalid lamp state. Use 0 or 1.")

    def setRedLamp(self, state):

        if state in (0, 1):
            self.redLampState = state
            print(f"Red lamp: {'on' if self.redLampState else 'off'}")
        else:
            print("Error: Invalid lamp state. Use 0 or 1.")

    def setYellowLamp(self, state):

        if state in (0, 1):
            self.yellowLampState = state
            print(f"Yellow lamp: {'on' if self.yellowLampState else 'off'}")
        else:
            print("Error: Invalid lamp state. Use 0 or 1.")

    def setGreenLamp(self, state):

        if state in (0, 1):
            self.greenLampState = state
            print(f"Green lamp: {'on' if self.greenLampState else 'off'}")
        else:
            print("Error: Invalid lamp state. Use 0 or 1.")

    # Methods for monitoring (parameters p, b1-b3)
    def setSwitchMode(self, mode):

        self.switchMode = mode
        print(f"Switch mode set: {self.switchMode}")

    def incrementButton1Count(self):

        self.button1Count += 1
        print(f"Button 1 pressed. Number of presses: {self.button1Count}")

    def setButton2Code(self, code):

        self.button2Code = code
        print(f"Button 2 code set: {self.button2Code}")

    def setButton3Code(self, code):

        self.button3Code = code
        print(f"Button 3 code set: {self.button3Code}")

    # Methods for getting the current state of parameters
    def getAllStates(self):

        print(f"Control panel state '{self.name}':")
        print(f"  Switch mode: {self.switchMode}")
        print(f"  Button 1 (number of presses): {self.button1Count}")
        print(f"  Button 2 code: {self.button2Code}")
        print(f"  Button 3 code: {self.button3Code}")
        print(f"  Blue lamp: {'on' if self.blueLampState else 'off'}")
        print(f"  Red lamp: {'on' if self.redLampState else 'off'}")
        print(f"  Yellow lamp: {'on' if self.yellowLampState else 'off'}")
        print(f"  Green lamp: {'on' if self.greenLampState else 'off'}")