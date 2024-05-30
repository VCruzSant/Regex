import re

# Meta caracteres: ^ $ ( )
# * -> 0 ou n
# + -> 1 ou n
# ? 0 ou 1
# {n}
# {min, max}

text = '''
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 4</p> <div>Frase 4</div>
'''

# all info together
print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', text))

# A info per time
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', text))
