import train

wordlist = train.manage_wordlist()
chars_sorted = train.prepare_text_data(wordlist)

dictionaries = train.create_dictionaries(chars_sorted)
char_indices = dictionaries[0]
pair_vector = train.vectorization(chars_sorted, char_indices)

length_chars_sorted = len(chars_sorted)
x = pair_vector[0]
y = pair_vector[1]

model = train.prepare_model(length_chars_sorted)
train.build_model(model, x, y)
