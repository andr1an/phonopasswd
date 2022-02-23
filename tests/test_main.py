from phonopasswd import PhonoPasswd
import re


def test_generate_password():
    re_passwd = re.compile(r"^[-_\da-z]{9,}$", re.IGNORECASE)
    passwordgen = PhonoPasswd(language="en")
    for i in range(10):
        assert re_passwd.match(passwordgen.generate_password())
