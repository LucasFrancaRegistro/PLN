import re

# Texto de review de exemplo
review = "The product is amazing! I loved the build quality. However, the battery life could be better."

# Expressão regular para tokenizar sentenças
token_pattern = r'[.!?]\s+'

# Tokenização usando a expressão regular
sentences = re.split(token_pattern, review)

# Remover possíveis tokens vazios resultantes do split
sentences = [s for s in sentences if s]

# Contar a quantidade de tokens de saída
token_count = len(sentences)

# Mostrar os tokens e a quantidade
print(f"Tokens: {sentences}")
print(f"Quantidade de tokens: {token_count}")
