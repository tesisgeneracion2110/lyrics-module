from __future__ import print_function

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.layers import Dropout
from keras.callbacks import ModelCheckpoint
from keras.optimizers import RMSprop

import numpy as np

from sample.adjust import parse
from sample.lstm import constant

sentences = []
next_chars = []


def manage_wordlist():
    return parse(constant.FILENAME_LYRICS)


def prepare_text_data(wordlist):

    for i in range(0, len(wordlist) - constant.MAX_LEN_CHARACTERS, constant.STEPS_TRAINING):
        sentences.append(wordlist[i: i + constant.MAX_LEN_CHARACTERS])
        next_chars.append(wordlist[i + constant.MAX_LEN_CHARACTERS])

    return sorted(list(set(wordlist)))


def create_dictionaries(chars):
    char_indices = dict((c, i) for i, c in enumerate(chars))
    indices_char = dict((i, c) for i, c in enumerate(chars))
    return char_indices, indices_char


def vectorization(chars, char_indices):

    x = np.zeros((len(sentences), constant.MAX_LEN_CHARACTERS, len(chars)), dtype=np.bool)
    y = np.zeros((len(sentences), len(chars)), dtype=np.bool)

    for i, sentence in enumerate(sentences):
        for t, char in enumerate(sentence):
            x[i, t, char_indices[char]] = 1
        y[i, char_indices[next_chars[i]]] = 1

    return x, y


def prepare_model(length_chars):

    model = Sequential()
    model.add(LSTM(constant.UNITS_LSTM, input_shape=(constant.MAX_LEN_CHARACTERS, length_chars)))
    model.add(Dropout(0.2))
    model.add(Dense(length_chars))
    model.add(Activation(constant.ACTIVATION_LSTM))
    return model


def build_model(model, x, y):

    optimizer = RMSprop(lr=0.01)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer)
    filepath = constant.PATH_LYRICS_TRAINING + constant.FILENAME_LYRICS_TRAINING
    checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
    callbacks_list = [checkpoint]
    model.fit(x, y, batch_size=constant.BATCH_SIZE, epochs=constant.EPOCHS, callbacks=callbacks_list)

