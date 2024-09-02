from nltk.corpus import mac_morpho
import nltk

#Baixando o treebank
nltk.download('mac_morpho')

#visualizando
arvore = mac_morpho.tagged_sents()
print(arvore[2])
