import numpy as np
import matplotlib.pyplot as plt


def constant_algo(items):
    result = items[0] * items[0]
    print()


constant_algo([4, 5, 6, 8])


x = [2, 4, 6, 8, 10, 12]

y = [2, 2, 2, 2, 2, 2]

plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Constant Complexity')
plt.show()
