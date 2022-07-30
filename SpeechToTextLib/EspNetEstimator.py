#!usr/bin/env python3

"""
Code written by Mattias Kockum
On 13/07/2022
The aim of this program is to compute WER from speech to text
"""


import sys
import os

import subprocess as s
import string
import soundfile
from espnet_model_zoo.downloader import ModelDownloader
from espnet2.bin.asr_inference import Speech2Text

def estimateText(wavFilePath, modelPath):
    d = ModelDownloader()
    decoder = Speech2Text(
        **d.download_and_unpack(modelPath),
        device="cpu", #cuda if gpu
        minlenratio=0.0,
        maxlenratio=0.0,
        ctc_weight=0.3,
        beam_size=10,
        batch_size=0,
        nbest=1
    )
    audio, rate = soundfile.read(wavFilePath)
    nbests = decoder(audio)
    text = nbests[0][0]
    return(text)


def main(parameters):
    """
    """
    text = estimateText(parameters[1], parameters[2])
    print(text)
    return(text)


if __name__ == "__main__":
    main(sys.argv)
