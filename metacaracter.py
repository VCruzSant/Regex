import re

# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | -> OU
# . -> Qualquer caractere (com esceção da quebra de linha)
# [] -> Conjunto de caracteres

text = '''
Na pequena vila de Belavista, onde o tempo parecia ter parado, vivia clara,
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

print(re.findall(r'Clara|espelho|m..ica', text))
print(re.findall(r'[Cc]lara|espelho|m..ica', text))
print(re.findall(r'[a-zA-z]lara', text))
print(re.findall(r'ClArA', text, flags=re.I))
