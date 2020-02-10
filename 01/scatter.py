import pandas as pd
from matplotlib import pyplot
import numpy as np
from random import randint
class Scatter:
    def draw_scatter(self):
        x = [1, 4, 5, 6, 7, 9, 12, 14, 17]
        y = [1, 4, 5, 6, 7, 9, 12, 14, 17]
        colors = [1, 4, 5, 6, 7, 9, 12, 14, 17]
        # point_size = 50
        point_size = [20, 50, 70, 60, 55, 66, 80, 90, 70]
        pyplot.scatter(x, y,
                       s=point_size,
                       # c='red',
                       c=colors,
                       edgecolors='black',
                       linewidths=2,
                       cmap="Reds", #only some fixed value
                       alpha=0.5
                       )
        colorbar = pyplot.colorbar()
        colorbar.set_label("Satisfaction")
        pyplot.show()
    def draw_scatter_from_csv(self):
        data = pd.read_csv('views.csv')
        view_counts = data["View Counts"]
        likes = data["Likes"]
        dislikes = data["Dislikes"]
        ratios = data["ratios"]
        import pdb
        pdb.set_trace()
        pyplot.scatter(view_counts, likes,
                       c=ratios,
                       edgecolors='black', linewidths=1, alpha=0.75)
        # pyplot.xscale('log')
        # pyplot.yscale('log')
        pyplot.xlabel("View Count")
        pyplot.ylabel("Total Likes")

        colorbar = pyplot.colorbar()
        colorbar.set_label("Likes/Dislike ratios")

        pyplot.show()
    def create_fake_csv(self):
        view_counts = []
        numbers_of_likes = []
        numbers_of_dislikes = []
        ratios = []
        for i in range(0, 10):
            view_count = randint(1000, 1000000)
            view_counts.append(view_count)
            likes = randint(0, view_count)
            numbers_of_likes.append(likes)
            dislikes = randint(0, view_count)
            numbers_of_dislikes.append(dislikes)
            ratio = likes / (dislikes + likes)
            ratio = round(ratio, 2)
            ratios.append(ratio)
        df = pd.DataFrame({"View Counts": view_counts, "Likes": likes, "Dislikes": dislikes, "ratios": ratios})
        df.to_csv('views.csv', header=True)