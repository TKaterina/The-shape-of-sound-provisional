import emd
import librosa


def masked_sift_1965(filename):
    # this mask works for the cello and viola, although the viola decomposition is not perfect.
    # Can't tell if the previous mask works better for the viola, both look quite similar.

    y, sr = librosa.load('C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/' +
                         filename + '.mp3', offset=0.25, duration=0.5)

    # used a slightly longer duration to make sure that that weird wave thing of the viola is showing
    # (it seemed important to include)

    mask_freq_1 = [1965/sr, 778/sr, 259/sr, 194/sr]
    imf, mask_freqs = emd.sift.mask_sift(y, mask_freqs=mask_freq_1, ret_mask_freq=True, max_imfs=4)

    fig_mask = emd.plotting.plot_imfs(imf[:sr, :])

    return fig_mask, mask_freqs


def masked_sift_2530(filename):

    # this mask frequency seems to work for the sax, trombone and double-bass.
    # originally the sax has a mask_freq of 2799 and the trombone 3169.
    # for the sax the decomposition is the same as when a custom mask was used, but for the trombone
    # the decomposition is different compared to before. Maybe this version of the decomposition is better because
    # imfs 2, 3, 4 look better this way.
    # surprisingly it also works for the violin. There seems to be some mode-mixing between imf3 and 4 but
    # that happens with the custom mask. Can't get rig of the mixing completely.
    y, sr = librosa.load('C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/' +
                         filename + '.mp3', offset=0.25, duration=0.25)

    mask_freq_4 = 2530/sr
    imf, mask_freqs = emd.sift.mask_sift(y, mask_freqs=mask_freq_4, ret_mask_freq=True, max_imfs=5)

    fig_mask = emd.plotting.plot_imfs(imf[:sr, :])

    return fig_mask, mask_freqs


def masked_sift_1939(filename):

    # this one works for both guitar and banjo and is better than the previous versions of the custom masks
    # Not perfect but pretty good.

    y, sr = librosa.load('C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/' +
                         filename + '.mp3', offset=0.25, duration=0.25)

    mask_freq_4 = [1939/sr, 969/sr, 500/sr, 300/sr, 100/sr]
    imf, mask_freqs = emd.sift.mask_sift(y, mask_freqs=mask_freq_4, ret_mask_freq=True, max_imfs=5)

    fig_mask = emd.plotting.plot_imfs(imf[:sr, :])

    return fig_mask, mask_freqs


def masked_sift_1322(filename):

    # this one works for the clarinet, bass-clarinet and flute.
    # it's possible that the decomposition is not as good for the clarinet, but it's not bad I think.

    y, sr = librosa.load('C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/' +
                         filename + '.mp3', offset=0.75, duration=0.25)

    # chose a later offset so that both of the weird wave things of the clarinet are visible.

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


# for the tuba the simple sift continues to be the best decomposition.


