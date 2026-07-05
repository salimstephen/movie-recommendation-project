# 🎬 Movie Recommendation System

A machine learning project that builds both **Popularity-Based** and **User-Based Collaborative Filtering** recommendation systems using the MovieLens dataset.

This project was developed as part of my journey into Data Science to gain a deep understanding of how modern recommendation systems work. Rather than simply following tutorials, the focus was on understanding the purpose behind every step, from data exploration to generating personalized movie recommendations.

---

# 📌 Project Overview

Recommendation systems are used by platforms such as Netflix, Amazon, Spotify, and YouTube to suggest content that users are likely to enjoy.

This project demonstrates two recommendation approaches:

* **Popularity-Based Recommendation** – recommends movies that are popular among all users.
* **User-Based Collaborative Filtering** – recommends movies based on users with similar viewing preferences.

The project was built step by step to understand both the business problem and the machine learning concepts behind recommendation systems.

---

# 🎯 Project Objectives

* Understand recommendation systems from first principles.
* Explore and analyze movie rating data.
* Build a popularity-based recommender.
* Build a personalized recommendation system using User-Based Collaborative Filtering.
* Practice data manipulation, feature engineering, and similarity calculations.
* Apply professional Git and GitHub version control throughout the project.

---

# 📂 Dataset

The project uses the MovieLens movie recommendation dataset consisting of:

| Dataset           | Description                                                                            |
| ----------------- | -------------------------------------------------------------------------------------- |
| **train.csv**     | Historical movie ratings used to train the recommendation system                       |
| **test.csv**      | User–movie pairs for prediction                                                        |
| **movies.csv**    | Movie titles and genres                                                                |
| **imdb_data.csv** | Additional movie metadata including cast, director, runtime, budget, and plot keywords |
| **links.csv**     | Links between MovieLens and external movie databases                                   |
| **tags.csv**      | User-generated movie tags                                                              |

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Jupyter Notebook
* Git
* GitHub

---

# 📊 Project Workflow

The project follows the complete machine learning workflow:

1. Data loading and inspection
2. Understanding the datasets
3. Exploratory Data Analysis (EDA)
4. Identifying popular movies
5. Building a Popularity-Based Recommendation System
6. Creating the User–Movie Matrix
7. Handling sparse data
8. Computing user similarity using Cosine Similarity
9. Identifying similar users
10. Filtering already watched movies
11. Ranking recommendation candidates
12. Producing personalized movie recommendations

---

# 🚀 Recommendation Approaches

## 1. Popularity-Based Recommendation

This recommender suggests movies that are widely watched and highly rated across all users.

Suitable for:

* New users
* Cold-start scenarios
* Trending movie recommendations

Example output:

* The Shawshank Redemption
* Forrest Gump
* The Matrix
* Fight Club

---

## 2. User-Based Collaborative Filtering

This recommender identifies users with similar movie preferences using **Cosine Similarity**.

Recommendation process:

* Build a user–movie matrix.
* Calculate similarity between users.
* Find the most similar users.
* Collect movies rated by similar users.
* Remove movies already watched by the target user.
* Rank the remaining movies based on average ratings.
* Recommend the highest-ranked movies.

Example recommendations:

* WALL·E
* Apocalypse Now
* The Imitation Game
* V for Vendetta
* Jerry Maguire

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

# 📈 Key Skills Demonstrated

* Exploratory Data Analysis (EDA)
* Data Cleaning
* Data Transformation
* Data Merging
* Recommendation Systems
* User-Based Collaborative Filtering
* Cosine Similarity
* Pandas
* Git & GitHub
* Problem Solving

---

# 📚 What I Learned

Throughout this project I developed a practical understanding of:

* How recommendation systems work.
* The difference between popularity-based and personalized recommendations.
* Why sparse datasets are common in recommendation systems.
* How Cosine Similarity identifies users with similar preferences.
* How to transform raw data into meaningful recommendations.
* The importance of documenting work and using version control in professional projects.

---

# 🔮 Future Improvements

Future versions of this project may include:

* Item-Based Collaborative Filtering
* Matrix Factorization
* Hybrid Recommendation Systems
* Model evaluation metrics (RMSE, MAE)
* Hyperparameter tuning
* Interactive web application deployment using Streamlit
* Movie recommendation API

---

# 👨‍💻 Author

**Stephen Otieno**

Aspiring Data Scientist passionate about solving real-world problems using data and machine learning.

This project is part of my portfolio showcasing practical data science skills and continuous learning.


