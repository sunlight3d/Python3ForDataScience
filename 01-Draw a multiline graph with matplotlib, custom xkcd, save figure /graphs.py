from matplotlib import pyplot #python's plot
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