import os.path
import numpy as np
import wave
import string
from random import choice
from data import ALPHABET_MORSEA, CONVERTER_WAVE_PARAMS, CONVERTER_PATHS


class Converter:
    def __init__(self, input_text):
        self.input_text = [*input_text.upper()]
        self.converted_text = self.convert_to_morse()
        self.file_path = self.generate_path()

    def convert_to_morse(self):
        text = ""
        for char in self.input_text:
            if char == "\u0020":  # \u0020 -> space in unicode
                text += "/" + "\u0020"
            else:
                text += ALPHABET_MORSEA[char] + "\u0020"
        return text

    @staticmethod
    def generate_path():
        letters = string.ascii_lowercase
        random_directory_name = ''.join(choice(letters) for i in range(10))
        dir_path = os.path.join(CONVERTER_PATHS['PARENT_DIR'], random_directory_name)
        os.mkdir(dir_path)
        file_path = f'{dir_path}{CONVERTER_PATHS["WAVE_FILE_NAME"]}'
        return file_path

    @staticmethod
    def generate_sound(duration, volume):
        esm = np.arange(duration * CONVERTER_WAVE_PARAMS['SAMPLE_RATE'])
        wf = np.sin(2 * np.pi * esm * CONVERTER_WAVE_PARAMS['FREQ'] / CONVERTER_WAVE_PARAMS['SAMPLE_RATE'])
        wf_quiet = wf * volume
        wave_file = np.int16(wf_quiet * 32767)
        return wave_file

    def save_sound(self):
        morse_wav = wave.open(self.file_path, "w")
        morse_wav.setparams(CONVERTER_WAVE_PARAMS['WAVE_PARAMS'])
        for char in self.converted_text:
            if char == ".":
                morse_wav.writeframesraw(self.generate_sound(duration=CONVERTER_WAVE_PARAMS['DOT_DURATION'],
                                                             volume=CONVERTER_WAVE_PARAMS['VOL']))
            elif char == "-":
                morse_wav.writeframesraw(self.generate_sound(duration=CONVERTER_WAVE_PARAMS['DAH_DURATION'],
                                                             volume=CONVERTER_WAVE_PARAMS['VOL']))
            elif char == " ":
                morse_wav.writeframesraw(self.generate_sound(duration=CONVERTER_WAVE_PARAMS['DAH_DURATION'],
                                                             volume=0.0))
            else:
                morse_wav.writeframesraw(self.generate_sound(duration=CONVERTER_WAVE_PARAMS['DOT_DURATION'],
                                                             volume=0.0))
            morse_wav.writeframesraw(self.generate_sound(duration=CONVERTER_WAVE_PARAMS['DOT_DURATION'],
                                                         volume=0.0))
        morse_wav.close()
