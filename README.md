# 🎬 Movie Recommendation System

A Python-based movie recommendation project built with the MovieLens dataset, exploring both popularity-based recommendations and personalized recommendations using user-based collaborative filtering.

The project was developed as part of my Data Science learning journey, with a focus on understanding how recommendation systems work from data exploration through recommendation generation.

---

# 📌 Project Overview

Recommendation systems help users discover relevant content based on popularity, preferences, or similarities between users and items.

In this project, I implemented two approaches:

- **Popularity-Based Recommendation** — recommends movies based on overall popularity and ratings.
- **User-Based Collaborative Filtering** — identifies users with similar rating patterns and uses their preferences to generate personalized recommendations.
  
The project focuses on understanding the underlying data and recommendation logic rather than treating the recommendation algorithm as a black box.

---

# 🎯 Objectives

The main objectives of the project were to:

- Explore and understand movie-rating data.
- Perform exploratory data analysis and data preparation.
- Build a popularity-based recommendation approach.
- Construct a user–movie rating matrix.
- Calculate user similarity using cosine similarity.
- Identify users with similar preferences.
- Generate personalized movie recommendations.
- Practice working with real-world-style datasets using Python.
- Apply Git and GitHub for project version control and documentation.

---

# 📂 Dataset

The project uses the MovieLens movie-rating dataset and related movie information.

The data used in the project includes information such as:

| Dataset           | Description                                                                            |
| ----------------- | -------------------------------------------------------------------------------------- |
| **train.csv**     | Historical movie ratings used to train the recommendation system                       |
| **test.csv**      | User–movie pairs for prediction                                                        |
| **movies.csv**    | Movie titles and genres                                                                |
| **imdb_data.csv** | Additional movie metadata including cast, director, runtime, budget, and plot keywords |
| **links.csv**     | Links between MovieLens and external movie databases                                   |
| **tags.csv**      | User-generated movie tags                                                              |

The datasets are not included in the repository where they are excluded by the project's Git configuration.

---

# 🔍 Project Workflow

The project follows a structured data science workflow:

1. Load and inspect the datasets.
2. Understand the structure and relationships between the data.
3. Perform exploratory data analysis.
4. Clean and transform the relevant data.
5. Explore movie popularity and rating patterns.
6. Build a popularity-based recommender.
7. Create a user–movie rating matrix.
8. Address the sparsity of the user–movie data.
9. Calculate user similarity using cosine similarity.
10. Identify users with similar preferences.
11. Filter movies already rated by the target user.
12. Rank recommendation candidates.
13. Generate personalized recommendations.

---

# 🚀 Recommendation Approaches

## 1. Popularity-Based Recommendation

The first approach recommends movies based on their overall popularity and rating performance.

This approach is useful when:

- There is limited information about a new user.
- Personalized user history is unavailable.
- The goal is to surface broadly popular content.

Example recommendations generated during the project include:

- The Shawshank Redemption
- Forrest Gump
- The Matrix
- Fight Club

## 2. User-Based Collaborative Filtering

The second approach provides personalized recommendations by comparing users based on their movie-rating patterns.

The process involves:

1. Creating a user–movie rating matrix.
2. Comparing users using Cosine Similarity.
3. Identifying users with similar rating patterns.
4. Collecting movies rated by similar users.
5. Removing movies already rated by the target user.
6. Ranking the remaining candidates.
7. Returning the highest-ranked recommendations.

Example recommendations generated during the project include:

- WALL·E
- Apocalypse Now
- The Imitation Game
- V for Vendetta
- Jerry Maguire

---
# 🧠 Key Technical Concepts

This project gave me practical experience with:

- Exploratory Data Analysis (EDA)
- Data cleaning
- Data transformation
- Data merging
- User–item matrices
- Sparse data
- Collaborative filtering
- Cosine similarity
- Recommendation logic
- Ranking recommendation candidates
- Python data analysis
- Git and GitHub

---
# 🛠️ Technologies Used

## Programming & Data

- Python
- Pandas
- NumPy

## Machine Learning

- Scikit-learn

## Development

- Jupyter Notebook
- Git
- GitHub

---
# 📁 Project Structure

```text
Movie_Recommendation_Project_2026/
│
├── data/
├── models/
├── notebooks/
│   └── movie_recommender.ipynb
├── reports/
├── submission/
├── project_notes.md
├── README.md
├── .gitignore
└── open_project.bat
```
---
# 📊 Current Limitations

This project is primarily focused on understanding and implementing recommendation-system concepts.

The current version does not yet include:

- Formal recommendation-model evaluation using metrics such as RMSE or MAE.
- Item-based collaborative filtering.
- Matrix factorization.
- A hybrid recommendation approach.
- A deployed web application.
- A production recommendation API.

These areas provide opportunities for future development.

---

# 🔮 Future Improvements

Potential improvements include:

- Implementing item-based collaborative filtering.
- Exploring matrix factorization techniques.
- Combining collaborative and content-based approaches.
- Adding formal model evaluation.
- Comparing recommendation approaches using appropriate metrics.
- Improving recommendation efficiency for larger datasets.
- Building an interactive application using Streamlit.
- Developing an API for serving recommendations.

---

# 📚 What I Learned

Through this project, I developed a stronger practical understanding of how recommendation systems can be built from user-rating data.

In particular, I learned how to:

- Transform raw rating data into a structure suitable for recommendation.
- Work with sparse user–movie matrices.
- Measure similarity between users.
- Generate recommendations from similar users.
- Distinguish between general popularity and personalized recommendations.
- Document a data science project using Git and GitHub.

---

# ▶️ Running the Project

## 1. Clone the repository
git clone https://github.com/salimstephen/movie-recommendation-project.git
## 2. Navigate into the project
cd movie-recommendation-project
## 3. Install the required Python libraries
pip install pandas numpy scikit-learn jupyter
## 4. Start Jupyter Notebook
jupyter notebook

Open the notebook inside the notebooks directory and run the cells sequentially.

Note: The required datasets are not stored directly in the repository. Make sure the expected dataset files are available in the appropriate local project location before running the notebook.

---

# 👨‍💻 Author

**Stephen (Salim) Otieno**

Data Science & Analytics practitioner building practical experience in:

**Python • SQL • Data Analysis • Power BI • Machine Learning**

This project is part of my portfolio and reflects my continued development in Data Science and Machine Learning.


