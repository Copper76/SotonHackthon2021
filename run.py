from tensorflow import keras
from tensorflow.keras.models import load_model

import numpy as np

model = load_model("./trained_model.h5")

optimizer = keras.optimizers.RMSprop(learning_rate=0.001)
model.compile(loss="categorical_crossentropy", optimizer=optimizer)

def sample(preds, temperature):
    preds = np.asarray(preds).astype("float64")
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

import io

path = "./dwscripts.txt"

with io.open(path, encoding="utf-8") as f:
    text = f.read().lower()

chars = sorted(list(set(text)))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

maxlen = 40
temperature = 0.5

# Take a seed
sentence = input("Enter seed: ")[:maxlen]

generated = ""
for i in range (400):

    # Vectorize the seed
    x_pred = np.zeros((1, maxlen, len(chars)))
    for t, char in enumerate(sentence):
        x_pred[0, t, char_indices[char]] = 1.0

    # Predict next character
    preds = model.predict(x_pred, verbose=0)[0]
    next_index = sample(preds, temperature)
    next_char = indices_char[next_index]

    sentence = sentence[1:] + next_char
    generated += next_char

# Match and replace keywords by edit distance

from replace import rep_words, rep_words_flex

# Open keywords
f = open("./keywords.txt", "r")
keywords = f.readlines()
f.close()

print(rep_words(generated, keywords, 3))
