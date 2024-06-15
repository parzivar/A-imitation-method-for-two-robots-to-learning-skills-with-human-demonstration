import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
csv_file = 'box_out.csv'  # 将'your_file.csv'替换为你的CSV文件路径
data = pd.read_csv(csv_file)

# 获取左臂和右臂的关节角
left_arm_angles = data.iloc[:, 3:9]  # [3, 8]列是左臂
right_arm_angles = data.iloc[:, 12:18]  # [12, 17]列是右臂

# 绘制左臂关节角图
plt.figure(figsize=(10, 6))
for i in range(left_arm_angles.shape[1]):
    plt.plot(left_arm_angles.index, left_arm_angles.iloc[:, i], label=f'Left Joint {i+1}')
plt.title('Left Arm Joint Angles')
plt.xlabel('Time')
plt.ylabel('Angle (degrees)')
plt.legend()
plt.grid(True)
plt.show()

# 绘制右臂关节角图
plt.figure(figsize=(10, 6))
for i in range(right_arm_angles.shape[1]):
    plt.plot(right_arm_angles.index, right_arm_angles.iloc[:, i], label=f'Right Joint {i+1}')
plt.title('Right Arm Joint Angles')
plt.xlabel('Time')
plt.ylabel('Angle (degrees)')
plt.legend()
plt.grid(True)
plt.show()