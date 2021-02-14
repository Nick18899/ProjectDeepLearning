import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def download_model():
    import fasttext.util
    fasttext.util.download_model('en', if_exists='ignore')  # English

# download_model()
import fasttext
model = fasttext.load_model('./cc.en.100.bin')
vect = model.get_sentence_vector("some string") # 1 sentence
print(vect)
