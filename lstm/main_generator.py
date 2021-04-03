import train
import lyric_generator as generator

import gc

wordlist = train.manage_wordlist()
chars_sorted = train.prepare_text_data(wordlist)

dictionaries = train.create_dictionaries(chars_sorted)
char_indices = dictionaries[0]
indices_char = dictionaries[1]

train.vectorization(chars_sorted, char_indices)
length_chars_sorted = len(chars_sorted)
model = train.prepare_model(length_chars_sorted)
model_generation = generator.generation(model)

random_point = generator.random_point(wordlist)
generated = random_point[0]
sentence = random_point[1]
print('generated: ', generated)
prediction = generator.prediction(model_generation, chars_sorted, char_indices, indices_char, generated, sentence)

gc.collect()
