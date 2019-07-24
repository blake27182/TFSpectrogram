from pydub import AudioSegment
import wave
import contextlib
from PIL import Image

target_file = 'test_knock.wav'
segment = 3


def get_duration(wav_file):
    with contextlib.closing(wave.open(wav_file, 'r')) as f:
        frames = f.getnframes()		        # store number of frames in file
        rate = f.getframerate()		        # store framerate
        duration = frames / float(rate)		    # float calculate duration of file
        return duration


def split_wav(wav_file, seg):
    n = 1		                # initialize file name iterator to 1
    s = seg * 1000		        # store number of milliseconds in segment
    duration = get_duration(wav_file)		    # store duration of file
    t1 = 0		                            # initialize t1 for lower limit of sliding time frame
    t2 = s 		                            # initialize t2 for upper limit of sliding time frame
    for i in range(int(duration / seg)):	    # for number of times segment fits into duration evenly
        newAudio = AudioSegment.from_wav(wav_file)	        # open original file with pydub
        newAudio = newAudio[t1:t2]		                # overwrite newAudio to only data between time frame
        newAudio.export(f'waves/{n}.wav', format="wav")	    # write newAudio to a file in waves directory
        print (n, t1, t2)
        n += 1		# increment n for next file name
        t1 = t2		# move lower limit to last high limit
        t2 = t2 + s 	# move upper limit to s millisecond later


split_wav(target_file, segment)
