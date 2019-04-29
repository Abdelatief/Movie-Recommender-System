# import numpy as np
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt
import seaborn as sns
from TableMod import *

class Graphs:
    def __init__(self):
        # self.ratings_data = pd.read_csv(r'E:\Python Projects\Movie Recomender System\ml-latest-small\\ratings.csv')
        self.ratings_data = pd.read_csv(' ')
        print(self.ratings_data.head())

        # self.movie_names = pd.read_csv(r'E:\Python Projects\Movie Recomender System\ml-latest-small\\movies.csv')
        self.movie_names = pd.read_csv(' ')

        print(self.movie_names.head())
        print(self.movie_names.title.head())

        self.movie_data = pd.merge(self.ratings_data, self.movie_names, on='movieId')
        print(self.movie_data.head())

        # table of the mean of the movies' ratings sorted
        #############################################################################################
        self.movie_data.groupby('title')['rating'].mean().sort_values(ascending=False) # table for the mean of the movies
        self.ratings_mean_count = pd.DataFrame(self.movie_data.groupby('title')['rating'])
        print(type(self.movie_data.groupby('title')['rating'].mean().sort_values(ascending=False)))
        #############################################################################################
        # table of the count of the ratings sorted
        #############################################################################################
        print(self.movie_data.groupby('title')['rating'].count().sort_values(ascending=False))  # table for the count of the ratings
        #############################################################################################
        self.ratings_mean_count = pd.DataFrame(self.movie_data.groupby('title')['rating'].mean())
        # table for the mean & count grouped by title
        print(self.ratings_mean_count.head())

        self.ratings_mean_count['rating_counts'] = pd.DataFrame(self.movie_data.groupby('title')['rating'].count())

        print(self.ratings_mean_count['rating_counts'].head())


        sns.set_style('dark')

        '''
        plt.figure(figsize=(8,6))
        plt.rcParams['patch.force_edgecolor'] = True
        ratings_mean_count['rating_counts'].hist(bins=50)
        '''

        # histogram for the mean count ratings
        ############################################################################################
    def hist(self):
        plt.rcParams['patch.force_edgecolor'] = True
        plt.hist(self.ratings_mean_count['rating_counts'], bins=50)
        plt.show()
        ############################################################################################
    def piechart(self):
        plt.figure(figsize=(5, 5))
        titles_list = list(self.ratings_mean_count.index.values)
        ratings_list = list(self.ratings_mean_count['rating'])
        print('\n')
        pprint(titles_list)
        pprint(ratings_list)

        plt.pie(ratings_list[0:5], labels=titles_list[0:5], autopct="%.1f%%")
        plt.show()
        ############################################################################################
    def barchart(self):
        plt.figure(figsize=(8, 6))
        plt.rcParams['patch.force_edgecolor'] = True
        self.ratings_mean_count['rating'].hist(bins=50)
        plt.show()

    def mean_table(self):
        table = Table(self.ratings_mean_count)
        table.show()

'''
        print(self.ratings_mean_count.head())
        ############################################################################################
        user_movie_rating = self.movie_data.pivot_table(index='userId', columns='title', values='rating')
        print(user_movie_rating.head())
        # top five ratings of the movie
        ############################################################################################
        forrest_gump_rating = user_movie_rating['Forrest Gump (1994)']
        print(forrest_gump_rating.head())
        ############################################################################################
'''

if __name__ == '__main__':
    g = Graphs()
    # g.hist()
    g.mean_table()