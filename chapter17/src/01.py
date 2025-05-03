# 17-1. Other Languages: Modify the API call in python_repos.py so it generates
# a chart showing the most popular projects in other languages. Try languages
# such as JavaScript, Ruby, C, Java, Perl, Haskell, and Go.

import requests
import plotly.express as px

LANGUAGE = 'go'

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += f"?q=language:{LANGUAGE}+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}

r = requests.get(url, headers=headers)

# Convert the response object to a dictionary.
response_dict = r.json()

# Process repository information.
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    # Build hover texts.
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# Make visualization.
title = f"Most-Starred {LANGUAGE.title()} Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()
