import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load datasets
file_path_movies = "./Cleaned_Animation_Movies.csv"
df = pd.read_csv(file_path_movies)

file_path_stats = "./Yearly_Animation_Stats.csv"
df_stats = pd.read_csv(file_path_stats)

# Sidebar filters
st.sidebar.header("Filter Options")
selected_years = st.sidebar.slider("Select Year Range", int(df["year"].min()), int(df["year"].max()), (1990, 2024))

# Filter data
df_filtered = df[df["year"].between(selected_years[0], selected_years[1])]

# Movie Count Line Chart
st.subheader("Number of Animated Movies Over Time")
fig_movie_count = px.line(df_stats, x="year", y="movie_count", 
                          title="Number of Animation Movies Released (1990-2024)", 
                          markers=True, template="plotly_white")
st.plotly_chart(fig_movie_count)

# Rating vs Revenue Scatter Plot
st.subheader("Do Higher Ratings Lead to Higher Revenue?")
fig_scatter = px.scatter(df_filtered, x="vote_average", y="revenue", size="vote_count", color="year",
                         title="Ratings vs. Revenue", hover_name="title", size_max=30, opacity=0.7, log_y=True)
st.plotly_chart(fig_scatter)

# Word Cloud for Top 10 Revenue Movies
st.subheader("Top 10 Highest Grossing Animated Movies")
top_revenue_movies = df.nlargest(10, "revenue")["title"].tolist()
wordcloud_revenue_text = " ".join(top_revenue_movies)
wordcloud_revenue = WordCloud(width=800, height=400, background_color='white').generate(wordcloud_revenue_text)
st.image(wordcloud_revenue.to_array())

# Word Cloud for Top 10 Budget Movies
st.subheader("Top 10 Most Expensive Animated Movies")
top_budget_movies = df.nlargest(10, "budget")["title"].tolist()
wordcloud_budget_text = " ".join(top_budget_movies)
wordcloud_budget = WordCloud(width=800, height=400, background_color='white').generate(wordcloud_budget_text)
st.image(wordcloud_budget.to_array())