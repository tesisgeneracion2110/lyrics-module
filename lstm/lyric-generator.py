from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.layers import Dropout
from keras.optimizers import RMSprop
import numpy as np
import random
import sys
import gc
import sample.adjust as adjust

#os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices'

# parse input file to words
fileName = "lyrics.txt"
modelData = "result/lyrics.txt-50-1.2610.hdf5"
raw_text = adjust.parse(fileName)

chars = sorted(list(set(raw_text)))
print('total chars:', len(chars))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

# cut the text in semi-redundant sequences of maxlen characters
maxlen = 10
step = 3
sentences = []
next_chars = []
for i in range(0, len(raw_text) - maxlen, step):
    sentences.append(raw_text[i: i + maxlen])
    next_chars.append(raw_text[i + maxlen])
print('nb sequences:', len(sentences))

print('Vectorization...')
X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        X[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1


# build the model: a single LSTM
print('Build model...')
model = Sequential()
model.add(LSTM(256, input_shape=(maxlen, len(chars))))
model.add(Dropout(0.2))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))

optimizer = RMSprop(lr=0.01)

model.load_weights(modelData)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)


def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

# generate text
print()
print('-' * 50)

# start at a random point in the input-text
start_index = random.randint(0, len(raw_text) - maxlen - 1)

diversity = 0.2

print()
print('----- diversity:', diversity)

generated = ''
sentence = raw_text[start_index: start_index + maxlen]
generated += ' '.join([value for value in sentence])
print('----- Generating with seed: "' + ' '.join([value for value in sentence]) + '"')
sys.stdout.write(generated)

for i in range(400):
    x = np.zeros((1, maxlen, len(chars)))
    for t, word in enumerate(sentence):
        x[0, t, char_indices[word]] = 1.

    preds = model.predict(x, verbose=0)[0]
    next_index = sample(preds, diversity)
    next_char = indices_char[next_index]

    generated += next_char + " "
    sentence = sentence[1:]
    sentence.append(next_char)

    sys.stdout.write(" " + next_char)
    sys.stdout.flush()
    print()
gc.collect()