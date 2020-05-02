import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
fig, ax = plt.subplots()
x = np.linspace(0,1,100)
ax.plot(x, np.sqrt(np.cos(x)), "b-",
        x, np.sin(x), 'r-.')
plt.show()
