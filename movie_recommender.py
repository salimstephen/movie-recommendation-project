#!/usr/bin/env python
# coding: utf-8



import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics.pairwise import cosine_similarity

import warnings
warnings.filterwarnings("ignore")

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 100)

print("Libraries loaded successfully")




import os
os.listdir("../data")




os.listdir("../data/movie-recommendation-hackathon-2026")




train = pd.read_csv("../data/movie-recommendation-hackathon-2026/train.csv")
test = pd.read_csv("../data/movie-recommendation-hackathon-2026/test.csv")
movies = pd.read_csv("../data/movie-recommendation-hackathon-2026/movies.csv")
imdb = pd.read_csv("../data/movie-recommendation-hackathon-2026/imdb_data.csv")
links = pd.read_csv("../data/movie-recommendation-hackathon-2026/links.csv")
tags = pd.read_csv("../data/movie-recommendation-hackathon-2026/tags.csv")




print("Dataset Shapes")
print("-" * 40)

print(f"Train dataset : {train.shape}")
print(f"Test dataset  : {test.shape}")
print(f"Movies dataset: {movies.shape}")
print(f"IMDb dataset  : {imdb.shape}")
print(f"Links dataset : {links.shape}")
print(f"Tags dataset  : {tags.shape}")




for name, df in [
    ("Train", train),
    ("Test", test),
    ("Movies", movies),
    ("IMDb", imdb),
    ("Links", links),
    ("Tags", tags)
]:
    print(f"\n{name} Dataset")
    print("-" * 30)
    print(df.columns.tolist())




train.head()




movies.head()




imdb.head()




train["rating"].describe()




import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))

train["rating"].hist(bins=10, edgecolor="black")

plt.title("Distribution of Movie Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Ratings")

plt.show()




movie_rating_counts = (
    train.groupby("movieId")["rating"]
    .count()
    .sort_values(ascending=False)
)




movie_rating_counts.head(10)




# Convert the Series into a DataFrame
movie_rating_counts = movie_rating_counts.reset_index()

# Rename the column
movie_rating_counts.columns = ["movieId", "rating_count"]

# Merge with the movies dataset
popular_movies = movie_rating_counts.merge(
    movies,
    on="movieId"
)

# Display the top 10
popular_movies.head(10)




user_rating_counts = (
    train.groupby("userId")["rating"]
    .count()
    .sort_values(ascending=False)
)

user_rating_counts.head(10)




import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))

user_rating_counts.hist(bins=50, edgecolor="black")

plt.title("Distribution of Number of Ratings per User")
plt.xlabel("Number of Ratings")
plt.ylabel("Number of Users")

plt.show()




print("Missing Values in Train Dataset")
print(train.isnull().sum())

print("\n" + "-"*40 + "\n")

print("Missing Values in Movies Dataset")
print(movies.isnull().sum())

print("\n" + "-"*40 + "\n")

print("Missing Values in IMDb Dataset")
print(imdb.isnull().sum())




# Split genres into separate values
genres = movies["genres"].str.split("|")

# Flatten the list of genres
all_genres = genres.explode()

# Count each genre
genre_counts = all_genres.value_counts()

# Display the top 10 genres
genre_counts.head(10)




movie_stats = (
    train
    .groupby("movieId")
    .agg(
        average_rating=("rating", "mean"),
        rating_count=("rating", "count")
    )
    .reset_index()
)

movie_stats.head()




popular_movies = movie_stats.merge(
    movies[["movieId", "title", "genres"]],
    on="movieId"
)

popular_movies.head()




popular_movies.sort_values(
    by=["rating_count", "average_rating"],
    ascending=False
).head(10)




sample_train = train[train["userId"] <= 5000]




sample_train.shape




print("Unique Users :", sample_train["userId"].nunique())
print("Unique Movies:", sample_train["movieId"].nunique())
print("Total Ratings:", len(sample_train))




sample_train = train[train["userId"] <= 1000]

print("Unique Users :", sample_train["userId"].nunique())
print("Unique Movies:", sample_train["movieId"].nunique())
print("Total Ratings:", len(sample_train))




user_movie_matrix = sample_train.pivot_table(
    index="userId",
    columns="movieId",
    values="rating"
)

user_movie_matrix.head()




user_movie_filled = user_movie_matrix.fillna(0)

user_movie_filled.head()




from sklearn.metrics.pairwise import cosine_similarity




user_similarity = cosine_similarity(user_movie_filled)




import pandas as pd

user_similarity_df = pd.DataFrame(
    user_similarity,
    index=user_movie_filled.index,
    columns=user_movie_filled.index
)

user_similarity_df.head()




user_similarity_df.loc[1].sort_values(ascending=False).head(10)




similar_users = user_similarity_df.loc[1].sort_values(ascending=False)[1:11]

similar_userssimilar_users = user_similarity_df.loc[1].sort_values(ascending=False)[1:11]

similar_users




similar_users_ratings = sample_train[
    sample_train["userId"].isin(similar_users.index)
]

similar_users_ratings.head()




user1_movies = sample_train[
    sample_train["userId"] == 1
]["movieId"]

user1_movies.head()




recommendation_candidates = similar_users_ratings[
    ~similar_users_ratings["movieId"].isin(user1_movies)
]

recommendation_candidates.head()




recommended_movies = (
    recommendation_candidates
    .groupby("movieId")["rating"]
    .mean()
    .sort_values(ascending=False)
)

recommended_movies.head(10)




recommended_movies = recommended_movies.reset_index()

recommended_movies = recommended_movies.merge(
    movies,
    on="movieId"
)

recommended_movies.head(10)





