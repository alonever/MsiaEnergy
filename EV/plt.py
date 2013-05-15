#import matplotlib libary
import matplotlib.pyplot as plt
import numpy as np

#define some data
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]

plt.figure(1)
#plot data
plt.plot(x, y, linestyle="dashed", marker="o", color="green")

#configure  X axes
plt.xlim(0.5,4.5)
plt.xticks([1,2,3,4])

#configure  Y axes
plt.ylim(19.8,21.2)
plt.yticks([20, 21, 20.5, 20.8])

#labels
plt.xlabel("this is X")
plt.ylabel("this is Y")

#title
plt.title("Simple plot")

plt.figure(2)
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')

#show plot
plt.show()