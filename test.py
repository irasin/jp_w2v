from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('word2vec.model', binary=False)



model.most_similar(positive=["トヨタ"], topn=10)

model.most_similar(positive=["富士山"],topn=10)
