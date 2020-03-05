from matplotlib import pyplot #python's plot
import csv
from collections import Counter
import numpy as np
import pandas as pd

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

def draw_histogram():
    data = pd.read_csv("ages.csv")
    customerIds = data["CustomerId"]
    ages = data["Age"]
    bins = np.arange(10, 50, 0.5)
    pyplot.hist(ages, bins = bins, edgecolor = "#04DE71", log=True)
    median_age = np.median(np.array(ages))
    pyplot.axvline(median_age, color='red', label="Age Medium")
    print("median = "+str(median_age))
    pyplot.title("Histogram example")
    pyplot.xlabel("Ages")
    pyplot.ylabel("Number of persons")
    pyplot.show()    
def draw_line_plot():
    data = pd.read_csv("salaries.csv")
    ages = data["Age"]
    fullstack_salaries = data["FullStack Dev"]
    java_salaries = data["Java"]
    python_salaries = data['Python']
    csharp_salaries = data['C#']
    #How to calculate median ?
    median = np.median(np.concatenate([np.array(java_salaries), 
                        np.array(python_salaries), np.array(csharp_salaries)]))
    medians = median * np.ones(len(ages))
    pyplot.plot(ages, fullstack_salaries,
                color='#04DE71',
                linestyle='--',
                label="Fullstack Developer"
                )
    pyplot.plot(ages, java_salaries,
                color='#00F5EA',                
                label="Java Salaries"
                )            
    pyplot.plot(ages, python_salaries,
                color='pink',                
                label="Python dev"
                ) 
    pyplot.plot(ages, csharp_salaries,
                    color="#2094FA",
                    label="C#"
                    )
    pyplot.plot(ages, medians,
                    color="red",
                    label="Median = "+str(median)
                    )   
    pyplot.fill_between(ages, 
                       fullstack_salaries, 
                       median,
                       where=(fullstack_salaries > median),
                       alpha=0.5,
                       color='red',
                       interpolate=True
                       )   
    pyplot.fill_between(ages, fullstack_salaries,                            
                        median,
                        where=(fullstack_salaries <= median),
                        interpolate=True,
                        alpha=0.5,
                        color='green'
                        )   
    pyplot.fill_between(ages, csharp_salaries, python_salaries,
                        where=(csharp_salaries >= python_salaries),
                        interpolate=True,
                        color='yellow'
                        )  
    pyplot.fill_between(ages, csharp_salaries,python_salaries,
                        where=(csharp_salaries < python_salaries),
                        interpolate=True,
                        color='purple'
                        )                               
    pyplot.legend()                 
    pyplot.show()
