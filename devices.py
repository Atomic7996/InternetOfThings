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
    def __init__(self):
        self.L1 = 0
        self.L2 = 0
        self.L3 = 0
        self.L4 = 0

    def connect(self):
        return json.dumps({
            'L1': self.L1,
            'L2': self.L2,
            'L3': self.L3,
            'L4': self.L4,
        })

    def set_properties(self, request):
        self.L1 = request.args.get('L1', '')
        self.L2 = request.args.get('L2', '')
        self.L3 = request.args.get('L3', '')
        self.L4 = request.args.get('L4', '')
        return {}

class BarcodeScanner(Device):
    def __init__(self, name):
        super().__init__(name)
        self.lastCode = None
        self.isScanning = False

    def emulate(self):
        self.lastCode = str(random.randint(10**11, 10**12-1))
        self.isScanning = random.choice([True, False])

    def connect(self):
        self.emulate()
        return json.dumps({
            'lastCode': self.lastCode,
            'isScanning': self.isScanning
        })


class ControlPanel(Device):
    def __init__(self, name):
        super().__init__(name)
        self.switchMode = 0
        self.button1Count = 0
        self.button2Code = 0
        self.button3Code = 0
        self.lampStates = [0]*4

    def emulate(self):
        self.switchMode = random.randint(0, 3)
        self.button1Count = random.randint(0, 100)
        self.button2Code = random.randint(1000, 9999)
        self.button3Code = random.randint(1000, 9999)
        self.lampStates = [random.randint(0,1) for _ in range(4)]

    def connect(self):
        self.emulate()
        return json.dumps({
            'switchMode': self.switchMode,
            'button1Count': self.button1Count,
            'button2Code': self.button2Code,
            'button3Code': self.button3Code,
            'lamps': self.lampStates
        })