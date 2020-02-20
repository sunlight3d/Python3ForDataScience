import csv
import pandas as pd
from matplotlib import pyplot
import numpy as np
class Histogram:
    def draw_histogram(self):
        # ages = [18, 16, 17,19, 18, 16, 17, 22, 23, 22, 21, 22, 23, 23, 35, 36]
        data = pd.read_csv("ages.csv")
        customerIds = data["CustomerId"]
        ages = data["Age"]
        #bins = [10, 12, 14, 16, 18]
        bins = np.arange(0, 100, 20)
        pyplot.hist(ages, bins=bins, edgecolor="#04DE71",log=True)
        median_age = np.median(np.array(ages))
        print("median = "+str(median_age))
        pyplot.axvline(median_age, color="red", label="Age Medium")
        pyplot.title("Histogram example")
        pyplot.xlabel("Ages")
        pyplot.ylabel("Number of persons")
        pyplot.show()
