import csv
from collections import Counter
from matplotlib import pyplot
class CsvReader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.films = []

    def read_csv(self):
        self.films = []
        with open(self.file_name) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:         
                film_name = row['Film']
                genre = row['Genre']
                lead_studio = row['Lead Studio']
                audience_score = row['Audience score %']
                profit = row['Profit']
                year = row['Year']            
                self.films.append({'film_name': film_name,
                            'genre': genre,
                            'lead_studio': lead_studio,
                            'audience_score': audience_score,
                            'profit': profit,
                            'year': year})            
        print("End of reading CSV file")
    
    def draw_films_by_years(self):
        #How many films in 2002, how many films in 2005, ....
        years = [int(film['year']) for film in self.films]
        counters = Counter(years)
        filtered_years = []
        number_of_films = []
        for key in counters.keys():
            filtered_years.append(key)
            number_of_films.append(counters.get(key))
        pyplot.barh(filtered_years, number_of_films, 
                    color='blue',
                    label="Films / years"                
                    )
        pyplot.show()        
    
    def draw_films_by_profits(self):
        film_names = [film['film_name'] for film in self.films]
        profits = [float(film['profit']) for film in self.films]
        pyplot.bar(film_names, profits, color='b', label="Films / Profits", width=0.2)
        pyplot.show()