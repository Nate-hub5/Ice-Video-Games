import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
@st.cache
def load_data():
    # Replace 'data.csv' with your dataset file name
    return pd.read_csv('data.csv')

data = load_data()

# Title and Description
st.title("Video Game Sales Analysis")
st.write("""
### Overview
Explore the trends in video game sales across different platforms, genres, and years. The insights are visualized through the following:
1. Number of games released over the years.
2. Total sales by platform.
3. Sales distribution over top platforms.
4. Average total sales by genre.
""")

# Visualization 1: Number of Games Released Each Year
st.subheader("1. Number of Games Released Each Year")
games_per_year = data['year_of_release'].value_counts().sort_index()

fig1, ax1 = plt.subplots(figsize=(12, 6))
ax1.bar(games_per_year.index, games_per_year.values, color='skyblue')
ax1.set_title('Number of Games Released Each Year')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Games Released')
ax1.tick_params(axis='x', rotation=-45)
st.pyplot(fig1)

# Visualization 2: Total Sales by Platform
st.subheader("2. Total Sales by Platform")
platform_sales = data.groupby('platform')['total_sales'].sum().sort_values(ascending=False)

fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.bar(platform_sales.index, platform_sales.values, color='skyblue')
ax2.set_title('Total Sales by Platform')
ax2.set_xlabel('Platform')
ax2.set_ylabel('Total Sales (in millions)')
ax2.tick_params(axis='x', rotation=-45)
st.pyplot(fig2)

st.write("**Top 5 Platforms by Total Sales:**")
st.write(platform_sales.head(5))

# Visualization 3: Sales Distribution Over Time for Top Platforms
st.subheader("3. Sales Distribution Over Years for Top Platforms")
top_platforms = platform_sales.head(5).index
sales_distribution = data[data['platform'].isin(top_platforms)].groupby(['year_of_release', 'platform'])['total_sales'].sum().unstack()

fig3, ax3 = plt.subplots(figsize=(12, 6))
sales_distribution.plot(ax=ax3, marker='o')
ax3.set_title('Total Sales Distribution Over Years for Top Platforms')
ax3.set_xlabel('Year')
ax3.set_ylabel('Total Sales (in millions)')
ax3.grid(True)
st.pyplot(fig3)

# Visualization 4: Average Total Sales by Genre
st.subheader("4. Average Total Sales by Genre")
genre_sales = data.groupby('genre')['total_sales'].sum().sort_values(ascending=False)
avg_sales_per_genre = data.groupby('genre')['total_sales'].mean()

fig4, ax4 = plt.subplots(figsize=(12, 6))
ax4.bar(avg_sales_per_genre.index, avg_sales_per_genre.values, color='skyblue')
ax4.set_title('Average Total Sales by Genre')
ax4.set_xlabel('Genre')
ax4.set_ylabel('Average Sales (in millions)')
ax4.tick_params(axis='x', rotation=45)
for i, avg in enumerate(avg_sales_per_genre.values):
    ax4.text(i, avg, f"Avg: {avg:.2f}M", ha='center', va='bottom', fontsize=10, color='red')
st.pyplot(fig4)
