import librosa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def note_data_frame(filename):

    # import mp3 file
    filepath = "C://Users/ktamp/OneDrive/Desktop/The shape of sound/mp3Gallery/" + filename + ".mp3"
    y, sr = librosa.load(filepath)
    df = pd.DataFrame({filename: y})

    # insert a time vector in milliseconds into the dataframe
    num_samples = df.shape[0]
    duration = (num_samples / sr) * 1000
    time = np.linspace(0, duration, num_samples)
    df.insert(0, 'Time(ms)', time)

    return df, y, sr, time


def plot_note(filename):
    
    df = note_data_frame(filename)[0]

    # plot the note
    fig_note = plt.figure(figsize=(16, 9))
    ax = plt.subplot(111)
    df.plot(x="Time(ms)", y=filename, ax=ax, xlim=(500, 525), title=filename)

    return fig_note


def autocorrelation(timeseries, lag):

    # calculate the autocorrelation function of the note
    x = timeseries[lag:]
    if lag > 0:
        y = timeseries[:-lag]
    else:
        y = timeseries

    acf = np.corrcoef(x, y)[0, 1]
    return acf


def plot_autocorrelation(filename):

    y = note_data_frame(filename)[1]
    n_lags = 240
    acf = np.zeros((n_lags,))
    for i in range(n_lags):
        acf[i] = autocorrelation(y, i)

    # plot the autocorrelation function of the note
    fig_auto = plt.figure(figsize=(16, 6))
    plt.plot(np.arange(n_lags), acf)
    plt.title("Autocorrelation function " + filename)

    return fig_auto


def both_plots(filename):

    df = note_data_frame(filename)[0]

    # plot the note
    fig_both, (ax1, ax2) = plt.subplots(1, 2, sharey='none')
    df.plot(x="Time(ms)", y=filename, ax=ax1, xlim=(500, 525), title=filename)

    # plot the autocorrelation
    n_lags = 240
    acf = np.zeros((n_lags,))
    for i in range(n_lags):
        acf[i] = autocorrelation(df[filename], i)

    ax2.plot(np.arange(n_lags), acf)
    plt.title("Autocorrelation function " + filename)

    return fig_both


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
