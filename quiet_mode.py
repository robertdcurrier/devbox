#!/usr/bin/env python3
import librosa
import soundfile as sf
import noisereduce as nr
print('loading noise data...')
ndata, nrate = librosa.load("./data/pump-noise.wav")
print('loading audio...')
data, rate = librosa.load('./data/noisy-glider.wav')
print('reducing noise...')
reduced_noise = nr.reduce_noise(audio_clip=data, noise_clip=ndata, verbose=True)
print('writing reduced.wav')
print(len(reduced_noise))
sf.write('quiet-glider.wav', reduced_noise, rate, subtype='PCM_24')
