import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,10000)
x = x[x**3 + 7 >= 0]
y = np.sqrt(x**3 + 7)

fig, ax = plt.subplots()
ax.plot(x,y, color='pink')
ax.plot(x,-y, color='pink')

ax.set(xlabel='x', ylabel='y', title='secp256k1')

fig.savefig("test.png")
plt.show()
