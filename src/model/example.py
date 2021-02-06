import fasttext
import numpy as np
model = fasttext.train_supervised(input="cooking.train")
model.predict("Which baking dish is best to bake a banana bread ?")
