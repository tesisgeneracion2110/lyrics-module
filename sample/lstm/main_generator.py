from sample.lstm.train import manage_wordlist, prepare_text_data, create_dictionaries, vectorization, prepare_model
from sample.lstm.lyric_generator import generation, random_point, prediction
import sample.adjust as adjust
from sample.lstm import constant

import gc


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
    adjust.generated_lyric(filename, predict)

    gc.collect()

    return filename
