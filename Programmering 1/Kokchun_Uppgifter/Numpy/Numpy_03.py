#importearr numpy o matplotlib
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(1,11)
y = 3*x+1

plt.plot(x,y)
plt.title("The loops of loops has begun\nand youre STUCK in it!)")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()