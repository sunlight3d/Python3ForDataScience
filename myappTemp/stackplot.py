import csv
import pandas as pd
from collections import Counter
from matplotlib import pyplot
import numpy as np
class StackPlot:
    def draw_stack_plot(self):
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # x = np.arange(1, 10, 1)
        y1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y2 = [2, 4, 3, 6.1, 7, 3.2, 4, 6.2 , 6, 8]
        y3 = [1.4, 2.5, 4, 3, 9, 10, 12, 13, 12, 14]
        colors = ["#00F5EA", "#FF3B30", "#04DE71"]
        labels = ["Player 1", "Player 2", "Player 3"]
        pyplot.stackplot(x, y1, y2, y3, labels=labels, colors=colors)
        pyplot.legend(
            # loc="upper left"
            loc=(0.1, 0.5)
        )
        pyplot.title("Player's point / minute")
        pyplot.show()
