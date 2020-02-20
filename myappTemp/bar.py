from matplotlib import pyplot
import numpy as np
def bar():
    #profits / company
    years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
    companyA = np.array([41596, 46000, 48510, 53310, 57200, 56000, 63316, 69741])
    companyB = np.array([37596, 42000, 45510, 47310, 51200, 55000, 60316, 65741])
    companyC = np.array([36596, 32010, 40510, 30310, 42200, 50100, 45116, 34741])
    print(pyplot.style.available)
    width = 0.2
    pyplot.bar(years-width, companyA, color='#00FF22',width = width,label="Company A")
    pyplot.bar(years, companyB,color='#000BFF',width = width)
    pyplot.bar(years+width, companyC,color='#B40062',width = width)

    pyplot.xlabel("Year")
    pyplot.xlabel("Profit(USD)")
    pyplot.title("Profit / Year")
    pyplot.legend(["Company A", "Company B", "Company C"])
    pyplot.grid(True)
    pyplot.savefig('myplot.png')

    pyplot.show()