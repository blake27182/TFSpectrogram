import matplotlib.pyplot as plt
from scipy.io import wavfile
# from pydub import AudioSegment
from PIL import Image
import os

def crop():
    a = os.listdir("specs")
    a.sort()
    a.pop(0)
    print(a)
    for name in a:
        try:
            original = Image.open("specs/%s" %name)
        except:
            print("couldn't open image\n")

        cropped = original.crop((675,800,3200,2050))
        cropped.save("specs/%s" %name)


crop()
