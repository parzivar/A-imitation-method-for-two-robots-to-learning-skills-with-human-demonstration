import time
import socket
import csv
from gripper_modbus_control import DhGripper

class AbbRobot:
    def __init__(self, host, robot_port, gripper_port=None, workspace_limits=None, use_dh_griper=False, use_camera=False) -> None:
        if workspace_limits is None:
            workspace_limits = [[-1, 1], [-1, 1], [0, 1]]
        self.host = host
        self.port = robot_port
        self.workspace_limits = workspace_limits
        self.use_dh_griper = use_dh_griper
        self.use_camera = use_camera
        if self.use_dh_griper:
            self.gripper = DhGripper(gripper_port)
        if self.use_camera:
            pass

        # 需要更改
        self.home = [602.66, 218, 474, 0.62804, -0.32469, -0.65242, -0.27292]
        # self.home = [383.48, 419.32, 593.36,1,0,0,0]
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def movel(self, target):

        data = f"MOVEL,{target[0]},{target[1]},{target[2]},{target[3]},{target[4]},{target[5]},{target[6]})"
        self.socket.send(str.encode(data))

        while self.socket.recv(1024) != b'ok':
            time.sleep(0.00001)
        print("movel success")
        # self.socket.close()

    def movej(self, target):
        # self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.socket.connect((self.host, self.port))

        data = f"MOVEJ,{target[0]},{target[1]},{target[2]},{target[3]},{target[4]},{target[5]},{target[6]})"
        self.socket.send(str.encode(data))

        while self.socket.recv(1024) != b'ok':
            time.sleep(0.00001)
        print("movej success")
        # self.socket.close()

    def moveabsj(self, target):
        data = f"MOVEAbsJ,{target[0]},{target[1]},{target[2]},{target[3]},{target[4]},{target[5]}"
        self.socket.send(str.encode(data))

        while self.socket.recv(1024) != b'ok':
            time.sleep(0.00001)
        print("moveabsj success")
        # self.socket.close()

    def read_csv_file(self, filename, start_idx, end_idx):
        joint_angles = []
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                joint_angles.append([float(x) for x in row[start_idx:end_idx]])
        print("read data success")
        return joint_angles

    def go_home(self):
        self.movej(self.home)
        print("go home success")

if __name__ == "__main__":
    robot = AbbRobot("192.168.10.20", 1024)
    robot.go_home()
    # robot.move_to_target_joint([3.92, 71.22, -47.40, 172.59, 24.92,53.78])
    robot.moveabsj([63.92, 71.22, -47.40, 172.59, 24.92,-53.78])
    # print(robot.home)