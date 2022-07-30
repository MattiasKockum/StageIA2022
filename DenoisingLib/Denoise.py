#!usr/bin/env python3

import soundfile as sf
import librosa
import numpy as np
import os
from DTLN_model import DTLN_model


def process_file(model_name, audio_file_name, out_file_name):
    '''
    Funtion to read an audio file, rocess it by the network and write the
    enhanced audio to .wav file.

    Parameters
    ----------
    model : Keras model
        name and path to model
    audio_file_name : STRING
        Name and path of the input audio file.
    out_file_name : STRING
        Name and path of the target file.

    '''
    # importing model
    modelClass = DTLN_model();
    if model_name.find('_norm_') != -1:
        norm_stft = True
    else:
        norm_stft = False
    modelClass.build_DTLN_model(norm_stft=norm_stft)
    modelClass.model.load_weights(model_name)
    model = modelClass.model
    # read audio file with librosa to handle resampling and enforce mono
    in_data,fs = librosa.core.load(audio_file_name, sr=16000, mono=True)
    # get length of file
    len_orig = len(in_data)
    # pad audio
    zero_pad = np.zeros(384)
    in_data = np.concatenate((zero_pad, in_data, zero_pad), axis=0)
    # predict audio with the model
    predicted = model.predict_on_batch(
        np.expand_dims(in_data,axis=0).astype(np.float32))
    # squeeze the batch dimension away
    predicted_speech = np.squeeze(predicted)
    predicted_speech = predicted_speech[384:384+len_orig]
    # write the file to target destination
    sf.write(out_file_name, predicted_speech,fs)
