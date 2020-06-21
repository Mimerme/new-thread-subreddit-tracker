# reddit-rss-tracker
tracks reddit rss feeds for posts matching a regex

## use case
for stuff like /r/minerswap, /r/hardwareexchange, etc.

# Usage
```regex.yaml``` is the main and only configuration file. it specifies what subs to watch and what regex expressions to match with

## ```rgex.yaml``` format
### EXAMPLE
```
https://old.reddit.com/r/dota2/new/.rss:
  "title": ["(?i)battlepass", ...]
```

```https://old.reddit.com/r/dota2/new/.rss```-  is the url to the rss feed

```title```- is the **field** in the each reddit post that the regex expressions will be matched to. possible fields are 

```["(?i)battlepass", ...]``` - a list of regex expressions that will be matched to each field