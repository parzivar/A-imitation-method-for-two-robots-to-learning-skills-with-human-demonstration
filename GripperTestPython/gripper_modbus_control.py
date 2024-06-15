import sys
import glob
import dh_modbus_gripper
import dh_socket_gripper
from time import sleep

class DhGripper:
    def __init__(self,gripper_port):
        self.gripper_port = gripper_port
        self.baudrate = 115200
        self.initstate = 0
        self.g_state = 0
        self.force = 100   # 预设设力和速度，范围是0-100
        self.speed = 100
        self.m_gripper = dh_modbus_gripper.dh_modbus_gripper()

        self.m_gripper.open(self.gripper_port, self.baudrate)
        self.m_gripper.Initialization()
        print('Send grip init')

        while (self.initstate != 1):
            self.initstate = self.m_gripper.GetInitState()
            sleep(0.2)

        self.m_gripper.SetTargetForce(self.force)
        self.m_gripper.SetTargetSpeed(self.speed)

    def gripper_close(self):
        self.m_gripper.SetTargetPosition(0)
        print("close success")

    def gripper_open(self):
        self.m_gripper.SetTargetPosition(1000)
        print("open success")

