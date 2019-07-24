import matplotlib.pyplot as plt
from scipy.io import wavfile
import os

n = 1


def graph_spectrogram(file):
    rate, data = wavfile.read(file)     # Getting data from wav_file
    nfft = 256          # Length of the windowing segments
    fs = 256            # Sampling frequency
    pxx, freqs, bins, ax = plt.specgram(data, nfft, fs, noverlap=128)
    plt.axis('equal')
    plt.axis('off')
    plt.savefig(f'specs/{n}.png',  # save graph in specs directory
                dpi=500,            # dots per inch
                frameon='False',    # no border
                aspect='normal',    # square pixels
                bbox_inches='tight',
                pad_inches=1)       # padding
    # plt.show()


def get_files(path):
    lst = os.listdir(path)
    return len(lst)            # get number of files in directory


if __name__ == '__main__':
    for i in range(get_files('waves')):
        wav_file = f'waves/{i+1}.wav'    # set name of the wav file to graph
        graph_spectrogram(wav_file)
        n += 1
