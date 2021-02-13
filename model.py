from tensorflow import keras
from tensorflow.keras import layers

import numpy as np
import random
import io

path = "./dwscripts.txt"

# Read file and strip new lines
with io.open(path, encoding="utf-8") as f:
    text = f.read().lower()
#text = text.replace("\n", " ")

bad = ["[","]","(",")",".","!","?",","]
for b in bad:
    text = text.replace(b, "")

print("Corpus length: ", len(text))

# Unique characters in corpus
chars = sorted(list(set(text)))

print("Total chars: ", len(chars))

# Map unique characters to index in the chars list
char_indices = dict((c, i) for i, c in enumerate(chars))

# Map index in the chars list to the unique character
indices_char = dict((i, c) for i, c in enumerate(chars))

# Cut the text into windows of maxlen characters
maxlen = 40
step = 3
sentences = []
next_chars = []
for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i : i + maxlen])
    next_chars.append(text[i + maxlen])
print("Number of sequences:", len(sentences))

# Vectorize inputs (one hot encode characters into binary arrays)

# Vectorize the overlapping sequences of maxlen (sequences, maxlen, unique characters)
x = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)

# Vectorize the characters that come after each sequence
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)

for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        x[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1


# Build the model
model = keras.Sequential(
    [
        keras.Input(shape=(maxlen, len(chars))),
        layers.LSTM(64),
        layers.Dense(len(chars), activation="softmax"),
    ]
)

# model = keras.Sequential(
#     [
#         keras.Input(shape=(maxlen, len(chars))),
#         layers.LSTM(256),
#         layers.Dropout(0.2),
#         layers.LSTM(256),
#         layers.Dropout(0.2),
#         layers.Dense(len(chars), activation="softmax")
#     ]
# )
# model.summary()

optimizer = keras.optimizers.RMSprop(learning_rate=0.0008)
model.compile(loss="categorical_crossentropy", optimizer=optimizer)

# Reweights distribution using temeperature and samples index from probability array
def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype("float64")
    preds = np.log(preds) / (temperature)
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

epochs = 60
batch_size = 64

for epoch in range(epochs):

    # Fit model for a single iteration
    model.fit(x, y, batch_size=batch_size, epochs=1)

    print("Generating text after epoch: %d" % epoch)

    model.save("trained_model.h5")

    # Select a text seed at random
    start_index = random.randint(0, len(text) - maxlen - 1)

    # Attempt generation with a range of temperatures
    # for diversity in [0.2, 0.5, 1.0, 1.2]:

    #     print("...Diversity:", diversity)

    #     generated = ""
    #     sentence = text[start_index : start_index + maxlen]
    #     print('...Generating with seed: "' + sentence + '"')

    #     # Generate N characters starting from the seed text
    #     for i in range(400):

    #         # Vectorize characters generated
    #         x_pred = np.zeros((1, maxlen, len(chars)))
    #         for t, char in enumerate(sentence):
    #             x_pred[0, t, char_indices[char]] = 1.0

    #         # Predict next character
    #         preds = model.predict(x_pred, verbose=0)[0]
    #         next_index = sample(preds, diversity)
    #         next_char = indices_char[next_index]

    #         # Build generated sentence
    #         sentence = sentence[1:] + next_char
    #         generated += next_char

    #     print("...Generated: ", generated)
    #     print()

model.save("trained_model.h5")
