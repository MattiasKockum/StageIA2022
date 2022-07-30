#!usr/bin/env python3

"""
Code written by Mattias Kockum
On 05/07/2022
The aim of this program is to wrap ModularBenchmarker and ModelTesters.py
"""


import sys

sys.path.insert(0, "DenoisingLib")

from ModularBenchmarker import *
from EvalFunctions import *


models = [
    None_Denoiser(),
    #Baseline_Denoiser(),
    Finetuned_Denoiser(),
    #Sox_Denoiser()
]

args = [
    1,
    5,
    #10,
    #20,
    #30,
    45
]

df_path = "./dataframeDenoising.csv"

BM = BenchMarker(models, args, df_path)
BM.populate()
BM.sort()
BM.plot_df("outFigDenoising.svg")
plt.show()

# test code for adding rows and columns
"""
x = Sox_Denoiser()
x.name = "Sox_Denoiser2"
BM.add_model(x)

BM.add_arg(40)

BM.compute_df()

BM.plot_df()
plt.show()
"""

def main(parameters):
    """
    BM = BenchMarker(models, args, df_path)
    BM.populate()
    """


if __name__ == "__main__":
    main(sys.argv)
