import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx

# Carregar o modelo de português
nlp = spacy.load("pt_core_news_sm")

# Texto em português
texto = """
O Processamento de Linguagem Natural (PLN) é uma área da Inteligência Artificial que foca na interação entre computadores e humanos por meio da linguagem natural.
Ele permite que as máquinas entendam, processem e respondam a informações escritas ou faladas de maneira significativa.
Com o avanço das tecnologias, o PLN tem sido amplamente utilizado em aplicações como tradutores automáticos, chatbots e assistentes virtuais.
"""

# 1. Tokenizar o texto em frases
doc = nlp(texto)
frases = [sent.text for sent in doc.sents]

# 2. Representar as frases usando TF-IDF
vectorizer = TfidfVectorizer()
matriz_tf_idf = vectorizer.fit_transform(frases)

# 3. Calcular a similaridade entre as frases
similaridade = cosine_similarity(matriz_tf_idf)

# 4. Criar o grafo com base na similaridade
grafo = nx.from_numpy_array(similaridade)

# 5. Aplicar o algoritmo PageRank para rankear as frases
scores = nx.pagerank(grafo)

# 6. Selecionar as frases mais relevantes
ranked_frases = sorted(((scores[i], s) for i, s in enumerate(frases)), reverse=True)

# Exibir o resumo com as N frases mais relevantes
N = 2  # Número de frases no resumo
resumo = " ".join([frase for _, frase in ranked_frases[:N]])

print("Resumo gerado:")
print(resumo)
