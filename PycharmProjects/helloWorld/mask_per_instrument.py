import emd
import librosa


def masked_sift_cello(filename):

    y, sr = librosa.load('C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/' +
                         filename + '.mp3', offset=0.25, duration=0.25)

    mask_freq_1 = [1965/sr, 982/sr, 225/sr, 122/sr]
    imf, mask_freqs = emd.sift.mask_sift(y, mask_freqs=mask_freq_1, ret_mask_freq=True, max_imfs=4)

    fig_mask = emd.plotting.plot_imfs(imf[:sr, :])

    return fig_mask, mask_freqs


def masked_sift_violin(filename):

    y, sr = librosa.load('C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/' +
                         filename + '.mp3', offset=0.25, duration=0.25)

    mask_freq_2 = [2679/sr, 1339/sr, 522/sr, 270/sr]
    imf, mask_freqs = emd.sift.mask_sift(y, mask_freqs=mask_freq_2, ret_mask_freq=True, max_imfs=4)

    fig_mask = emd.plotting.plot_imfs(imf[:sr, :])

    return fig_mask, mask_freqs


def masked_sift_viola(filename):

    y, sr = librosa.load('C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/' +
                         filename + '.mp3',  offset=0.25, duration=0.5)

    # used a slightly longer duration to make sure that that weird wave thing is showing
    # (it seemed important to include)

    mask_freq_3 = [1557/sr, 778/sr, 259/sr, 194/sr]
    imf, mask_freqs = emd.sift.mask_sift(y, mask_freqs=mask_freq_3, ret_mask_freq=True, max_imfs=5)

    fig_mask = emd.plotting.plot_imfs(imf[:sr, :])

    return fig_mask, mask_freqs


def masked_sift_double_bass(filename):

    y, sr = librosa.load('C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/' +
                         filename + '.mp3', offset=0.25, duration=0.25)

    mask_freq_4 = 2530/sr
    imf, mask_freqs = emd.sift.mask_sift(y, mask_freqs=mask_freq_4, ret_mask_freq=True, max_imfs=5)

    fig_mask = emd.plotting.plot_imfs(imf[:sr, :])

    return fig_mask, mask_freqs


def masked_sift_guitar(filename):

    y, sr = librosa.load('C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/' +
                         filename + '.mp3', offset=0.25, duration=0.25)

    mask_freq_4 = [1939/sr, 969/sr, 484/sr, 261/sr, 100/sr]
    imf, mask_freqs = emd.sift.mask_sift(y, mask_freqs=mask_freq_4, ret_mask_freq=True, max_imfs=5)

    fig_mask = emd.plotting.plot_imfs(imf[:sr, :])

    return fig_mask, mask_freqs


def masked_sift_banjo(filename):

    y, sr = librosa.load('C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/' +
                         filename + '.mp3', offset=0.25, duration=0.25)

    mask_freq_4 = [1081/sr, 522/sr, 254/sr, 135/sr]
    imf, mask_freqs = emd.sift.mask_sift(y, mask_freqs=mask_freq_4, ret_mask_freq=True, max_imfs=5)

    fig_mask = emd.plotting.plot_imfs(imf[:sr, :])

    return fig_mask, mask_freqs


def masked_sift_trombone(filename):

    y, sr = librosa.load('C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/' +
                         filename + '.mp3', offset=0.25, duration=0.25)

    mask_freq_4 = 3169/sr
    imf, mask_freqs = emd.sift.mask_sift(y, mask_freqs=mask_freq_4, ret_mask_freq=True, max_imfs=5)

    fig_mask = emd.plotting.plot_imfs(imf[:sr, :])

    return fig_mask, mask_freqs


def masked_sift_clarinet(filename):

    y, sr = librosa.load('C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/' +
                         filename + '.mp3', offset=0.25, duration=0.25)

    mask_freq_4 = 1622/sr
    imf, mask_freqs = emd.sift.mask_sift(y, mask_freqs=mask_freq_4, ret_mask_freq=True, max_imfs=5)

    fig_mask = emd.plotting.plot_imfs(imf[:sr, :])

    return fig_mask, mask_freqs


def masked_sift_flute(filename):

    y, sr = librosa.load('C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/' +
                         filename + '.mp3', offset=0.75, duration=0.25)

    mask_freq_4 = 1182/sr
    imf, mask_freqs = emd.sift.mask_sift(y, mask_freqs=mask_freq_4, ret_mask_freq=True, max_imfs=5)

    fig_mask = emd.plotting.plot_imfs(imf[:sr, :])

    return fig_mask, mask_freqs


def masked_sift_sax(filename):

    y, sr = librosa.load('C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/' +
                         filename + '.mp3', offset=0.25, duration=0.25)

    mask_freq_4 = 2799/sr
    imf, mask_freqs = emd.sift.mask_sift(y, mask_freqs=mask_freq_4, ret_mask_freq=True, max_imfs=5)

    fig_mask = emd.plotting.plot_imfs(imf[:sr, :])

    return fig_mask, mask_freqs


def masked_sift_bass_clarinet(filename):

    y, sr = librosa.load('C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/' +
                         filename + '.mp3', offset=0.25, duration=0.25)

    mask_freq_4 = [1461/sr, 730/sr, 260/sr, 182/sr]
    imf, mask_freqs = emd.sift.mask_sift(y, mask_freqs=mask_freq_4, ret_mask_freq=True, max_imfs=5)

    fig_mask = emd.plotting.plot_imfs(imf[:sr, :])

    return fig_mask, mask_freqs

# for the trumpet the iterated masked sift seems to work better than manually selecting masks
# for the tuba the simple sift continues to be the best decomposition, maybe try to add a parameter to improve the simple
# sift instead of trying to create a custom mask.
# for the oboe the iterated masked sift seems to work well.

