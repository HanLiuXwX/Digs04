import pandas as pd
import plotly.express as px

# Load the cleaned dataset
file_path_movies = "./Cleaned_Animation_Movies.csv"
df = pd.read_csv(file_path_movies)

# Create an optimized interactive scatter plot for Rating vs. Revenue
title_rating_vs_revenue = "Do Higher Ratings Lead to Higher Revenue? (Animated Movies)"
fig_rating_vs_revenue = px.scatter(
    df, x="vote_average", y="revenue", 
    size="vote_count", color="year",
    title=title_rating_vs_revenue,
    labels={"vote_average": "Average Rating", "revenue": "Total Revenue (USD)", "vote_count": "Number of Votes", "year": "Year"},
    template="plotly_white",
    hover_name="title",
    size_max=30,  # Reduce maximum bubble size for better visibility
    opacity=0.7,  # Make bubbles more transparent to reduce overlap
    log_y=True,  # Use log scale to improve revenue visualization
    color_continuous_scale="Viridis"  # Improve color contrast
)

# Update axes for better readability
fig_rating_vs_revenue.update_layout(
    xaxis=dict(title="Average Rating", range=[4, 10]),  # Filter out very low ratings
    yaxis=dict(title="Total Revenue (Log Scale)")
)

# Show plot
fig_rating_vs_revenue.show()

#Generate word cloud for top 10 budget movies
top_budget_movies = df.nlargest(10, "budget")["title"].tolist()
top_budget_text = " ".join(top_budget_movies)
wordcloud_budget = WordCloud(width=800, height=400, background_color='white').generate(top_budget_text)

# Generate word cloud for top 10 revenue movies
top_revenue_movies = df.nlargest(10, "revenue")["title"].tolist()
top_revenue_text = " ".join(top_revenue_movies)
wordcloud_revenue = WordCloud(width=800, height=400, background_color='white').generate(top_revenue_text)

# Plot word clouds
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

axes[0].imshow(wordcloud_budget, interpolation='bilinear')
axes[0].axis("off")
axes[0].set_title("Top 10 Most Expensive Animated Movies")

axes[1].imshow(wordcloud_revenue, interpolation='bilinear')
axes[1].axis("off")
axes[1].set_title("Top 10 Highest Grossing Animated Movies")

plt.show()