
import os
import re
import subprocess


DEVNULL = open(os.devnull, "w")


def _transcribe_kaldi(audio_path):

    tscript = []
    tstamps = []

    # run transcription command
    tscript_cmd = ["transcribe_kaldi.sh", audio_path]
    subprocess.call(tscript_cmd)

    # load ctm file
    ctm_path = os.path.splitext(audio_path)[0] + ".ctm"
    with open(ctm_path, "r") as fh:
        ctm = [line.split(" ") for line in fh]
        align = [(elem[4], elem[2]) for elem in ctm]

    # postprocess transcript
    for word in align:
        if all(ch not in "[]<>" for ch in word[0]):
            tscript.append(re.sub("[^a-zA-Z]+", "", word[0]))
            tstamps.append(float(word[1]))

    return (tscript, tstamps)


def _transcribe_dspeech():

    raise NotImplementedError("deep speech not implemented")


def transcribe(audio_path, method="kaldi"):

    # run audio through transcriber
    if method == "kaldi":
        return _transcribe_kaldi(audio_path)
    elif method == "dspeech":
        return _transcribe_dspeech(audio_path)


if __name__ == "__main__":

    # test audio path
    test_audio = "/tmp/20170728_pmoney_pmpod785.mp3"

    result = transcribe(test_audio, method="kaldi")
    #result = transcribe(test_audio, method="dspeech")

    print(result[0])

