import streamlit as st
import pickle
import pandas as pd
import requests

st.markdown('''<style>
#MainMenu {
    visibility: hidden;
    scroll-behavior: smooth;
}
.st-emotion-cache-1brpe1m{
    visibility: hidden;
}

footer {
    visibility: hidden;
    scroll-behavior: smooth;
}
</style>''', unsafe_allow_html=True)

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=36d7798070eb20ebe655912221cbc53f&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
#get the similarity.pkl from https://drive.google.com/file/d/1E_kSKyyvvaS2WFtfS3Jbtse8lXLGPkaM/view?usp=sharing as it can not be uploaded due to its large size
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append((movies.iloc[i[0]].title, fetch_poster(movie_id)))
    return recommended_movies

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'Choose a movie',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    for idx, (name, poster) in enumerate(recommendations):
        if idx % 5 == 0:
            with col1:
                st.markdown(f"{name}")
                st.image(poster, use_column_width=True)
        elif idx % 5 == 1:
            with col2:
                st.markdown(f"{name}")
                st.image(poster, use_column_width=True)
        elif idx % 5 == 2:
            with col3:
                st.markdown(f"{name}")
                st.image(poster, use_column_width=True)
        elif idx % 5 == 3:
            with col4:
                st.markdown(f"{name}")
                st.image(poster, use_column_width=True)
        else:
            with col5:
                st.markdown(f"{name}")
                st.image(poster, use_column_width=True)
