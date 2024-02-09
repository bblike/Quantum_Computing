import matplotlib.pyplot as plt
import numpy as np
f = open("text.txt", "r")
temp = []
for l in f.readlines():
    temp.append(l.strip().split("\t"))

    f.close()
print(temp)
xs = []
y1s = []
y2s = []
y3s = []
for i in temp[1:]:

    xs.append(float(i[9]))
    y1s.append(round(float(i[2]), 3))
    y2s.append(round(float(i[3]), 3))
    y3s.append(round(float(i[4]), 3))

xs = np.log10(xs)
plt.figure()

plt.scatter(xs, y1s, label = "1%")
plt.scatter(xs, y2s, label = "5%")
plt.scatter(xs, y3s, label = "10%")
plt.ylim(0, 1.2)
plt.xlabel("$log_{10}$(time steps/s)")
plt.ylabel("probability")
plt.legend()
plt.title("Percentages of errors due to time steps")
plt.show()
