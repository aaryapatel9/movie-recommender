# 🎬 CineMatch — Content-Based Movie Recommender

A content-based movie recommender system built in two parts:
- **`movie_recommender_system.ipynb`** — Python/ML pipeline (data processing, vectorization, cosine similarity)
- **`movie_recommender.html`** — Frontend web app powered entirely by the TMDB API

---

## 📸 Preview

> Search any movie → get 5 similar recommendations with posters, cast, director, genres, and match scores.

---

## 🧠 How It Works

This project mirrors a classic NLP-based recommender pipeline:

1. **Feature Extraction** — For each movie, tags are built from:
   - Overview (plot description)
   - Genres
   - Keywords
   - Top 3 cast members
   - Director

2. **Vectorization** — Tags are converted to vectors using `CountVectorizer` (top 5000 features, English stop words removed)

3. **Stemming** — Words are reduced to their root form using NLTK's `PorterStemmer`

4. **Similarity Scoring** — Cosine similarity is computed across all movie vectors to find the closest matches

5. **Frontend** — The web app replicates this logic live using TMDB's `/recommendations` endpoint, scored by genre overlap + vote average

---

## 🗂 Project Structure

```
movie-recommender/
├── movie_recommender_system.ipynb   # ML pipeline (Python)
├── movie_recommender.html           # Frontend web app
└── README.md
```

> **Note:** The notebook requires `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` from [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).

---

## 🚀 Running the Web App

### Prerequisites
- A free TMDB API key from [themoviedb.org](https://www.themoviedb.org/settings/api)
- Python installed (for local server)

### Steps

1. Clone the repo
   ```cmd
   git clone https://github.com/your-username/movie-recommender.git
   cd movie-recommender
   ```

2. Add your TMDB API key — open `movie_recommender.html` and update line:
   ```js
   const TMDB_KEY = "your_tmdb_api_key_here";
   ```

3. Start a local server
   ```cmd
   python -m http.server 8000
   ```

4. Open in browser
   ```
   http://localhost:8000/movie_recommender.html
   ```

---

## 🐍 Running the Notebook

### Prerequisites

```cmd
pip install numpy pandas scikit-learn nltk
```

### Dataset

Download from Kaggle: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

Place both files in the same folder as the notebook:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

### Run

Open `movie_recommender_system.ipynb` in Jupyter and run all cells. The notebook will output:
- `movies.pkl` — processed movie dataframe
- `similarity.pkl` — precomputed cosine similarity matrix

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Data Processing | Python, Pandas, NumPy |
| NLP / Vectorization | scikit-learn `CountVectorizer`, NLTK `PorterStemmer` |
| Similarity | scikit-learn `cosine_similarity` |
| Frontend | HTML, CSS, Vanilla JavaScript |
| Movie Data & Posters | TMDB API |

---

## 📦 Dependencies (Notebook)

```txt
numpy
pandas
scikit-learn
nltk
```

---

## 🙏 Acknowledgements

- [TMDB](https://www.themoviedb.org/) for the movie database and API
- [Kaggle TMDB 5000 Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) for training data
