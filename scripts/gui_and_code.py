# Graphic for GUI vs code
from os.path import join as pjoin, dirname

import numpy as np
import matplotlib.pyplot as plt

plt.xkcd()


here = dirname(__file__)


def sigmoid(x, center, width, height=100):
    return height / (1 + np.e ** ((center - x) / width))


def normalize(vals):
    vals -= min(vals)
    return vals / max(vals)


fig, (easy_ax, hard_ax) = plt.subplots(1, 2, figsize=(11, 6))
x = np.arange(100)
gui = sigmoid(x, 15, 3) + x * 0.25
easy_ax.plot(x, normalize(gui) * 85, label='GUI')
easy_ax.plot(x, normalize(sigmoid(x, 40, 12)) * 100, label='Code')
easy_ax.set_xlabel('Experience')
easy_ax.set_ylabel('Productivity')
easy_ax.set_title('Easy tasks')
gui_h = sigmoid(x, 30, 10, 20) + x * 0.1
hard_ax.plot(x, normalize(gui_h) * 30, label='GUI')
hard_ax.plot(x, normalize(sigmoid(x, 50, 20)) * 100, label='Code')
hard_ax.set_xlabel('Experience')
hard_ax.legend()
hard_ax.set_title('Hard tasks');
fig.savefig(pjoin(here, '..', 'images', 'gui_and_code.png'), dpi=150)
