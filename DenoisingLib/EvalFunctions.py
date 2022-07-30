#!usr/bin/env python3

"""
Code written by Mattias Kockum
On 05/07/2022
The aim of this program is to provide functions for testing models
for the benchmarking tool
"""


#import numpy as np
import scipy.io.wavfile
import os
import re
import subprocess
import shutil
import configparser

from Noiser import *

from Denoise import *

class Denoiser(object):
    """
    A denoiser generic class
    """
    def __init__(self):
        self.name = "DefaultDenoiser"
        self.model_name = "DefaultModel.h5"

    def denoise(self, noisy_file, denoised_file):
        #print(f"I am being called as {self.name}")
        process_file(
            self.model_name,
            f"{noisy_file}",
            f"{denoised_file}"
        )

    def open_dirs(self, snr, path):
        #print("opening directories")
        Dirs_to_open = [
            f"{path}", f"{path}/clean", f"{path}/noisy",
            f"{path}/noisy/{snr}", f"{path}/Denoisers/{self.name}",
            f"{path}/Denoisers/{self.name}/{snr}"
        ]
        for d in Dirs_to_open:
            if not os.path.exists(d):
                os.makedirs(d)

    def compute_noisy_dir(self, snr, path):
        #print("creating noisy database")
        noise_list = [
            f"{path}/noise/"+ n
            for n in os.listdir(f"{path}/noise/")
        ]
        for root, dirs, files in os.walk(f"{path}/clean"):
            for file in files:
                if not os.path.exists(f"{path}/noisy/{snr}/{file}"):
                    #print(f"creating : {path}/noisy/{snr}/{file}")
                    add_noise(
                        f"{path}/clean/{file}",
                        noise_list,
                        f"{path}/noisy/{snr}/{file}",
                        snr
                    )

    def denoise_dir(self, snr, path):
        #print("Denoising")
        for root, dirs, files in os.walk(f"{path}/noisy/{snr}"):
            for file in files:
                if not os.path.exists(f"{path}/Denoisers/{self.name}/{snr}/{file}"):
                    #print(f"creating : {path}/Denoisers/{self.name}/{snr}/{file}")
                    self.denoise(
                        f"{path}/noisy/{snr}/{file}",
                        f"{path}/Denoisers/{self.name}/{snr}/{file}"
                    )
                else:
                    pass
                    #print("File already denoised")

    def compare_dirs(self, snr, path):
        #print("Comparing")
        s = 0 # sum of snr
        n = 0 # nb of files compared
        for root, dirs, files in os.walk(
            f"{path}/Denoisers/{self.name}/{snr}"):
            for file in files:
                clean_sr, clean_data = scipy.io.wavfile.read(
                    f"{path}/clean/{file}"
                )
                denoised_sr, denoised_data = scipy.io.wavfile.read(
                    f"{path}/Denoisers/{self.name}/{snr}/{file}"
                )
                s += compute_snr(clean_data, denoised_data)
                n += 1
        if n == 0:
            return(-1)
        else:
            # returning mean SNR
            return(float(s/n))

    def eval(self, snr, path="./dataset"):
        """
        +dataset
            \-clean
                \- clean1.wav
                \- clean2.wav
            \-noisy
                \-snr (ex 50)
                    \- noisy1.wav
                    \- noisy2.wav
            \-Denoisers
                \-self.name (ex : baseline)
                    \-snr (ex : 50)
                        \- denoised1.wav
                        \- denoised2.wav
        """
        #print(f"Evaluation running : Denoiser={self.name}, SNR={snr}")
        #print(f"path : {path}")
        # opening directories
        self.open_dirs(snr, path)
        # computing noisy files
        self.compute_noisy_dir(snr, path)
        # denoising
        self.denoise_dir(snr, path)
        # comparing
        return(self.compare_dirs(snr, path))


class None_Denoiser(Denoiser):
    """
    """
    def __init__(self):
        self.name = "None_Denoiser"

    def denoise(self, noisy_file, denoised_file):
        shutil.copy(noisy_file, denoised_file)

class Baseline_Denoiser(Denoiser):
    """
    """
    def __init__(self):
        self.name = "Baseline_Denoiser"
        self.model_name = "DenoisingLib/pretrained_models/DTLN_norm_40h.h5"


class Finetuned_Denoiser(Denoiser):
    """
    """
    def __init__(self):
        self.name = "Finetuned_Denoiser"
        self.model_name =  "DenoisingLib/pretrained_models/DTLN_norm_500h.h5"

class Sox_Denoiser(Denoiser):
    """
    """
    def __init__(self):
        self.name = "Sox_Denoiser"

    def denoise(self, noisy_file, denoised_file):
        shutil.copy(noisy_file, denoised_file)


# Denoisers
denoisers = {
    "none" : None_Denoiser,
    "baseline" : Baseline_Denoiser,
    "finetuned" : Finetuned_Denoiser,
    "sox" : Sox_Denoiser
}

