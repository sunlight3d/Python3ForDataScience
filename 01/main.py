from multipline import multiline
from bar import bar
# multiline()
# bar()
from csv_reader import CsvReader
csv_reader = CsvReader('movies.csv')
csv_reader.read_csv()
# csv_reader.draw_films_by_years()
csv_reader.draw_films_by_profits()