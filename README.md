# Movie Recommendation System

A Python-based movie recommendation project that explores movie-rating data and implements **user-based collaborative filtering using cosine similarity**.

The project was developed as part of my Data Science learning journey, with a focus on understanding how recommendation systems can use historical user-rating behavior to identify similar users and generate personalized movie recommendations.

## Project Overview

Recommendation systems are widely used by platforms such as Netflix, Amazon, Spotify, and YouTube to help users discover relevant content.

This project explores the underlying data and demonstrates a user-based collaborative filtering approach:

* Analyze movie-rating and user activity data.
* Explore movie popularity, ratings, and genres.
* Build a user-movie rating matrix.
* Calculate similarity between users using cosine similarity.
* Identify users with similar rating patterns.
* Generate recommendation candidates from similar users.
* Remove movies already rated by the target user.
* Rank recommendation candidates using their average ratings.

The project focuses on understanding the recommendation process from the data level through to generating personalized recommendations.

## Dataset

The project uses a MovieLens-based movie recommendation dataset containing several related files:

| Dataset         | Description                                                        |
| --------------- | ------------------------------------------------------------------ |
| `train.csv`     | Historical user-movie ratings used for analysis and recommendation |
| `test.csv`      | User-movie pairs provided as part of the dataset                   |
| `movies.csv`    | Movie titles and genres                                            |
| `imdb_data.csv` | Additional movie metadata                                          |
| `links.csv`     | Links between MovieLens movie IDs and external databases           |
| `tags.csv`      | User-generated movie tags                                          |

The datasets are stored locally and are excluded from the Git repository through `.gitignore`.

## Exploratory Data Analysis

The project performs several exploratory analyses, including:

* Rating distribution
* Number of ratings per user
* Number of ratings per movie
* Average movie ratings
* Movie rating counts
* Genre frequency
* Missing-value checks
* Identification of highly rated and frequently rated movies

These analyses help provide context before building the recommendation component.

## Recommendation Approach

### User-Based Collaborative Filtering

The main recommendation approach uses **user-based collaborative filtering**.

The process is:

1. Select a subset of users for the similarity analysis.
2. Create a user-movie rating matrix.
3. Fill missing ratings with zero for the similarity calculation.
4. Calculate pairwise user similarity using cosine similarity.
5. Identify users most similar to the target user.
6. Collect movies rated by those similar users.
7. Remove movies already rated by the target user.
8. Calculate average ratings for recommendation candidates.
9. Rank the candidates to produce recommendations.

### Cosine Similarity

Cosine similarity is used to compare users based on their movie-rating patterns.

Conceptually:

```text
User Ratings
     |
     v
User-Movie Matrix
     |
     v
Cosine Similarity
     |
     v
Similar Users
     |
     v
Recommendation Candidates
     |
     v
Remove Already-Rated Movies
     |
     v
Rank Candidates
     |
     v
Movie Recommendations
```

## Popularity Analysis

The project also analyzes movie popularity using:

* Number of ratings received by each movie
* Average rating for each movie

Movies can therefore be ranked based on rating activity and average rating to understand which titles have the strongest overall engagement.

This analysis provides a useful baseline for understanding the dataset, while the collaborative filtering component provides personalized recommendations.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Jupyter Notebook
* Git
* GitHub

## Key Skills Demonstrated

* Exploratory Data Analysis
* Data Cleaning and Validation
* Data Transformation
* Data Aggregation
* User-Movie Matrix Construction
* Collaborative Filtering
* Cosine Similarity
* Recommendation Logic
* Data Visualization
* Python Programming
* Git and GitHub

## Project Structure

```text
Movie_Recommendation_Project_2026/
|
├── data/
├── models/
├── notebooks/
|   └── movie_recommender.ipynb
├── reports/
├── submission/
├── movie_recommender.py
├── project_notes.md
├── README.md
├── .gitignore
└── open_project.bat
```

## Limitations

This project is a learning-focused recommendation system prototype rather than a production recommendation engine.

Current limitations include:

* The similarity analysis uses a subset of users.
* Missing ratings are represented as zero when calculating user similarity.
* No formal recommendation evaluation metrics such as RMSE or MAE are implemented.
* The project does not currently compare multiple recommendation algorithms.
* The system has not been deployed as a web application or API.

## Future Improvements

Possible future improvements include:

* Item-based collaborative filtering
* Matrix factorization
* Hybrid recommendation systems
* Formal recommendation evaluation
* Improved handling of sparse rating data
* More efficient similarity calculations
* Interactive deployment using Streamlit
* Recommendation API development

## What I Learned

This project strengthened my understanding of:

* How recommendation systems use historical user behavior.
* How user-movie matrices represent rating interactions.
* How cosine similarity can identify users with similar preferences.
* How collaborative filtering can generate personalized recommendations.
* How exploratory analysis helps inform machine learning workflows.
* The importance of documenting projects and maintaining reproducible work with Git and GitHub.

## Author

**Stephen Otieno**

Data Science & Analytics practitioner building practical skills through hands-on projects, structured learning, and real-world datasets.

This project is part of my Data Science portfolio.
