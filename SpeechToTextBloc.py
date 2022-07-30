#!usr/bin/env python3

"""
Code written by Mattias Kockum
On 13/07/2022
The aim of this program is to measure how well each StT works
"""


import sys
import os
os.environ["MPLCONFIGDIR"] =  os.getcwd() + "/configs/"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

sys.path.insert(0, "SpeechToTextLib")

from ModularBenchmarker import *
from SpeechToTextModels import *


models = [
    Wav2Vec2Model(),
    EspnetModel()
]

args = [
    "./dataset/clean",
    "./dataset/noisy/1",
    "./dataset/noisy/5",
    "./dataset/noisy/45",
    "./dataset/Denoisers/Finetuned_Denoiser/1"
]

df_path = "./dataframeSTT.csv"

BM = BenchMarker(models, args, df_path)
BM.populate()
BM.sort_values()
BM.plot_df("outFigSTT.svg")
plt.show()

def main(parameters):
    """
    """


if __name__ == "__main__":
    main(sys.argv)
