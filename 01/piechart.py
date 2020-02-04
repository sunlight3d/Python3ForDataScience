import csv
import pandas as pd
from collections import Counter
from matplotlib import pyplot
class PieChart:
    def draw_pie_chart(self):
        slices = [9.4, 10.8, 11.3, 12.4, 24.8, 31.3]
        labels = ["C++", "C#", "Javascript", "PHP", "Python", "Java"]
        colors = [""]