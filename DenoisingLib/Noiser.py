#!usr/bin/env python3

"""
Code written by Mattias Kockum
On 08/07/2022
The aim of this program is to add noises to a wav file
"""

import sys
import os
import scipy.io.wavfile
import random
import numpy as np


def add_noise(clean_file, noise_list, noisy_file, snr):
    """
    adds noises chosen at random in a list to a clean file
    """
    # reading clean
    clean_samplerate, clean_data = scipy.io.wavfile.read(clean_file)
    # picking enough noise
    noise_data_list = []
    noise_len = 0
    clean_len = len(clean_data)
    while noise_len < clean_len:
        nf = random.choice(noise_list)
        nsr , nd = scipy.io.wavfile.read(nf)
        nl = len(nd)
        noise_data_list += list(nd)
        noise_len += nl
    # clipping
    noise_data = np.array(noise_data_list[:clean_len])
    # adjusting noise volume
    c = int(10**((snr+23.2)/40))
    noise_data //= c
    # adding
    noisy_data = np.array([c+n for c,n in zip(clean_data, noise_data)])
    # writing to wav
    scipy.io.wavfile.write(noisy_file, clean_samplerate, noisy_data)
    #scipy.io.wavfile.write(noise_file, clean_samplerate, noise_data)
    # returning obtained SNR (remove for better performances)
    return(compute_snr(clean_data, noisy_data))


def compute_snr(clean_data, noisy_data):
    signal_RMS_squared = RMS_squared(clean_data)
    noise_RMS_squared = RMS_squared(clean_data-noisy_data)
    if noise_RMS_squared == 0:
        return(scipy.inf)
    else:
        return(dB(signal_RMS_squared/noise_RMS_squared))

def RMS_squared(array):
    squares_sum = sum([x**2 for x in array])
    return(squares_sum/len(array))

def dB(x):
    return(20*np.log10(x))


def main(parameters):
    clean_file = "./dataset/clean/clean1.wav"
    noise_list = ["./dataset/noise/---1_cCGK4M.wav"]
    #noise_file = "./noise.wav"
    noisy_file = "./out.wav"
    snr = 25
    add_noise(clean_file, noise_list, noisy_file, snr)
    return(0)


if __name__ == "__main__":
    main(sys.argv)
