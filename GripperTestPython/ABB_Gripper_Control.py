from robot_socket_control import AbbRobot
from time import sleep
import threading

def run():
    left_robot = AbbRobot("192.168.10.20", 1024, "com3")
    right_robot = AbbRobot("192.168.10.10", 1024, "com4")
    filename = 'inferred_trajectory3.csv'  # replace with your CSV file name
    left_joint_angles = left_robot.read_csv_file(filename, 3, 9)
    right_joint_angles = right_robot.read_csv_file(filename, 12, 18)
    left_robot.moveabsj([-47.35, 18.98, 38.73, -131.18, 65.45, -22.98])   # left home
    print("move left home success")
    # right_robot.movej([602.66, 218, 474, 0.62804, -0.32469, -0.65242, -0.27292])
    right_robot.moveabsj([61.03, 32.26, 51.80, -179.96, 81.38, -6.32])  # right home
    print("move right home success")
    # 在实例上调用方法
    # left_robot.gripper.gripper_open()
    # right_robot.gripper.gripper_open()
    # sleep(2)

    # BIP
    def move_left_robot():
        for i in range(0, len(left_joint_angles), 20):
            print("left joint angles", left_joint_angles[i])
            left_robot.moveabsj(left_joint_angles[i])
            sleep(0.01)
    def move_right_robot():
        for j in range(0, len(right_joint_angles), 20):
            print("right joint angles", right_joint_angles[j])
            right_robot.moveabsj(right_joint_angles[j])
            sleep(1)
    # 创建双线程
    right_thread = threading.Thread(target=move_right_robot)
    left_thread = threading.Thread(target=move_left_robot)
    # 启动
    left_thread.start()
    right_thread.start()

    left_thread.join()
    right_thread.join()
    print("BIP progress finished")

    # robot.go_home()
    left_robot.socket.close()
    right_robot.socket.close()
if __name__ == "__main__":
    run()

    # robot.movel([7.76,736.38,198.43,0,1,0,0])
    # robot.move_to_target_joint([63.92, 71.22, -47.40, 172.59, 24.92,3.78])
    # robot.move_to_target_joint([3.92, 71.22, -47.40, 172.59, 24.92,53.78])
    # robot.move_to_target_joint([63.92, 71.22, -47.40, 172.59, 24.92,-53.78])
    # robot.move_to_target_joint([94.49, 57.45, -36.40, 71.72, 8.10, -0.15])
    # robot.move_to_target_joint([81.82, -28.39, 54.27, 0, 64.12, -98.08])
    # robot.movel([47.76,336.38,298.43,0,1,0,0])




