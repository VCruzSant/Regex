import re
from pprint import pprint

# Meta caracteres: ^ $ ( )

text = '''
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>
'''

# A info per time
# \/\2 -> Mirror for group
# ?: -> not save in memory
# tags = re.findall(r'(<([pdiv]{1,3})>(?:.*?)<\/\2>)', text)
# tags = re.findall(r'<(?P<tag>[pdiv]{1,3})>(.*?)<\/(?P=tag)>', text)

# for tag in tags:
#     one, two, three = tag
#     print(three)

# pprint(tags)

# cpf = '123.456.789-00 a'
# pprint(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', cpf))
# pprint(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

pprint(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 "MAIS \3 COISAS" \4', text))
