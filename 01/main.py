from multipline import multiline
from bar import bar
from piechart import PieChart
from stackplot import StackPlot
from lineplot import LinePlot
# multiline()
# bar()
from csv_reader import CsvReader
csv_reader = CsvReader('movies.csv')
csv_reader.read_csv()
# csv_reader.draw_films_by_years()
# csv_reader.draw_films_by_profits()
# pie_chart = PieChart()
# pie_chart.draw_pie_chart()
# stack_plot = StackPlot()
# stack_plot.draw_stack_plot()
line_plot = LinePlot()
line_plot.draw_line_plot()