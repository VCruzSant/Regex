import re

# re.X -> comments

cpf = '123.123.123-12'
cpf_reg_exp = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
# print(cpf_reg_exp.search(cpf))

ip_reg_exp = re.compile(r'''
    ^
    (?:
        (?:
            25[0-5]| # 250-255
            2[0-4][0-9]|# 200-249
            1[0-9]{2}| # 100-199
            [1-9][0-9]| # 10-99
            [0-9] # 0-9
        )
        \.?
    ){4}
    \b
    $
''', flags=re.X)

for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip, ip_reg_exp.findall(ip))
