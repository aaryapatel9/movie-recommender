from http.client import responses

import streamlit as st
import pickle
import pandas as pd
import requests

import gdown
import os

if not os.path.exists("similarity.pkl"):
    url = "https://drive.google.com/drive/folders/1Gp0WojVGi4AfwyXrc3Pv4XDoxK3fwX3p?usp=sharing"
    gdown.download(url, "similarity.pkl", quiet=False)

def fetch_poster(movie_id):
    api_key = "3e946bf60052429d208af3ba0c99934e"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"

    response = requests.get(url)
    data = response.json()

    if 'poster_path' in data and data['poster_path']:
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movies = pickle.load(open('movies.pkl', 'rb'))
movies_dict = movies['title'].values

@st.cache_resource
def load_similarity():
    return pickle.load(open('similarity.pkl', 'rb'))

similarity = load_similarity()

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie',
    movies_dict)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.header(names[0])
        st.image(posters[0])
    with col2:
        st.header(names[1])
        st.image(posters[1])
    with col3:
        st.header(names[2])
        st.image(posters[2])
    with col4:
        st.header(names[3])
        st.image(posters[3])
    with col5:
        st.header(names[4])
        st.image(posters[4])
