import re
# from pprint import pprint
# https://regex101.com/

regex = re.compile(
    r"^((?:\(\d{2}\)\s*)?(?:9\s*)?(?:\d{4}-\d{4}))$", flags=re.M)

test_str = ("(21) 9 8852-5214\n"
            "(11)9955-1231\n"
            "(11)            9955-1231\n"
            "(35) 9 9975-4521\n"
            "(31) 3851-2587\n"
            "9 8571-5213\n"
            "1234-5647\n")

# pprint(regex.findall(test_str))

for phone in regex.findall(test_str):
    print(phone)
