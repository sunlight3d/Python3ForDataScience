import csv
import pandas as pd
from collections import Counter
from matplotlib import pyplot

# pd.read_csv()
class CsvReader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.films = []
    def read_csv(self):
        with open('movies.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                film_name = row['Film']
                genre = row['Genre']
                lead_studio = row['Lead Studio']
                audience_score = row['Audience score %']
                profit = row['Profit']
                year = row['Year']
                print('film_name: '+film_name +
                      ',genre : '+genre +
                      ',lead studio: '+lead_studio +
                      ',audience score: ' + audience_score +
                      ',profit : ' + profit +
                      ',year : ' + year)
                self.films.append({'film_name': film_name,
                                   'genre': genre,
                                   'lead_studio': lead_studio,
                                   'audience_score': audience_score,
                                   'profit': profit,
                                   'year': year})

    def draw_films_by_years(self):
        """Draw graph films/years"""
        # films_counter = Counter(self.years)
        # films_counter.get('2008')
        years = [int(film['year']) for film in self.films]
        counters = Counter(years)
        filtered_years = []
        number_of_films = []
        for key in counters.keys():
            filtered_years.append(key)
            number_of_films.append(counters.get(key))
        pyplot.barh(filtered_years, number_of_films, color='b', label="Films / years", height=0.5)
        pyplot.show()

    def draw_films_by_profits(self):
        film_names = [film['film_name'] for film in self.films]
        profits = [float(film['profit']) for film in self.films]
        pyplot.bar(film_names, profits, color='b', label="Films / Profits", width=0.2)
        pyplot.xticks(film_names, film_names, rotation='vertical')
        pyplot.show()
