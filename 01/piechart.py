import csv
import pandas as pd
from collections import Counter
from matplotlib import pyplot
class PieChart:
    def draw_pie_chart(self):
        slices = [9.4, 10.8, 11.3, 12.4, 24.8, 31.3]
        labels = ["C++", "C#", "Javascript", "PHP", "Python", "Java"]
        colors = ["#FA114F", "#04DE71", "#00F5EA", "#FF3B30", "#FFE620", "#2094FA"]
        explode = [0, 0.1, 0, 0, 0, 0]
        pyplot.title("Programming language chart")
        pyplot.pie(slices, labels=labels, colors=colors,
                   explode=explode,
                   startangle=0,
                   autopct='%1.3f%%',
                   wedgeprops={'edgecolor': 'white', 'linewidth': 1.5})
        pyplot.tight_layout()
        pyplot.show()