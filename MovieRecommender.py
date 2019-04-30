# import numpy as np
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt
import seaborn as sns
from TableMod import *
from sys import stderr


class Graphs:
    def __init__(self):

        self.ratings_data = pd.read_csv('ratings.csv')
       # print(self.ratings_data.head())

        self.movie_names = pd.read_csv('movies.csv')

        self.ratings_data = pd.read_csv(r"ratings.csv")
       # print(self.ratings_data.head())

        self.movie_names = pd.read_csv(r"movies.csv")
        # print(self.movie_names.head())
        # print(self.movie_names.title.head())

        self.movie_data = pd.merge(self.ratings_data, self.movie_names, on='movieId')
        self.ratings_mean_count = pd.DataFrame(self.movie_data.groupby('title')['rating'])
        self.ratings_mean_count = pd.DataFrame(self.movie_data.groupby('title')['rating'].mean())
        self.ratings_mean_count['rating_counts'] = pd.DataFrame(self.movie_data.groupby('title')['rating'].count())
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
        # print('\n')
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
        try:
            self.table = Table(self.ratings_mean_count)
            self.table.show()
        except IndexError:
            print(str(IndexError), file=stderr)

    def correlation_table(self, movie_name):

        user_movie_rating = self.movie_data.pivot_table(index='userId', columns='title', values='rating')
        forrest_gump_ratings = user_movie_rating[movie_name]  # instead of forrest gumb  name of a variable
        movies_like_forest_gump = user_movie_rating.corrwith(forrest_gump_ratings)
        corr_forrest_gump = pd.DataFrame(movies_like_forest_gump, columns=['Correlation'])
        print(corr_forrest_gump)
        corr_forrest_gump.dropna(inplace=True)
        corr_forrest_gump = corr_forrest_gump.join(self.ratings_mean_count['rating_counts'])
        # print(corr_forrest_gump[corr_forrest_gump['rating_counts'] > 50].sort_values('Correlation', ascending=False).head())
        correlation_df = corr_forrest_gump[corr_forrest_gump['rating_counts'] > 50].sort_values('Correlation', ascending=False).head()
        # print(correlation_df)
        table = Table(correlation_df)
        table.show()
        return table

    def boxplot(self):
        pass



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
