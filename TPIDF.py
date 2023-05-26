from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np

corpus = ['This is the first document.','This is the second second document.','And the third one.','Is this the first document?']

vectorizer =CountVectorizer()
X = vectorizer.fit_transform(corpus)

word = vectorizer.get_feature_names_out()

print("Vocabulary:",word)

print("BOW=\n", X.toarray())