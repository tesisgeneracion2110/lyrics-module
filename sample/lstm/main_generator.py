from sample.lstm.train import manage_wordlist, prepare_text_data, create_dictionaries, vectorization, prepare_model
from sample.lstm.lyric_generator import generation, random_point, prediction
import sample.adjust as adjust
from sample.lstm import constant
import re

import gc


def lyric_formatter(data):
    lines = data.split("\n")
    data_formatted = ""
    print("Num lines: ", len(lines))
    old_line = ""
    for line in lines:
        line_format = re.sub(r"[^a-zA-Z0-9áéíóúÁÉÍÓÚ]+", ' ', line).lstrip()
        if line_format.isspace():
            continue

        line_format = old_line + line_format
        old_line = ""
        words = line_format.split(" ")
        if len(words) < constant.MIN_LENGTH_LINE:
            old_line = line_format
            continue

        elif len(words) < constant.MAX_LENGTH_LINE:
            data_formatted += line_format + "\n"
            continue

        new_line = ""
        for word_position in range(0, len(words)):
            new_line += words[word_position] + " "
            if (word_position != 0 and word_position % constant.MAX_LENGTH_LINE == 0) or word_position == len(words):
                if not new_line.isspace():
                    if word_position == len(words):
                        old_line = new_line
                        continue
                    else:
                        data_formatted += new_line.lstrip() + "\n"
                new_line = ""

    print("data_formatted: ", data_formatted)
    return data_formatted


def init_generator():
    wordlist = manage_wordlist()
    chars_sorted = prepare_text_data(wordlist)

    dictionaries = create_dictionaries(chars_sorted)
    char_indices = dictionaries[0]
    indices_char = dictionaries[1]

    vectorization(chars_sorted, char_indices)
    length_chars_sorted = len(chars_sorted)
    model = prepare_model(length_chars_sorted)
    model_generation = generation(model)

    point = random_point(wordlist)
    generated = point[0]
    sentence = point[1]
    predict = prediction(model_generation, chars_sorted, char_indices, indices_char, generated, sentence)

    filename = constant.PATH_LYRICS_GENERATED + constant.FILENAME_LYRICS_GENERATED

    if constant.FILE_INDEX == constant.MAX_FILE_INDEX:
        constant.FILE_INDEX = 0
    else:
        constant.FILE_INDEX += 1

    filename += str(constant.FILE_INDEX) + constant.FORMAT_LYRICS_GENERATED
    data = lyric_formatter(predict)
    adjust.generated_lyric(filename, data)
    gc.collect()

    return filename


init_generator()
