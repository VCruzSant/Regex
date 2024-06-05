import re
from pprint import pprint

regex = re.compile(r'^[+-]?\d+(?:\.\d+)?$', flags=re.M)


test_str = ("Válidos\n"
            "0.0\n"
            "00.00\n"
            "000.000\n"
            "+0.0\n"
            "-00.00\n"
            "+000.000\n"
            "10\n"
            "50\n"
            "8.5\n"
            "-8.5\n"
            "+10.5005412136\n"
            "1231345458.54654564\n"
            "-133215646589.6543215648978977\n"
            "+1.11123123\n"
            "-0.154987\n"
            "1.121654987\n"
            "10.123\n"
            "10.1\n"
            "-1.1\n\n"
            "Inválidos\n"
            "10..2\n"
            "++1213\n"
            "--1235050\n"
            ".124546\n"
            "-.1231324\n"
            "10.\n"
            ".1\n"
            ".10\n"
            "10.\n"
            "+10.\n"
            "-10.\n"
            "5a\n"
            "b5[")

pprint(regex.findall(test_str))


def is_float(str: str) -> bool:
    return bool(re.search(r'^[+-]?\d+(?:\.\d+)?$', str))


def is_int(str: str) -> bool:
    return bool(re.search(r'^[+-]?\d+$', str))


while True:
    number = input('Number:')

    if is_int(number):
        number = int(number)
        print(f'{number} converted to int')
        continue

    elif is_float(number):
        number = float(number)
        print(f'{number} converted to float')
        continue
