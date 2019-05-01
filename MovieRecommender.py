import numpy as np
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt
import seaborn as sns
from TableMod import *
from sys import stderr
import seaborn as sns


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
        self.ratings = pd.DataFrame(self.movie_data.groupby('title')['rating'])
        self.ratings_mean_count = pd.DataFrame(self.movie_data.groupby('title')['rating'].mean())
        self.ratings_mean_count['rating_counts'] = pd.DataFrame(self.movie_data.groupby('title')['rating'].count())
        sns.set_style('dark')
        # def of correlation
        #####################################################################




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

    def correlation_table(self, movie):
        ''''
        self.user_movie_rating = self.movie_data.pivot_table(index='userId', columns='title', values='rating')
        self.movie_ratings = self.user_movie_rating[movie_name]
        self.movies_like_the_movie = self.user_movie_rating.corrwith(self.movie_ratings)
        self.corr_movie = pd.DataFrame(self.movies_like_the_movie, columns=['Correlation'])
        self.corr_movie.dropna(inplace=True)
        self.corr_movie = self.corr_movie.join(self.ratings_mean_count['rating_counts'])
        self.correlation_df = self.corr_movie[self.corr_movie['rating_counts'] > 100].sort_values('Correlation', ascending=False)
        plt.show()
        '''
        self.data_rating = pd.read_csv('ratings.csv', index_col=0)
        self.data_movie = pd.read_csv('movies.csv', index_col=0)
        self.merged_data = pd.merge(self.data_movie, self.data_rating, on='movieId')
        self.ratings_merged = pd.DataFrame(self.merged_data.groupby(movie)['rating'])
        print(self.ratings_merged)
        corr = self.ratings_merged.corr()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        cax = ax.matshow(corr, cmap='plasma', vmin=-1, vmax=1)
        fig.colorbar(cax)
        ticks = np.arange(0, len(self.ratings_merged.columns), 1)
        ax.set_xticks(ticks)
        plt.xticks(rotation=90)
        ax.set_yticks(ticks)
        ax.set_xticklabels(self.ratings_merged.columns)
        ax.set_yticklabels(self.ratings_merged.columns)
        plt.show()

    def boxplot(self):
        self.ratings_head=self.ratings_mean_count.head(5)
        self.ratings_head.boxplot(by='rating', column=['rating_counts'], grid=False)
        plt.show()

        # bplot=sns.boxplot(data=self.ratings_mean_count,width=.5,palette="colorblind")




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
    g.hist()
    g.mean_table()
    g.correlation_table()
