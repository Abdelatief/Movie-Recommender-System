# import numpy as np
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt
import seaborn as sns

ratings_data = pd.read_csv(r'E:\Python Projects\Movie Recomender System\ml-latest-small\\ratings.csv')
print(ratings_data.head())

movie_names = pd.read_csv(r'E:\Python Projects\Movie Recomender System\ml-latest-small\\movies.csv')
print(movie_names.head())
print(movie_names.title.head())

movie_data = pd.merge(ratings_data, movie_names, on='movieId')
print(movie_data.head())

# table of the mean of the movies' ratings sorted
#############################################################################################
print(movie_data.groupby('title')['rating'].mean().sort_values(ascending=False))  # table for the mean of the movies
#############################################################################################
# table of the count of the ratings sorted
#############################################################################################
print(movie_data.groupby('title')['rating'].count().sort_values(ascending=False))  # table for the count of the ratings
#############################################################################################
ratings_mean_count = pd.DataFrame(movie_data.groupby('title')['rating'].mean())
# table for the mean & count grouped by title
print(ratings_mean_count.head())

ratings_mean_count['rating_counts'] = pd.DataFrame(movie_data.groupby('title')['rating'].count())

print(ratings_mean_count['rating_counts'].head())


sns.set_style('dark')

'''
plt.figure(figsize=(8,6))
plt.rcParams['patch.force_edgecolor'] = True
ratings_mean_count['rating_counts'].hist(bins=50)
'''

# histogram for the mean count ratings
############################################################################################
plt.rcParams['patch.force_edgecolor'] = True
plt.hist(ratings_mean_count['rating_counts'], bins=50)
plt.show()
############################################################################################

plt.figure(figsize=(5, 5))
titles_list = list(ratings_mean_count.index.values)
ratings_list = list(ratings_mean_count['rating'])
print('\n')
pprint(titles_list)
pprint(ratings_list)

plt.pie(ratings_list[0:5], labels=titles_list[0:5], autopct="%.1f%%")
plt.show()
############################################################################################
plt.figure(figsize=(8, 6))
plt.rcParams['patch.force_edgecolor'] = True
ratings_mean_count['rating'].hist(bins=50)
plt.show()

print(ratings_mean_count.head())
############################################################################################
user_movie_rating = movie_data.pivot_table(index='userId', columns='title', values='rating')
print(user_movie_rating.head())
# top five ratings of the movie
############################################################################################
forrest_gump_rating = user_movie_rating['Forrest Gump (1994)']
print(forrest_gump_rating.head())
############################################################################################
