import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Enter the URL of the LinkedIn feed to be scraped
url = "https://www.linkedin.com/feed/"

# Send a GET request to the URL and store the response
response = requests.get(url)

# Parse the response using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the posts on the feed
posts = soup.find_all("div", class_="post-container")

# Initialize variables to store the like and comment counts
like_count = 0
comment_count = 0

# Loop through the posts and extract the like and comment counts
for post in posts:
likes = post.find("div", class_="post-likes-container").text
comments = post.find("div", class_="post-comments-container").text

# Aggregate the counts
like_count += int(likes)
comment_count += int(comments)

# Plot the counts in a bar chart
plt.bar(["Likes", "Comments"], [like_count, comment_count])
plt.show()
