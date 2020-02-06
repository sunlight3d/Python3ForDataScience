import csv
import pandas as pd
from matplotlib import pyplot
import numpy as np
class LinePlot:
    def draw_line_plot(self):
        data = pd.read_csv("salaries.csv")
        ages = data['Age']
        fullstack_salaries = data['FullStack Dev']
        java_salaries = data['Java']
        python_salaries = data['Python']
        csharp_salaries = data['C#']
        median = np.median(np.concatenate([np.array(java_salaries), np.array(python_salaries), np.array(csharp_salaries)]))
        medians = median * np.ones(len(ages))
        # print("median = " + str(median))
        # "#04DE71", "#00F5EA", "#FF3B30"
        pyplot.plot(ages, fullstack_salaries,
                    color="#04DE71",
                    linestyle='--',
                    label="Fullstack Developer"
                    )
        pyplot.plot(ages, java_salaries,
                    color="#00F5EA",
                    label="Java"
                    )
        pyplot.plot(ages, python_salaries,
                    color="pink",
                    label="Python"
                    )
        pyplot.plot(ages, csharp_salaries,
                    color="#2094FA",
                    label="C#"
                    )
        pyplot.plot(ages, medians,
                    color="r",
                    label="Median = " + str(median)
                    )
        pyplot.style.use('dark_background')
        # pyplot.fill_between(ages, fullstack_salaries,
        #                     # alpha=0.8,
        #                     median,
        #                     where=(fullstack_salaries > median),
        #                     interpolate=True,
        #                     alpha=0.5,
        #                     color='r'
        #                     )
        # pyplot.fill_between(ages, fullstack_salaries,
        #                     # alpha=0.8,
        #                     median,
        #                     where=(fullstack_salaries <= median),
        #                     interpolate=True,
        #                     alpha=0.5,
        #                     color='green'
        #                     )
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
        pyplot.title("Salary by Age")
        pyplot.xlabel("Ages")
        pyplot.ylabel("Salaries")
        pyplot.show()
