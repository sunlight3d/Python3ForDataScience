from matplotlib import pyplot
import numpy as np
def multiline():
    #profits / company
    years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
    companyA = [41596, 46000, 48510, 53310, 57200, 56000, 63316, 69741]
    companyB = [37596, 42000, 45510, 47310, 51200, 55000, 60316, 65741]
    companyC = [36596, 32010, 40510, 30310, 42200, 50100, 45116, 34741]
    print(pyplot.style.available)
    # pyplot.style.use('dark_background')
    # pyplot.xkcd() #sketch-style drawing mod
    pyplot.plot(years, companyA, color='#00FF22')
    #marker - line - color
    #pyplot.plot(years, companyB, 'k--')
    pyplot.plot(years, companyB, color='#000BFF', linestyle='--', marker='.')
    # pyplot.plot(years, companyC, color='#ff00ff', marker='.')
    pyplot.bar(years, companyC, color='#B40062')

    pyplot.xlabel("Year")
    pyplot.xlabel("Profit(USD)")
    pyplot.title("Profit / Year")
    pyplot.legend(["Company A", "Company B", "Company C"])
    pyplot.grid(True)
    pyplot.savefig('myplot.png')

    pyplot.show()