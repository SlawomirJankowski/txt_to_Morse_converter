import os.path
import numpy as np
import wave
import string
from random import choice


WAVE_PARAMS = (1, 2, 22050, 0, "NONE", "Not compressed")

# -- Morse code rules --
SAMPLE_RATE = 20050
FREQ = 850.0
DOT_DURATION = 0.1058
DAH_DURATION = 3 * DOT_DURATION
VOL = 0.5
# DAH should be three DOTs.
# Space between DOTs and DAHs should be one DOT.
# Space between two letters should be one DAH.
# Space between two words should be DOT DAH DAH.


def generate_sound(duration, volume):
    esm = np.arange(duration * SAMPLE_RATE)
    wf = np.sin(2 * np.pi * esm * FREQ / SAMPLE_RATE)
    wf_quiet = wf * volume
    wav_f_int = np.int16(wf_quiet * 32767)
    return wav_f_int


def generate_path():
    letters = string.ascii_lowercase
    directory = ''.join(choice(letters) for i in range(10))
    parent_directory = './static/media/'
    path = os.path.join(parent_directory, directory)
    os.mkdir(path)
    file_path = f'{path}/converted_text_as_sound.wav'
    return file_path


def save_sound(converted_text, file_path):

    morse_wav = wave.open(file_path, "w")
    morse_wav.setparams(WAVE_PARAMS)

    for char in converted_text:
        if char == ".":
            morse_wav.writeframesraw(generate_sound(duration=DOT_DURATION, volume=VOL))
        elif char == "-":
            morse_wav.writeframesraw(generate_sound(duration=DAH_DURATION, volume=VOL))
        elif char == " ":
            morse_wav.writeframesraw(generate_sound(duration=DAH_DURATION, volume=0.0))
        else:
            morse_wav.writeframesraw(generate_sound(duration=DOT_DURATION, volume=0.0))
        morse_wav.writeframesraw(generate_sound(duration=DOT_DURATION, volume=0.0))

    morse_wav.close()
