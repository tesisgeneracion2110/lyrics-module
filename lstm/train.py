from __future__ import print_function

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.layers import Dropout
from keras.callbacks import ModelCheckpoint
from keras.optimizers import RMSprop

import numpy as np
import random
import sys
import gc

import sample.adjust as adjust

# parse input file to words
fileName_lyrics = "lyrics_no_parentheses.txt"
filename_lyrics_training = "lyricsTraining"

raw_text = adjust.parse(fileName_lyrics)

chars = sorted(list(set(raw_text)))
print('total chars:', len(chars))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))
print('char_indices: ', char_indices)
print('indices_char: ', indices_char)

# cut the text in semi-redundant sequences of max_len characters
max_len = 10
step = 3
sentences = []
next_chars = []

# if steps are changed, the training should have best results?
# if max-len are change, the training should have best results?
for i in range(0, len(raw_text) - max_len, step):
    sentences.append(raw_text[i: i + max_len])
    next_chars.append(raw_text[i + max_len])
print('Number of sequences: ', len(sentences))
#print('sentences: ', sentences)
#print('next_chars', next_chars)

print('Vectorization...')
x = np.zeros((len(sentences), max_len, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
print('x: ', x)
print('y: ', y)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        x[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1


# build the model: a single LSTM
print('Build model...')
model = Sequential()
# the value 256 if are changing, the result is best?
model.add(LSTM(256, input_shape=(max_len, len(chars))))
model.add(Dropout(0.2))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))

optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)


def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

# train the model, 40 epochs, generate output and save model for later generation
print()
print('-' * 50)
filepath = "result/" + filename_lyrics_training + ".hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]
model.fit(x, y, batch_size=128, epochs=5, callbacks=callbacks_list)

start_index = random.randint(0, len(raw_text) - max_len - 1)