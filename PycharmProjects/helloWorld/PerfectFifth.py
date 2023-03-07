import numpy as np
from scipy import signal, ndimage
import emd
import matplotlib.pyplot as plt

from scipy import signal
import simpleaudio as sa

def play_note(note):
    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)


#%% --------------------------------
##

sample_rate = 44100
seconds = 3
time = np.linspace(0, seconds, seconds*sample_rate)

f1 = 440
fifth = 3/2  # 3:2, 4:3, 5:4, 6:5
f2 = f1 * fifth

x = np.sin(2*np.pi*f1*time)
y = np.sin(2*np.pi*f2*time)
z = x + y


#%% --------------------------------
# EMD

#imf = emd.sift.sift(z, imf_opts={'stop_method': 'rilling'})
imf = emd.sift.sift(z, imf_opts={'sd_thresh': 1e-6})

IP, IF, IA = emd.spectra.frequency_transform(imf, sample_rate, 'hilbert', smooth_phase=441)
freq_edges, freq_centres = emd.spectra.define_hist_bins(100, 2000, 512, 'linear')
f, hht = emd.spectra.hilberthuang(IF, IA, freq_edges, mode='amplitude', sum_time=False)

# Sum within short time windows - otherwis the plot is too big...
hht = hht.reshape(len(freq_centres), -1, 4).sum(axis=2)
#hht = ndimage.gaussian_filter(hht, 1)


#%% --------------------------------
# FFT

f2, t2, pxx = signal.spectrogram(z, fs=sample_rate, nperseg=sample_rate//10, noverlap=sample_rate//20)


#%% --------------------------------
# Figure

plt.figure()
plt.subplot(121)
plt.imshow(hht, interpolation=None, aspect='auto', cmap='hot_r', origin='lower')
plt.title('EMD - Hilbert-Huang Transform')
plt.yticks(np.linspace(0, 512, 10), np.linspace(100,2000,10))
plt.xticks(np.linspace(0, hht.shape[1], 11), np.linspace(0, 10, 11))
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time  (secs)')
plt.subplot(122)
plt.imshow(pxx[10:200, :], interpolation=None, aspect='auto', cmap='hot_r', origin='lower')
plt.title('Short Time Fourier Transform')
plt.yticks(np.linspace(0, 160, 10), np.linspace(100,2000,10))
plt.xticks(np.linspace(0, pxx.shape[1], 11), np.linspace(0, 10, 11))
plt.xlabel('Time  (secs)')



