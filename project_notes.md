# \# Movie Recommendation Project Journal

# 

# \---

# 

# \## Day 1: Data Loading \& Understanding

# 

# \### Dataset Loaded Successfully

# 

# \#### Train Dataset

# 

# \* Shape: \*\*10,000,038 rows × 4 columns\*\*

# \* Columns:

# 

# &#x20; \* userId

# &#x20; \* movieId

# &#x20; \* rating

# &#x20; \* timestamp

# 

# \#### Movies Dataset

# 

# \* Shape: \*\*62,423 rows × 3 columns\*\*

# \* Columns:

# 

# &#x20; \* movieId

# &#x20; \* title

# &#x20; \* genres

# 

# \---

# 

# \### Initial Observations

# 

# \* No structural issues detected during data loading.

# \* Ratings range from \*\*0.5 to 5.0\*\*.

# \* Large-scale dataset suitable for collaborative filtering.

# \* Movies dataset contains rich metadata including titles and genres.

# 

# \---

# 

# \### Key Insight

# 

# We are solving a \*\*rating prediction problem\*\*.

# 

# \*\*Input:\*\*

# 

# \* userId

# \* movieId

# 

# \*\*Output:\*\*

# 

# \* Predicted rating

# 

# \---

# 

# \### Notes

# 

# \* Data is clean at first inspection.

# \* No preprocessing applied yet.

# \* Next step: build a baseline recommender model (popularity-based).

# 

# \---

# 

# \## Day 2: Project Setup \& Version Control

# 

# \### Dataset \& Environment Setup

# 

# \* Successfully located the project folder.

# \* Opened Jupyter Notebook using:

# &#x20; `python -m notebook`

# \* Verified notebook:

# &#x20; `movie\_recommender.ipynb`

# 

# \---

# 

# \### Version Control Setup

# 

# \* Initialized Git repository.

# \* Created first commit:

# &#x20; \*\*"Initial movie recommendation project structure and notebook"\*\*

# \* Git status:

# 

# &#x20; \* Working tree clean.

# &#x20; \* Branch: main.

# 

# \---

# 

# \### Project Structure

# 

# \* data/

# \* notebooks/

# \* models/

# \* reports/

# \* submission/

# 

# \---

# 

# \### Key Insight

# 

# Version control is now integrated into the project.

# 

# Future work can be resumed easily, and all progress can be tracked through Git commits.

# 

# \---

# 

# \### Next Steps

# 

# \* Continue building the recommendation model.

# \* Test recommendation outputs.

# \* Save models in the models folder.

# \* Prepare the final report.

# 

# \---

# 

# \### Session Reminder

# 

# 1\. Start Jupyter Notebook.

# 2\. Open `movie\_recommender.ipynb`.

# 3\. Review `project\_notes.md`.

# 4\. Continue from the previous session.

# 5\. Commit changes to Git.

# 
## Day 3: Understanding the Data

### Objective

Understand the purpose of each dataset and how they relate to the recommendation problem.

---

### Datasets Explored

- **train.csv** – Contains historical user ratings and serves as the primary training dataset.
- **test.csv** – Contains user–movie pairs for which ratings will be predicted.
- **movies.csv** – Contains movie titles and genres.
- **imdb_data.csv** – Provides additional movie metadata such as cast, director, runtime, budget, and plot keywords.
- **links.csv** – Maps MovieLens movie IDs to external databases.
- **tags.csv** – Contains user-generated descriptive tags for movies.

---

### Key Observations

- Each row in the **train** dataset represents one rating given by one user to one movie.
- The **movies** dataset stores descriptive information about movies and avoids repeating movie details in the training data.
- The **IMDb** dataset enriches the movies with additional metadata useful for content-based recommendation.
- The **movieId** column is the common key that links multiple datasets together.
- The **train** dataset is the most important dataset because it contains the user ratings that the recommendation model will learn from.

---

### Key Insight

A recommendation system is not built from a single dataset.

It combines user behavior with movie information to predict how much a user is likely to enjoy a movie.

---

### Next Step

Begin Exploratory Data Analysis (EDA) to understand user rating behavior and movie popularity before building recommendation models.
