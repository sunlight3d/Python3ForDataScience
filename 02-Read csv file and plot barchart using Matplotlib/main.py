'''How to install matplotlib ?'''
from graphs import draw_multiline
from CsvReader import CsvReader
# draw_multiline()
csv_reader = CsvReader("movies.csv")
csv_reader.read_csv()
#csv_reader.draw_films_by_years()
csv_reader.draw_films_by_profits()
