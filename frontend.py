import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  

    distances = similar[movie_index]
        
    movies_list = sorted(enumerate(distances), key=lambda x: x[1], reverse=True)[1:6]  
    
    recommended_movies = []
    for i in movies_list:
       movie_id= i[0]
       recommended_movies.append(movies.iloc[i[0]]['title'])
    return recommended_movies 

# Load the movies dictionary
movies_dict = pickle.load<("Path to your pickle file(movies) created in main program")>
similar = pickle.load<("Path to your pickle file(similarity) created in main program")>

# Convert to DataFrame
try:
    movies = pd.DataFrame(movies_dict)
except ValueError as e:
    st.error(f"Error while creating DataFrame: {e}")
    st.stop()

# Streamlit code
st.title('Movie Recommender System')
option = st.selectbox('Select a movie:', movies['title'].values)
if st.button('Recommend'):
    recommendations=recommend(option)
    for i in recommendations:
        st.write(i)
    


