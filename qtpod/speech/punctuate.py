
import numpy as np
import requests


# Punctuator API endpoint
PUNCTUATE_API = "http://bark.phon.ioc.ee/punctuator"

# threshold between timestamps to add a break
TSTAMP_THRESH = 0.4


def _paragraphify(tscript, tstamps):

    split = ""
    pgraphs = []

    diffs = np.diff(tstamps)

    for n in range(len(tscript) - 1):
        split += tscript[n] + " "

        # within timestamp threshold -> new split
        if diffs[n] > TSTAMP_THRESH:
            pgraphs.append(split.strip())
            split = ""

    return pgraphs


def _punctuator_api(text):

    # call the API endpoint
    resp = requests.post(PUNCTUATE_API, data={"text": text})
    resp.raise_for_status()
    resp.close()

    return resp.text


def punctuate(tscript, tstamps, method="unified"):

    # unified method
    if method == "unified":
        splits = _paragraphify(tscript, tstamps)
        for (n, text) in enumerate(splits):
            splits[n] = _punctuator_api(text)

        return " ".join(splits)

    else:
        raise ValueError("unknown puncutate method")

