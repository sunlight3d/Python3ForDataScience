from multipline import multiline
from bar import bar
from piechart import PieChart
from stackplot import StackPlot
from lineplot import LinePlot
from histogram import Histogram
from scatter import Scatter
# multiline()
# bar()
from csv_reader import CsvReader
from random import randint
csv_reader = CsvReader('movies.csv')
csv_reader.read_csv()
# csv_reader.draw_films_by_years()
# csv_reader.draw_films_by_profits()
# pie_chart = PieChart()
# pie_chart.draw_pie_chart()
# stack_plot = StackPlot()
# stack_plot.draw_stack_plot()
# line_plot = LinePlot()
# line_plot.draw_line_plot()

# histogram_plot = Histogram()
# histogram_plot.draw_histogram()

scatter_plot = Scatter()
# scatter_plot.draw_scatter()
scatter_plot.create_fake_csv()
# scatter_plot.draw_scatter_from_csv()
