import numpy as np
import emd
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
# from scipy.io.wavfile import write

mod = 1
sr = 48000
time = np.linspace(0, 1, sr)

carrier = [440, 700, 1000]
am = [5, 10, 20, 40, 80, 160, 320]


for i in np.arange(0,3):
    for j in np.arange(0,7):
        carrier_tone = np.sin(2*np.pi*carrier[i]*time)
        amp = np.cos(2*np.pi*am[j]*time)
        tone = carrier_tone * (1 + mod * amp)

        imf = emd.sift.sift(tone, imf_opts={'sd_thresh': 1e-3})
        IP, IF, IA = emd.spectra.frequency_transform(imf, sr, 'hilbert', smooth_phase=441)
        fig = emd.plotting.plot_imfs(imf[:5000, :])
        plt.show()

        N = sr * 1
        yf = fft(imf[:sr, 0])
        xf = fftfreq(N, 1 / sr)

        plt.plot(xf, np.abs(yf))
        plt.show()

        print(np.average(IF[:, 0], weights=IA[:, 0]))


# extracts first imf
# imf[:sample_rate, 0]


# fourier = np.fft.fft(imf[:sr, 0])
# n = signal.size
# timestep = 0.1
# freq = np.fft.fftfreq(n, d=timestep)
# freq
