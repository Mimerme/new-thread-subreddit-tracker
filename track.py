import yaml
import re
import feedparser
import pdb
import time
from notify_run import Notify
import sys

UPDATE_INTERVAL = 30
# Save the ids of already processed posts
CACHED_POSTS = set([])

notify = Notify()

# Fill in this method with something that you want to do
# Possible keys:
# authors, author_detail, href, author, tags, content, summary, id, guidislink, link, links, updated, updated_parsed, title, title_detail
def matched(entry):
    print("Found a new post: "+ entry["links"][0]["href"])
    notify.send("Found a post that matches!", entry["links"][0]["href"])

def get_posts(subreddit):
    sub_feed = feedparser.parse(subreddit)
    return sub_feed


def main():
    # Dictionary of regex filters loaded from a file
    # Key corresponds to subreddit (regexes under "default" are applied to all subs)
    regex_filters = {}

    with open('regex.yaml') as file:
        regex_filters = yaml.safe_load(file)


    print("Compiling regex expressisons...")
    for key, search_filters in regex_filters.items():
        for field, regexes in search_filters.items():
            regex_filters[key][field] = list(map(lambda regex: re.compile(regex) , regex_filters[key][field]))
    print("Finished compiling regex expresions")

    sub_list = [*regex_filters]

    print("Listening...")
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
                        if regex.search(entry[key]):
                            matched(entry)
                CACHED_POSTS.add(entry["id"])
        time.sleep(UPDATE_INTERVAL)

if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        notify.send("This is a test", "https://google.com")
    else:
        main()
