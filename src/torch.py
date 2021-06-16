# -*- coding: utf-8 -*-
"""torch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17eyty6zBcAN9PJ1DQifUtMksfcMiaXPa
"""

!rm ./tweets.csv* # Удалить дубликаты и старые версии файла на всякий случай
!wget 'https://raw.githubusercontent.com/Nick18899/Dataset/main/tweets.csv'
!cat './tweets.csv' | head -n 10

"""# Загрузка датасета в объекст ```pandas.Dataframe```"""

import pandas as pd
import numpy as np
from keras.preprocessing.text import Tokenizer

unparsed_data = pd.read_csv('./tweets.csv', usecols=['author', 'content', 'date_time', 'language', 'number_of_likes', 'number_of_shares'])
# data.head()
# Отфильтровать твиты на наличие хештегов и английский язык
multilanguage_data = unparsed_data.iloc[[index for index, value in unparsed_data.content.str.contains('#').iteritems() if value]]
data = unparsed_data.iloc[[index for index, value in multilanguage_data.language.str.contains('en').iteritems() if value]]
assert(data.count().author < multilanguage_data.count().author < unparsed_data.count().author) 
# Язык везде английский
data = data.reset_index(drop=True).drop(columns='language')

"""# Токенизация

* Каждый твит нужно распарсить на отдельные слова или лексемы 
* Также отделить каждый тег проблема, чтобы потом проще было экстрадировать теги из твита
"""

try:
  from tokenizer import tokenizer
except ModuleNotFoundError:
  !pip install git+https://github.com/erikavaris/tokenizer.git
  from tokenizer import tokenizer
T = tokenizer.TweetTokenizer(preserve_case=False, preserve_handles=False, preserve_hashes=True, regularize=True, preserve_len=False, preserve_emoji=False, preserve_url=False)

data['content'] = data['content'].apply(lambda tweet: T.tokenize(str(tweet).replace('# ', '#').replace('@ ', '@'))) # некоторые челики ставят пробле между # и текстом самого твита, нам такого не надо

"""# Выделение твитов в отдельный столбец"""

data['tags'] = data['content'].apply(lambda separatedTweet: list(filter(lambda token: '#' in token, separatedTweet)))
data.head()



"""# Убираем хештеги из самих твитов, так как мы не рассматриваем их, как смысловую часть текста"""

data['content'] = data['content'].apply(lambda separatedTweet: np.array(list(filter(lambda token: not ('#' in token), separatedTweet))))
data['content'].head()

import gensim.downloader
EMBEDDINGS_DIMENSIONS = 50
glove_vectors = gensim.downloader.load('glove-twitter-' + str(EMBEDDINGS_DIMENSIONS)) ## Импорт эмбеддингов при помощи оберкти gensim
# Допустимые размерности векторов: 25, 50, 100, 200
# Чтобы посмотреть список эмбеддингов: gensim.downloader.info(name_only=True)

"""# Тестим, насколько эмбеддинги [соответсвуют идеалу](https://www.technologyreview.com/2015/09/17/166211/king-man-woman-queen-the-marvelous-mathematics-of-computational-linguistics/)"""

word = 'ball' # Работа со эмбеддингами: можно по токену узнать вектор для него, можно по слову узнать его индекс в словаре, что позже надо будет сделать для распарсенных эмбеддингов
glove_vectors.get_vector(word)
ind = glove_vectors.vocab[word].index;
glove_vectors.get_vector(glove_vectors.index2word[ind])
len(glove_vectors.vocab)

import numpy as np
test = glove_vectors.get_vector('nepo')
glove_vectors.similar_by_vector(test)

"""#Убрать из твитов какие-то левые слова , которых нет в эмбеддингах"""

data['content'] = data['content'].apply(lambda tweet: list(filter(lambda word: word in glove_vectors.vocab.keys(), tweet)))

# glove_vectors.get_keras_embedding



"""# ```Multilable-Кодирование``` твитов при помощи sklearn ```MultiLabelBinarizer```

"""



"""Каждому твиту в соответсвие поставим вектор с информацией, какие хештеги содержатся в данном твите. Позже это пригодится для решение задачи multilable-классификации тегов"""

try: 
  from sklearn.preprocessing import MultiLabelBinarizer
except ModuleNotFoundError:
  !pip install sklearn
  from sklearn.preprocessing import MultiLabelBinarizer

all_tags = []
data['tags'].apply(all_tags.extend)
# all_tags = [[all_tags[i], i] for i in range(len(all_tags))]
all_tags[:10]





from collections import Counter
encoder = MultiLabelBinarizer()
categorized_labels_from_tags = encoder.fit_transform(data['tags'])
top_tags, top_counts = zip(*Counter(all_tags).most_common(10))

#sum(values[29])
# max_tags_count = max(map(sum, values))
# print(max_tags_count)

import torch # Запихнем всё в торч
torch_tags_categories = torch.tensor(categorized_labels_from_tags)
torch_like_tensors = torch.tensor(data['number_of_likes'])

#torch_tweets_vectors = [[glove_vectors.get_vector(word)  for word in tweet] for tweet in data['content']]
def get_matrix_from_tweet(tweet):
  return [[glove_vectors.get_vector(word) for word in tweet]]

def tweet_to_tensor(tweet): 
  return torch.tensor(get_matrix_from_tweet(tweet))

tensored_tweets = data['content'].apply(tweet_to_tensor)
tensored_tweets[0].shape



"""# TODO:
  * Подготовка данных текста
    * [x] Удалить из текстов твитов слова с хештегеми, (они уже  лежат в отдельном столбце в dataframe ```data```)
    * [x] Токенезировать исходные тексты твитов; получить ```vocabulary```
  * Подготовка данных хештегов
    * [x] Каждый хештег должен представлять из себя категорию (количетсво хештегов - мощность категориального вножества)
    * [x] У каждого твита может быть несколько хештегов
    * [x] Заюзать ```one-hot кодирование в вектор длиной в количетсво хештегов```, с помощью которого будет описано, какие хештеги встретились в твите (к каким категориям его отнёс автор)

  * Сделать обучение....
    * Рекурент очка
    * На вход
      1. Текст твита (матрица из эмбеддингов)
      2. Хештеги в твите (категориальный признак)
    * На выход
      1. Число (предполагаемое количество лайков на твите)
"""



"""# Deep ~~Dark Fantasy~~ Learning Part"""

import torch # Загрузка эмбеддингов из gensim в torch
import torch.nn as nn
weight = torch.FloatTensor(glove_vectors.vectors)
embedding = nn.Embedding.from_pretrained(weight, freeze=True)
assert(embedding.weight.size()[0] == len(glove_vectors.vocab) and embedding.embedding_dim == glove_vectors.vector_size) # Проверка, что эмбеддинги загрузились правильно (правильное количетсво эмбеддингов и правильная размерность у каждого)
glove_vectors.similar_by_vector(weight[5].cpu().detach().numpy())
# glove_vectors.similar_by_vector(weight[0])
# glove_vectors.similar_by_vector(test_vector)

class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size
        self.i2h = nn.Linear(input_size + hidden_size, hidden_size)
        self.i2o = nn.Linear(input_size + hidden_size, output_size)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, input, hidden):
        combined = torch.cat((input, hidden), 1)
        hidden = self.i2h(combined)
        output = self.i2o(combined)
        output = self.softmax(output)
        return output, hidden

    def initHidden(self):
        return torch.zeros(1, self.hidden_size)

n_hidden = 128
# rrn = RNN()
