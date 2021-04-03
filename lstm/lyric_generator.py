from keras.optimizers import RMSprop

import numpy as np
import random
import sys

import constant


def generation(model):
    optimizer = RMSprop(lr=0.01)
    model_data = constant.PATH_LYRICS_TRAINING + constant.FILENAME_LYRICS_TRAINING
    model.load_weights(model_data)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer)
    return model


def random_point(wordlist):
    start_index = random.randint(0, len(wordlist) - constant.MAX_LEN_CHARACTERS - 1)
    sentence = wordlist[start_index: start_index + constant.MAX_LEN_CHARACTERS]

    generated = ''
    generated += ' '.join([value for value in sentence])
    return generated, sentence


def prediction(model, chars, char_indices, indices_char, generated, sentence):
    for i in range(constant.WORDS_RANGE):
        x = np.zeros((1, constant.MAX_LEN_CHARACTERS, len(chars)))
        for t, word in enumerate(sentence):
            x[0, t, char_indices[word]] = 1.

        predictions = model.predict(x, verbose=0)[0]
        next_index = sample(predictions, constant.DIVERSITY)
        next_char = indices_char[next_index]

        generated += next_char + " "
        sentence = sentence[1:]
        sentence.append(next_char)

        sys.stdout.write(" " + next_char)
        sys.stdout.flush()


def sample(predictions, temperature=1.0):
    # helper function to sample an index from a probability array
    predictions = np.asarray(predictions).astype('float64')
    predictions = np.log(predictions) / temperature
    exp_predictions = np.exp(predictions)
    predictions = exp_predictions / np.sum(exp_predictions)
    probability = np.random.multinomial(1, predictions, 1)
    return np.argmax(probability)
