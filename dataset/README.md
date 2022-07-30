Exemple of how the dataset directory is working

dataset
├── clean
│   └── clean1.wav
├── Denoisers
│   ├── Baseline_Denoiser
│   │   ├── 1
│   │   │   └── clean1.wav
│   │   ├── 10
│   │   │   └── clean1.wav
│   │   ├── 20
│   │   │   └── clean1.wav
│   │   ├── 30
│   │   │   └── clean1.wav
│   │   ├── 45
│   │   │   └── clean1.wav
│   │   └── 5
│   │       └── clean1.wav
│   ├── Finetuned_Denoiser
│   │   ├── 1
│   │   │   └── clean1.wav
│   │   ├── 10
│   │   │   └── clean1.wav
│   │   ├── 20
│   │   │   └── clean1.wav
│   │   ├── 30
│   │   │   └── clean1.wav
│   │   ├── 45
│   │   │   └── clean1.wav
│   │   └── 5
│   │       └── clean1.wav
│   ├── None_Denoiser
│   │   ├── 1
│   │   │   └── clean1.wav
│   │   ├── 10
│   │   │   └── clean1.wav
│   │   ├── 20
│   │   │   └── clean1.wav
│   │   ├── 30
│   │   │   └── clean1.wav
│   │   ├── 45
│   │   │   └── clean1.wav
│   │   └── 5
│   │       └── clean1.wav
│   └── Sox_Denoiser
│       ├── 1
│       │   └── clean1.wav
│       ├── 10
│       │   └── clean1.wav
│       ├── 20
│       │   └── clean1.wav
│       ├── 30
│       │   └── clean1.wav
│       ├── 45
│       │   └── clean1.wav
│       └── 5
│           └── clean1.wav
├── noise
│   └── ---1_cCGK4M.wav
├── noisy
│   ├── 1
│   │   └── clean1.wav
│   ├── 10
│   │   └── clean1.wav
│   ├── 20
│   │   └── clean1.wav
│   ├── 30
│   │   └── clean1.wav
│   ├── 45
│   │   └── clean1.wav
│   └── 5
│       └── clean1.wav
├── SpeechToTexters
│   ├── EspnetSTT
│   │   ├── clean
│   │   │   └── clean1.txt
│   │   ├── Denoisers
│   │   │   └── Finetuned_Denoiser
│   │   │       └── 1
│   │   │           └── clean1.txt
│   │   └── noisy
│   │       ├── 1
│   │       │   └── clean1.txt
│   │       ├── 10
│   │       │   └── clean1.txt
│   │       └── 5
│   │           └── clean1.txt
│   └── Wav2Vec2STT
│       ├── clean
│       │   └── clean1.txt
│       ├── Denoisers
│       │   └── Finetuned_Denoiser
│       │       └── 1
│       │           └── clean1.txt
│       └── noisy
│           ├── 1
│           │   └── clean1.txt
│           ├── 10
│           │   └── clean1.txt
│           └── 5
│               └── clean1.txt
├── text
│   └── clean1.txt
└── unusedNoises
    ├── -00j9zuOIpw.wav
    ├── -02m1Zi-IXI.wav
    ├── ---1_cCGK4M.wav
    ├── --65x-naOz0.wav
    ├── --9VR_F7CtY.wav
    ├── --AErD4Wx6c.wav
    ├── --diQGtdz9Q.wav
    ├── --iFD6IyQW8.wav
    ├── --Jcz_RawUA.wav
    ├── --Lj4Y_96f0.wav
    ├── --mMv-eQ2yQ.wav
    ├── --OBFOUWZi0.wav
    ├── --qEoNMshyY.wav
    ├── --WKuD_46Fk.wav
    ├── --XCrxv9u8M.wav
    ├── --Xn_Zfv9sQ.wav
    └── --Z4X0SQxBc.wav
