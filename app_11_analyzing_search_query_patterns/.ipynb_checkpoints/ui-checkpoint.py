import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import IFrame

# Sample Data
data = {
    'user_id': [1, 2, 3, 4, 5, 6, 7],
    'timestamp': ['2023-01-01 08:00:00', '2023-01-01 08:15:00', '2023-01-01 08:15:00',
                  '2023-01-01 08:15:00', '2023-01-01 08:15:00', '2023-01-01 08:15:00',
                  '2023-01-01 08:15:00'],
    'search_query': ['machine learning', 'data visualization', 'natural language processing',
                     'deep learning frameworks', 'python programming', 'cloud computing', 'machine learning'],
    'search_results': [20, 21, 21, 30, 22, 15, 21],
    'clicked_result': [3, 2, 1, 5, 2, 7, 4],
    'query_type': ['transactional', 'informational', 'informational', 'navigational', 'transactional', 'informational', 'navigational'],
}

df = pd.DataFrame(data)
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Set custom color palettes for the visuals
palette1 = sns.color_palette("Paired", n_colors=df['query_type'].nunique())
palette2 = sns.color_palette("coolwarm", n_colors=2)

# Streamlit App
st.title('User Behavior Insights and Click Metrics')

# User Behavior Overview
st.subheader('User Behavior Overview')
user_behavior_chart = sns.countplot(x='query_type', data=df, palette=palette1)
st.pyplot(user_behavior_chart.figure)

# Click Distribution Overview
st.subheader('Click Distribution Overview')
df['hour_of_day'] = df['timestamp'].dt.hour
click_distribution_chart = sns.lineplot(x='hour_of_day', y='clicked_result', data=df, marker='o', hue='query_type', palette=palette1)
st.pyplot(click_distribution_chart.figure)

# User Engagement Overview
st.subheader('User Engagement Overview')
df['user_engaged'] = df['clicked_result'].apply(lambda x: 'Engaged' if x > 0 else 'Not Engaged')
user_engagement_chart = df['user_engaged'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=palette2)
st.pyplot(user_engagement_chart.figure)

# PDF Embedding
st.subheader('PDF Embedding')
pdf_path = 'https://pdf.navdeeshsingha2.repl.co/'
st.write(f'<iframe src="{pdf_path}" width="100%" height="1000px"></iframe>', unsafe_allow_html=True)
