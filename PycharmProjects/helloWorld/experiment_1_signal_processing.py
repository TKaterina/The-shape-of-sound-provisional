import numpy as np
import emd
import matplotlib.pyplot as plt


mod = 1
sr = 48000
time = np.linspace(0, 1, sr)

carrier = [440, 700, 1000]
am = [5, 10, 20, 40, 80, 160, 320]
mask_freq_1 = 450/sr
mask_freq_2 = 724/sr
mask_freq_3 = 1014/sr

for i in np.arange(0,3):
    for j in np.arange(0,7):
        carrier_tone = np.sin(2*np.pi*carrier[i]*time)
        amp = np.cos(2*np.pi*am[j]*time)
        tone = carrier_tone * (1 + mod * amp)

        imf, mask_freqs = emd.sift.mask_sift(tone, mask_freqs=[(carrier[i]+am[i])/sr, (carrier[i]-am[i])/sr],
                                             ret_mask_freq=True, max_imfs=4)
        fig_mask = emd.plotting.plot_imfs(imf[:sr, :])


        # other sifting options:

        # imf, mask_freqs = emd.sift.mask_sift(tone, mask_freqs=carrier[i]/sr, ret_mask_freq=True, max_imfs=4)
        # fig_mask = emd.plotting.plot_imfs(imf[:sr, :])

        # imf, mask_freqs = emd.sift.iterated_mask_sift(tone, sample_rate=sr, w_method='amplitude', max_imfs=5,
        #                                             ret_mask_freq=True)
        #
        # fig_mask = emd.plotting.plot_imfs(imf[:sr, :])

        # imf = emd.sift.sift(tone, imf_opts={'sd_thresh': 1e-3})
        # fig = emd.plotting.plot_imfs(imf[:sr, :])

        plt.show()
