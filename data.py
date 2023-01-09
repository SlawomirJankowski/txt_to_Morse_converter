# --App secret key--
APP_SECRET_KEY = 'dsjfsd7887hs3[]'


######## Converter data and parameters ########

# -- Alphabet Morse'a--
ALPHABET_MORSEA = {
    "A": ".-",    "B": "-...",    "C": "-.-.",    "D": "-..",   "E": ".",    "F": "..-.",    "G": "--.",    "H": "....",
    "I": "..",    "J": ".---",    "K": "-.-",    "L": ".-..",    "M": "--",    "N": "-.",    "O": "---",    "P": ".--.",
    "Q": "--.-",    "R": ".-.",    "S": "...",    "T": "-",    "U": "..-",    "V": "...-",    "W": ".--",   "X": "-..-",
    "Y": "-.--",    "Z": "--..",    "Ą": ".-.-",    "Ć": "-.-..",    "Ę": "..-..",    "Ł": ".-..-",    "Ń": "--.--",
    "Ó": "---.",    "Ś": "...-...",    "Ź": "--..-.",    "Ż": "--..-",
    "0": "-----",    "1": ".----",    "2": "..---",    "3": "...--",    "4": "....-",    "5": ".....",    "6": "-....",
    "7": "--...",    "8": "---..",    "9": "----.",
    ".": ".-.-.-",    ",": "--..--",    "?": "..--..",    "'": ".----.",    "!": "-.-.--",    "/": "-..-.","(": "-.--.",
    ")": "-.--.-",    "&": ".-...",    ":": "---...",    ";": "-.-.-.",    "=": "-...-",    "+": ".-.-.", "-": "-....-",
    "_": "..--.-",    '"':	".-..-.",    "$": "...-..-",    "@": ".--.-.",    "¿": "..-.-",    "¡": "--...-",
}

# -- Converter error messages --
CONVERTER_ERROR_MSG = {
    'KEY_ERROR_MSG': "You have entered unrecognized character: ",
    'NO_TEXT_MSG': "Please enter a text to convert ... ",
    }

CONVERTER_WAVE_PARAMS = {
    # -- Wave file parameters--
    'WAVE_PARAMS': (1, 2, 22050, 0, "NONE", "Not compressed"),
    # -- Morse code rules --
    'SAMPLE_RATE': 20050,
    'FREQ': 850.0,
    'DOT_DURATION': 0.1058,
    'DAH_DURATION': 3 * 0.1058,
    'VOL': 0.5,
    }

CONVERTER_PATHS = {
    # -- Temporary media path data --
    'PARENT_DIR': './static/media/',
    'WAVE_FILE_NAME': '/converted_text_as_sound.wav',
    }


# -- Scheduler parameters--
SCHEDULER_PARAMS = {
    'FILE_LIFETIME': 1,  # set the proper value (in minutes) files older than this value will be deleted
    'DELETE_LOG_FILE_PATH': './static/logs/delete_log.txt',
    'CLEAN_MEDIA_DIR_INTERVAL': 20,  # in minutes
    }


# -- E-mail notification parameters --
MAIL_NOTIFICATION_PARAMS = {
    'SERVER': 'smtp.gmail.com: 587',
    'SENDER_EMAIL': 'sjankowski903@gmail.com',
    'PASSWORD': 'jblrrkhfewhlunrw',
    'RECEIVER_EMAIL': 'slajan@interia.eu',
}

