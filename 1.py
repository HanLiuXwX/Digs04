import pandas as pd
import plotly.express as px

# Load the cleaned dataset
file_path = "./Yearly_Animation_Stats.csv"
df = pd.read_csv(file_path)

# Create an interactive line chart for movie count
title_movie_count = "Number of Animation Movies Released (1990-2024)"
fig_movie_count = px.line(
    df, x="year", y="movie_count", 
    title=title_movie_count,
    labels={"year": "Year", "movie_count": "Number of Movies"},
    markers=True, template="plotly_white"
)

# Add hover interaction
fig_movie_count.update_traces(mode="markers+lines", hovertemplate="Year: %{x}<br>Movies Released: %{y}")

# Show plot
fig_movie_count.show()

