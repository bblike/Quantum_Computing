import numpy as np
import matplotlib.pyplot as plt

# 初始化参数
num_qubits = 1000
total_time = 1.0  # 总时间
time_step = 0.01  # 演化时间步长
jump_probability = 0.01  # 跃迁的概率
results = []

# 初始化波函数，所有比特都在[0, 1]态
wave_functions = np.sqrt(0.5) * np.array([[1, 1], [1, -1]])

# 记录处于[1, 0]态的比特数量
num_qubits_in_10 = []

# 模拟时间演化
for t in np.arange(0, total_time, time_step):
    num_10_state = 0

    for qubit in range(num_qubits):
        # 生成随机数r
        r = np.random.rand()

        # 计算波函数的模长的平方
        prob_00 = np.abs(wave_functions[0, 0])**2
        prob_10 = np.abs(wave_functions[1, 0])**2

        # 发生跃迁
        if r > prob_00:
            wave_functions = np.array([[1, 0], [0, 0]], dtype=complex)
        else:
            wave_functions /= np.linalg.norm(wave_functions)  # 归一化波函数

        # 记录处于[1, 0]态的比特数量
        if wave_functions[1, 0] == 1:
            num_10_state += 1

    # 记录数据
    num_qubits_in_10.append(num_10_state)
    results.append([t, num_10_state])

# 绘制处于[1, 0]态的比特数量随时间的变化
time, num_10_state = zip(*results)
plt.plot(time, num_10_state)
plt.xlabel("Time")
plt.ylabel("Number of Qubits in [1, 0] State")
plt.show()
