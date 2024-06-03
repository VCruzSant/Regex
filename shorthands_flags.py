import re
from pprint import pprint

# \w -> [a-z0-9A-ZÀ-ú_] | Negation: \W -> [^a-z0-9A-ZÀ-ú_]
# re.A -> [a-z0-9A-Z_]
# \d -> [0,9] | Negation : \D [^0,9]
# \s -> [ \r\n\f\n\t] = spaces | Negation : \S -> [ ^\r\n\f\n\t]
# \b -> edges


text = '''
Na pequena vila de Belavista 1990, onde o tempo parecia ter parado,
vivia clara,
uma menina de dez anos que adorava
explorar os arredores.
Um dia, ao seguir um rastro de borboletas azuis, Clara encontrou um antigo
espelho enterrado sob uma árvore centenária. Ao limpá-lo, viu refletida uma
versão mágica de sua vila, onde animais falavam e flores dançavam.
Com o coração cheio de coragem, ela atravessou o espelho e descobriu que,
ao ajudar os habitantes desse mundo encantado, conseguia trazer um pouco de
magia para sua própria realidade, tornando Belavista um lugar onde
sonhos e realidade se entrelaçavam de maneira maravilhosa.
'''

# pprint(re.findall(r'[a-z]+', text, flags=re.I))

# acentos:
# pprint(re.findall(r'[a-z0-9À-ú]+', text, flags=re.I))
# pprint(re.findall(r'\w+', text, flags=re.A))
# pprint(re.findall(r'\d+', text, flags=re.A))
# pprint(re.findall(r'\s+', text, flags=re.A))
# pprint(re.findall(r'\w+e\b', text, flags=re.A))

# 4 letters, use edges for words completes
# pprint(re.findall(r'\b\w{4}\b', text, flags=re.A))

# re.A -> ASCII
#  re.I -> IGNORECASE
# re.M -> Multiline -> ^ $
# re.S -> Dotall]

# text2 = '''
# 123.456.789-00 ABC
# 000.111.222-33 CBA
# 123.123.123-12
# '''

# pprint(re.findall(r'\d{3}\.\d{3}\.\d{3}\-\d{2}', text2, flags=re.M))

text2 = '''Na pequena vila de Belavista 1990,
onde o tempo parecia ter parado'''
pprint(re.findall(r'^n.*o$', text2, flags=re.I | re.S))
