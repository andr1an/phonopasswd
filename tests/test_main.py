from phonopasswd import generate_password
import re


def test_generate_password():
    re_passwd = re.compile(r'^[-_\da-z]{9,}$', re.IGNORECASE)
    for i in range(10):
        assert re_passwd.match(generate_password())
