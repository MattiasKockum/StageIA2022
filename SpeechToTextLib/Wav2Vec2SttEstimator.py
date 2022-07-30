#!usr/bin/env python3

"""
Code written by Mattias Kockum
On 13/07/2022
The aim of this program is to compute WER from speech to text
"""


import sys
import os

from wav2vec2_stt import Wav2Vec2STT
import wave

def estimateText(wavFilePath, modelPath):
    decoder = Wav2Vec2STT(modelPath)
    # Getting read text through wav file
    wavFile = wave.open(wavFilePath)
    wavSamples = wavFile.readframes(wavFile.getnframes())
    # Estimating said text with decoder
    estimatedText = decoder.decode(wavSamples)
    return(estimatedText)

def main(parameters):
    """
    """
    text = estimateText(parameters[1], parameters[2])
    print(text)
    return(text)


if __name__ == "__main__":
    main(sys.argv)
