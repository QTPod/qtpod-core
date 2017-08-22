"""
podcast.py: An extremely simple podcast encapsulation.
"""

import multiprocessing
import os
import re
import subprocess
import tempfile
import xml.etree.ElementTree as ET

import requests

from .speech import punctuate, transcribe


class Episode(object):

    def __init__(self, podcast, data):

        self._podcast = podcast

        # episode elements/parameters
        self._guid = None
        self._title = None
        self._desc = None
        self._date = None

        # URL to audio source (mp3, etc...)
        self._audio_url = None
        self._audio_type = None
        self._audio_path = None
        self._audio_dir = tempfile.mkdtemp()

        # podcast transcript, to be computed using speech engine
        self._tscript = None
        self._tstamps = None

        for elem in data:
            if elem.tag in ["guid"]:
                self._guid = elem.text
            elif elem.tag in ["title"]:
                self._title = elem.text
            elif elem.tag in ["description", "summary"]:
                self._desc = elem.text
            elif elem.tag in ["updated"]:
                self._date = elem.text
            elif elem.tag in ["enclosure"]:
                self._audio_url = elem.attrib["url"]
                self._audio_type = elem.attrib["type"]
            elif elem.tag in ["link"] and "rel" in elem.attrib:
                if elem.attrib["rel"] == "enclosure":
                    self._audio_url = elem.attrib["href"]
                    self._audio_type = elem.attrib["type"]

    def _get_audio(self):

        # ensure that URL has been parsed
        if self._audio_url is None:
            raise ValueError("no audio URL provided")

        # parse filename from audio URL
        fname = self._audio_url.split("/")[-1].split("?")[0]
        self._audio_path = os.path.join(self._audio_dir, fname)

        # get audio data from URL
        while True:
            try:
                resp = requests.get(self._audio_url)
                resp.raise_for_status()
                break
            except requests.exceptions.ConnectionError:
                msg = "Failed {0}, retrying".format(self._audio_url)
                sys.stderr.write(msg + "\n")
                continue

        # grab the content and save it to the directory
        with open(self._audio_path, "wb") as fh:
            for chunk in resp.iter_content(chunk_size=1024):
                fh.write(chunk)

        resp.close()

    def transcribe(self):

        # ensure that audio has been downloaded
        if self._audio_path is None:
            self._get_audio()

        # transcribe and punctuate audio
        (tscript, tstamps) = transcribe(self._audio_path)
        self._tscript = punctuate(tscript, tstamps, method="tstamp")

    # add getters for podcast elements
    guid = property(lambda self: self._guid)
    title = property(lambda self: self._title)
    desc = property(lambda self: self._desc)
    date = property(lambda self: self._date)
    tscript = property(lambda self: self._tscript)


class Podcast(object):

    def __init__(self, feed_url):

        self._feed_url = feed_url

        # podcast elements/parameters
        self._spec = None
        self._name = None
        self._desc = None
        self._link = None
        self._category = None

        # to be populated with guid->Episode (objects)
        self._episodes = []

        self.refresh()

    def refresh(self):

        # grab and parse the XML data
        raw = requests.get(self._feed_url).text
        xml = raw.encode("ascii", "ignore")
        feed = ET.fromstring(xml)

        # check feed type (RSS vs Atom)
        if feed.tag == "rss":
            self._spec = "rss"
            data = feed.find("channel")
        elif feed.tag == "feed":
            self._spec = "atom"
            data = feed
        else:
            raise ValueError, "unknown feed standard"

        # populate class variables
        for elem in data:
            if elem.tag in ["title"]:
                self._name = elem.text
            elif elem.tag in ["description", "subtitle"]:
                self._desc = elem.text
            elif elem.tag in ["link"]:
                self._link = elem.text
            elif elem.tag in ["category"]:
                self._category = elem.text
            elif elem.tag in ["item", "entry"]:
                self._episodes.append(Episode(self, elem))

    def as_string(self):

        output = ""
        output += "Name:      {0}\n".format(self._name)
        output += "Subtitle:  {0}\n".format(self._desc)
        output += "Link:      {0}\n".format(self._link)
        output += "Category:  {0}\n".format(self._category)
        output += "Episodes:  {0}\n".format(len(self._episodes))
        output += "\n"

        return output

    # add getters for podcast elements
    spec = property(lambda self: self._spec)
    name = property(lambda self: self._name)
    desc = property(lambda self: self._desc)
    link = property(lambda self: self._link)
    category = property(lambda self: self._category)

    # return tuple to prevent accidental modification
    episodes = property(lambda self: tuple(self._episodes))


def make_train_data(feed_url, n_ep=5):

    # load podcast
    podcast = Podcast(feed_url)
    name = podcast.name.lower()
    name = re.sub("[^0-9a-zA-Z]+", "", name)

    # process episodes
    path = "/tmp/" + name + "_tscript.txt"
    with open(path, "w") as fh:
        for ep in podcast.episodes[:n_ep]:
            ep.transcribe()
            fh.write(ep.tscript + "\n\n\n")


if __name__ == "__main__":

    # test feed URLs
    test_urls = [
        "http://feed.thisamericanlife.org/talpodcast?format=xml",
        "http://www.howstuffworks.com/podcasts/stuff-you-should-know.rss",
        "https://www.npr.org/rss/podcast.php?id=510298",
        "https://www.npr.org/rss/podcast.php?id=510307",
        "http://feeds.feedburner.com/freakonomicsradio?format=xml",
        "https://www.npr.org/rss/podcast.php?id=510318",
        "https://www.npr.org/rss/podcast.php?id=510289",
        "http://feeds.wnyc.org/radiolab?format=xml",
        "https://www.npr.org/rss/podcast.php?id=381444908",
        "http://feeds.podtrac.com/zKq6WZZLTlbM",
        "https://www.npr.org/rss/podcast.php?id=344098539",
        "http://joeroganexp.joerogan.libsynpro.com/rss",
        "https://www.npr.org/rss/podcast.php?id=510310",
        "https://www.npr.org/rss/podcast.php?id=510308",
        "http://feeds.feedburner.com/pod-save-america?format=xml",
        "http://feeds.99percentinvisible.org/99percentinvisible?format=xml",
        "https://www.npr.org/rss/podcast.php?id=510313",
        "http://feeds.stownpodcast.org/stownpodcast?format=xml",
        "http://feeds.themoth.org/themothpodcast?format=xml",
        "http://thewayiheardit.rsvmedia.com/rss",
    ]

