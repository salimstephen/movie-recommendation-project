# Movie Recommendation Project Journal

This journal documents the complete development process of the Movie Recommendation System, including the reasoning behind each step, the insights discovered, and how every stage contributes to building a reliable recommendation model.

---

# Day 1: Project Understanding & Data Loading

## Objective

Understand the machine learning problem and successfully load all datasets required for the project.

---

## Machine Learning Problem

The objective of this project is to build a recommendation system capable of predicting how a user is likely to rate a movie.

**Input**

- User ID
- Movie ID

**Output**

- Predicted movie rating

This is a **supervised machine learning regression problem**, since the model learns from historical user ratings.

---

## Datasets Loaded Successfully

### 1. Training Dataset (`train.csv`)

**Shape:** **10,000,038 rows × 4 columns**

**Columns**

- userId
- movieId
- rating
- timestamp

This dataset contains historical ratings given by users and serves as the primary training dataset.

---

### 2. Movies Dataset (`movies.csv`)

**Shape:** **62,423 rows × 3 columns**

**Columns**

- movieId
- title
- genres

This dataset provides descriptive information about every movie.

---

## Initial Observations

- Data loaded successfully without structural issues.
- Ratings range from **0.5 to 5.0**.
- Dataset size is large enough for building recommendation models.
- Movie information is stored separately from user ratings to reduce duplication.

---

## Key Insight

The recommendation system learns from previous user behavior.

The model studies historical ratings to predict how users may rate movies they have not watched.

---

## Next Step

Understand every dataset before beginning exploratory data analysis.

---

# Day 2: Project Setup & Version Control

## Objective

Create a professional project structure and integrate version control to track development.

---

## Environment Setup

Successfully configured the project environment.

- Opened Jupyter Notebook using:

```bash
python -m notebook
```

- Verified notebook:

```
movie_recommender.ipynb
```

---

## Git Version Control

Completed the initial Git workflow.

- Initialized Git repository.
- Created the first commit.
- Connected the project to GitHub.
- Learned how to stage, commit, and push changes.
- Configured `.gitignore` to exclude large datasets from version control.

---

## Project Structure

```text
Movie_Recommendation_Project_2026/
│
├── data/
├── notebooks/
├── models/
├── reports/
├── submission/
├── project_notes.md
├── README.md
└── .gitignore
```

---

## Key Insight

Version control is an essential part of professional data science.

Using Git allows every experiment, improvement, and milestone to be tracked and restored whenever necessary.

---

## Next Step

Begin exploring the datasets to understand how they relate to one another.

---

# Day 3: Understanding the Data

## Objective

Understand the purpose of every dataset and how they work together to solve the recommendation problem.

---

## Datasets Explored

### train.csv

Contains historical user ratings.

Each row represents one user rating for one movie.

This is the dataset the recommendation model learns from.

---

### test.csv

Contains user–movie pairs whose ratings must be predicted.

---

### movies.csv

Contains movie titles and genres.

This dataset provides descriptive information about each movie.

---

### imdb_data.csv

Contains additional movie metadata including:

- Cast
- Director
- Runtime
- Budget
- Plot Keywords

These features may later support content-based recommendation.

---

### links.csv

Maps MovieLens movie IDs to external movie databases.

---

### tags.csv

Contains user-generated descriptive tags for movies.

---

## Relationships Between Datasets

The common key connecting the datasets is:

**movieId**

This allows movie information to be merged with user ratings whenever additional movie details are required.

---

## Key Observations

- The training dataset contains user behavior.
- The movies dataset contains movie characteristics.
- The IMDb dataset enriches movie information with additional metadata.
- The recommendation system relies on multiple datasets rather than a single source.

---

## Key Insight

Recommendation systems combine user interactions with movie information to better understand user preferences.

The richer the available information, the more intelligent the recommendations can become.

---

## Next Step

Perform Exploratory Data Analysis (EDA) to understand the structure and quality of the data before building models.

---

# Day 4: Exploratory Data Analysis (EDA)

## Objective

Explore the data to understand user behavior, movie popularity, data quality, and movie characteristics before building recommendation models.

---

## Rating Distribution

### Findings

- Ratings range from **0.5 to 5.0**.
- The average rating is approximately **3.53**.
- Most ratings fall between **3.0 and 4.0**.
- Rating **4.0** appears most frequently.

### Insight

Users generally give positive ratings, indicating that people are more likely to rate movies they enjoy.

This positive trend is useful because the model will learn from a large number of favorable user interactions.

---

## Movie Popularity Analysis

### Method

- Grouped ratings by `movieId`.
- Counted how many ratings each movie received.
- Merged the results with the `movies` dataset.

### Findings

The most frequently rated movies include:

- The Shawshank Redemption
- Forrest Gump
- Pulp Fiction
- The Matrix
- Jurassic Park
- Fight Club

### Insight

Popular movies provide a strong foundation for a baseline recommendation system.

A popularity-based recommender can effectively recommend movies to new users before sufficient personal history is available.

---

## User Activity Analysis

### Findings

- A small number of users contributed thousands of ratings.
- Most users rated only a relatively small number of movies.

### Insight

User activity is highly imbalanced.

Highly active users provide rich information for learning user preferences, while inactive users create the **cold-start problem**, making personalized recommendations more difficult.

---

## Missing Value Analysis

### Results

#### Train Dataset

No missing values.

#### Movies Dataset

No missing values.

#### IMDb Dataset

Missing values were identified in:

- title_cast
- director
- runtime
- budget
- plot_keywords

### Insight

Missing values are common in real-world datasets.

Since the recommendation model initially relies on user ratings, these missing values do not prevent development of the baseline model.

However, they should be considered if the IMDb features are used in future content-based recommendation models.

---

## Genre Analysis

### Objective

Understand the distribution of movie genres and their importance in recommendation systems.

### Findings

The most common genres are:

1. Drama
2. Comedy
3. Thriller
4. Romance
5. Action

Movies frequently belong to multiple genres simultaneously.

Example:

**Forrest Gump (1994)**

- Comedy
- Drama
- Romance
- War

Genre counts therefore represent the frequency of genre appearances rather than the number of unique movies.

### Insight

Genres describe movie content rather than user behavior.

This information becomes especially valuable for content-based recommendation systems because users often prefer particular genres.

---

# Overall Progress Summary

At this stage, the project has successfully completed:

- Machine learning problem definition.
- Dataset loading.
- Dataset relationship analysis.
- Git and GitHub integration.
- Project organization.
- Exploratory Data Analysis.
- Rating distribution analysis.
- Movie popularity analysis.
- User activity analysis.
- Missing value analysis.
- Genre analysis.

The project now has a solid understanding of both the data and the recommendation problem, providing a strong foundation for building the first recommendation model.

---

# Next Phase

The next stage of the project is to build the **baseline popularity-based recommendation system**.

This model will serve as the project's first benchmark and establish a reference point against which more advanced recommendation algorithms will later be evaluated.

---

# Day 5: Building the Baseline Recommendation System

## Objective

Build the first working recommendation engine using a **popularity-based recommendation approach**.

Before introducing personalized recommendations, it is important to establish a simple baseline model that recommends movies which are generally popular among all users.

This baseline will later serve as a benchmark for evaluating more advanced recommendation algorithms.

---

## Why Start with a Popularity-Based Recommender?

A recommendation system cannot personalize recommendations for a user who has never interacted with the platform.

This challenge is known as the **Cold Start Problem**.

For a completely new user, the system has no information such as:

- Previously watched movies
- Ratings
- Favorite genres
- Preferred actors or directors

Since no personal preferences are available, the safest strategy is to recommend movies that have been watched and appreciated by a large number of users.

---

## Computing Movie Statistics

The first step was to calculate two important statistics for every movie in the training dataset.

### Average Rating

Represents the overall quality of a movie based on user ratings.

### Rating Count

Represents how many users have rated the movie.

This measures the popularity and reliability of the rating.

The statistics were calculated by grouping the training dataset using the `movieId` column.

---

## Why Average Rating Alone Is Not Enough

A movie with an average rating of **5.0** based on only two ratings is less reliable than a movie with an average rating of **4.7** based on 30,000 ratings.

For this reason, recommendation systems should not rely solely on average ratings.

The number of ratings provides confidence that the movie's quality has been validated by many users.

---

## Combining Movie Information

The calculated statistics only contained numerical information such as:

- movieId
- average_rating
- rating_count

These values are useful for the algorithm but not meaningful to users.

To create understandable recommendations, the statistics were merged with the `movies.csv` dataset using the common key:

**movieId**

This added:

- Movie title
- Movie genres

to every recommendation.

---

## Ranking Strategy

Movies were ranked using two criteria:

1. Rating Count
2. Average Rating

The movies were sorted in descending order (`ascending=False`) so that the most popular and highly rated movies appear first.

This ranking strategy balances both popularity and quality.

---

## Results

The highest-ranked movies included:

- The Shawshank Redemption (1994)
- Forrest Gump (1994)
- Pulp Fiction (1994)
- The Silence of the Lambs (1991)
- The Matrix (1999)
- Star Wars: Episode IV – A New Hope (1977)
- Jurassic Park (1993)
- Schindler's List (1993)
- Braveheart (1995)
- Fight Club (1999)

These movies are widely recognized as popular films with consistently high user ratings, indicating that the recommendation strategy is producing sensible results.

---

## Key Learning

This milestone demonstrated that a recommendation system does not need machine learning to provide useful recommendations.

By analyzing historical user ratings, we can already recommend movies that have been trusted and enjoyed by thousands of users.

Although this approach does not personalize recommendations, it provides an excellent baseline for comparison with more advanced recommendation techniques.

---

## Business Value

Popularity-based recommendation systems are commonly used for:

- New users with no watch history.
- Trending movie sections.
- "Most Popular" recommendations.
- Featured content on home pages.

This approach helps solve the Cold Start Problem by providing meaningful recommendations before sufficient user interaction data has been collected.

---

## Limitations

Despite its simplicity, the popularity-based recommender has several limitations.

- Every user receives the same recommendations.
- Individual preferences are ignored.
- Favorite genres are not considered.
- Watching history is not used.
- The recommendations never change based on user behavior.

Because of these limitations, popularity-based recommendations are typically used only as a baseline or for new users.

---

## Milestone Summary

At this stage of the project, the following components have been successfully completed:

- Problem Definition
- Dataset Understanding
- Exploratory Data Analysis (EDA)
- Rating Distribution Analysis
- Movie Popularity Analysis
- User Activity Analysis
- Missing Value Analysis
- Genre Analysis
- Baseline Popularity-Based Recommendation System

The project now has its first fully functional recommendation engine.

The next milestone is to build a **personalized recommendation system** that recommends different movies to different users based on their individual preferences and historical interactions.