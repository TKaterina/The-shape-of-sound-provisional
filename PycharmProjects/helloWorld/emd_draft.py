import emd
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


sample_rate = 1000
seconds = 1
num_samples = sample_rate*seconds
time_vect = np.linspace(0, seconds, num_samples)
freq = 15

# Change extent of deformation from sinusoidal shape [-1 to 1]
nonlinearity_deg = .25

# Change left-right skew of deformation [-pi to pi]
nonlinearity_phi = -np.pi/4

# Create a non-linear oscillation
x = emd.simulate.abreu2010(freq, nonlinearity_deg, nonlinearity_phi, sample_rate, seconds)

x -= np.sin(2 * np.pi * 0.22 * time_vect)   # Add part of a very slow cycle as a trend

# Add a little noise - with low frequencies removed to make this example a
# little cleaner...
np.random.seed(42)
n = np.random.randn(1000,) * .2
nf = signal.savgol_filter(n, 3, 1)
n = n - nf

x = x + n

plt.figure()
plt.plot(x, 'k')

# sphinx_gallery_thumbnail_number = 8

imf = emd.sift.sift(x, imf_opts={'sd_thresh': 0.1})
emd.plotting.plot_imfs(imf)

# compute instantaneous frequency, phase and amplitude using the normalised hilbert transform
phase, frequency, amplitude = emd.spectra.frequency_transform(imf, sample_rate, 'hilbert')

# compute the hilbert-huang transform
frequency_range = (0.1, 10, 80, 'log')
f, hht = emd.spectra.hilberthuang(frequency, amplitude, frequency_range, sum_time=False)

# plot the hilbert-huang transform
fig_hht = plt.figure(figsize=(10, 6))
emd.plotting.plot_hilberthuang(hht, time_vect, f, time_lims=(2, 4),
                               freq_lims=(0.1, 15), fig=fig_hht, log_y=True)
