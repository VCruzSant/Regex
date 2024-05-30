import re

# Meta caracteres: ^ $ ( )
# * -> 0 ou n
# + -> 1 ou n
# ? 0 ou 1
# {n}
# {min, max}

text = '''
Na pequena vila de Belavista, onde o tempo parecia ter parado, vivia clara,
uma menina de dez anos que adorava
explorar os arredores.
Um dia, ao seguir um rastro de borboletas azuis, Clara encontrou um antigo
espelho enterrado sob uma árvore centenária. Ao limpá-lo, viu refletida uma
versão maaaaaaaaaaaaaaagiiiiiiiiiica de sua vila, onde animais falavam e
flores dançavam.
Com o coração cheio de coragem, ela atravessou o espelho e descobriu que,
ao ajudar os habitantes desse mundo encantado, conseguia trazer um pouco de
magia para sua própria realidade, tornando Belavista um lugar onde
sonhos e realidade se entrelaçavam de maneira maravilhosa.
'''

# print(re.findall(r'ma+gi+ca', text, flags=re.I))
# print(re.findall(r'ma{1,}gi{1,}ca', text, flags=re.I))
# print(re.sub(r'ma+gi+ca', 'Mágica', text, flags=re.I))

text2 = 'Clara ama ser amada'

print(re.findall(r'ama[da]*', text2, flags=re.I))
