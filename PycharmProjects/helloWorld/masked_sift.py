import emd
import librosa


def masked_sift_1965(filename):
    # filenames when calling:cello_C4_1_fortissimo_arco-normal
    #                        viola_C4_1_fortissimo_arco-normal
    # Can't tell if the previous custom mask works better for the viola since both look quite similar

    y, sr = librosa.load('C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/' +
                         filename + '.mp3', offset=0.25, duration=0.5)

    # slightly longer duration to make sure that that weird wave thing of the viola is visible

    mask_freq_1 = [1965/sr, 778/sr, 259/sr, 194/sr]
    imf, mask_freqs = emd.sift.mask_sift(y, mask_freqs=mask_freq_1, ret_mask_freq=True, max_imfs=4)

    fig_mask = emd.plotting.plot_imfs(imf[:sr, :])

    return fig_mask, mask_freqs


def masked_sift_2530(filename):
    # filenames when calling:double-bass_C4_1_fortissimo_arco-normal
    #                        violin_C4_1_fortissimo_arco-normal
    #                        saxophone_C4_1_fortissimo_normal
    #                        trombone_C4_1_fortissimo_normal
    # Cannot tell if for the trombone the decomposition is better than when using the custom mask,
    # but imfs 2, 3, 4, seem a bit better.
    # For the violin there seems to be some mode-mixing between imf3 and 4 but
    # that happens with the custom mask. Can't get rig of the mixing completely.
    y, sr = librosa.load('C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/' +
                         filename + '.mp3', offset=0.25, duration=0.25)

    mask_freq_4 = 2530/sr
    imf, mask_freqs = emd.sift.mask_sift(y, mask_freqs=mask_freq_4, ret_mask_freq=True, max_imfs=5)

    fig_mask = emd.plotting.plot_imfs(imf[:sr, :])

    return fig_mask, mask_freqs


def masked_sift_1939(filename):
    # filenames when calling:guitar_C4_very - long_forte_normal
    #                        banjo_C4_very-long_forte_normal
    # this one works better than the previous versions of the custom masks, probably not perfect still.

    y, sr = librosa.load('C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/' +
                         filename + '.mp3', offset=0.25, duration=0.25)

    mask_freq_4 = [1939/sr, 969/sr, 500/sr, 300/sr, 100/sr]
    imf, mask_freqs = emd.sift.mask_sift(y, mask_freqs=mask_freq_4, ret_mask_freq=True, max_imfs=5)

    fig_mask = emd.plotting.plot_imfs(imf[:sr, :])

    return fig_mask, mask_freqs


def masked_sift_1322(filename):
    # filenames when calling:clarinet_C4_1_fortissimo_normal
    #                        flute_C4_1_forte_normal
    #                        bass-clarinet_C4_1_fortissimo_normal
    # it's possible that the decomposition is not as good for the clarinet, but it's not bad I think.

    y, sr = librosa.load('C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/' +
                         filename + '.mp3', offset=0.75, duration=0.25)

    # later offset so that both of the weird wave things of the clarinet are visible.

    mask_freq_4 = 1322/sr
    imf, mask_freqs = emd.sift.mask_sift(y, mask_freqs=mask_freq_4, ret_mask_freq=True, max_imfs=5)

    fig_mask = emd.plotting.plot_imfs(imf[:sr, :])

    return fig_mask, mask_freqs


def iterated_masked_sift(filename):
    # filenames when calling: oboe_C4_1_fortissimo_normal
    #                         trumpet_C4_1_fortissimo_normal

    y, sr = librosa.load('C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/' +
                         filename + '.mp3', offset=0.25, duration=0.25)

    imf, mask_freqs = emd.sift.iterated_mask_sift(y, sample_rate=sr, w_method='amplitude', max_imfs=5, ret_mask_freq=True)
    # default for w_method is 'power'

    fig_mask = emd.plotting.plot_imfs(imf[:sr, :])

    return fig_mask, mask_freqs


# for the tuba the simple sift seems to be the best decomposition


