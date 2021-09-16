# JOIN MY DISCORD! discord.gg/dVSVGgqv2Q
import praw,requests,re
import os

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="Scraper by u/Twisterzzz",
    username="",
    password="",       
)
    





subreddit = reddit.subreddit('memes')

#print(subreddit.display_name)
# Output: r/memes
#print(subreddit.title)
# Output: reddit development
#print(subreddit.description)
# Output: a subreddit for discussion of

for submission in subreddit.new(limit=100):
    url = (submission.url)
    file_name = url.split('/')
    if len(file_name) == 0:
        file_name = re.findall("/(.*?)", url)
    file_name = file_name[-1]
    if "." not in file_name:
        file_name += ".jpg"
    print(file_name)
    r = requests.get(url)
    with open(file_name, "wb") as f:
        f.write(r.content)
