import matplotlib.pyplot as plt
from scipy.io import wavfile
import os

n = 1

def graph_spectrogram(wav_file):
    rate, data = wavfile.read(wav_file)     # Getting data from wav_file
    nfft = 256          # Length of the windowing segments
    fs = 256            # Sampling frequency
    pxx, freqs, bins, ax = plt.specgram(data,nfft,fs,noverlap=128)      
    plt.axis('equal')
    plt.axis('off')
    plt.savefig('specs/%s.png' %n,  # save graph in specs directory
                dpi=500,            # dots per inch
                frameon='False',    # no border
                aspect='normal',    # square pixels
                bbox_inches='tight',
                pad_inches=1)       # padding
    # plt.show()

def get_files(path):
    list = os.listdir(path)
    return len(list)            # get number of files in directory

if __name__ == '__main__':      # Main function
    for i in range(get_files('waves')):     # for number of files in waves directory
        wav_file = 'waves/%s.wav' %(i+1)    # set name of the wav file to graph
        graph_spectrogram(wav_file)
        n += 1                              # increment file name