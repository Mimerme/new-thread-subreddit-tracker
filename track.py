import yaml
import re
import feedparser
import pdb
import time

UPDATE_INTERVAL = 30
# Save the ids of already processed posts
CACHED_POSTS = set([])

# Fill in this method with something that you want to do
# Possible keys:
# authors, author_detail, href, author, tags, content, summary, id, guidislink, link, links, updated, updated_parsed, title, title_detail
def matched(entry):
    print(entry["href"])

def get_posts(subreddit):
    sub_feed = feedparser.parse(subreddit)
    return sub_feed

# Dictionary of regex filters loaded from a file
# Key corresponds to subreddit (regexes under "default" are applied to all subs)
regex_filters = {}

with open('regex.yaml') as file:
    regex_filters = yaml.load(file, Loader=yaml.FullLoader)

# TODO: compile the regex expressions in advance
sub_list = [*regex_filters]
while True:
    for sub in sub_list:
        rss_feed = get_posts(sub)
        # Iterate over each rss entry
        for entry in rss_feed["entries"]:

            # If we've parsed this entry before skip over it
            if entry["id"] in CACHED_POSTS:
                continue

            # For each entry try each regex expression
            for key, regexs in regex_filters[sub].items():
                # Try every specified regex
                for regex in regexs:
                    # If the regex matches at least once then execute a python method
                    if re.compile(regex).search(entry[key]):
                        matched(entry)
            CACHED_POSTS.add(entry["id"])
    time.sleep(UPDATE_INTERVAL)