import time
import traitlets
from traitlets.config.configurable import SingletonConfigurable
# from Adafruit_MotorHAT import Adafruit_MotorHAT
# from .motor import Motor
import requests


class Robot(SingletonConfigurable):
    
    # left_motor = traitlets.Instance(Motor)
    # right_motor = traitlets.Instance(Motor)

    # # config
    # i2c_bus = traitlets.Integer(default_value=1).tag(config=True)
    # left_motor_channel = traitlets.Integer(default_value=1).tag(config=True)
    # left_motor_alpha = traitlets.Float(default_value=1.0).tag(config=True)
    # right_motor_channel = traitlets.Integer(default_value=2).tag(config=True)
    # right_motor_alpha = traitlets.Float(default_value=1.0).tag(config=True)
    
    def __init__(self, *args, **kwargs):
        super(Robot, self).__init__(*args, **kwargs)
        # self.motor_driver = Adafruit_MotorHAT(i2c_bus=self.i2c_bus)
        # self.left_motor = Motor(self.motor_driver, channel=self.left_motor_channel, alpha=self.left_motor_alpha)
        # self.right_motor = Motor(self.motor_driver, channel=self.right_motor_channel, alpha=self.right_motor_alpha)
        
    def set_motors(self, left_speed, right_speed):
        pass
        
    def forward(self, speed=1.0, duration=None):
        # self.left_motor.value = speed
        # self.right_motor.value = speed
        requests.get('http://192.168.4.1/State?State=F')

    def backward(self, speed=1.0):
        # self.left_motor.value = -speed
        # self.right_motor.value = -speed
        requests.get('http://192.168.4.1/State?State=B')

    def left(self, speed=1.0):
        # self.left_motor.value = -speed
        # self.right_motor.value = speed
        requests.get('http://192.168.4.1/State?State=L')

    def right(self, speed=1.0):
        # self.left_motor.value = speed
        # self.right_motor.value = -speed
        requests.get('http://192.168.4.1/State?State=R')

    def stop(self):
        # self.left_motor.value = 0
        # self.right_motor.value = 0
        requests.get('http://192.168.4.1/State?State=S')
