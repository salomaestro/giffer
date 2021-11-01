import numpy as np
import matplotlib.pyplot as plt
from giffer import Gif
import os

# set a path
path = os.path.dirname(__file__)

# initialize gif object
gif = Gif(path)

# construct plots
fig, axs = plt.subplots(2, 1)

x = np.arange(100)
for i in range(10):

    # clear axes
    axs[0].cla()
    axs[1].cla()

    y1 = np.sin(x * i)
    y2 = np.cos(x * i)
    
    axs[0].plot(x, y1)
    axs[1].plot(x, y2)
    
    # make animation
    plt.pause(0.1)

    # capture frame
    gif.frame()

# save and combine to a .gif
gif.save("my_gif.gif")