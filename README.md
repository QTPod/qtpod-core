# qtpod-core

## Introduction

This repository contains QTPod's core backend.

## Requirements

 - Python (2.6, 2.7, or 3.5+)
 - requests >= 2.9.1

## Usage

```
import podcast

feed_url = "https://www.npr.org/rss/podcast.php?id=510289"
pod = podcast.Podcast(feed_url)

# print website:
print("{0} website: {1}".format(pod.name, pod.link))

# count the number of episodes
print("Number of episodes: {0}".format(len(pod.episodes)))

# download audio for the first episode to a temporary folder
ep = pod.episodes[0]
ep.transcribe()
print(ep.tscript)
```
