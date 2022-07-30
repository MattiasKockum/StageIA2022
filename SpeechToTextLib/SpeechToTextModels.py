#!usr/bin/env python3

"""
Code written by Mattias Kockum
On 13/07/2022
The aim of this program is to compute WER from speech to text
"""


import sys
import os
import subprocess

# WARNING : imports are a bit all over

#import speech_recognition as sr # Can't import on server


StTmodel1Path = "SpeechToTextLib/pretrained_models/facebook_wav2vec2-base-960h"
#  TODO must be updated dor ESPNET
StTmodel2Path = "Shinji Watanabe/librispeech_asr_train_asr_transformer_e18_raw_bpe_sp_valid.acc.best"
#  TODO must be updated for Kaldi
StTmodel3Path = "SpeechToTextLib/pretrained_models/facebook_wav2vec2-base-960h"
StTmodel4Path = "en-EN" # not actually a path but it is easier like that

TTP1 = "./dataset/text"

class SpeechToTextModel(object):
    """
    A generic class for ASR
    Sub-classes are meant to support a specific model
    """
    def __init__(self, textsPath = TTP1, modelPath = StTmodel1Path):
        self.name = "Default StT Model"
        self.textsPath = textsPath
        self.modelPath = modelPath
        #self.decoder =  None

    def open_dir(self, directory):
        """
        Make sure the directory exists
        """
        if not os.path.exists(directory):
            os.makedirs(directory)

    def eval(self, directory):
        """
        Returns the combined wer of the predictions from the model
        when applied to the wav files in the directory
        """
        # getting estimated texts directory path
        out_dir = directory.split("/")
        out_dir.insert(2, self.name)
        out_dir.insert(2, "SpeechToTexters")
        out_dir = "/".join(out_dir)
        # opening files
        self.open_dir(out_dir)
        # for each clean text, calulate WER with estimated text
        WER = self.ComputeWERfromDir(directory, out_dir)
        return(WER)

    def ComputeWERfromDir(self, directory, out_dir):
        from jiwer import wer
        s = 0
        n = 0
        for root, dirs, files in os.walk(f"{self.trueTextsPath}"):
            for file in files:
                # verifiying if estimated text is already created
                if os.path.exists(f"{out_dir}/{file}"):
                    print("estimatedText found")
                    f = open(f"{out_dir}/{file}", 'r')
                    estimatedText = f.readlines()[0]
                    f.close()
                else:
                    print("estimatedText not found")
                    # estimating text
                    wavFilePath = directory + "/" + file[:-3] + "wav"
                    estimatedText = self.estimateText(wavFilePath)
                    # Saving estimated text
                    f = open(f"{out_dir}/{file}", 'w')
                    f.write(estimatedText)
                    f.close()
                trueTextsPath = root + "/" + file
                f = open(trueTextsPath, 'r')
                trueText = f.readlines()[0]
                f.close()
                # Computing WER
                s = wer(trueText, estimatedText)
                n += 1
        return(s/n)

    def estimateText(self, wavFilePath):
        """
        a blank function to estimate text from a wav file
        """
        return("---------NO TEXT ESTIMATED---------")


class Wav2Vec2Model(SpeechToTextModel):
    def __init__(self,
                 trueTextsPath = TTP1,
                 modelPath = StTmodel1Path):
        self.name = "Wav2Vec2STT"
        self.trueTextsPath = trueTextsPath
        self.modelPath = modelPath

    def estimateText(self, wavFilePath):
        """
        Function calls for another python script in order to avoid
        conflictual packages imports
        """
        code_path = "SpeechToTextLib/Wav2Vec2SttEstimator.py"
        cmd = f"python '{code_path}' '{wavFilePath}' '{self.modelPath}'"
        r = subprocess.check_output(cmd, shell=True)
        estimatedText = str(r)[2:-3]
        return(estimatedText)


class EspnetModel(SpeechToTextModel):
    def __init__(self,
                 trueTextsPath = TTP1,
                 modelPath = StTmodel2Path
                ):
        self.name = "EspnetSTT"
        self.trueTextsPath = trueTextsPath
        self.modelPath = modelPath


    def estimateText(self, wavFilePath):
        """
        Function calls for another python script in order to avoid
        conflictual packages imports
        """
        code_path = "SpeechToTextLib/EspNetEstimator.py"
        cmd = f"python '{code_path}' '{wavFilePath}' '{self.modelPath}'"
        r = subprocess.check_output(cmd, shell=True)
        estimatedText = str(r)[2:-3]
        return(estimatedText)

"""
class KaldiModel(SpeechToTextModel):
    def __init__(self,
                 trueTextsPath = TTP1,
                 modelPath = StTmodel3Path
                ):
        self.name = "KaldiSTT"
        self.trueTextsPath = trueTextsPath
        self.modelPath = modelPath
        self.decoder = None


    def estimateText(self, wavFilePath):
        pass

"""

"""
class SpeechRecognitionModel(SpeechToTextModel):
    def __init__(self,
                 trueTextsPath = TTP1,
                 modelPath = StTmodel4Path
                ):
        self.name = "SpeechRecognitionStT"
        self.trueTextsPath = trueTextsPath
        self.modelPath = modelPath
        #self.decoder = None


    def estimateText(self, wavFilePath):
        r = sr.Recognizer()
        with sr.AudioFile(wavFilePath) as source:
            audio = r.record(source)
        t = r.recognize_google(audio, language=self.modelPath).upper()
        return(t)
"""

def main(parameters):
    """
    """


if __name__ == "__main__":
    main(sys.argv)
