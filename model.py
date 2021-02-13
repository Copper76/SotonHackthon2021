from tensorflow import keras
from tensorflow.keras import layers

import numpy as np
import random
import io

path = "./dwscripts.txt"

with io.open(path, encoding="utf-8") as f:
    text = f.read().lower()
text = text.replace("\n", " ")
print("Corpus length: ", len(text))

chars = sorted(list(set(text)))
print("Total chars: ", len(chars))
