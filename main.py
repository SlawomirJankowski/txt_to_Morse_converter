from alphabet import ALPHABET_MORSEA


def convert_to_morse():
    txt_to_convert = ([*input("Podaj tekst do skonwertowania na Alfabet Morse'a: ").upper()])
    converted_text = ""
    for char in txt_to_convert:
        if char == "\u0020":  # \u0020 -> space in unicode
            converted_text += "/" + "\u0020"
        else:
            converted_text += ALPHABET_MORSEA[char] + "\u0020"
    return converted_text


print(convert_to_morse())
