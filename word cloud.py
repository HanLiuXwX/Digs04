import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load the cleaned dataset
file_path = "./Cleaned_Animation_Movies.csv"
df = pd.read_csv(file_path)

# Generate word cloud for top 10 revenue movies
top_revenue_movies = df.nlargest(10, "revenue")["title"].tolist()
top_revenue_text = " ".join(top_revenue_movies)
wordcloud_revenue = WordCloud(width=800, height=400, background_color='white').generate(top_revenue_text)

# Generate word cloud for top 10 budget movies
top_budget_movies = df.nlargest(10, "budget")["title"].tolist()
top_budget_text = " ".join(top_budget_movies)
wordcloud_budget = WordCloud(width=800, height=400, background_color='white').generate(top_budget_text)

# Plot word clouds
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

axes[0].imshow(wordcloud_revenue, interpolation='bilinear')
axes[0].axis("off")
axes[0].set_title("Top 10 Highest Grossing Animated Movies")

axes[1].imshow(wordcloud_budget, interpolation='bilinear')
axes[1].axis("off")
axes[1].set_title("Top 10 Most Expensive Animated Movies")

plt.show()
