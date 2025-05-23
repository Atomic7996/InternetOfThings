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
        self.L1 = 0
        self.L2 = 0
        self.L3 = 0
        self.L4 = 0

    def connect(self):
        self.emulate()
        return json.dumps({
            'L1': self.L1,
            'L2': self.L2,
            'L3': self.L3,
            'L4': self.L4,
        })

    def emulate(self):
        # Keep current values unless they haven't been set
        if not hasattr(self, '_initialized'):
            self.L1 = random.randint(0, 1)
            self.L2 = random.randint(0, 1)
            self.L3 = random.randint(0, 1)
            self.L4 = random.randint(0, 1)
            self._initialized = True

    def set_properties(self, request):
        if 'L1' in request.args:
            self.L1 = int(request.args.get('L1'))
        if 'L2' in request.args:
            self.L2 = int(request.args.get('L2'))
        if 'L3' in request.args:
            self.L3 = int(request.args.get('L3'))
        if 'L4' in request.args:
            self.L4 = int(request.args.get('L4'))
        return {'status': 'success'}


class BarcodeScanner(Device):
    def __init__(self, name):
        super().__init__(name)
        self.lastCode = "0"
        self.isScanning = 0
        self.scanCommand = 0  # 0 - idle, 1 - start scan

    def emulate(self):
        if self.scanCommand == 1:
            self.lastCode = str(random.randint(10**11, 10**12-1))
            self.isScanning = 1
            self.scanCommand = 0  # Reset command after processing
        else:
            self.isScanning = 0

    def connect(self):
        self.emulate()
        return json.dumps({
            'lastCode': self.lastCode,
            'isScanning': self.isScanning
        })

    def set_properties(self, request):
        if 'scanCommand' in request.args:
            self.scanCommand = int(request.args.get('scanCommand'))
        return {'status': 'success'}


class ControlPanel(Device):
    def __init__(self, name):
        super().__init__(name)
        self.switchMode = 0
        self.button1Count = 0
        self.button2Code = 0
        self.button3Code = 0
        self.lampStates = [0]*4
        self.lampCommands = [0]*4  # To receive commands from UI

    def emulate(self):
        # Update lamp states based on commands
        for i in range(4):
            if self.lampCommands[i] != -1:  # -1 means no command
                self.lampStates[i] = self.lampCommands[i]
                self.lampCommands[i] = -1  # Reset command after processing

        # Randomize other properties
        self.switchMode = random.randint(0, 3)
        self.button1Count = random.randint(0, 100)
        self.button2Code = random.randint(1000, 9999)
        self.button3Code = random.randint(1000, 9999)

    def connect(self):
        self.emulate()
        return json.dumps({
            'switchMode': self.switchMode,
            'button1Count': self.button1Count,
            'button2Code': self.button2Code,
            'button3Code': self.button3Code,
            'lamps': self.lampStates
        })

    def set_properties(self, request):
        for i in range(4):
            lamp_key = f'lamp{i+1}'
            if lamp_key in request.args:
                self.lampCommands[i] = int(request.args.get(lamp_key))
        return {'status': 'success'}