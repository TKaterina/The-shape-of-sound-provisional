import numpy as np
from scipy import signal, ndimage
import emd
import matplotlib.pyplot as plt

from scipy import signal
import simpleaudio as sa


#%% --------------------------------
##

sample_rate = 44100
seconds = 10
time = np.linspace(0, seconds,  int(seconds*sample_rate))

# w is the amplitude envelope - an oscillation that gradually speeds up over
# time. Start and finish speed controlled by f0 and f1
w = signal.chirp(time, f0=0.1, f1=75, t1=seconds, method='linear') / 2 + 1
# w = signal.chirp(time, f0=0.1, f1=15, t1=seconds, method='linear') / 2  # only fluctuation
# w = signal.chirp(time, f0=0.1, f1=70, t1=seconds, method='linear') / 2  # fluctuation and roughness
# w = signal.chirp(time, f0=0.1, f1=300, t1=seconds, method='linear') / 2  # reaches residue pitch
w = signal.chirp(time, f0=0.1, f1=1000, t1=seconds, method='linear') / 2

# Carrier is the pure tone that will be modulated - set at 300Hz (arbitrary for now)
carrier = np.sin(2*np.pi*5500*time)  # ITD can only be heard here
# carrier = np.sin(2*np.pi*1000*time)
# carrier = np.sin(2*np.pi*300*time)  # only fluctuation and roughness will be heard
# carrier = np.sin(2*np.pi*700*time)  # just another frequency to see if the plots are consistent.


note = w * carrier


#%% --------------------------------
## This tone is super weird - note that it initally sounds like tremolo but
# shifts into a dropping pitch.


# Ensure that highest value is in 16-bit range
audio = note * (2**15 - 1) / np.max(np.abs(note))
# Convert to 16-bit data
audio = audio.astype(np.int16)

play = False
if play:
    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)

#%% --------------------------------
# EMD

imf = emd.sift.sift(note, imf_opts={'sd_thresh': 1e-3}) # initial threshold 1e-6

IP, IF, IA = emd.spectra.frequency_transform(imf, sample_rate, 'hilbert', smooth_phase=441)
freq_edges, freq_centres = emd.spectra.define_hist_bins(5200, 5700, 128, 'linear')
f, hht = emd.spectra.hilberthuang(IF, IA, freq_edges, mode='amplitude', sum_time=False)

# Sum within short time windows - otherwise the plot is too big...
hht = hht.reshape(len(freq_centres), -1, 4).sum(axis=2)
hht = ndimage.gaussian_filter(hht, 1)


#%% --------------------------------
# FFT

f2, t2, pxx = signal.spectrogram(note, fs=sample_rate, nperseg=sample_rate//10, noverlap=sample_rate//20)


#%% --------------------------------
# Figure


plt.figure()
plt.subplot(121)
plt.imshow(hht, interpolation=None, aspect='auto', cmap='hot_r', origin='lower')
plt.title('EMD - Hilbert-Huang Transform')
plt.yticks(np.linspace(0, 128, 5), np.linspace(5200,5700,5))
plt.xticks(np.linspace(0, hht.shape[1], 11), np.linspace(0, 10, 11))
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time  (secs)')
plt.subplot(122)
plt.imshow(pxx[10:50,:], interpolation=None, aspect='auto', cmap='hot_r', origin='lower')
plt.title('Short Time Fourier Transform')
plt.yticks(np.linspace(0, 40, 5), np.linspace(5200,5700,5))
plt.xticks(np.linspace(0, pxx.shape[1], 11), np.linspace(0, 10, 11))
plt.xlabel('Time  (secs)')



