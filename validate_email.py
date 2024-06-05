# Básica
# ^\w+(?:[.\-+!%]\w+)*@\w+(?:[.\-]\w+)+$
# https://regex101.com/r/9s4bgv/1/

# Básica 2
# ^[^\s@<>\(\)[\]\.]+(?:\.[^\s@<>\(\)\[\]\.]+)*@\w+(?:[\.\-_]\w+)*$
# https://regex101.com/r/mH4ChC/2/

# rfc 5322
# ^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$
# https://regex101.com/r/fkxI15/1/

import re
from pprint import pprint


regex = re.compile(r"^\w+(?:[.\-+!%]\w+)*@\w+(?:[.\-]\w+)+$", flags=re.M)

test_str = ("Valid email addresses\n"
            "o-que_vai.te+dar+dor-de.cabeca@gmail-com-traco.com.br\n"
            "simple@example.com\n"
            "very.common@example.com\n"
            "disposable.style.email.with+symbol@example.com\n"
            "other.email-with-hyphen@example.com\n"
            "fully-qualified-domain@example.com\n"
            "user.name+tag+sorting@example.com\n"
            "x@example.com\n"
            "example-indeed@strange-example.com\n"
            "example@s.example\n"
            "a@a.com.br\n"
            "mailhost!username@example.org\n"
            "user%example.com@example.org\n"
            "email@example.com\n"
            "firstname.lastname@example.com\n"
            "email@subdomain.example.com\n"
            "firstname+lastname@example.com\n"
            "email@123.123.123.123\n"
            "\"email\"@example.com\n"
            "1234567890@example.com\n"
            "email@example-one.com\n"
            "_______@example.com\n"
            "email@example.name\n"
            "email@example.museum\n"
            "email@example.co.jp\n"
            "firstname-lastname@example.com\n\n\n"

            "Invalid email addresses\n"
            "Abc.example.com\n"
            "<aqui-te-um@email-pra-validar.com.br>\n"
            "A@b@c@example.com\n"
            "a\"b(c)d,e:f;g<h>i[j\\k]l@example.com\n"
            "just\"not\"right@example.com\n"
            "this is\"not\\allowed@example.com\n"
            "this\\ still\\\"not\\\\allowed@example.com\n"
            "plainaddress\n"
            "#@%^%#$@#$@#.com\n"
            "@example.com\n"
            "<email@example.com>\n"
            "email.example.com\n"
            "email@example@example.com\n"
            ".email@example.com\n"
            "email.@example.com\n"
            "email..email@example.com\n"
            "あいうえお@example.com\n"
            "email@example\n"
            "email@-example.com\n"
            "email@example..com\n"
            "Abc..123@example.com\n"
            "”(),:;<>[\\]@example.com\n"
            "just”not”right@example.com\n"
            "this\\ is\"really\"not\\allowed@example.com")


pprint(regex.findall(test_str))
