import nltk
from nltk.corpus import floresta

#Baixando o treebank
nltk.download('floresta')


# Exibindo a árvore de uma sentença
arvore = floresta.parsed_sents()[2]
arvore.draw()
