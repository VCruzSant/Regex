import re
from pprint import pprint
# Meta caracteres: ^ $
# ^ -> Start
# $ -> End
#  [^a-z] -> anything that isn't between a and z

cpf = '123.456.789-00'
pprint(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
pprint(re.findall(r'[^a-z]+', cpf))
pprint(re.findall(r'[^0-9]+', cpf))
pprint(re.findall(r'[^.-]+', cpf))
