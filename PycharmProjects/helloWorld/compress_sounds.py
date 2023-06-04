import glob 
from pydub import AudioSegment
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

infiles = glob.glob('C:\\Users\ktamp\OneDrive\Desktop\TheShapeofSound\mp3Gallery\*.mp3')

for ifile in infiles:
    print(ifile)
    audio = AudioSegment.from_file(ifile)

    x = np.array(audio.get_array_of_samples())
    env = np.abs(signal.hilbert(x))
    env = signal.medfilt(env, 1001)

    y = x / env

    y = (y * (x.max() / y.max())).astype('int16')
    wavfile.write(ifile.replace('.mp3', '_ampnorm.wav'), 44100, y)

    plt.figure()
    plt.subplot(311)
    plt.plot(x)
    plt.title(ifile)
    plt.subplot(312)
    plt.plot(env)
    plt.subplot(313)
    plt.plot(y)
