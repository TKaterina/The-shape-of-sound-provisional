import emd
import librosa


def simple_sift(filename):

    y, sr = librosa.load('C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/' +
                         filename + '.mp3', duration=0.5)
    # extract the imfs
    imf = emd.sift.sift(y, max_imfs=5, imf_opts={'sd_thresh': 0.1})

    # plot the imfs
    fig_imf = emd.plotting.plot_imfs(imf[:sr, :])

    return fig_imf


def noise_assisted_sift(filename):
    y, sr = librosa.load('C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/' +
                         filename + '.mp3', duration=0.5)

    # extract the imfs
    imf = emd.sift.ensemble_sift(y, max_imfs=5, nensembles=4, nprocesses=1,
                                 ensemble_noise=0.2, imf_opts={'sd_thresh': 0.1})

    # plot imfs
    fig_ensemble = emd.plotting.plot_imfs(imf[:sr, :])

    return fig_ensemble


def masked_sift(filename):

    y, sr = librosa.load('C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/' +
                         filename + '.mp3', duration=0.5) # offset=0.25, duration=0.25)

    # if the mask frequency is not defined (mask_freqs and ret_mask_freq are removed), then the mask frequency is
    # automatically determined by the zero crossings of the signal
    # mask_freqs = 30/sr
    # that 30 is the frequency of the mask that's being applied, it should be changed depending on the signal
    # imf = emd.sift.mask_sift(y, mask_freqs=mask_freqs, ret_mask_freq=True, max_imfs=4)[0]

    imf, mask_freqs = emd.sift.iterated_mask_sift(y, sample_rate=sr, w_method='amplitude', max_imfs=5, ret_mask_freq=True)
    # default for x_method is 'power'

    fig_mask = emd.plotting.plot_imfs(imf[:sr, :])

    return fig_mask, mask_freqs


# filenames when calling: cello_C4_1_fortissimo_arco-normal
#                       violin_C4_1_fortissimo_arco-normal
#                       viola_C4_1_fortissimo_arco-normal
#                       double-bass_C4_1_fortissimo_arco-normal
#                       guitar_C4_very-long_forte_normal
#                       banjo_C4_very-long_forte_normal
#                       trumpet_C4_1_fortissimo_normal
#                       trombone_C4_1_fortissimo_normal
#                       tuba_C4_1_fortissimo_normal
#                       oboe_C4_1_fortissimo_normal
#                       clarinet_C4_1_fortissimo_normal
#                       flute_C4_1_forte_normal
#                       saxophone_C4_1_fortissimo_normal
#                       bass-clarinet_C4_1_fortissimo_normal
