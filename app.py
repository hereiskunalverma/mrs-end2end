# -*- coding: utf-8 -*-

#  R E X


# @Author: Kunal Verma

# CodeForces - kunalverma19
# CodeChef   - kunalverma_19
# AtCoder    - TLKunalVermaRX

# @Last Modified by:   Kunal Verma
# @Modified Time: 2022-05-02 09:58:27 (IST)
import streamlit as st
import pickle
import requests
import pandas as pd

api_key = 'f6d26636e8d0527ad28fd7bd2774d0ee'
# st.text(str(pd.__version__))


def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarities[movie_index]
    movies_list = sorted(list(enumerate(distances)),
                         reverse=True, key=lambda x: x[1])[1:6]
    recommended = list()  # recommended movies
    recommended_posters = list()  # recommended posters
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended.append(movies.iloc[i[0]].title)
        # fetch movie poster from TMDB api
        recommended_posters.append(fetch_poster(movie_id))

    return recommended, recommended_posters


movies = pickle.load(open('movies.pkl', 'rb'))
similarities = pickle.load(open('similarity.pkl', 'rb'))
movies_list = movies['title'].values
st.title("Movie Recommendation System")
selected_movie = st.selectbox(
    'Select movie from drop down and get recommendations ! ', movies_list)

if st.button('Recommend Me'):
    recommendations, posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])
    with col2:
        st.text(recommendations[1])
        st.image(posters[1])
    with col3:
        st.text(recommendations[2])
        st.image(posters[2])
    with col4:
        st.text(recommendations[3])
        st.image(posters[3])
    with col5:
        st.text(recommendations[4])
        st.image(posters[4])
