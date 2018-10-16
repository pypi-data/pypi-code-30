#
# Generated by erpcgen 1.6.0 on Thu Jul 26 16:07:23 2018.
#
# AUTOGENERATED - DO NOT EDIT
#

import erpc

# Enumerators data types declarations
class LightMode:
    eLightOff = 0
    eLightOn = 1
    eLightPulsing = 2

class BarrierPosition:
    eBarPosOpen = 1
    eBarPosClosed = 2
    eBarPosUnknown = 0
    eBarPosError = 3

class BarrierAction:
    eBarActIdle = 0
    eBarActOpening = 1
    eBarActWaiting = 5
    eBarActClosing = 2
    eBarActAutoStopped = 6

class VehiclePosition:
    eVehicleNone = 0
    eVehicleA = 1
    eVehicleB = 2
    eVehicleAB = 3

class TrackerResult:
    ePassthroughOK = 1
    ePassthroughWrongWay = 2
    ePassthroughRetreated = 3

class PinDirection:
    ePinInput = 0
    ePinOutput = 1


# Structures data types declarations
class Colour(object):
    def __init__(self, r=None, g=None, b=None):
        self.r = r # uint8
        self.g = g # uint8
        self.b = b # uint8

    def _read(self, codec):
        self.r = codec.read_uint8()
        self.g = codec.read_uint8()
        self.b = codec.read_uint8()
        return self

    def _write(self, codec):
        if self.r is None:
            raise ValueError("r is None")
        codec.write_uint8(self.r)
        if self.g is None:
            raise ValueError("g is None")
        codec.write_uint8(self.g)
        if self.b is None:
            raise ValueError("b is None")
        codec.write_uint8(self.b)

    def __str__(self):
        return "<%s@%x r=%s g=%s b=%s>" % (self.__class__.__name__, id(self), self.r, self.g, self.b)

    def __repr__(self):
        return self.__str__()
        
class Timings(object):
    def __init__(self, onTime=None, offTime=None, stepTime=None):
        self.onTime = onTime # uint16
        self.offTime = offTime # uint16
        self.stepTime = stepTime # uint8

    def _read(self, codec):
        self.onTime = codec.read_uint16()
        self.offTime = codec.read_uint16()
        self.stepTime = codec.read_uint8()
        return self

    def _write(self, codec):
        if self.onTime is None:
            raise ValueError("onTime is None")
        codec.write_uint16(self.onTime)
        if self.offTime is None:
            raise ValueError("offTime is None")
        codec.write_uint16(self.offTime)
        if self.stepTime is None:
            raise ValueError("stepTime is None")
        codec.write_uint8(self.stepTime)

    def __str__(self):
        return "<%s@%x onTime=%s offTime=%s stepTime=%s>" % (self.__class__.__name__, id(self), self.onTime, self.offTime, self.stepTime)

    def __repr__(self):
        return self.__str__()
        
class Coefficients(object):
    def __init__(self, A=None, B=None):
        self.A = A # float
        self.B = B # float

    def _read(self, codec):
        self.A = codec.read_float()
        self.B = codec.read_float()
        return self

    def _write(self, codec):
        if self.A is None:
            raise ValueError("A is None")
        codec.write_float(self.A)
        if self.B is None:
            raise ValueError("B is None")
        codec.write_float(self.B)

    def __str__(self):
        return "<%s@%x A=%s B=%s>" % (self.__class__.__name__, id(self), self.A, self.B)

    def __repr__(self):
        return self.__str__()
        
class PathStatus(object):
    def __init__(self, vehicle_position=None, loopA_timeout=None, loopB_timeout=None, barrier_timeout=None, barrier_position=None, barrier_action=None, tracker_result=None):
        self.vehicle_position = vehicle_position # VehiclePosition
        self.loopA_timeout = loopA_timeout # bool
        self.loopB_timeout = loopB_timeout # bool
        self.barrier_timeout = barrier_timeout # bool
        self.barrier_position = barrier_position # BarrierPosition
        self.barrier_action = barrier_action # BarrierAction
        self.tracker_result = tracker_result # TrackerResult

    def _read(self, codec):
        self.vehicle_position = codec.read_uint32()
        self.loopA_timeout = codec.read_bool()
        self.loopB_timeout = codec.read_bool()
        self.barrier_timeout = codec.read_bool()
        self.barrier_position = codec.read_uint32()
        self.barrier_action = codec.read_uint32()
        self.tracker_result = codec.read_uint32()
        return self

    def _write(self, codec):
        if self.vehicle_position is None:
            raise ValueError("vehicle_position is None")
        codec.write_uint32(self.vehicle_position)
        if self.loopA_timeout is None:
            raise ValueError("loopA_timeout is None")
        codec.write_bool(self.loopA_timeout)
        if self.loopB_timeout is None:
            raise ValueError("loopB_timeout is None")
        codec.write_bool(self.loopB_timeout)
        if self.barrier_timeout is None:
            raise ValueError("barrier_timeout is None")
        codec.write_bool(self.barrier_timeout)
        if self.barrier_position is None:
            raise ValueError("barrier_position is None")
        codec.write_uint32(self.barrier_position)
        if self.barrier_action is None:
            raise ValueError("barrier_action is None")
        codec.write_uint32(self.barrier_action)
        if self.tracker_result is None:
            raise ValueError("tracker_result is None")
        codec.write_uint32(self.tracker_result)

    def __str__(self):
        return "<%s@%x vehicle_position=%s loopA_timeout=%s loopB_timeout=%s barrier_timeout=%s barrier_position=%s barrier_action=%s tracker_result=%s>" % (self.__class__.__name__, id(self), self.vehicle_position, self.loopA_timeout, self.loopB_timeout, self.barrier_timeout, self.barrier_position, self.barrier_action, self.tracker_result)

    def __repr__(self):
        return self.__str__()
        

