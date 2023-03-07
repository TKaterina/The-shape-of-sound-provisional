import numpy as np
from scipy import signal, ndimage
import emd
import matplotlib.pyplot as plt

from scipy import signal, stats
import simpleaudio as sa

def play_note(note):
    note = stats.zscore(note)
    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)

#%% --------------------------------
##

sample_rate = 44100
seconds = 1
time = np.linspace(0, seconds,  int(seconds*sample_rate))

f0 = 440
nharmonics = 6  # Including f0

freqs = np.arange(1, nharmonics+1)*f0

x = np.zeros((len(time), nharmonics))
for ii in range(len(freqs)):
    x[:, ii] = np.sin(2*np.pi*freqs[ii]*time)

# Full
y = x.sum(axis=1)
# Missing Fundamental
z = x[:, 1:].sum(axis=1)


#%% --------------------------------
##

imf_y = emd.sift.sift(y, imf_opts={'sd_thresh': 1e-6})
imf_z = emd.sift.sift(z, imf_opts={'sd_thresh': 1e-6})



IPy, IFy, IAy = emd.spectra.frequency_transform(imf_y, sample_rate, 'hilbert', smooth_phase=441)
IPz, IFz, IAz = emd.spectra.frequency_transform(imf_z, sample_rate, 'hilbert', smooth_phase=441)


#%% --------------------------------
##

# Quick plot - the higher components are well matched. The f0 frequency is much
# lower amplitude in the 'missing' condition - but not zero!
# Also note that the fastest component retains an amplitude modulation (for nharmonics=6 at least)

plt.figure()
plt.plot(IFy.mean(axis=0), IAy.mean(axis=0), 'o')
plt.plot(IFz.mean(axis=0), IAz.mean(axis=0), 'o')
plt.legend(['Full', 'Missing Fundamental'], frameon=False)
plt.xlabel('Mean IF over time')
plt.ylabel('Mean IA over time')
plt.xticks(freqs)
plt.grid(True)
plt.title('Average IF and IA of IMFs')


plt.figure()
plt.subplot(211)
plt.plot(x[:1000, 1:], lw=0.5)
plt.plot(z[:1000], 'k')
lgd = ['f{}'.format(ii) for ii in range(1, nharmonics)]
lgd.append('Sum')
plt.legend(lgd, frameon=False)
plt.ylim(-5, 5)
plt.xlim([0, 1250])
plt.subplot(212)
plt.plot(x[:1000, 0])
plt.plot(imf_y[:1000,-2])
plt.plot(imf_z[:1000,-2])
plt.legend(['f0', 'f0 full', 'f0 missing'], frameon=False)
plt.xlim([0, 1250])
