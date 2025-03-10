import pandas as pd

# Load the dataset
file_path = r"C:\Users\l2427\Desktop\Animation_Movies.csv"
df = pd.read_csv(file_path)

# Convert release_date to datetime format
df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")

# Extract year from release_date
df["year"] = df["release_date"].dt.year

# Filter movies released after 1990
df_cleaned = df[df["year"] >= 1990]

# Remove movies with zero revenue
df_cleaned = df_cleaned[df_cleaned["revenue"] > 0]

# Remove short movies (less than 60 minutes)
df_cleaned = df_cleaned[df_cleaned["runtime"] >= 60]

# Select relevant columns
df_cleaned = df_cleaned[["title", "year", "vote_average", "vote_count", "revenue", "budget", "runtime", "genres", "production_companies"]]

# Compute yearly statistics
yearly_stats = df_cleaned.groupby("year").agg(
    total_revenue=("revenue", "sum"),
    avg_rating=("vote_average", "mean"),
    movie_count=("title", "count")
).reset_index()

# Save cleaned data and yearly statistics
df_cleaned.to_csv("C:\\Users\\l2427\\Desktop\\dig04\\final project\\Cleaned_Animation_Movies.csv", index=False)
yearly_stats.to_csv("C:\\Users\\l2427\\Desktop\\dig04\\final project\\Yearly_Animation_Stats.csv", index=False)
