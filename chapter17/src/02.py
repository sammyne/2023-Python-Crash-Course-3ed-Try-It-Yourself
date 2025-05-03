# 17-2. Active Discussions: Using the data from hn_submissions.py, make a bar
# chart showing the most active discussions currently happening on Hacker News.
# The height of each bar should correspond to the number of comments each sub-
# mission has. The label for each bar should include the submission’s title and act
# as a link to the discussion page for that submission. If you get a KeyError when
# creating a chart, use a try-except block to skip over the promotional posts.

from operator import itemgetter
import requests
import plotly.express as px

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:10]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    #print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    # Build a dictionary for each article.
    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    except KeyError:
        print(f"skip '{response_dict['title']}'")
    else:
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
submission_links, comments,  = [], []
for submission_dict in submission_dicts:
    title = submission_dict['title']
    url = submission_dict['hn_link']
    link = repo_link = f"<a href='{url}'>{title}</a>"

    submission_links.append(link)
    comments.append(submission_dict['comments'])
    # print(f"\nTitle: {submission_dict['title']}")
    # print(f"Discussion link: {submission_dict['hn_link']}")
    # print(f"Comments: {submission_dict['comments']}")

# Make visualization.
title = "Active Discussions on Hacker News"
labels = {'x': 'Discussion', 'y': 'Comments'}
fig = px.bar(x=submission_links, y=comments, title=title, labels=labels)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()
