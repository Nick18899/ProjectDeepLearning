import fasttext
import fasttext.util
# fasttext.util.download_model('en', if_exists='ignore')
ft = fasttext.load_model('cc.en.300.bin')
print(ft.get_dimension())
print(ft.get_nearest_neighbors('hello'))


