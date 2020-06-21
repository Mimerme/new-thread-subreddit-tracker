# subreddit-post-tracker
do something when a reddit post's strings match a regex (in this case it send a push notification)

originally meant for subs like /r/minerswap, /r/hardwareexchange, etc. so I'd know when something I wanted was posted

# Usage
```regex.yaml``` is the main and only configuration file. it specifies what subs to watch and what regex expressions to match with. it monitors subs with rss feeds because its faster than parsing the html and allows for more configuration in the URL query parameters.

## ```regex.yaml``` format
### EXAMPLE
```
https://old.reddit.com/r/dota2/new/.rss:
  "title": ["(?i)battlepass", ...]
https://old.reddit.com/r/hardwareswap/new/.rss:
  "title": ["RX 590", "1060", "RX 580", "1660", "1070", "1080"]
```

```https://old.reddit.com/r/dota2/new/.rss```-  is the url to the rss feed

```title```- is the **field** in the each reddit post that the regex expressions will be matched to. possible fields are 

```["(?i)battlepass", ...]``` - a list of regex expressions that will be matched to each field