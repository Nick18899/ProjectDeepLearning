# import fasttext
# import fasttext.util

# fasttext.util.download_model('en', if_exists='ignore')
# ft = fasttext.load_model('cc.en.300.bin')
# print(ft.get_dimension())
# fasttext.util.reduce_model(ft, 100)
# print(ft.get_dimension())
# ft.save_model('cc.en.100.bin')

from gensim.models.wrappers import FastText
model = FastText.load_fasttext_format('cc.en.100.bin')
print(model.most_similar('better'))
