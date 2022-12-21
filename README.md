The project consists in the making of a benchmarking tool to measure and compare the efficiency of multiple denoisers.

![Alt text](https://raw.githubusercontent.com/MattiasKockum/StageIA2022/26bd30fb97b37fea3ec87fb46daaf4251a3c266c/ClassDiagram.svg)
<img src="https://raw.githubusercontent.com/MattiasKockum/StageIA2022/26bd30fb97b37fea3ec87fb46daaf4251a3c266c/ClassDiagram.svg">


Example of a working directory tree structure

```bash
.
├── configs
│   └── fontlist-v330.json
├── dataset
│   ├── clean
│   │   └── clean1.wav
│   ├── noise
│   │   └── ---1_cCGK4M.wav
│   ├── README.md
│   ├── text
│   │   └── clean1.txt
│   └── unusedNoises
│       ├── -00j9zuOIpw.wav
│       ├── -02m1Zi-IXI.wav
│       ├── ---1_cCGK4M.wav
│       ├── --65x-naOz0.wav
│       ├── --9VR_F7CtY.wav
│       ├── --AErD4Wx6c.wav
│       ├── --diQGtdz9Q.wav
│       ├── --iFD6IyQW8.wav
│       ├── --Jcz_RawUA.wav
│       ├── --Lj4Y_96f0.wav
│       ├── --mMv-eQ2yQ.wav
│       ├── --OBFOUWZi0.wav
│       ├── --qEoNMshyY.wav
│       ├── --WKuD_46Fk.wav
│       ├── --XCrxv9u8M.wav
│       ├── --Xn_Zfv9sQ.wav
│       └── --Z4X0SQxBc.wav
├── DenoisingBloc.py
├── DenoisingLib
│   ├── Denoise.py
│   ├── DTLN_model.py
│   ├── EvalFunctions.py
│   ├── Noiser.py
│   ├── pretrained_models
│   │   ├── 0013_librispeech_v1_chain.tar.gz
│   │   ├── DTLN_norm_40h.h5
│   │   ├── DTLN_norm_40h_saved_model
│   │   │   ├── saved_model.pb
│   │   │   └── variables
│   │   │       ├── variables.data-00000-of-00002
│   │   │       ├── variables.data-00001-of-00002
│   │   │       └── variables.index
│   │   ├── DTLN_norm_500h.h5
│   │   ├── DTLN_norm_500h_saved_model
│   │   │   ├── saved_model.pb
│   │   │   └── variables
│   │   │       ├── variables.data-00000-of-00002
│   │   │       ├── variables.data-00001-of-00002
│   │   │       └── variables.index
│   │   ├── dtln_saved_model
│   │   │   ├── saved_model.pb
│   │   │   └── variables
│   │   │       ├── variables.data-00000-of-00001
│   │   │       └── variables.index
│   │   ├── exp
│   │   │   └── chain_cleaned
│   │   │       └── tdnn_1d_sp
│   │   │           ├── 0.mdl
│   │   │           ├── 0.trans_mdl
│   │   │           ├── accuracy.report
│   │   │           ├── cmvn_opts
│   │   │           ├── configs
│   │   │           │   ├── final.config
│   │   │           │   ├── init.config
│   │   │           │   ├── init.raw
│   │   │           │   ├── lda.mat
│   │   │           │   ├── network.xconfig
│   │   │           │   ├── ref.config
│   │   │           │   ├── ref.raw
│   │   │           │   ├── vars
│   │   │           │   ├── xconfig
│   │   │           │   ├── xconfig.expanded.1
│   │   │           │   └── xconfig.expanded.2
│   │   │           ├── den.fst
│   │   │           ├── final.ie.id
│   │   │           ├── final.mdl
│   │   │           ├── frame_subsampling_factor
│   │   │           ├── lda.mat
│   │   │           ├── normalization.fst
│   │   │           ├── num_jobs
│   │   │           ├── phone_lm.fst
│   │   │           ├── phones.txt
│   │   │           ├── srand
│   │   │           └── tree
│   │   ├── model_1.onnx
│   │   ├── model_1.tflite
│   │   ├── model_2.onnx
│   │   ├── model_2.tflite
│   │   ├── model.h5
│   │   ├── model_quant_1.tflite
│   │   └── model_quant_2.tflite
│   └── __pycache__
│       ├── Denoise.cpython-39.pyc
│       ├── DTLN_model.cpython-39.pyc
│       ├── EvalFunctions.cpython-39.pyc
│       └── Noiser.cpython-39.pyc
├── ModularBenchmarker.py
├── PipeLine.sh
├── __pycache__
│   ├── Denoise.cpython-39.pyc
│   ├── DTLN_model.cpython-39.pyc
│   ├── EvalFunctions.cpython-39.pyc
│   ├── ModularBenchmarker.cpython-39.pyc
│   └── Noiser.cpython-39.pyc
├── README.md
├── Reset.sh
├── SpeechToTextBloc.py
└── SpeechToTextLib
    ├── EspNetEstimator.py
    ├── pretrained_models
    │   └── exp
    │       └── chain_cleaned
    │           └── tdnn_1d_sp
    │               ├── 0.mdl
    │               ├── 0.trans_mdl
    │               ├── accuracy.report
    │               ├── cmvn_opts
    │               ├── configs
    │               │   ├── final.config
    │               │   ├── init.config
    │               │   ├── init.raw
    │               │   ├── lda.mat
    │               │   ├── network.xconfig
    │               │   ├── ref.config
    │               │   ├── ref.raw
    │               │   ├── vars
    │               │   ├── xconfig
    │               │   ├── xconfig.expanded.1
    │               │   └── xconfig.expanded.2
    │               ├── den.fst
    │               ├── final.ie.id
    │               ├── final.mdl
    │               ├── frame_subsampling_factor
    │               ├── lda.mat
    │               ├── normalization.fst
    │               ├── num_jobs
    │               ├── phone_lm.fst
    │               ├── phones.txt
    │               ├── srand
    │               └── tree
    ├── __pycache__
    │   ├── EspNet.cpython-39.pyc
    │   ├── SpeechToTextModels.cpython-39.pyc
    │   └── Wav2VecStt.cpython-39.pyc
    ├── SpeechToTextModels
    │   ├── facebook_wav2vec2-base-960h
    │   │   ├── decoder.zip
    │   │   └── encoder.zip
    │   └── facebook_wav2vec2-base-960h.zip
    ├── SpeechToTextModels.py
    └── Wav2Vec2SttEstimator.py
```bash
