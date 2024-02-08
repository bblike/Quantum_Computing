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
for i in temp:

    xs.append(float(i[1]))
    y1s.append(round(float(i[2]), 3))
    y2s.append(round(float(i[3]), 3))
    y3s.append(round(float(i[4]), 3))

plt.figure()

plt.scatter(xs, y1s, label = "99")
plt.scatter(xs, y2s, label = "95")
plt.scatter(xs, y3s, label = "90")
plt.ylim(0, 1.2)
plt.legend()
plt.show()
