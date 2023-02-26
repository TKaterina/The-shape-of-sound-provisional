import librosa
import simpleaudio as sa
import numpy as np


def note_playback(filename):
    filepath = "C://Users/ktamp/OneDrive/Desktop/TheShapeofSound/mp3Gallery/" + filename + ".mp3"
    y, sr = librosa.load(filepath)
    audio = y * (2 ** 15 - 1) / np.max(np.abs(y))
    audio = audio.astype(np.int16)

    # start playback
    play_obj = sa.play_buffer(audio, 1, 2, sr)
    return play_obj

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
