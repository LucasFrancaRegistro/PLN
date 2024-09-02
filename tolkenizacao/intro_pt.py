import nltk
nltk.download('punkt_tab')
import spacy
import numpy as np
import pandas as pd
import copy as cp
import joblib
from texto import criaTexto

#recolhemos o texto
sentence = criaTexto()
words = sentence.split()
print(f"Total de caracteres no texto:{len(words)}")

#Usando o modelo pre-treinado na pasta "data" tokenizamos o texto por sentenças
#e exibimos em formato de tabela as 5 primeiras sentenças e suas tags
trained_data_folder = 'data/'
portuguese_tagger = joblib.load(trained_data_folder+'POS_tagger_brill.pkl')
pos_tags = portuguese_tagger.tag(nltk.sent_tokenize(sentence))
pos_tags_df = pd.DataFrame(pos_tags).T
print("Tolkenização por sentença")
print(pos_tags_df.iloc[:, :5])

#Em seguida usando o mesmo modelo tokenizamos o texto por palavras e exibimos
#as 5 primeiras junto as respectivas tags
pos_tags = portuguese_tagger.tag(nltk.word_tokenize(sentence))
pos_tags_df = pd.DataFrame(pos_tags).T
print("Tolkenização por palavra")
print(pos_tags_df.iloc[:, :5])



