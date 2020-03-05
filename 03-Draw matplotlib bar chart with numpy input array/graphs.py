from matplotlib import pyplot #python's plot
import csv
from collections import Counter
import numpy as np
def draw_multiline():    
    years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
    companyA = [41596, 46000, 48510, 53310, 57200, 56000, 63316, 69741] #profit of CompanyA
    companyB = [37596, 42000, 45510, 47310, 51200, 55000, 60316, 65741]
    companyC = [36596, 32010, 40510, 30310, 42200, 50100, 45116, 34741]
    #sketch-style drawing mode
    # pyplot.xkcd()
    # pyplot.style.use('dark_background')
    pyplot.plot(years, companyA, color='red', linestyle='--', marker='.', markersize=20)
    pyplot.plot(years, companyB, color='#000BFF', marker='.', markersize=10)
    pyplot.bar(years, companyC, color='#B40062')
    pyplot.xlabel("Year")
    pyplot.ylabel("Profit(USD)")
    pyplot.legend(["Company A", "Company B", "Company C"])
    pyplot.grid(True)
    # take photograph ?
    pyplot.savefig("multiline.png")
    pyplot.show()
    # print(pyplot.style.available)
def draw_bar():
    years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
    companyA = np.array([41596, 46000, 48510, 53310, 57200, 56000, 63316, 69741])
    companyB = np.array([37596, 42000, 45510, 47310, 51200, 55000, 60316, 65741])  
    companyC = np.array([36596, 32010, 40510, 30310, 42200, 50100, 45116, 34741])  
    #years - 0.2 ? using numpy
    BAR_WIDTH = 0.2
    pyplot.bar(years - BAR_WIDTH, companyA, color='red', width = BAR_WIDTH, label='Company A')
    pyplot.bar(years, companyB, color='green', width=BAR_WIDTH)
    pyplot.bar(years + BAR_WIDTH, companyC, color='blue', width=BAR_WIDTH)
    pyplot.legend(["Company A", "Company B", "Company C"])
    pyplot.xlabel("Year")
    pyplot.ylabel("Profit")
    pyplot.title("Profit / Year")
    pyplot.grid(True)
    pyplot.savefig("bargraph.png")
    pyplot.show()